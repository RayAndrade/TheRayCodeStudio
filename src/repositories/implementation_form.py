from PySide6.QtWidgets import QMessageBox


def save_record(self):
        """
        Save one Implementation using the values
        entered on the form.
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
