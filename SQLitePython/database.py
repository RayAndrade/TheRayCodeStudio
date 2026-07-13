import sqlite3
from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQLite Database")
        self.setGeometry(100,100,500,100)

        #Create QLabel
        name_label = QLabel("Name")
        profession_label = QLabel("Profession")
        address_label = QLabel("Address")
        age_label = QLabel("Age") # 3:43

        #Create QLine Edit
        self.name_line_edit = QLineEdit()
        self.profession_line_edit = QLineEdit()
        self.address_line_edit = QLineEdit()
        self.age_line_edit = QLineEdit()

        # QPushButton for adding and updating
        button_add_data = QPushButton("Add new row")
        button_add_data.clicked.connect(self.add_data)

        button_update_data = QPushButton("Update delected row")
        button_update_data.clicked.connect(self.update_data())

        # 4:41 Name QLabel and Name QLineEdit from horizontal layout
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name_label)
        h_layout1.addWidget(self.name_line_edit)

        # Profession  and  QLineEdit from horizontal layout
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(profession_label)
        h_layout2.addWidget(self.profession_line_edit)

        # Profession  and  QLineEdit from horizontal layout
        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(address_label)
        h_layout3.addWidget(self.address_line_edit)

        # Profession  and  QLineEdit from horizontal layout
        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(age_label)
        h_layout4.addWidget(self.age_line_edit)  # go to next line 22

        # Profession  and  QLineEdit from horizontal layout
        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(button_add_data)
        h_layout5.addWidget(button_update_data)

        # GroupLabels, edits and push buttons
        add_form = QGroupBox("Add New Employee")

        # Lay out all items in group vertically
        form_layout = QVBoxLayout()
        form_layout.addLayout(h_layout1)
        form_layout.addLayout(h_layout2)
        form_layout.addLayout(h_layout3)
        form_layout.addLayout(h_layout4)
        form_layout.addLayout(h_layout5)
        add_form.setLayout(form_layout)

        # 8:00 Create QTabel
        self.table = QTableWidget(self)
        self.table.setMaximumWidth(800)

        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)

        self.table.setHorizontalHeaderLabels(["Name", "Profession", "Address", "Age"])

        # 9:15 Create more QPushButtons
        button_insert_data = QPushButton("Insert demo data")
        #button_insert_data.clicked.connect(self.insert_data)

        button_load_data = QPushButton("Load demo data")
        #button_load_data.clicked.connect(self.load_data)

        button_call_data = QPushButton("Extract data")
        #button_call_data.clicked.connect(self.call_data)

        button_delete_data = QPushButton("Delete data")  # 9:57
        #button_delete_data.clicked.connect(self.delete_data)

        # Display all elements vertically 10:23 goto main and run
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(add_form)
        layout.addWidget(button_insert_data)
        layout.addWidget(button_load_data)
        layout.addWidget(button_call_data)
        layout.addWidget(button_delete_data)

        self.setLayout(layout)

    def create_connection(self): # 1:11
        #Create SQLite Database connection
        self.connection = sqlite3.connect("employees.db")

        return self.connection

    def insert_data(self):
        self.cursor = self.create_connection().cursor() # 12:44 made a corection

        self.cursor.execute("create table employees_list (Name text, Profession text, Address text, Age integer)") # 11:19

        # List employee details in tuple
        self.List_of_employees = [
            ("Emmanel Olega","Software Engineer","Kamapa", 28),
            ("Ray Andrade", "Machinist","Tujunga", 91),
            ("Jimmy Page","Guitarist","London", 62),
            ("America", "Home","USA", 250),
        ]

        # 12:00 Insert mutiple rows
        self.cursor.executemany("Insert into employees_list values (?,?,?,?)", self.List_of_employees)
        print("Employees inserted successfully")
        self.connection.commit()
        self.connection.close()

    def add_data(self):
        pass

    def load_data(self):
        pass

    def call_data(self):
        pass

    def update_data(self):
        pass

    def delete_data(self):
        pass


