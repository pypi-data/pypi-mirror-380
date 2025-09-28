# Indico Feed Sync Plugin

Synchronizes events from external Indico feeds into this instance.

## Features

- **Configurable feeds** – each feed can target a different category and control whether updates, deletions, detailed event exports and a `startdate_day` cutoff are used.
- **Event mirroring** – new, updated or deleted events in the remote feed are reflected locally, including timetable blocks and event log entries.
- **Attachment links** – remote attachments (files, links, material resources) are linked into the cloned event without copying the binary content.
- **Manual and scheduled synchronization** – feeds can be refreshed on demand from the admin UI or periodically by Celery beat.
- **Progress tracking** – the admin status table shows queued/running/completed states, per-action counters and Celery task IDs for queued jobs.
- **Background force sync** – “Force sync” actions enqueue Celery jobs so the UI responds instantly; errors are logged and mirrored in the status column.
- **Audit logging** – every create/update/delete is also recorded in Admin → Logs with the feed id, action type, local event id/title and remote external id for easy auditing.

## Usage Example

1. **Add feeds in plugin settings** – open Admin → Plugins → Feed Sync, edit the JSON, and define the feed URL, target category ID, flags (e.g. `allow_updates`, `allow_deletions`), plus an optional `startdate_day` (defaults to `-30` meaning “only events starting within the last 30 days or later”).
2. **Manual refresh** – click “Refresh now” for incremental updates, or “Force sync” to re-import everything; watch the progress status in the table.
3. **Background queue** – “Force sync” queues a Celery job; monitor its progress in the admin status column or in the Celery log.
4. **Timetable & attachments** – the plugin automatically copies timetable blocks and exposes external attachments as links so attendees see the same agenda and files.

## Notes

- Requires a running Celery worker and Redis broker; without them “Force sync” fails immediately with an error message.
- Progress data lives in `feed_state`; if you edit the JSON manually, keep feed IDs consistent.
- Regular (non-force) sync still runs synchronously for quick incremental updates.
- The `startdate_day` filter only affects new synchronizations; older events that already exist locally are left untouched even if they fall outside the window.
- Enable the plugin in your `indico.conf` (or `.indico.conf`) by adding `PLUGINS = {'feed_sync'}` and restarting the services.
