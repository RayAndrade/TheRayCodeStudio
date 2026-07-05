This is directory for theraycode.db

To access the SQLite db 

```
$ sqlite3 theraycode.db
```

```
.tables
```
Category        Implementation  Pattern         Segment         YouTubeVideo  
Clip            Language        Platform        VimeoVideo    

```
.schema Category
```
CREATE TABLE Category
(
    category_id   INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
);

```
SELECT * FROM Category;
```
1|Creational
2|Structural
3|Behavioral
```
.schema Implementation
```
CREATE TABLE Implementation
(
    implementation_id INTEGER PRIMARY KEY,

    language_id       INTEGER NOT NULL,
    category_id       INTEGER NOT NULL,
    pattern_id        INTEGER NOT NULL,

    version           INTEGER NOT NULL DEFAULT 1,

    title             TEXT NOT NULL,
    notes             TEXT,

    created_at        TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at        TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(language_id)
        REFERENCES Language(language_id),

    FOREIGN KEY(category_id)
        REFERENCES Category(category_id),

    FOREIGN KEY(pattern_id)
        REFERENCES Pattern(pattern_id),

    UNIQUE(language_id, pattern_id, version)
);
```
SELECT * FROM Implementation;
```
1|1|1|1|1|TRCStudio First Record|Created from Version 4.|2026-06-30 22:07:11|2026-06-30 22:07:11
2|3|2|2|1|Just a title||2026-07-01 22:42:58|2026-07-01 22:42:58
3|2|3|1|1|xxx||2026-07-03 13:54:40|2026-07-03 13:54:40
sqlite> 

```
.schema Pattern
```
CREATE TABLE Pattern
(
    pattern_id   INTEGER PRIMARY KEY,
    pattern_name TEXT NOT NULL UNIQUE
);

```
SELECT * FROM Pattern;
```
1|Abstract Factory
2|Builder
3|Factory Method
4|Prototype
5|Singleton
6|Adapter
7|Bridge
8|Composite
9|Decorator
10|Facade
11|Flyweight
12|Proxy
13|Chain of Responsibility
14|Command
15|Interpreter
16|Iterator
17|Mediator
18|Memento
19|Observer
20|State
21|Strategy
22|Template Method
23|Visitor
```
.schema Segment
```
CREATE TABLE Segment
(
    segment_id    INTEGER PRIMARY KEY,
    segment_name  TEXT NOT NULL UNIQUE,
    display_order INTEGER NOT NULL
);
```
SELECT * FROM Segment;
```
1|Open|1
2|Why|2
3|UML|3
4|Code|4
5|Mid|5
6|SWOT|6
7|Close|7
8|Full|8

```
.schema YouTubeVideo
```
REATE TABLE YouTubeVideo
(
    youtube_video_id  INTEGER PRIMARY KEY,

    implementation_id INTEGER NOT NULL,

    youtube_share_url TEXT,
    publish_date      TEXT,
    notes             TEXT,

    FOREIGN KEY(implementation_id)
        REFERENCES Implementation(implementation_id)
);
```
SELECT * FROM Clip;
```
```
.schema Language
```
CREATE TABLE Language
(
    language_id   INTEGER PRIMARY KEY,
    language_name TEXT NOT NULL UNIQUE
);
```
SELECT * FROM Language;
```
1|C++
2|C#
3|Java
4|JavaScript
5|PHP
6|Python
7|English
8|Portuguese
9|German
```
.schema Platform
```
CREATE TABLE Platform
(
    platform_id   INTEGER PRIMARY KEY,
    platform_name TEXT NOT NULL UNIQUE
);
```
SELECT * FROM Platform;
```
1|YouTube
2|Vimeo
3|GitHub
4|Facebook
5|X
6|LinkedIn
7|Instagram
8|Website
9|Newsletter
```
SELECT * FROM VimeoVideo;
```

```
.tables
```
Category        Implementation  Pattern         Segment         YouTubeVideo  
Clip            Language        Platform        VimeoVideo    

```
