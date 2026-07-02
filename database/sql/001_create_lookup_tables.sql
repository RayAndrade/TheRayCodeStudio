PRAGMA foreign_keys = ON;

CREATE TABLE Language
(
    language_id   INTEGER PRIMARY KEY,
    language_name TEXT NOT NULL UNIQUE
);

CREATE TABLE Category
(
    category_id   INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE Pattern
(
    pattern_id   INTEGER PRIMARY KEY,
    pattern_name TEXT NOT NULL UNIQUE
);

CREATE TABLE Segment
(
    segment_id    INTEGER PRIMARY KEY,
    segment_name  TEXT NOT NULL UNIQUE,
    display_order INTEGER NOT NULL
);

CREATE TABLE Platform
(
    platform_id   INTEGER PRIMARY KEY,
    platform_name TEXT NOT NULL UNIQUE
);
