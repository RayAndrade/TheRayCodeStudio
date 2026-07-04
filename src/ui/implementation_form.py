"""
------------------------------------------------------------
File: implementation_form.py

Project:
    TRCStudio

Purpose:
    Display and edit one Implementation.

Responsibilities:
    - Display the user interface.
    - Collect user input.
    - Populate lookup combo boxes.
    - Delegate database work to repositories.

Notes:
    Version 6

Author:
    Ray Andrade
------------------------------------------------------------
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QTextEdit,
    QMessageBox,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
)

from repositories.implementation_repository import (
    ImplementationRepository
)

from repositories.lookup_repository import (
    LookupRepository
)


class ImplementationForm(QMainWindow):
    """
    Main TRCStudio Implementation window.
    """

    def __init__(self):
        super().__init__()

        #
        # Repositories
        #
        self.repository = ImplementationRepository()
        self.lookup_repository = LookupRepository()

        #
        # Current Implementation
        #
        self.implementation_id = None

        #
        # Window
        #
        self.setWindowTitle("TRC Studio")
        self.resize(900, 650)

        #
        # Central Widget
        #
        central = QWidget()
        self.setCentralWidget(central)

        #
        # Main Layout
        #
        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        #
        # Title
        #
        title = QLabel("Implementation")
        title.setStyleSheet(
            "font-size:24px;"
            "font-weight:bold;"
        )

        main_layout.addWidget(title)

        #
        # Grid
        #
        grid = QGridLayout()

        #
        # Language
        #
        grid.addWidget(QLabel("Language"), 0, 0)

        self.language_combo = QComboBox()
        grid.addWidget(self.language_combo, 0, 1)

        #
        # Category
        #
        grid.addWidget(QLabel("Category"), 1, 0)

        self.category_combo = QComboBox()
        grid.addWidget(self.category_combo, 1, 1)

        #
        # Pattern
        #
        grid.addWidget(QLabel("Pattern"), 2, 0)

        self.pattern_combo = QComboBox()
        grid.addWidget(self.pattern_combo, 2, 1)

        #
        # Version
        #
        grid.addWidget(QLabel("Version"), 3, 0)

        self.version_edit = QLineEdit("1")
        grid.addWidget(self.version_edit, 3, 1)

        #
        # Title
        #
        grid.addWidget(QLabel("Title"), 4, 0)

        self.title_edit = QLineEdit()
        grid.addWidget(self.title_edit, 4, 1)

        #
        # Notes
        #
        grid.addWidget(QLabel("Notes"), 5, 0)

        self.notes_edit = QTextEdit()
        grid.addWidget(self.notes_edit, 5, 1)

        #
        # Created
        #
        grid.addWidget(QLabel("Created"), 6, 0)

        self.created_label = QLabel("---")
        grid.addWidget(self.created_label, 6, 1)

        #
        # Updated
        #
        grid.addWidget(QLabel("Updated"), 7, 0)

        self.updated_label = QLabel("---")
        grid.addWidget(self.updated_label, 7, 1)

        main_layout.addLayout(grid)

        #
        # Buttons
        #
        button_layout = QHBoxLayout()

        self.new_button = QPushButton("Add")
        self.save_button = QPushButton("Save")
        self.save_button.setText("Add")
        self.search_button = QPushButton("Search")
        self.delete_button = QPushButton("Delete")
        self.exit_button = QPushButton("Exit")

        self.save_button.clicked.connect(self.save_record)
        self.exit_button.clicked.connect(self.close)

        button_layout.addWidget(self.new_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.delete_button)

        button_layout.addStretch()

        button_layout.addWidget(self.exit_button)

        main_layout.addLayout(button_layout)

        #
        # Populate combo boxes
        #
        self.load_lookup_tables()

    def load_lookup_tables(self):
        """
        Populate lookup combo boxes.
        """

        for language_id, language_name in (
                self.lookup_repository.get_languages()
        ):
            self.language_combo.addItem(
                language_name,
                language_id
            )

        for category_id, category_name in (
                self.lookup_repository.get_categories()
        ):
            self.category_combo.addItem(
                category_name,
                category_id
            )

        for pattern_id, pattern_name in (
                self.lookup_repository.get_patterns()
        ):
            self.pattern_combo.addItem(
                pattern_name,
                pattern_id
            )

    def save_record(self):
        """
        Save one Implementation.
        """

        try:

            language_id = self.language_combo.currentData()

            category_id = self.category_combo.currentData()

            pattern_id = self.pattern_combo.currentData()

            version = int(self.version_edit.text())

            title = self.title_edit.text().strip()

            notes = self.notes_edit.toPlainText().strip()

            if title == "":

                QMessageBox.warning(
                    self,
                    "Validation",
                    "Title is required."
                )

                return

            self.implementation_id = self.repository.save(
                language_id=language_id,
                category_id=category_id,
                pattern_id=pattern_id,
                version=version,
                title=title,
                notes=notes,
            )

            QMessageBox.information(
                self,
                "TRC Studio",
                f"Record {self.implementation_id} saved successfully."
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Database Error",
                str(error)
            )

    def search_records(self):
        """
        Search for Implementations matching the
        selected Language, Category and Pattern.
        """

        try:

            language_id = self.language_combo.currentData()

            category_id = self.category_combo.currentData()

            pattern_id = self.pattern_combo.currentData()

            rows = self.repository.search(
                language_id=language_id,
                category_id=category_id,
                pattern_id=pattern_id,
            )

            print()
            print("=" * 70)
            print("SEARCH RESULTS")
            print("=" * 70)

            if len(rows) == 0:
                print("No matching Implementations found.")

                QMessageBox.information(
                    self,
                    "Search",
                    "No matching Implementations found."
                )

                return

            print(
                f"{'ID':<6}"
                f"{'VER':<6}"
                f"{'TITLE':<40}"
                f"{'CREATED'}"
            )

            print("-" * 70)

            for implementation_id, version, title, created_at in rows:
                print(
                    f"{implementation_id:<6}"
                    f"{version:<6}"
                    f"{title:<40}"
                    f"{created_at}"
                )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Search Error",
                str(error)
            )

    def closeEvent(self, event):
        """
        Close database connections.
        """

        self.lookup_repository.close()
        self.repository.close()

        event.accept()
