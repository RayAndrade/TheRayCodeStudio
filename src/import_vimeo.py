from pathlib import Path

from db import get_connection

VIDEO_DIRECTORY = Path("/home/theraycode/Work/Vimeo")

LANGUAGE_MAP = {
    "cpp": "C++",
    "csharp": "C#",
    "java": "Java",
    "js": "JavaScript",
    "php": "PHP",
    "py": "Python",
}


def get_language_id(connection, language):

    language_name = LANGUAGE_MAP[language]

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT language_id
          FROM Language
         WHERE language_name = ?
        """,
        (language_name,)
    )

    row = cursor.fetchone()

    if row is None:
        raise ValueError(f"Unknown language: {language_name}")

    return row[0]


def parse_filename(connection, filename):

    name = filename.removesuffix(".mp4")
    parts = name.split("-")

    version = 1

    if len(parts) == 4:
        language, category, pattern, segment = parts

    elif len(parts) == 5 and parts[4].startswith("v"):
        language, category, pattern, segment, version_text = parts
        version = int(version_text.removeprefix("v"))

    else:
        print(f"Filename : {filename}")
        print("Status   : INVALID")
        print()
        return

    language_id = get_language_id(connection, language)

    print(f"Filename    : {filename}")
    print(f"Language    : {language}")
    print(f"Language ID : {language_id}")
    print(f"Category    : {category}")
    print(f"Pattern     : {pattern}")
    print(f"Segment     : {segment}")
    print(f"Version     : {version}")
    print()


def main():

    print(f"Directory : {VIDEO_DIRECTORY}")
    print()

    connection = get_connection()

    print("Connected to database.")
    print()

    for file in sorted(VIDEO_DIRECTORY.glob("*.mp4")):
        parse_filename(connection, file.name)

    connection.close()


if __name__ == "__main__":
    main()

