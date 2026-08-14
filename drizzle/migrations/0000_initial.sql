-- Aether Core — initial schema (MySQL 8+ / TiDB compatible)
CREATE TABLE IF NOT EXISTS `users` (
  `id` varchar(64) NOT NULL,
  `email` varchar(255) NOT NULL,
  `display_name` varchar(128) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`),
  KEY `idx_users_email` (`email`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `journeys` (
  `user_id` varchar(64) NOT NULL,
  `step` int NOT NULL DEFAULT 1,
  `completed_at` json NOT NULL,
  `certificate_issued` boolean NOT NULL DEFAULT FALSE,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  KEY `idx_journeys_user` (`user_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `telemetry` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t` float NOT NULL,
  `schumann` float NOT NULL,
  `coherence` float NOT NULL,
  `entropy` float NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_telemetry_time` (`t`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `characters` (
  `id` varchar(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  `gender` varchar(8) NOT NULL,
  `attributes` json NOT NULL,
  `created` varchar(16) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_characters_name` (`name`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
