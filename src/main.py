"""
------------------------------------------------------------
File: main.py

Project:
    TRCStudio

Purpose:
    This is the application's entry point.

Responsibilities:
    - Create the Qt application.
    - Create the main window.
    - Start the application's event loop.

Notes:
    This file should remain very small.

    It should never contain business logic,
    SQL statements, or user-interface code.

Author:
    Ray Andrade

------------------------------------------------------------
"""

import sys

from PySide6.QtWidgets import QApplication

from ui.implementation_form import ImplementationForm


def main():
    """
    Application entry point.
    """

    app = QApplication(sys.argv)

    window = ImplementationForm()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()