--Данные о продуктах--
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  product TEXT NOT NULL,
  fats REAL NOT NULL,
  proteins REAL NOT NULL,
  carbohydrates REAL NOT NULL,
  calories INTEGER NOT NULL
);