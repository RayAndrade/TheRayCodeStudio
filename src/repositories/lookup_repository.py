"""
------------------------------------------------------------
File: lookup_repository.py

Project:
    TRCStudio

Purpose:
    Read lookup table information used to populate
    the application's combo boxes.

Responsibilities:
    - Read Languages.
    - Read Categories.
    - Read Patterns.

Notes:
    This repository is READ ONLY.

    Lookup tables are maintained separately from
    the business tables.

Author:
    Ray Andrade
------------------------------------------------------------
"""

from db import get_connection


class LookupRepository:
    """
    Repository responsible for all lookup tables.
    """

    def __init__(self):

        self.connection = get_connection()

    def get_languages(self):
        """
        Return every language.

        Returns:
            List of tuples:
            (language_id, language_name)
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT
                language_id,
                language_name
            FROM Language
            ORDER BY language_name
            """
        )

        return cursor.fetchall()

    def get_categories(self):
        """
        Return every category.

        Returns:
            List of tuples:
            (category_id, category_name)
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT
                category_id,
                category_name
            FROM Category
            ORDER BY category_name
            """
        )

        return cursor.fetchall()

    def get_patterns(self):
        """
        Return every pattern.

        Returns:
            List of tuples:
            (pattern_id, pattern_name)
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT
                pattern_id,
                pattern_name
            FROM Pattern
            ORDER BY pattern_name
            """
        )

        return cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """

        self.connection.close()
