-- HIGH-RISK TEST ONLY
-- This migration is intentionally designed to test SecurePR's
-- destructive database change detection.

ALTER TABLE users DROP COLUMN status;