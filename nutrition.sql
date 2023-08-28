-- Создаем таблицу питания
CREATE TABLE IF NOT EXISTS nutrition (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    meal_type TEXT NOT NULL,
    weight INTEGER NOT NULL,
    date_meal TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES clients (id)
);
