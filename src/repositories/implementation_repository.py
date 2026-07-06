"""
------------------------------------------------------------
File: implementation_repository.py

Project:
    TRCStudio

Purpose:
    Encapsulate all database access for the
    Implementation table.

Responsibilities:
    - Insert a new Implementation.
    - Update an existing Implementation.
    - Delete an Implementation.
    - Retrieve one or more Implementations.

Notes:
    Version 2

Author:
    Ray Andrade
------------------------------------------------------------
"""

from db import get_connection


class ImplementationRepository:
    """
    Repository responsible for the
    Implementation table.
    """

    def __init__(self):

        self.connection = get_connection()

    def save(
            self,
            language_id,
            category_id,
            pattern_id,
            version,
            title,
            notes,
    ):
        """
        Insert one Implementation record.

        Returns:
            implementation_id
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO Implementation  ( language_id, category_id, pattern_id, version, title, notes ) VALUES
            ( ?, ?, ?, ?, ?, ? )
            """,
            ( language_id, category_id, pattern_id, version, title, notes, ), )

        self.connection.commit()

        return cursor.lastrowid

    def search(
            self,
            language_id,
            category_id,
            pattern_id,
    ):
        """
        Return every Implementation matching the
        selected Language, Category and Pattern.
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT implementation_id,
                   version,
                   title,
                   created_at
            FROM Implementation
            WHERE language_id = ?
              AND category_id = ?
              AND pattern_id = ?
            ORDER BY version
            """,
            (
                language_id,
                category_id,
                pattern_id,
            ),
        )

        return cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """

        self.connection.close()
