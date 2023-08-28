--Данные о калориях--
CREATE TABLE IF NOT EXISTS calories (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  user_id INTEGER NOT NULL,
  calories INTEGER NOT NULL,
  date_meal TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES clients (id)
);