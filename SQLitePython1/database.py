import sqlite3
from email import message
# from html.entities import name

from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQLite Database")
        self.setGeometry(100, 100, 1000, 100)

        # Create QLabels
        name_label = QLabel("Name")
        profession_label = QLabel("Profession")
        address_label = QLabel("Address")
        age_label = QLabel("Age")

        # Create QLine Edit
        self.name_line_edit = QLineEdit()
        self.profession_line_edit = QLineEdit()
        self.address_line_edit = QLineEdit()
        self.age_line_edit = QLineEdit()

        # QPushButtons for adding and updating
        button_add_data = QPushButton("Add new row")
        button_add_data.clicked.connect(self.add_data)

        button_update_data = QPushButton("Update delected row")
        button_update_data.clicked.connect(self.update_data)

        # Name QLable and Name QLineEdit form horizontal layout
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name_label)
        h_layout1.addWidget(self.name_line_edit)

        # Profession Label and QLineEdit form horizontal layout
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(profession_label)
        h_layout2.addWidget(self.profession_line_edit)

        # Profession Label and QLineEdit form horizontal layout
        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(address_label)
        h_layout3.addWidget(self.address_line_edit)

        # Profession Label and QLineEdit form horizontal layout
        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(age_label)
        h_layout4.addWidget(self.age_line_edit)

        # Profession Label and QLineEdit form horizontal layout
        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(button_add_data)
        h_layout5.addWidget(button_update_data)

        # GoupLabels, Edits and Pushbuttons
        add_form = QGroupBox("Add New Employee")

        # Lay out all items in group vertically
        form_layout = QVBoxLayout()
        form_layout.addLayout(h_layout1)
        form_layout.addLayout(h_layout2)
        form_layout.addLayout(h_layout3)
        form_layout.addLayout(h_layout4)
        form_layout.addLayout(h_layout5)
        add_form.setLayout(form_layout)

        # Create QTable
        self.table = QTableWidget()
        self.table.setMaximumWidth(800)

        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 50)

        self.table.setHorizontalHeaderLabels(["Name", "Profession", "Address", "Age"])

        # Create more QPushButtons
        button_insert_data = QPushButton("Insert Demo Data")
        button_insert_data.clicked.connect(self.insert_data)

        button_load_data = QPushButton("Load Data")
        button_load_data.clicked.connect(self.load_data)

        button_call_data = QPushButton("Extract Data")
        button_call_data.clicked.connect(self.call_data)

        button_delete_data = QPushButton("Delete Data")
        button_delete_data.clicked.connect(self.delete_data)

        # Display all elements vertically
        layout = QVBoxLayout()
        layout.addWidget(add_form)
        layout.addWidget(self.table)
        layout.addWidget(button_insert_data)
        layout.addWidget(button_load_data)
        layout.addWidget(button_call_data)
        layout.addWidget(button_delete_data)
        self.setLayout(layout)

    def create_connection(self):
        # Create SQL conection
        self.connection = sqlite3.connect("employees.db")

        return self.connection

    def insert_data(self):

        self.cursor = self.create_connection().cursor()

        self.cursor.execute("create table employees_list (Name text, Profession text, Address text, Age integer)",)

        # List employee details in tuples
        self.List_of_employees = [
            ("Emmanuel Olega", "Software Engineer", "Kampala",28),
            ("Ester Olega", "Veterinarian", "Wakiso", 24),
            ("Jjuuko Henry", "Accountant", "Masaka", 25),
            ("Apio Brenda", "Civil Engineer", "Gulu", 22)
        ]

        # Insert multiple rows
        self.cursor.executemany("Insert into employees_list values (?, ?, ?, ?)", self.List_of_employees)
        print("Insert demo data successfully")
        self.connection.commit()
        self.connection.close()

    def add_data(self):
        self.cursor = self.create_connection().cursor()

        # First initialize employee information from QLine edits as a list
        self.new_employee = [
            self.name_line_edit.text(),
            self.profession_line_edit.text(),
            self.address_line_edit.text(),
            self.age_line_edit.text()
        ]

        # To add new employee to sqlite table
        self.cursor.execute("insert into employees_list values (?, ?, ?, ?)",self.new_employee)

        print("New name added:", self.name_line_edit.text())

        # Clear line edit text
        self.name_line_edit.clear()
        self.profession_line_edit.clear()
        self.address_line_edit.clear()
        self.age_line_edit.clear()

        self.connection.commit()
        self.connection.close()

    def load_data(self):
        self.cursor = self.create_connection().cursor()
        rowCount_sqlquery = "SELECT COUNT(*) FROM employees_list"
        employees_sqlquery = "SELECT * FROM employees_list"

        # find the number of rows in the table
        self.cursor.execute(rowCount_sqlquery)
        results = self.cursor.fetchone()

        print("Number of rows:",results[0])
        self.table.setRowCount(results[0])

        # Add employess from table to QTable
        table_row = 0

        for i in self.cursor.execute(employees_sqlquery):
            self.table.setItem(table_row, 0, QTableWidgetItem(i[0]))
            self.table.setItem(table_row, 1, QTableWidgetItem(i[1]))
            self.table.setItem(table_row, 2, QTableWidgetItem(i[2]))
            self.table.setItem(table_row, 3, QTableWidgetItem(str(i[3])))
            table_row += 1

    def call_data(self):
        current_row_index = self.table.currentRow()

        # Call employee details and assign to variable
        self.name_edit = str(self.table.item(current_row_index, 0).text())
        self.profession_edit = str(self.table.item(current_row_index, 1).text())
        self.address_edit = str(self.table.item(current_row_index, 2).text())
        self.name_age = str(self.table.item(current_row_index, 3).text())

        # Change QLine Edits to above variables
        self.name_line_edit.setText(self.name_edit)
        self.profession_line_edit.setText(self.profession_edit)
        self.address_line_edit.setText(self.address_edit)
        self.age_line_edit.setText(self.name_age)

    def update_data(self):
        self.cursor = self.create_connection().cursor()

        # Get Current text from QLineEdit
        params = (
            self.name_line_edit.text(),
            self.profession_line_edit.text(),
            self.address_line_edit.text(),
            self.age_line_edit.text(),
            self.name_edit
        )

        self.cursor.execute("UPDATE employees_list SET Name=?, Profession=?, Address=?, Age=? WHERE Name=?", params)

        print("The old name was ",self.name_edit)
        print("The new name is ", self.name_line_edit.text())

        # Clear line edit text 22:54
        self.name_line_edit.clear()
        self.profession_line_edit.clear()
        self.address_line_edit.clear()
        self.age_line_edit.clear()

        self.connection.commit()
        self.connection.close()

    def delete_data(self):
         self.cursor = self.create_connection().cursor()
         current_row_index = self.table.currentRow()

         # Call name in row and assign to variable
         name_item = str(self.table.item(current_row_index, 0))

         if current_row_index < 0:
             Warning = QMessageBox.warning(self,"Warning, please select a record to delete")
         else:
             message = QMessageBox.question(self, 'Confirm Delete', 'Are you sure you want to delete this record?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

             if message == QMessageBox.StandardButton.Yes:
                 sqlquery = "DELETE FROM employees_list WHERE Name=?"
                 self.cursor.execute(sqlquery(name_item,))
                 print("Deleted record", name_item)

                 self.connection.commit()
                 self.connection.close()


