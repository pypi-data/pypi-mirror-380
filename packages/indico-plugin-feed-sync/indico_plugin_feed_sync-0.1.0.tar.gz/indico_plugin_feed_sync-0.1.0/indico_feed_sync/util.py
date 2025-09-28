from __future__ import annotations

import hashlib
import logging
import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

import pytz
import requests
from markupsafe import Markup, escape
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from indico.core.db import db
from indico.modules.categories import Category
from indico.modules.attachments.models.attachments import Attachment, AttachmentType
from indico.modules.attachments.models.folders import AttachmentFolder
from indico.modules.events import Event, EventLogRealm
from indico.modules.events.models.events import EventType
from indico.modules.events.models.labels import EventLabel
from indico.modules.events.models.persons import EventPersonLink
from indico.modules.events.persons.util import get_event_person
from indico.modules.events.timetable.models.breaks import Break
from indico.modules.events.timetable.models.entries import (TimetableEntry,
                                                            TimetableEntryType)
from indico.modules.events.util import track_location_changes, track_time_changes
from indico.modules.users import User
from indico.util.date_time import now_utc
from indico.modules.logs import LogKind
from indico.modules.logs.models.entries import AppLogEntry, AppLogRealm
from sqlalchemy import func


USER_AGENT = 'IndicoFeedSync/0.1'
REQUEST_TIMEOUT = 20
DEFAULT_MAX_ITEMS = 200

disable_warnings(InsecureRequestWarning)


