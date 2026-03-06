DROP TABLE IF EXISTS quizes;

CREATE TABLE quizes (
    titel TEXT PRIMARY KEY,
    frage TEXT NOT NULL,
    a1 TEXT NOT NULL,
    a2 TEXT NOT NULL,
    a3 TEXT NOT NULL,
);