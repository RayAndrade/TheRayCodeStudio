PRAGMA foreign_keys = ON;

------------------------------------------------------------
-- Implementation
------------------------------------------------------------
DROP TABLE IF EXISTS Implementation;

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

------------------------------------------------------------
-- Clip
------------------------------------------------------------
DROP TABLE IF EXISTS Clip;

CREATE TABLE Clip
(
    clip_id           INTEGER PRIMARY KEY,

    implementation_id INTEGER NOT NULL,
    segment_id        INTEGER NOT NULL,

    filename          TEXT NOT NULL,
    duration          TEXT,
    notes             TEXT,

    FOREIGN KEY(implementation_id)
        REFERENCES Implementation(implementation_id),

    FOREIGN KEY(segment_id)
        REFERENCES Segment(segment_id),

    UNIQUE(implementation_id, segment_id)
);

------------------------------------------------------------
-- YouTubeVideo
------------------------------------------------------------
DROP TABLE IF EXISTS YouTubeVideo;

CREATE TABLE YouTubeVideo
(
    youtube_video_id  INTEGER PRIMARY KEY,

    implementation_id INTEGER NOT NULL,

    youtube_share_url TEXT,
    publish_date      TEXT,
    notes             TEXT,

    FOREIGN KEY(implementation_id)
        REFERENCES Implementation(implementation_id)
);

------------------------------------------------------------
-- VimeoVideo
------------------------------------------------------------
DROP TABLE IF EXISTS VimeoVideo;

CREATE TABLE VimeoVideo
(
    vimeo_video_id    INTEGER PRIMARY KEY,

    clip_id           INTEGER NOT NULL,

    vimeo_share_url   TEXT,
    notes             TEXT,

    FOREIGN KEY(clip_id)
        REFERENCES Clip(clip_id)
);
