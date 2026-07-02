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
            INSERT INTO Implementation
            (
                language_id,
                category_id,
                pattern_id,
                version,
                title,
                notes
            )
            VALUES
            (
                ?, ?, ?, ?, ?, ?
            )
            """,
            (
                language_id,
                category_id,
                pattern_id,
                version,
                title,
                notes,
            ),
        )

        self.connection.commit()

        return cursor.lastrowid

    def close(self):
        """
        Close the database connection.
        """

        self.connection.close()
