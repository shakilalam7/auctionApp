-- Create notifications table
CREATE TABLE IF NOT EXISTS api_notification (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    notification_type VARCHAR(20) NOT NULL,
    title VARCHAR(200) NOT NULL,
    message TEXT NOT NULL,
    link VARCHAR(200),
    is_read BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES api_user (id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_notification_user ON api_notification(user_id);
CREATE INDEX IF NOT EXISTS idx_notification_created ON api_notification(created_at);
CREATE INDEX IF NOT EXISTS idx_notification_read ON api_notification(is_read);
