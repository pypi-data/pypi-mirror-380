from __future__ import annotations

from flask import flash, jsonify, redirect, request
from werkzeug.exceptions import NotFound

from indico.core.plugins import plugin_engine
from indico.modules.admin import RHAdminBase
from indico.modules.events.management.controllers.base import RHManageEventBase
from indico.util.i18n import _
from indico.web.flask.util import url_for
from indico.web.flask.wrappers import IndicoBlueprint

from .tasks import sync_all_task, sync_feed_task
from .util import FeedSyncCoordinator


blueprint = IndicoBlueprint('plugin_feed_sync', __name__, url_prefix='/plugin/feed-sync')


class RHFeedSyncBase(RHAdminBase):
    plugin_name = 'feed_sync'

    def _process_args(self):
        self.plugin = plugin_engine.get_plugin(self.plugin_name)
        if not self.plugin:
            raise NotFound(_('Feed sync plugin is not available'))

    def _json_requested(self) -> bool:
        if request.is_json:
            return True
        best = request.accept_mimetypes.best
        return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']

    def _redirect_with_flash(self, result: dict):
        status = result.get('status', 'ok')
        message = result.get('message') or _('Feed synchronization finished.')
        flash(message, 'success' if status == 'ok' else 'error')
        return redirect(url_for('plugins.details', plugin=self.plugin_name))


class RHRefreshFeed(RHFeedSyncBase):
    CSRF_ENABLED = True

    def _process(self):  # type: ignore[override]
        feed_id = request.view_args['feed_id']
        force = request.args.get('force') == '1'
        if force:
            try:
                with self.plugin.plugin_context():
                    async_result = sync_feed_task.delay(feed_id, force=True, triggered_by='manual-force')
                    task_id = async_result.id
                    self.plugin.mark_feed_queued(feed_id, task_id, triggered_by='manual-force')
            except Exception as exc:  # pragma: no cover - defensive
                with self.plugin.plugin_context():
                    self.plugin.mark_feed_failed(feed_id, str(exc))
                self.plugin.logger.exception('Failed to enqueue force sync for feed %s', feed_id)
                message = _('Failed to queue force sync for feed {feed}: {error}').format(feed=feed_id, error=exc)
                if self._json_requested():
                    return jsonify({'status': 'error', 'message': message}), 500
                flash(message, 'error')
                return redirect(url_for('plugins.details', plugin=self.plugin_name))

            message = _('Force sync queued for feed "{feed}".').format(feed=feed_id)
            if self._json_requested():
                return jsonify({'status': 'accepted', 'message': message, 'task_id': task_id}), 202
            flash(message, 'info')
            return redirect(url_for('plugins.details', plugin=self.plugin_name))

        with self.plugin.plugin_context():
            coordinator = FeedSyncCoordinator(self.plugin)
            result = coordinator.sync_single_feed(feed_id, triggered_by='manual', force=False)
        if self._json_requested():
            status = result.get('status', 'ok')
            payload = dict(result)
            if status == 'ok':
                payload['redirect'] = url_for('plugins.details', plugin=self.plugin_name)
            return jsonify(payload), (200 if status == 'ok' else 400)
        return self._redirect_with_flash(result)


class RHRefreshAll(RHFeedSyncBase):
    CSRF_ENABLED = True

    def _process(self):  # type: ignore[override]
        force = request.args.get('force') == '1'
        if force:
            try:
                with self.plugin.plugin_context():
                    async_result = sync_all_task.delay(force=True, triggered_by='manual-force')
                    task_id = async_result.id
                    for feed in self.plugin.get_active_feeds():
                        self.plugin.mark_feed_queued(feed['id'], task_id, triggered_by='manual-force')
            except Exception as exc:  # pragma: no cover - defensive
                with self.plugin.plugin_context():
                    self.plugin.mark_all_feeds_failed(str(exc))
                self.plugin.logger.exception('Failed to enqueue force sync for all feeds')
                message = _('Failed to queue force sync for all feeds: {error}').format(error=exc)
                if self._json_requested():
                    return jsonify({'status': 'error', 'message': message}), 500
                flash(message, 'error')
                return redirect(url_for('plugins.details', plugin=self.plugin_name))

            message = _('Force sync queued for all feeds.')
            if self._json_requested():
                return jsonify({'status': 'accepted', 'message': message, 'task_id': task_id}), 202
            flash(message, 'info')
            return redirect(url_for('plugins.details', plugin=self.plugin_name))

        with self.plugin.plugin_context():
            coordinator = FeedSyncCoordinator(self.plugin)
            result = coordinator.sync_all_feeds(triggered_by='manual', force=False)
        if self._json_requested():
            status = result.get('status', 'ok')
            payload = dict(result)
            if status == 'ok':
                payload['redirect'] = url_for('plugins.details', plugin=self.plugin_name)
            return jsonify(payload), (200 if status == 'ok' else 400)
        return self._redirect_with_flash(result)


class RHRefreshEvent(RHManageEventBase):
    CSRF_ENABLED = True

    def _process_args(self):  # type: ignore[override]
        super()._process_args()
        self.plugin = plugin_engine.get_plugin('feed_sync')
        if not self.plugin:
            raise NotFound(_('Feed sync plugin is not available'))

    def _process(self):  # type: ignore[override]
        feed_id = self.plugin.find_feed_by_event(self.event.id)
        if not feed_id:
            message = _('This event is not managed by the feed sync plugin.')
            if request.is_json:
                return jsonify({'status': 'error', 'message': message}), 404
            flash(message, 'error')
            return redirect(self.event.url)

        try:
            with self.plugin.plugin_context():
                async_result = sync_feed_task.delay(feed_id, force=True, triggered_by='event-force')
                task_id = async_result.id
                self.plugin.mark_feed_queued(feed_id, task_id, triggered_by='event-force')
        except Exception as exc:  # pragma: no cover - defensive
            with self.plugin.plugin_context():
                self.plugin.mark_feed_failed(feed_id, str(exc))
            self.plugin.logger.exception('Failed to enqueue force sync for event %s', self.event)
            message = _('Failed to queue event sync: {error}').format(error=exc)
            if request.is_json:
                return jsonify({'status': 'error', 'message': message}), 500
            flash(message, 'error')
            return redirect(self.event.url)

        message = _('Event sync queued.')
        if request.is_json:
            return jsonify({'status': 'accepted', 'message': message, 'task_id': task_id}), 202
        flash(message, 'info')
        return redirect(self.event.url)


blueprint.add_url_rule('/feeds/<string:feed_id>/refresh', 'refresh_feed', RHRefreshFeed, methods=('POST',))
blueprint.add_url_rule('/feeds/refresh-all', 'refresh_all', RHRefreshAll, methods=('POST',))
blueprint.add_url_rule('/events/<int:event_id>/refresh', 'refresh_event', RHRefreshEvent, methods=('POST',))


__all__ = ("blueprint",)