@dataclass
class NormalizedEvent:
    external_id: str
    title: str
    description: str
    start_dt: datetime
    end_dt: datetime
    timezone: str
    original_url: str
    location: Dict[str, str]
    event_type: EventType
    keywords: List[str]
    references: List[Dict[str, Any]]
    map_url: str
    contact_title: Optional[str]
    contact_emails: Optional[List[str]]
    contact_phones: Optional[List[str]]
    chairs: List[Dict[str, Any]]
    label_title: Optional[str]
    label_color: Optional[str]
    label_is_event_not_happening: Optional[bool]
    label_message: Optional[str]
    raw_payload: Dict[str, Any]

    @property
    def hash(self) -> str:
        serializable = json.dumps(self.raw_payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(serializable.encode('utf-8')).hexdigest()


class FeedSyncCoordinator:
    def __init__(self, plugin):
        self.plugin = plugin
        self.logger = logging.getLogger('indico.plugins.feed_sync')

    def sync_single_feed(self, feed_id: str, *, triggered_by: str = 'manual', force: bool = False) -> Dict[str, Any]:
        feed = self.plugin.get_feed(feed_id)
        if not feed:
            return {'status': 'error', 'message': f'Unknown feed id: {feed_id}'}
        if force:
            self.plugin.reset_feed_state(feed_id)
        service = FeedSyncService(self.plugin, feed, triggered_by=triggered_by, force=force)
        return service.sync()

    def sync_all_feeds(self, *, triggered_by: str = 'manual', force: bool = False) -> Dict[str, Any]:
        results = {}
        failed = []
        for feed in self.plugin.get_active_feeds():
            result = self.sync_single_feed(feed['id'], triggered_by=triggered_by, force=force)
            results[feed['id']] = result
            if result.get('status') != 'ok':
                failed.append(feed['id'])
        if failed:
            return {
                'status': 'error',
                'message': f'Failed feeds: {", ".join(failed)}',
                'results': results
            }
        return {
            'status': 'ok',
            'message': 'All feeds processed successfully',
            'results': results
        }


class FeedSyncService:
    def __init__(self, plugin, feed: Dict[str, Any], *, triggered_by: str, force: bool = False):
        self.plugin = plugin
        self.feed = feed
        self.triggered_by = triggered_by
        self.force = force
        self.logger = logging.getLogger('indico.plugins.feed_sync')
        self.now = now_utc()
        self.state = plugin.get_feed_state(feed['id']) or {}
        self.events_state: Dict[str, Dict[str, Any]] = self.state.get('events', {})
        self.category = Category.get(feed['category_id'])
        self.creator = self._resolve_creator()
        self.use_event_details = feed.get('use_event_details', True)
        self.allow_deletions = feed.get('allow_deletions', True)
        try:
            self.startdate_offset_days = int(feed.get('startdate_day', -30))
        except (ValueError, TypeError):
            self.startdate_offset_days = -30
        self.start_threshold = (self.now + timedelta(days=self.startdate_offset_days)).replace(microsecond=0)
        self._folder_cache: Dict[str, AttachmentFolder] = {}

    def sync(self) -> Dict[str, Any]:
        if not self.category:
            msg = f'Category {self.feed["category_id"]} does not exist'
            self.logger.error('[%s] %s', self.feed['id'], msg)
            self._record_error(msg)
            return {'status': 'error', 'message': msg}

        fetcher = FeedFetcher(self.feed)
        fetch_result = fetcher.fetch()
        if fetch_result['status'] != 'ok':
            message = fetch_result['message']
            self.logger.error('[%s] %s', self.feed['id'], message)
            self._record_error(message)
            return {'status': 'error', 'message': message}

        raw_events = fetch_result['items']
        processed_count = 0
        eligible_total = 0
        self.state['last_trigger'] = self.triggered_by
        self._set_status('running', meta={
            'total': 0,
            'processed': 0,
            'created': 0,
            'updated': 0,
            'unchanged': 0,
            'deleted': 0
        })
        processed = []
        created = 0
        updated = 0
        unchanged = 0
        deleted = 0

        seen_ids = set()
        for item in raw_events:
            external_id = str(item.get('id')) if item.get('id') is not None else None
            include = self._should_include_item(item)
            detailed = None

            if include is False:
                if external_id:
                    seen_ids.add(external_id)
                continue

            if self.use_event_details and (include is None or include):
                detailed = fetcher.fetch_event_details(item.get('id'))
                if detailed:
                    item = detailed
                    include = self._should_include_item(item)

            if include is False:
                if external_id:
                    seen_ids.add(external_id)
                continue

            if include is None:
                include = True

            normalized = self._normalize_event(item)
            seen_ids.add(normalized.external_id)
            outcome = self._apply_event(normalized)
            processed.append(outcome)
            if outcome['action'] == 'created':
                created += 1
            elif outcome['action'] == 'updated':
                updated += 1
            else:
                unchanged += 1
            processed_count += 1
            eligible_total += 1
            self._update_progress(processed=processed_count, total=eligible_total, created=created,
                                  updated=updated, unchanged=unchanged, deleted=deleted)

        # Update last_seen for events not in current feed snapshot
        for external_id in list(self.events_state.keys()):
            if external_id not in seen_ids:
                entry = self.events_state[external_id]
                start_dt_str = entry.get('start_dt') if isinstance(entry, dict) else None
                skip_deletion = False
                if start_dt_str:
                    try:
                        entry_start_dt = datetime.fromisoformat(start_dt_str)
                    except ValueError:
                        entry_start_dt = None
                    if entry_start_dt and entry_start_dt < self.start_threshold:
                        skip_deletion = True
                if skip_deletion:
                    entry['last_seen_at'] = self.now.isoformat()
                    continue
                if self.allow_deletions:
                    event = Event.get(entry.get('event_id')) if entry.get('event_id') else None
                    if event and not event.is_deleted:
                        reason = f'Removed via feed synchronization (feed {self.feed.get("id")}, external {external_id})'
                        event.delete(reason, user=self.creator)
                        self._log_event_action(event, 'deleted', None, external_id=external_id)
                        deleted += 1
                    processed.append({'external_id': external_id, 'event_id': entry.get('event_id'), 'action': 'deleted'})
                    self.events_state.pop(external_id, None)
                else:
                    entry['last_seen_at'] = self.now.isoformat()

        self._update_progress(processed=processed_count, total=eligible_total, created=created,
                              updated=updated, unchanged=unchanged, deleted=deleted)

        self.state['events'] = self.events_state
        self.state['last_synced_at'] = self.now.isoformat()
        self.state['last_error'] = None
        summary = {
            'status': 'ok',
            'message': f'{created} created, {updated} updated, {unchanged} unchanged, {deleted} deleted',
            'created': created,
            'updated': updated,
            'unchanged': unchanged,
            'deleted': deleted,
            'processed': processed
        }
        self.state['last_summary'] = {
            'created': created,
            'updated': updated,
            'unchanged': unchanged,
            'deleted': deleted,
            'processed': processed_count,
            'total': eligible_total
        }
        self._set_status('completed', meta=self.state['last_summary'])

        db.session.commit()

        self.logger.info('[%s] %s', self.feed['id'], summary['message'])
        return summary

    # Internal helpers --------------------------------------------------------

    def _normalize_event(self, item: Dict[str, Any]) -> NormalizedEvent:
        start_dt = _parse_date(item.get('startDate'))
        end_dt = _parse_date(item.get('endDate')) or start_dt
        timezone = item.get('timezone') or item.get('startDate', {}).get('tz') or 'UTC'
        original_url = item.get('url') or self.feed['url']
        description_parts = [
            f'<p><strong>Original event:</strong> <a href="{original_url}" rel="noreferrer" target="_blank">{original_url}</a></p>',
            item.get('description') or ''
        ]
        meta_block = _build_metadata_block(item)
        if meta_block:
            description_parts.append(meta_block)
        refs_block = _build_references_block(item.get('references') or [])
        if refs_block:
            description_parts.append(refs_block)
        description_html = ''.join(description_parts)
        description_html = _rewrite_relative_urls(description_html, original_url)
        location = {
            'venue_name': item.get('location') or '',
            'room_name': item.get('room') or '',
            'address': item.get('address') or ''
        }
        event_type = _map_event_type(item.get('type'))
        keywords = item.get('keywords') or []
        references = item.get('references') or []
        external_id = str(item.get('id'))
        map_url = item.get('roomMapURL') or item.get('mapURL') or ''
        contact_title = item.get('contactTitle') or item.get('contact_title')
        contact_emails = _split_multi_value(item.get('contactEmail') or item.get('contactEmails') or
                                            item.get('contact_email') or item.get('contact_emails'))
        contact_phones = _split_multi_value(item.get('contactPhone') or item.get('contactPhones') or
                                            item.get('contact_phone') or item.get('contact_phones'))
        chairs = item.get('chairs') or []
        label_info = item.get('label') or {}
        label_title = (label_info.get('title') or '').strip() or None
        label_color = (label_info.get('color') or '').strip() or None
        label_is_not_happening = label_info.get('is_event_not_happening')
        if label_is_not_happening is None:
            label_is_not_happening = label_info.get('isEventNotHappening')
        if label_is_not_happening is not None:
            label_is_not_happening = bool(label_is_not_happening)
        label_message = label_info.get('message')
        if label_message is None:
            label_message = item.get('label_message') or item.get('labelMessage')
        return NormalizedEvent(
            external_id=external_id,
            title=item.get('title') or f'Imported event {external_id}',
            description=description_html,
            start_dt=start_dt,
            end_dt=end_dt,
            timezone=timezone,
            original_url=original_url,
            location=location,
            event_type=event_type,
            keywords=keywords,
            references=references,
            map_url=map_url,
            contact_title=contact_title,
            contact_emails=contact_emails,
            contact_phones=contact_phones,
            chairs=chairs,
            label_title=label_title,
            label_color=label_color,
            label_is_event_not_happening=label_is_not_happening,
            label_message=label_message,
            raw_payload=item
        )

    def _apply_event(self, normalized: NormalizedEvent) -> Dict[str, Any]:
        entry = self.events_state.get(normalized.external_id)
        current_hash = normalized.hash
        allow_updates = self.feed.get('allow_updates', True)

        changed_fields: List[str] = []
        if entry:
            event = Event.get(entry.get('event_id')) if entry.get('event_id') else None
            if not event or event.is_deleted:
                self.logger.warning('[%s] Missing local event for external id %s; recreating',
                                    self.feed['id'], normalized.external_id)
                event = self._create_event(normalized)
                action = 'created'
            elif self.force or entry.get('last_hash') != current_hash:
                if allow_updates or self.force:
                    changed_fields = self._update_event(event, normalized)
                    action = 'updated'
                else:
                    self.logger.info('[%s] Skipping update for %s because allow_updates is disabled',
                                     self.feed['id'], normalized.external_id)
                    action = 'skipped'
            else:
                action = 'unchanged'
        else:
            event = self._create_event(normalized)
            action = 'created'

        entry = entry or {}
        if event:
            entry['event_id'] = event.id
        entry['external_id'] = normalized.external_id
        if action != 'skipped':
            entry['last_hash'] = current_hash
        entry['source_url'] = normalized.original_url
        entry['last_synced_at'] = self.now.isoformat()
        entry['last_seen_at'] = self.now.isoformat()
        entry['last_action'] = action
        entry['start_dt'] = normalized.start_dt.isoformat()
        self.events_state[normalized.external_id] = entry
        if event and action == 'updated':
            self._log_event_action(event, 'updated', normalized, changed_fields)
        if event and action == 'unchanged':
            meta_changes = self._apply_additional_metadata(event, normalized)
            if self._sync_attachments(event, normalized):
                meta_changes.append('attachments')
            if meta_changes:
                self._log_event_action(event, 'updated', normalized, meta_changes)
            db.session.flush()
        if event and action != 'skipped':
            self._sync_timetable(event, normalized)
        return {'external_id': normalized.external_id, 'event_id': entry.get('event_id'), 'action': action}

    def _create_event(self, data: NormalizedEvent) -> Optional[Event]:
        event = Event(category=self.category, type_=data.event_type)
        event.title = data.title
        event.description = Markup(data.description)
        event.start_dt = data.start_dt
        event.end_dt = data.end_dt
        event.timezone = data.timezone
        event.creator = self.creator
        event.keywords = data.keywords
        event.own_venue_name = data.location.get('venue_name', '')
        event.own_room_name = data.location.get('room_name', '')
        event.own_address = data.location.get('address', '')
        event.inherit_location = False if any(data.location.values()) else True
        metadata_changes = self._apply_additional_metadata(event, data)
        db.session.add(event)
        db.session.flush()
        if self._sync_attachments(event, data):
            metadata_changes.append('attachments')
        self._log_event_action(event, 'created', data, metadata_changes)
        self._sync_timetable(event, data)
        return event

    def _update_event(self, event: Event, data: NormalizedEvent) -> List[str]:
        changed_fields: List[str] = []
        if event.title != data.title:
            event.title = data.title
            changed_fields.append('title')
        if str(event.description) != data.description:
            event.description = Markup(data.description)
            changed_fields.append('description')
        with track_time_changes():
            if event.start_dt != data.start_dt:
                event.move_start_dt(data.start_dt)
                changed_fields.append('start_dt')
            if event.end_dt != data.end_dt:
                event.end_dt = data.end_dt
                changed_fields.append('end_dt')
        if event.timezone != data.timezone:
            event.timezone = data.timezone
            changed_fields.append('timezone')
        if set(event.keywords or []) != set(data.keywords or []):
            event.keywords = data.keywords
            changed_fields.append('keywords')
        with track_location_changes():
            if any(data.location.values()):
                event.inherit_location = False
                event.own_venue_name = data.location.get('venue_name', '')
                event.own_room_name = data.location.get('room_name', '')
                event.own_address = data.location.get('address', '')
                changed_fields.append('location')
            else:
                event.inherit_location = True
                event.own_venue_name = ''
                event.own_room_name = ''
                event.own_address = ''
                changed_fields.append('location')
        metadata_changes = self._apply_additional_metadata(event, data)
        if self._sync_attachments(event, data):
            metadata_changes.append('attachments')
        changed_fields.extend(metadata_changes)
        db.session.flush()
        return changed_fields

    def _record_error(self, message: str) -> None:
        self.state['last_error'] = message
        self.state['last_synced_at'] = self.now.isoformat()
        self.state.setdefault('events', self.events_state)
        self.state.pop('last_summary', None)
        self._set_status('failed', meta={'message': message})

    def _resolve_creator(self) -> User:
        user_id = self.plugin.settings.get('creator_user_id')
        if user_id:
            user = User.get(user_id)
            if user:
                return user
            self.logger.warning('[%s] Configured creator user %s does not exist; falling back to system user',
                                self.feed['id'], user_id)
        return User.get_system_user()

    def _apply_contact_info(self, event: Event, data: NormalizedEvent) -> List[str]:
        changes: List[str] = []
        if data.contact_title is not None:
            new_title = data.contact_title or ''
            if (event.contact_title or '') != new_title:
                event.contact_title = new_title
                changes.append('contact_title')
        if data.contact_emails is not None:
            current_emails = list(event.contact_emails or [])
            if current_emails != data.contact_emails:
                event.contact_emails = data.contact_emails
                changes.append('contact_emails')
        if data.contact_phones is not None:
            current_phones = list(event.contact_phones or [])
            if current_phones != data.contact_phones:
                event.contact_phones = data.contact_phones
                changes.append('contact_phones')
        return changes

    def _apply_label(self, event: Event, data: NormalizedEvent) -> List[str]:
        changes: List[str] = []
        label_title = (data.label_title or '').strip()
        if not label_title:
            if event.label is not None or (event.label_message or ''):
                event.label = None
                event.label_message = ''
                changes.append('label')
            return changes

        label = self._get_or_create_label(label_title, data.label_color, data.label_is_event_not_happening)
        if label is None:
            if event.label is not None or (event.label_message or ''):
                event.label = None
                event.label_message = ''
                changes.append('label')
            return changes

        if event.label != label:
            event.label = label
            changes.append('label')

        message = (data.label_message or '').strip()
        if event.label_message != message:
            event.label_message = message
            if 'label' not in changes:
                changes.append('label')

        return changes

    def _get_or_create_label(self, title: str, color: Optional[str], is_event_not_happening: Optional[bool]) -> Optional[EventLabel]:
        normalized = title.strip()
        if not normalized:
            return None

        query = EventLabel.query.filter(func.lower(EventLabel.title) == normalized.lower())
        label = query.first()
        created = False
        if not label:
            label = EventLabel(title=normalized,
                               color=(color or 'blue'),
                               is_event_not_happening=bool(is_event_not_happening))
            db.session.add(label)
            created = True
        else:
            updated = False
            if color and label.color != color:
                label.color = color
                updated = True
            if is_event_not_happening is not None and label.is_event_not_happening != bool(is_event_not_happening):
                label.is_event_not_happening = bool(is_event_not_happening)
                updated = True
            if updated:
                db.session.flush()
        if created:
            db.session.flush()
        return label

    def _apply_additional_metadata(self, event: Event, data: NormalizedEvent) -> List[str]:
        changes: List[str] = []
        new_map = data.map_url or ''
        if (event.own_map_url or '') != new_map:
            event.own_map_url = new_map
            changes.append('map_url')
        changes.extend(self._apply_contact_info(event, data))
        changes.extend(self._apply_label(event, data))
        if self._sync_chairs(event, data.chairs):
            changes.append('chairs')
        return changes

    def _sync_chairs(self, event: Event, chairs: List[Dict[str, Any]]) -> bool:
        if chairs is None:
            return False

        def _fingerprint(links: List[EventPersonLink]) -> List[Tuple[str, str, str]]:
            return [
                ((link.person.first_name or '').strip(),
                 (link.person.last_name or '').strip(),
                 (link.person.email or '').strip().lower())
                for link in sorted(links, key=lambda l: l.display_order)
            ]

        before_fp = _fingerprint(list(event.person_links))
        desired_links: List[EventPersonLink] = []
        existing_links = {link.person: link for link in event.person_links}
        seen_people = set()
        for order, chair in enumerate(chairs):
            first = (chair.get('first_name') or '').strip()
            last = (chair.get('last_name') or '').strip()
            email = (chair.get('email') or chair.get('emailAddress') or '').strip()
            if not first and not last:
                continue
            if not last:
                last = first or 'Chair'
            affiliation = (chair.get('affiliation') or '').strip()
            person_data = {
                'first_name': first,
                'last_name': last,
                'email': email.lower(),
                'affiliation': affiliation
            }
            person = get_event_person(event, person_data, create_untrusted_persons=True, allow_external=True)
            if person in seen_people:
                continue
            seen_people.add(person)
            db.session.add(person)
            link = existing_links.get(person)
            if not link:
                link = EventPersonLink(event=event, person=person)
            db.session.add(link)
            link.display_order = order
            desired_links.append(link)
        if desired_links:
            event.person_links = desired_links
        else:
            event.person_links = []
        after_fp = _fingerprint(list(event.person_links))
        return before_fp != after_fp

    def _set_status(self, status: str, *, meta: Optional[Dict[str, Any]] = None) -> None:
        self.state['status'] = status
        now_ts = now_utc().isoformat()
        if status == 'running':
            self.state['status_started_at'] = now_ts
            self.state.pop('status_finished_at', None)
        elif status in {'completed', 'failed'}:
            self.state['status_finished_at'] = now_ts
        if meta is not None:
            self.state['status_meta'] = meta
        elif 'status_meta' in self.state:
            self.state.pop('status_meta')
        self.state['last_trigger'] = self.triggered_by
        self.plugin.update_feed_state(self.feed['id'], self.state)

    def _update_progress(self, *, processed: int, total: int, created: int, updated: int,
                         unchanged: int, deleted: int) -> None:
        if self.state.get('status') != 'running':
            return
        meta = self.state.setdefault('status_meta', {})
        meta.update({
            'processed': processed,
            'total': total,
            'created': created,
            'updated': updated,
            'unchanged': unchanged,
            'deleted': deleted,
            'updated_at': now_utc().isoformat()
        })
        self.plugin.update_feed_state(self.feed['id'], self.state)

    def _should_include_item(self, item: Dict[str, Any]) -> Optional[bool]:
        start_info = item.get('startDate') if isinstance(item, dict) else None
        if not start_info:
            return None
        try:
            start_dt = _parse_date(start_info)
        except Exception:  # pragma: no cover - defensive
            return None
        return start_dt >= self.start_threshold

    def _sync_attachments(self, event: Event, normalized: NormalizedEvent) -> bool:
        remote_attachments = self._collect_remote_attachments(normalized)
        event_state = self.events_state.setdefault(normalized.external_id, {})
        attachments_state = event_state.setdefault('attachments', {})
        seen_ids = set()
        changed = False

        for remote_id, remote in remote_attachments.items():
            seen_ids.add(remote_id)
            entry_state = attachments_state.get(remote_id, {})
            attachment = None
            if entry_state.get('attachment_id'):
                attachment = Attachment.get(entry_state['attachment_id'])
                if attachment and attachment.folder.object != event:
                    attachment = None
            folder = self._get_or_create_folder(event, attachments_state, remote.get('folder_key'),
                                                remote['folder_title'], remote['folder_description'])
            if attachment is None:
                attachment = Attachment(folder=folder, user=self.creator, type=AttachmentType.link)
                attachment.title = remote['title']
                attachment.description = remote['description']
                attachment.link_url = remote['url']
                db.session.add(attachment)
                db.session.flush()
                attachments_state[remote_id] = {'attachment_id': attachment.id}
                changed = True
                self._log_attachment_change(event, 'created', remote)
            else:
                updated_fields: List[str] = []
                if attachment.is_deleted:
                    attachment.is_deleted = False
                    updated_fields.append('is_deleted')
                if attachment.folder != folder:
                    attachment.folder = folder
                    updated_fields.append('folder')
                if attachment.title != remote['title']:
                    attachment.title = remote['title']
                    updated_fields.append('title')
                if (attachment.description or '') != remote['description']:
                    attachment.description = remote['description']
                    updated_fields.append('description')
                if attachment.link_url != remote['url']:
                    attachment.link_url = remote['url']
                    updated_fields.append('link_url')
                if attachment.type != AttachmentType.link:
                    attachment.type = AttachmentType.link
                    updated_fields.append('type')
                if entry_state.get('last_hash') != remote['hash']:
                    entry_state['last_hash'] = remote['hash']
                    if not updated_fields:
                        updated_fields.append('fingerprint')
                if updated_fields:
                    changed = True
                    self._log_attachment_change(event, 'updated', remote, updated_fields)
            entry_state = attachments_state.setdefault(remote_id, {})
            entry_state['attachment_id'] = attachment.id
            entry_state['last_hash'] = remote['hash']
            entry_state['last_synced_at'] = self.now.isoformat()
            entry_state['last_seen_at'] = self.now.isoformat()
            entry_state['source_type'] = remote.get('source_type')
            entry_state['folder_title'] = remote.get('folder_title')
            entry_state['folder_key'] = remote.get('folder_key')

        if self.allow_deletions:
            for remote_id in list(attachments_state.keys()):
                if remote_id in seen_ids:
                    continue
                entry_state = attachments_state.pop(remote_id)
                attachment = Attachment.get(entry_state.get('attachment_id')) if entry_state.get('attachment_id') else None
                if attachment and not attachment.is_deleted and attachment.folder.object == event:
                    attachment.is_deleted = True
                    changed = True
                    snapshot = {
                        'id': remote_id,
                        'title': attachment.title or 'Attachment',
                        'url': attachment.link_url,
                        'folder_title': entry_state.get('folder_title') or (attachment.folder.title if attachment.folder.title else None),
                        'folder_description': attachment.folder.description or '',
                        'source_type': entry_state.get('source_type') or 'remote'
                    }
                    self._log_attachment_change(event, 'deleted', snapshot)
        else:
            for entry_state in attachments_state.values():
                entry_state['last_seen_at'] = self.now.isoformat()

        if changed:
            db.session.flush()
        return changed

    def _log_event_action(self, event: Event, action: str, normalized: Optional[NormalizedEvent],
                          changed_fields: Optional[List[str]] = None, *, external_id: Optional[str] = None) -> None:
        feed_id = self.feed.get('id')
        ext_id = external_id or (normalized.external_id if normalized else None)
        data = {'Feed': feed_id}
        if ext_id:
            data['External ID'] = ext_id
        if normalized:
            data['Source title'] = normalized.title
        if changed_fields:
            data['Fields'] = sorted(set(changed_fields))
        if action == 'created':
            kind = LogKind.positive
            message = f'Event created via feed synchronization ({feed_id})'
        elif action == 'updated':
            kind = LogKind.change
            message = f'Event updated via feed synchronization ({feed_id})'
        elif action == 'deleted':
            kind = LogKind.negative
            message = f'Event deleted via feed synchronization ({feed_id})'
        else:
            kind = LogKind.change
            message = f'Event processed via feed synchronization ({feed_id})'
        event.log(EventLogRealm.event, kind, 'Feed Sync', message, self.creator, data=data)
        self._log_admin_feed_action(event, kind, action, feed_id, ext_id)

    def _log_admin_feed_action(self, event: Event, kind: LogKind, action: str, feed_id: str,
                               external_id: Optional[str]) -> None:
        if not event:
            return
        action_label = action.capitalize()
        summary = f'{action_label} event #{event.id} via feed {feed_id}'
        data = {
            'event_id': event.id,
            'event_title': event.title,
            'feed_id': feed_id,
            'action': action,
            'event_url': event.url
        }
        if external_id:
            data['external_id'] = external_id
        AppLogEntry.log(AppLogRealm.admin, kind, 'feed_sync', summary, user=self.creator, data=data)

    def _log_attachment_change(self, event: Event, action: str, remote: Dict[str, Any],
                               changes: Optional[List[str]] = None) -> None:
        feed_id = self.feed.get('id')
        data = {'Feed': feed_id}
        if remote.get('title'):
            data['Title'] = remote['title']
        if remote.get('url'):
            data['URL'] = remote['url']
        if remote.get('folder_title'):
            data['Folder'] = remote['folder_title']
        if remote.get('source_type'):
            data['Kind'] = remote['source_type']
        if changes:
            data['Fields'] = sorted(set(changes))
        if action == 'created':
            kind = LogKind.positive
            message = f'Attachment link created via feed synchronization ({feed_id})'
        elif action == 'updated':
            kind = LogKind.change
            message = f'Attachment link updated via feed synchronization ({feed_id})'
        elif action == 'deleted':
            kind = LogKind.negative
            message = f'Attachment link deleted via feed synchronization ({feed_id})'
        else:
            kind = LogKind.change
            message = f'Attachment link processed via feed synchronization ({feed_id})'
        event.log(EventLogRealm.event, kind, 'Attachment Sync', message, self.creator, data=data)

    def _get_or_create_folder(self, event: Event, attachments_state: Dict[str, Dict[str, Any]],
                              folder_key: Optional[str], title: Optional[str],
                              description: str) -> AttachmentFolder:
        cache_key = f'{event.id}:{folder_key or title or "__default__"}'
        folder = self._folder_cache.get(cache_key)
        if folder:
            if title is not None and folder.title != title:
                folder.title = title
            if description and folder.description != description:
                folder.description = description
            return folder

        if folder_key:
            for state in attachments_state.values():
                if state.get('folder_key') == folder_key and state.get('attachment_id'):
                    existing = Attachment.get(state['attachment_id'])
                    if existing and existing.folder and existing.folder.object == event:
                        folder = existing.folder
                        break

        if folder is None:
            if title:
                folder = AttachmentFolder.get_or_create(event, title=title)
            else:
                folder = AttachmentFolder.get_or_create(event)

        if title is not None and folder.title != title:
            folder.title = title
        if description and folder.description != description:
            folder.description = description
        if folder.id is None:
            db.session.add(folder)
            db.session.flush()
        self._folder_cache[cache_key] = folder
        return folder

    def _collect_remote_attachments(self, normalized: NormalizedEvent) -> Dict[str, Dict[str, Any]]:
        payload = normalized.raw_payload or {}
        results: Dict[str, Dict[str, Any]] = {}
        base_url = normalized.original_url

        def _add_entry(remote_id: str, *, title: str, description: str, url: str,
                       folder_key: str, folder_title: Optional[str], folder_description: str, source_type: str,
                       extra: Optional[Dict[str, Any]] = None) -> None:
            if not url:
                return
            full_url = self._normalize_attachment_url(url, base_url)
            hash_payload = {
                'title': title,
                'description': description,
                'url': full_url,
                'folder': folder_title or '',
                'folder_key': folder_key,
                'source_type': source_type
            }
            if extra:
                hash_payload.update({k: v for k, v in extra.items() if v not in (None, '')})
            remote_hash = hashlib.sha256(json.dumps(hash_payload, sort_keys=True).encode('utf-8')).hexdigest()
            results[remote_id] = {
                'id': remote_id,
                'title': title or 'Attachment',
                'description': description or '',
                'url': full_url,
                'folder_key': folder_key,
                'folder_title': folder_title,
                'folder_description': folder_description or '',
                'hash': remote_hash,
                'source_type': source_type
            }

        for folder in payload.get('folders') or []:
            folder_id = folder.get('id') or 'default'
            folder_title = folder.get('title') or None
            folder_desc = folder.get('description') or ''
            for attachment in folder.get('attachments') or []:
                url = attachment.get('link_url') or attachment.get('download_url')
                if not url:
                    continue
                title = attachment.get('title') or attachment.get('filename') or 'Attachment'
                description = attachment.get('description') or ''
                remote_id = f'folder:{folder_id}:{attachment.get('id') or url}'
                folder_key = f'folder:{folder_id}'
                extra = {
                    'checksum': attachment.get('checksum'),
                    'modified': attachment.get('modified_dt'),
                    'size': attachment.get('size'),
                    'type': attachment.get('type'),
                    'protected': bool(attachment.get('is_protected'))
                }
                _add_entry(remote_id, title=title, description=description, url=url,
                           folder_key=folder_key,
                           folder_title=folder_title, folder_description=folder_desc,
                           source_type=attachment.get('type') or 'file', extra=extra)

        for material in payload.get('material') or []:
            material_id = material.get('id') or material.get('title') or 'material'
            folder_title = material.get('title') or None
            folder_desc = material.get('description') or ''
            for resource in material.get('resources') or []:
                url = resource.get('url')
                if not url:
                    continue
                title = resource.get('name') or resource.get('title') or folder_title or 'Resource'
                description = resource.get('description') or ''
                remote_id = f"material:{material_id}:{resource.get('id') or resource.get('name') or url}"
                folder_key = f'material:{material_id}'
                _add_entry(remote_id, title=title, description=description, url=url,
                           folder_key=folder_key,
                           folder_title=folder_title, folder_description=folder_desc,
                           source_type='material')

        return results

    def _normalize_attachment_url(self, url: str, base_url: str) -> str:
        if not url:
            return url
        return urljoin(base_url, url)

    def _index_timetable_entries(self, event: Event) -> Dict[Tuple[datetime, str], List[TimetableEntry]]:
        index: Dict[Tuple[datetime, str], List[TimetableEntry]] = {}
        for entry in event.timetable_entries:
            if entry.type != TimetableEntryType.BREAK:
                continue
            title = getattr(entry.break_, 'title', '') if entry.break_ else ''
            key = self._timetable_key(entry.start_dt, title)
            index.setdefault(key, []).append(entry)
        return index

    def _timetable_key(self, start_dt: datetime, title: str) -> Tuple[datetime, str]:
        return (start_dt, (title or '').strip())

    def _timetable_key_from_remote(self, remote: Dict[str, Any]) -> Tuple[datetime, str]:
        return self._timetable_key(remote['start_dt'], remote.get('title') or '')

    def _match_existing_timetable_entry(self, index: Dict[Tuple[datetime, str], List[TimetableEntry]],
                                        key: Tuple[datetime, str], used_ids: Set[int]) -> Optional[TimetableEntry]:
        for entry in index.get(key, []):
            if entry.id in used_ids:
                continue
            used_ids.add(entry.id)
            return entry
        return None

    def _deduplicate_timetable_bucket(self, index: Dict[Tuple[datetime, str], List[TimetableEntry]],
                                       key: Tuple[datetime, str], keep_entry: TimetableEntry,
                                       event: Event, remote: Dict[str, Any]) -> None:
        entries = index.get(key, [])
        if not entries:
            index[key] = [keep_entry] if keep_entry else []
            return
        survivors: List[TimetableEntry] = []
        for entry in entries:
            if keep_entry and entry.id == keep_entry.id:
                survivors.append(entry)
                continue
            if self.allow_deletions and entry.event == event:
                db.session.delete(entry)
                self._log_duplicate_timetable_entry(event, entry, remote)
            else:
                survivors.append(entry)
        if keep_entry and all(entry.id != keep_entry.id for entry in survivors):
            survivors.append(keep_entry)
        index[key] = survivors

    def _log_duplicate_timetable_entry(self, event: Event, entry: TimetableEntry, remote: Dict[str, Any]) -> None:
        feed_id = self.feed.get('id')
        data = {
            'Feed': feed_id,
            'RemovedEntryID': entry.id,
            'Title': getattr(entry.break_, 'title', ''),
            'Start': entry.start_dt.isoformat(),
        }
        if hasattr(entry, 'end_dt') and entry.end_dt is not None:
            data['End'] = entry.end_dt.isoformat()
        message = f'Duplicate timetable entry removed via feed synchronization ({feed_id})'
        event.log(EventLogRealm.management, LogKind.change, 'Timetable Sync', message, self.creator, data=data)

    def _sync_timetable(self, event: Event, normalized: NormalizedEvent) -> None:
        timetable_payload = self._fetch_timetable(normalized.external_id)
        if not timetable_payload:
            return
        remote_entries = self._normalize_timetable_entries(timetable_payload)
        event_state = self.events_state.setdefault(normalized.external_id, {})
        schedule_state = event_state.setdefault('timetable', {})
        existing_index = self._index_timetable_entries(event)
        used_entry_ids: Set[int] = set()

        for remote_id, remote in remote_entries.items():
            remote_hash = remote['hash']
            entry_state = schedule_state.get(remote_id)
            key = self._timetable_key_from_remote(remote)
            entry = None
            if entry_state:
                entry = TimetableEntry.get(entry_state.get('entry_id'))
                if entry is not None and entry.event != event:
                    if self.allow_deletions:
                        db.session.delete(entry)
                    entry = None
                if entry is not None:
                    used_entry_ids.add(entry.id)
            if entry is None:
                entry = self._match_existing_timetable_entry(existing_index, key, used_entry_ids)
                if entry is not None:
                    schedule_state[remote_id] = {'entry_id': entry.id, 'last_hash': remote_hash}
            if entry is None:
                entry = self._create_break_entry(event, remote)
                schedule_state[remote_id] = {'entry_id': entry.id, 'last_hash': remote_hash}
                used_entry_ids.add(entry.id)
                self._log_timetable_change(event, 'created', remote)
            else:
                entry_state = schedule_state.setdefault(remote_id, {'entry_id': entry.id})
                if entry_state.get('last_hash') != remote_hash:
                    changes = self._update_break_entry(entry, remote)
                    entry_state['last_hash'] = remote_hash
                    if changes:
                        self._log_timetable_change(event, 'updated', remote, changes)
                else:
                    entry_state['last_hash'] = remote_hash
                used_entry_ids.add(entry.id)

            bucket = existing_index.setdefault(key, [])
            if entry not in bucket:
                bucket.append(entry)
            self._deduplicate_timetable_bucket(existing_index, key, entry, event, remote)

        if self.allow_deletions:
            for remote_id in list(schedule_state.keys()):
                if remote_id not in remote_entries:
                    entry_state = schedule_state.pop(remote_id)
                    entry = TimetableEntry.get(entry_state.get('entry_id'))
                    if entry and entry.event == event:
                        snapshot = {
                            'id': remote_id,
                            'title': getattr(entry.break_, 'title', ''),
                            'start_dt': entry.start_dt,
                            'end_dt': entry.end_dt
                        }
                        db.session.delete(entry)
                        self._log_timetable_change(event, 'deleted', snapshot)

    def _fetch_timetable(self, external_id: str) -> Optional[Dict[str, Any]]:
        fetcher = FeedFetcher(self.feed)
        try:
            return fetcher.fetch_timetable(external_id)
        except Exception as exc:  # pragma: no cover - safety net
            self.logger.warning('[%s] Failed to fetch timetable for %s: %s', self.feed['id'], external_id, exc)
            return None

    def _normalize_timetable_entries(self, payload: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        result: Dict[str, Dict[str, Any]] = {}

        def _collect(container: Any) -> None:
            if isinstance(container, dict):
                if 'startDate' in container and 'endDate' in container:
                    remote_id = container.get('uniqueId') or container.get('id')
                    if not remote_id:
                        return
                    start_dt = _parse_date(container.get('startDate'))
                    end_dt = _parse_date(container.get('endDate')) or start_dt
                    if end_dt <= start_dt:
                        end_dt = start_dt + timedelta(minutes=1)
                    entry = {
                        'id': str(remote_id),
                        'title': _select_entry_title(container),
                        'description': container.get('description') or '',
                        'start_dt': start_dt,
                        'end_dt': end_dt,
                        'location': container.get('location') or '',
                        'room': container.get('room') or '',
                        'inherit_location': container.get('inheritLoc', True),
                    }
                    entry['hash'] = self._build_timetable_hash(entry)
                    result[str(remote_id)] = entry
                for value in container.values():
                    _collect(value)
            elif isinstance(container, list):
                for value in container:
                    _collect(value)

        _collect(payload.get('results', {}))
        return result

    def _build_timetable_hash(self, entry: Dict[str, Any]) -> str:
        payload = {
            'start': entry['start_dt'].isoformat(),
            'end': entry['end_dt'].isoformat(),
            'title': entry['title'],
            'description': entry['description'],
            'location': entry['location'],
            'room': entry['room'],
            'inherit_location': entry['inherit_location']
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode('utf-8')).hexdigest()

    def _create_break_entry(self, event: Event, remote: Dict[str, Any]) -> TimetableEntry:
        duration = remote['end_dt'] - remote['start_dt']
        if duration.total_seconds() <= 0:
            duration = timedelta(minutes=1)
        break_obj = Break(title=remote['title'], duration=duration)
        break_obj.description = remote['description']
        if remote.get('inherit_location'):
            break_obj.inherit_location = True
        else:
            break_obj.inherit_location = False
            break_obj.own_venue_name = remote.get('location') or ''
            break_obj.own_room_name = remote.get('room') or ''
            break_obj.own_address = ''
        entry = TimetableEntry(event=event, type=TimetableEntryType.BREAK, start_dt=remote['start_dt'], break_=break_obj)
        db.session.add(entry)
        db.session.flush()
        return entry

    def _update_break_entry(self, entry: TimetableEntry, remote: Dict[str, Any]) -> List[str]:
        changes: List[str] = []
        if entry.start_dt != remote['start_dt']:
            entry.start_dt = remote['start_dt']
            changes.append('start_dt')
        new_duration = remote['end_dt'] - remote['start_dt']
        if new_duration.total_seconds() <= 0:
            new_duration = timedelta(minutes=1)
        if entry.break_.duration != new_duration:
            entry.break_.duration = new_duration
            changes.append('duration')
        if entry.break_.title != remote['title']:
            entry.break_.title = remote['title']
            changes.append('title')
        if (entry.break_.description or '') != remote['description']:
            entry.break_.description = remote['description']
            changes.append('description')
        inherit = remote.get('inherit_location')
        if bool(entry.break_.inherit_location) != bool(inherit):
            entry.break_.inherit_location = bool(inherit)
            changes.append('location')
        if not entry.break_.inherit_location:
            if (entry.break_.own_venue_name or '') != (remote.get('location') or ''):
                entry.break_.own_venue_name = remote.get('location') or ''
                changes.append('location')
            if (entry.break_.own_room_name or '') != (remote.get('room') or ''):
                entry.break_.own_room_name = remote.get('room') or ''
                changes.append('location')
        else:
            entry.break_.own_venue_name = ''
            entry.break_.own_room_name = ''
        return changes

    def _log_timetable_change(self, event: Event, action: str, remote: Dict[str, Any],
                              changes: Optional[List[str]] = None) -> None:
        feed_id = self.feed.get('id')
        data = {
            'Feed': feed_id,
            'Entry ID': remote.get('id'),
        }
        start_dt = remote.get('start_dt')
        end_dt = remote.get('end_dt')
        if start_dt:
            data['Start'] = start_dt.isoformat()
        if end_dt:
            data['End'] = end_dt.isoformat()
        if remote.get('title'):
            data['Title'] = remote['title']
        if changes:
            data['Fields'] = sorted(set(changes))
        if action == 'created':
            kind = LogKind.positive
            message = f'Timetable entry created via feed synchronization ({feed_id})'
        elif action == 'updated':
            kind = LogKind.change
            message = f'Timetable entry updated via feed synchronization ({feed_id})'
        elif action == 'deleted':
            kind = LogKind.negative
            message = f'Timetable entry deleted via feed synchronization ({feed_id})'
        else:
            kind = LogKind.change
            message = f'Timetable entry processed via feed synchronization ({feed_id})'
        event.log(EventLogRealm.management, kind, 'Timetable Sync', message, self.creator, data=data)


class FeedFetcher:
    def __init__(self, feed: Dict[str, Any]):
        self.feed = feed
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': USER_AGENT})
        self._base = urlsplit(feed['url'])
        token = (feed.get('api_token') or '').strip()
        if token:
            self.session.headers['Authorization'] = f'Bearer {token}'

    def fetch(self) -> Dict[str, Any]:
        url = self._prepare_url()
        try:
            response = self.session.get(url, timeout=REQUEST_TIMEOUT, verify=False)
            response.raise_for_status()
        except requests.RequestException as exc:
            return {'status': 'error', 'message': f'Failed to fetch feed: {exc}'}

        try:
            payload = response.json()
        except ValueError as exc:
            return {'status': 'error', 'message': f'Invalid JSON in feed response: {exc}'}

        items = payload.get('results') or []
        return {'status': 'ok', 'items': items, 'raw': payload}

    def fetch_event_details(self, external_id: Optional[str]) -> Optional[Dict[str, Any]]:
        if not external_id:
            return None
        event_path = f'/export/event/{external_id}.json'
        event_url = urlunsplit((self._base.scheme, self._base.netloc, event_path, '', ''))
        try:
            response = self.session.get(event_url, timeout=REQUEST_TIMEOUT, verify=False)
            response.raise_for_status()
            payload = response.json()
            results = payload.get('results') or []
            return results[0] if results else None
        except requests.RequestException as exc:
            logging.getLogger('indico.plugins.feed_sync').warning('Failed to fetch event %s details: %s',
                                                                 external_id, exc)
        except ValueError as exc:
            logging.getLogger('indico.plugins.feed_sync').warning('Invalid JSON for event %s details: %s',
                                                                 external_id, exc)
        return None

    def fetch_timetable(self, external_id: str) -> Optional[Dict[str, Any]]:
        timetable_path = f'/export/timetable/{external_id}.json'
        timetable_url = urlunsplit((self._base.scheme, self._base.netloc, timetable_path, '', ''))
        try:
            response = self.session.get(timetable_url, timeout=REQUEST_TIMEOUT, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as exc:
            logging.getLogger('indico.plugins.feed_sync').warning('Failed to fetch timetable %s: %s',
                                                                 external_id, exc)
        except ValueError as exc:
            logging.getLogger('indico.plugins.feed_sync').warning('Invalid JSON for timetable %s: %s',
                                                                 external_id, exc)
        return None

    def _prepare_url(self) -> str:
        url = self.feed['url']
        parsed = urlsplit(url)
        query_list = parse_qsl(parsed.query, keep_blank_values=True)
        query_keys = {key for key, _ in query_list}
        if 'limit' not in query_keys:
            limit = self.feed.get('max_items') or DEFAULT_MAX_ITEMS
            if limit:
                query_list.append(('limit', str(limit)))
        query = urlencode(query_list)
        return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, query, parsed.fragment))


# Utility functions -----------------------------------------------------------

def _map_event_type(value: Optional[str]) -> EventType:
    if not value:
        return EventType.conference
    value = value.lower()
    mapping = {
        'lecture': EventType.lecture,
        'meeting': EventType.meeting,
        'conference': EventType.conference,
        'simple_event': EventType.lecture
    }
    return mapping.get(value, EventType.conference)


def _parse_date(data: Optional[Dict[str, Any]]) -> datetime:
    if not data:
        return now_utc()
    date_part = data.get('date')
    time_part = data.get('time') or '00:00:00'
    if not date_part:
        return now_utc()
    if 'T' in time_part:
        iso_fragment = time_part
    else:
        iso_fragment = f"{date_part}T{time_part}"
    try:
        naive = datetime.fromisoformat(iso_fragment)
    except ValueError:
        cleaned_time = time_part.split('.')[0]
        naive = datetime.strptime(f"{date_part} {cleaned_time}", '%Y-%m-%d %H:%M:%S')
    tz_name = data.get('tz') or 'UTC'
    tzinfo = pytz.timezone(tz_name)
    if naive.tzinfo is None:
        localized = tzinfo.localize(naive)
    else:
        localized = naive.astimezone(tzinfo)
    return localized.astimezone(pytz.UTC)


def _split_multi_value(value: Any) -> Optional[List[str]]:
    if value is None:
        return None
    if isinstance(value, list):
        return [str(x).strip() for x in value if x]
    if isinstance(value, str):
        if not value.strip():
            return []
        parts = re.split(r'[;,\n]+', value)
        return [part.strip() for part in parts if part.strip()]
    return [str(value).strip()]


def _select_entry_title(entry: Dict[str, Any]) -> str:
    title = (entry.get('title') or '').strip()
    slot_title = (entry.get('slotTitle') or '').strip()
    if slot_title:
        if not title:
            return slot_title
        if title.isdigit() and not slot_title.isdigit():
            return slot_title
        if len(slot_title) > len(title) and not slot_title.isdigit():
            return slot_title
    if title:
        return title
    if slot_title:
        return slot_title
    if entry.get('code'):
        return str(entry['code'])
    if entry.get('entryType'):
        return str(entry['entryType'])
    return 'Block'


def _rewrite_relative_urls(html: str, base_url: str) -> str:
    if not html or not base_url:
        return html

    def _replace(match: re.Match) -> str:
        prefix, url = match.groups()
        stripped = url.strip()
        if stripped.startswith(('http://', 'https://', '//', 'data:', 'mailto:')):
            return match.group(0)
        absolute = urljoin(base_url, stripped)
        return f"{prefix}{absolute}"

    pattern = re.compile(r"(\b(?:src|href)=['\"])([^'\"]+)", re.IGNORECASE)
    return pattern.sub(_replace, html)


def _build_metadata_block(item: Dict[str, Any]) -> str:
    meta_items: List[Tuple[str, Any]] = []

    def add(label: str, value: Any) -> None:
        if value not in (None, '', [], {}):
            meta_items.append((label, value))

    add('Category', item.get('category'))
    add('Start', _format_datetime(item.get('startDate')))
    add('End', _format_datetime(item.get('endDate')))
    add('Timezone', item.get('timezone') or item.get('startDate', {}).get('tz'))
    add('Organizer', item.get('organizer'))
    add('Location', item.get('location'))
    add('Room', item.get('room'))
    add('Address', item.get('address'))
    add('Language', item.get('language'))
    visibility = item.get('visibility')
    if isinstance(visibility, dict):
        add('Visibility', visibility.get('name'))
    else:
        add('Visibility', visibility)
    keywords = item.get('keywords')
    if keywords:
        add('Keywords', ', '.join(keywords))

    if not meta_items:
        return ''

    rows = ''.join(
        f"<li><strong>{escape(label)}:</strong> {escape(str(value))}</li>"
        for label, value in meta_items
    )
    return f"<h3>Event details</h3><ul>{rows}</ul>"


def _build_references_block(references: List[Dict[str, Any]]) -> str:
    links = []
    for ref in references:
        url = ref.get('url') or ref.get('value')
        if not url:
            continue
        title = ref.get('title') or ref.get('value') or url
        links.append(
            "<li><a href='{url}' target='_blank' rel='noreferrer'>{title}</a></li>".format(
                url=escape(url), title=escape(title)
            )
        )
    if not links:
        return ''
    return f"<h3>Related links</h3><ul>{''.join(links)}</ul>"


def _format_datetime(data: Optional[Dict[str, Any]]) -> str:
    if not data:
        return ''
    date = data.get('date')
    time = data.get('time')
    if date and time:
        return f"{date} {time}"
    return date or ''


__all__ = (
    'FeedSyncCoordinator',
)
