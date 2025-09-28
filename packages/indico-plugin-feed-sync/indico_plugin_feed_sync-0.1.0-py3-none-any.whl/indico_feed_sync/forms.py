from __future__ import annotations

import json
import re
from typing import Any, Dict, List

from wtforms import IntegerField, TextAreaField
from wtforms.validators import NumberRange, Optional, ValidationError

from indico.util.i18n import _
from indico.web.forms.base import IndicoForm


_SLUG_RE = re.compile(r'^[a-z0-9][a-z0-9_-]*$')
VALID_EVENT_TYPES = {'lecture', 'meeting', 'conference'}


class FeedsJSONField(TextAreaField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parsed_data: List[Dict[str, Any]] = []

    def process_data(self, value):
        if isinstance(value, str):
            self.data = value
            try:
                self.parsed_data = json.loads(value) if value else []
            except ValueError:
                self.parsed_data = []
        else:
            self.parsed_data = value or []
            self.data = json.dumps(self.parsed_data, indent=2, ensure_ascii=False) if self.parsed_data else ''

    def process_formdata(self, valuelist):
        raw = valuelist[0] if valuelist else ''
        self.data = raw

    def set_parsed(self, feeds: List[Dict[str, Any]]):
        self.parsed_data = feeds
        self.data = json.dumps(feeds, indent=2, ensure_ascii=False) if feeds else ''


class FeedSettingsForm(IndicoForm):
    feeds = FeedsJSONField(
        label=_('Feeds (JSON)'),
        validators=[Optional()],
        description=_('JSON list of feed definitions. Each entry must contain "id", "title", "url" and '
                      '"category_id". Optional keys: "enabled", "event_type", "allow_updates", "allow_deletions", '
                      '"use_event_details", API credentials ("api_token" is sent as an Authorization Bearer header), '
                      '"max_items" (override the default page size for the remote feed).')
    )
    poll_interval_minutes = IntegerField(
        label=_('Automatic sync interval (minutes)'),
        validators=[NumberRange(min=5)],
        default=60,
        description=_('Interval used by periodic background jobs. This does not schedule jobs on its own; '
                      'it provides a hint for external schedulers.')
    )
    creator_user_id = IntegerField(
        label=_('Creator user ID'),
        validators=[Optional()],
        description=_('Optional user ID used as the creator for imported events. Leave empty to use the system user.')
    )

    def validate_feeds(self, field: FeedsJSONField) -> None:  # type: ignore[override]
        raw = (field.data or '').strip()
        if not raw:
            parsed: List[Dict[str, Any]] = []
        else:
            try:
                parsed = json.loads(raw)
            except ValueError as exc:
                raise ValidationError(_('Invalid JSON: {error}').format(error=exc)) from exc

        if not isinstance(parsed, list):
            raise ValidationError(_('Expected a list of feed definitions.'))

        seen_ids: set[str] = set()
        sanitized: List[Dict[str, Any]] = []
        for item in parsed:
            if not isinstance(item, dict):
                raise ValidationError(_('Each feed entry must be an object.'))
            missing = [key for key in ('id', 'title', 'url', 'category_id') if key not in item]
            if missing:
                raise ValidationError(_('Feed entry is missing required keys: {keys}').format(keys=', '.join(missing)))
            feed_id = str(item['id']).strip().lower()
            if not _SLUG_RE.match(feed_id):
                raise ValidationError(_('Invalid feed id "{feed_id}". Use lowercase letters, digits, dash or underscore.').
                                      format(feed_id=feed_id))
            if feed_id in seen_ids:
                raise ValidationError(_('Duplicate feed id "{feed_id}".').format(feed_id=feed_id))
            seen_ids.add(feed_id)
            enabled = self._parse_bool(item.get('enabled', True))
            allow_updates = self._parse_bool(item.get('allow_updates', True))
            allow_deletions = self._parse_bool(item.get('allow_deletions', True))
            use_event_details = self._parse_bool(item.get('use_event_details', True))
            event_type = (item.get('event_type') or 'conference').lower()
            if event_type not in VALID_EVENT_TYPES:
                raise ValidationError(_('Invalid event type "{event_type}".').format(event_type=event_type))
            category_id = item.get('category_id')
            if category_id in (None, ''):
                raise ValidationError(_('Feed "{feed_id}" is missing a category_id.').format(feed_id=feed_id))
            try:
                category_id = int(category_id)
            except (TypeError, ValueError):
                raise ValidationError(_('Feed "{feed_id}" has an invalid category_id.').format(feed_id=feed_id))
            max_items_raw = item.get('max_items')
            if max_items_raw in (None, ''):
                max_items = None
            else:
                try:
                    max_items = int(max_items_raw)
                except (TypeError, ValueError):
                    raise ValidationError(_('Feed "{feed_id}" has an invalid max_items value.').format(feed_id=feed_id))
                if max_items <= 0:
                    raise ValidationError(_('Feed "{feed_id}" requires a positive max_items value.').format(feed_id=feed_id))

            sanitized.append({
                'id': feed_id,
                'title': str(item['title']).strip(),
                'url': str(item['url']).strip(),
                'category_id': category_id,
                'enabled': enabled,
                'event_type': event_type,
                'allow_updates': allow_updates,
                'allow_deletions': allow_deletions,
                'use_event_details': use_event_details,
                'api_token': (item.get('api_token') or '').strip() or None,
                'api_key': (item.get('api_key') or '').strip() or None,
                'api_secret': (item.get('api_secret') or '').strip() or None,
                'max_items': max_items,
            })
        field.set_parsed(sanitized)

    @property
    def data(self):  # type: ignore[override]
        data = super().data
        data['feeds'] = self.feeds.parsed_data
        return data

    @staticmethod
    def _parse_bool(value: Any) -> bool:
        if isinstance(value, bool):
            return value
        if value in (None, ''):
            return False
        if isinstance(value, (int, float)):
            return bool(value)
        value = str(value).strip().lower()
        if value in {'1', 'true', 'yes', 'y', 'on'}:
            return True
        if value in {'0', 'false', 'no', 'n', 'off'}:
            return False
        return True

    def set_defaults(self, **kwargs):  # compatibility helper to satisfy mypy
        super().set_defaults(**kwargs)
