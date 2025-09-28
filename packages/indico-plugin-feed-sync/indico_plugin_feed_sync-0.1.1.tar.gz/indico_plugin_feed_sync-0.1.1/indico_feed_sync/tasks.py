from __future__ import annotations

from indico.core.celery import celery
from indico.core.plugins import plugin_engine

from .util import FeedSyncCoordinator


@celery.task(name='feed_sync.sync_feed')
def sync_feed_task(feed_id: str, *, force: bool = False, triggered_by: str = 'celery') -> dict:
    plugin = plugin_engine.get_plugin('feed_sync')
    if not plugin:
        return {'status': 'error', 'message': 'feed_sync plugin is not loaded'}
    with plugin.plugin_context():
        coordinator = FeedSyncCoordinator(plugin)
        return coordinator.sync_single_feed(feed_id, triggered_by=triggered_by, force=force)


@celery.task(name='feed_sync.sync_all')
def sync_all_task(*, force: bool = False, triggered_by: str = 'celery') -> dict:
    plugin = plugin_engine.get_plugin('feed_sync')
    if not plugin:
        return {'status': 'error', 'message': 'feed_sync plugin is not loaded'}
    with plugin.plugin_context():
        coordinator = FeedSyncCoordinator(plugin)
        return coordinator.sync_all_feeds(triggered_by=triggered_by, force=force)
