-- Creates a table if not exists
CREATE TABLE IF NOT EXISTS users(
        id INTEGER AUTO_INCREMENT NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
        PRIMARY KEY (id)
)
