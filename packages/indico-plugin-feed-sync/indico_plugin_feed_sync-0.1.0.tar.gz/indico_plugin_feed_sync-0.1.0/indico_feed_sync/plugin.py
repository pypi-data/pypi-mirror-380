from __future__ import annotations

from typing import Any, Dict, List, Optional

from celery.schedules import crontab

from indico.core import signals
from indico.core.celery import celery
from indico.core.plugins import IndicoPlugin, PluginCategory, render_plugin_template
from indico.util.i18n import _

from .blueprint import blueprint
from .forms import FeedSettingsForm


class FeedSyncPlugin(IndicoPlugin):
    """Synchronize external Indico feeds into local events."""

    configurable = True
    category = PluginCategory.importers
    settings_form = FeedSettingsForm
    default_settings = {
        'feeds': [
            {
                'id': 'dkf-hpc',
                'title': 'DKF HPC feed',
                'url': 'https://konferencia.dkf.hu/export/categ/3.json',
                'category_id': None,
                'enabled': False,
                'event_type': 'conference',
                'allow_updates': True,
                'allow_deletions': True,
                'use_event_details': True,
                'startdate_day': -30
            }
        ],
        'feed_state': {},
        'poll_interval_minutes': 60,
        'creator_user_id': None
    }
    #: widen the JSON textarea a bit
    settings_form_field_opts = {'feeds': {'style': 'font-family: monospace;', 'rows': 12}}

    def init(self) -> None:
        super().init()
        self.template_hook('plugin-details', self._inject_details_panel)
        self.template_hook('event-actions', self._inject_event_action)
        self.template_hook('event-header', self._inject_display_action)
        self.template_hook('conference-header-right-column', self._inject_display_action)
        self.connect(signals.core.import_tasks, self._ensure_tasks_imported)
        self._ensure_periodic_task()

    # Helpers -----------------------------------------------------------------

    # Template hooks ----------------------------------------------------------

    def _inject_details_panel(self, plugin, **kwargs) -> str:
        if plugin != self:
            return ''
        feeds = self.settings.get('feeds') or []
        feed_state = self.settings.get('feed_state') or {}
        poll_interval = self.settings.get('poll_interval_minutes')
        return render_plugin_template('indico_feed_sync/details_extra.html', plugin=self, feeds=feeds,
                                      feed_state=feed_state, poll_interval=poll_interval)

    def _inject_event_action(self, event=None, user=None, **kwargs) -> str:
        from flask import g, session
        from indico.web.flask.util import url_for

        event = event or kwargs.get('event')
        if event is None:
            return ''

        user = user or kwargs.get('user') or getattr(g, 'user', None) or getattr(session, 'user', None)
        if user is None or not event.can_manage(user):
            return ''

        feed_state = self.settings.get('feed_state') or {}
        feed_id = self.find_feed_by_event(event.id)
        if not feed_id:
            return ''

        refresh_url = url_for('plugin_feed_sync.refresh_event', event_id=event.id)
        return render_plugin_template('indico_feed_sync/event_action_button.html', refresh_url=refresh_url,
                                      event=event, feed_id=feed_id)

    def _inject_display_action(self, event=None, user=None, **kwargs) -> str:
        from flask import g, session
        from indico.web.flask.util import url_for

        event = event or kwargs.get('event')
        if event is None:
            return ''

        user = user or kwargs.get('user') or getattr(g, 'user', None) or getattr(session, 'user', None)
        if user is None or not event.can_manage(user):
            return ''

        feed_id = self.find_feed_by_event(event.id)
        if not feed_id:
            return ''

        refresh_url = url_for('plugin_feed_sync.refresh_event', event_id=event.id)
        return render_plugin_template('indico_feed_sync/display_action_button.html', refresh_url=refresh_url,
                                      event=event, feed_id=feed_id)

    def find_feed_by_event(self, event_id: int) -> Optional[str]:
        state = self.settings.get('feed_state') or {}
        for feed_id, data in state.items():
            events = data.get('events', {}) if isinstance(data, dict) else {}
            for entry in events.values():
                if isinstance(entry, dict) and entry.get('event_id') == event_id:
                    return feed_id
        return None

    # Signals -----------------------------------------------------------------

    def _ensure_tasks_imported(self, sender, **kwargs) -> None:
        # Importing tasks registers them with Celery
        from . import tasks  # noqa: F401

    def _ensure_periodic_task(self) -> None:
        schedule = dict(celery.conf.beat_schedule or {})
        schedule.setdefault(
            'feed_sync_sync_all',
            {
                'task': 'feed_sync.sync_all',
                'schedule': crontab(minute=0),  # hourly at :00
                'options': {'expires': 55 * 60}
            }
        )
        celery.conf.beat_schedule = schedule

    # Utility -----------------------------------------------------------------

    def get_feed(self, feed_id: str) -> Optional[Dict[str, Any]]:
        for feed in self.settings.get('feeds') or []:
            if feed.get('id') == feed_id:
                return feed
        return None

    def reset_feed_state(self, feed_id: str) -> None:
        state = self.settings.get('feed_state') or {}
        feed_state = state.get(feed_id)
        if not feed_state:
            return
        for event_state in feed_state.get('events', {}).values():
            event_state['last_hash'] = None
            timetable_state = event_state.get('timetable') or {}
            for block_state in timetable_state.values():
                if isinstance(block_state, dict):
                    block_state['last_hash'] = None
            attachment_state = event_state.get('attachments') or {}
            for link_state in attachment_state.values():
                if isinstance(link_state, dict):
                    link_state['last_hash'] = None
        feed_state['last_error'] = None
        state[feed_id] = feed_state
        self.settings.set('feed_state', state)

    def mark_feed_queued(self, feed_id: str, task_id: str, *, triggered_by: str) -> None:
        state = self.settings.get('feed_state') or {}
        feed_state = state.get(feed_id) or {}
        feed_state['status'] = 'queued'
        feed_state['status_meta'] = {'task_id': task_id}
        feed_state.pop('status_started_at', None)
        feed_state.pop('status_finished_at', None)
        feed_state['last_error'] = None
        feed_state['last_trigger'] = triggered_by
        state[feed_id] = feed_state
        self.settings.set('feed_state', state)

    def mark_feed_failed(self, feed_id: str, error: str) -> None:
        state = self.settings.get('feed_state') or {}
        feed_state = state.get(feed_id) or {}
        feed_state['status'] = 'failed'
        feed_state['status_meta'] = {'message': error}
        feed_state['last_error'] = error
        state[feed_id] = feed_state
        self.settings.set('feed_state', state)

    def mark_all_feeds_failed(self, error: str) -> None:
        for feed in self.settings.get('feeds') or []:
            self.mark_feed_failed(feed['id'], error)

    def get_active_feeds(self) -> List[Dict[str, Any]]:
        return [feed for feed in (self.settings.get('feeds') or []) if feed.get('enabled')]

    def update_feed_state(self, feed_id: str, state: Dict[str, Any]) -> None:
        stored_state = self.settings.get('feed_state') or {}
        stored_state[feed_id] = state
        self.settings.set('feed_state', stored_state)

    def get_feed_state(self, feed_id: str) -> Dict[str, Any]:
        stored_state = self.settings.get('feed_state') or {}
        return stored_state.get(feed_id, {})

    def get_blueprints(self):
        return blueprint


__all__ = ("FeedSyncPlugin",)
