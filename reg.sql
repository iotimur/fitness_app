PRAGMA foreign_keys = ON;

--Данные о пользователе--
CREATE TABLE IF NOT EXISTS clients (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  login TEXT NOT NULL,
  password TEXT NOT NULL
);