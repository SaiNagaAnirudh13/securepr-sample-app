-- Medium-risk test: schema change for user account status.
-- This change modifies the database structure and should be reviewed.

ALTER TABLE users
ADD COLUMN status VARCHAR(20) DEFAULT 'active';

-- Existing records will receive the default status.
-- Application code must handle the new status field.