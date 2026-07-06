
## `lookup_repository.py`


### 1. Why does this file exist?

Its only purpose is to answer this question:

> **"What choices should appear in the combo boxes?"**

Nothing more.

It does **not** create records.

It does **not** update records.

It simply reads the lookup tables.

---

### 2. What is a lookup table?

A lookup table contains information that changes very rarely.

Examples:

```
Language

1  C#
2  C++
3  Java
4  JavaScript
5  PHP
6  Python
```

or

```
Category

1  Creational
2  Structural
3  Behavioral
```

These tables are almost like constants.

---

### 3. Why have a separate repository?

Imagine if `ImplementationRepository` contained:

* save()
* update()
* delete()
* search()
* get_languages()
* get_categories()
* get_patterns()

That class would quickly become responsible for two different jobs.

Instead we split them.

```
ImplementationRepository

Create
Read
Update
Delete
```

```
LookupRepository

Languages

Categories

Patterns
```

Each class has a single responsibility.

---

### 4. What does `__init__()` do?

```python
self.connection = get_connection()
```

It opens one SQLite connection.

Every method in the repository uses that same connection.

---

### 5. `get_languages()`

This method asks SQLite:

```
SELECT
    language_id,
    language_name
FROM Language
ORDER BY language_name
```

SQLite returns something like:

```python
[
    (2, "C#"),
    (1, "C++"),
    (3, "Java"),
    (4, "JavaScript"),
    (5, "PHP"),
    (6, "Python")
]
```

Notice each tuple contains:

```
(id, display name)
```

The UI stores the **id** internally while showing the **display name** to the user.

---

### 6. `get_categories()`

Exactly the same idea.

Returns:

```python
[
    (3, "Behavioral"),
    (1, "Creational"),
    (2, "Structural")
]
```

---

### 7. `get_patterns()`

Again, the same pattern.

SQLite returns every design pattern.

The combo box displays the names.

Internally it remembers the IDs.

---

### 8. `close()`

```python
self.connection.close()
```

When TRCStudio exits, this closes the database connection cleanly.

---

# How does it fit into the application?

```
ImplementationForm
        │
        ▼
LookupRepository
        │
        ▼
SQLite
```

When the form starts:

```
ImplementationForm
```

asks:

```
LookupRepository
```

for:

* Languages
* Categories
* Patterns

The repository asks SQLite and returns the answers.

The form never writes to those tables.

---

# The important design lesson

This repository is **read-only**.

Its job is:

> "Tell me what choices exist."

It should **never** contain:

* `INSERT`
* `UPDATE`
* `DELETE`

Only `SELECT`.

That's why it's called a **LookupRepository**.

--------------------------------------------------------------------------

##implementation_form.py##



One note: the file that was uploaded is **not the complete `implementation_form.py`**. It only contains the `save_record()` method, not the whole class. 

Even so, since we've been building TRCStudio together, I can explain the role of **`implementation_form.py`** in the application.

# What is `implementation_form.py`?

It is the **main window** of TRCStudio.

Think of it as the **conductor of an orchestra**.

It doesn't play the instruments itself—it tells everyone else when to play.

---

# Where does it fit?

```text
                 main.py
                    │
                    ▼
        ImplementationForm
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
LookupRepository      ImplementationRepository
        │                       │
        └───────────┬───────────┘
                    ▼
                 SQLite
```

Each box has one job.

---

# What does the form own?

It owns every control you see on the screen.

For example:

```python
self.language_combo

self.category_combo

self.pattern_combo

self.title_edit

self.notes_edit

self.save_button

self.search_button
```

Those objects **live** inside `ImplementationForm`.

---

# What does it NOT do?

Notice something important.

There is **no SQL** in the form.

Instead, the form asks another class to do database work.

For example:

```python
self.repository.save(...)
```

The form never says:

```sql
INSERT INTO Implementation ...
```

That's the repository's responsibility.

---

# What happens when the program starts?

The sequence is:

```
main.py

↓

ImplementationForm()

↓

create controls

↓

load lookup tables

↓

display window
```

Nothing is saved yet.

Nothing is searched yet.

The form is simply ready for the user.

---

# What does `save_record()` do?

This is the method shown in your uploaded file. 

Its responsibility is very straightforward:

### Step 1

Read the controls.

```python
language_id

category_id

pattern_id

version

title

notes
```

---

### Step 2

Validate.

Right now the only validation is:

```
Title cannot be empty.
```

If it is empty:

```
Show a warning.

Return.
```

Nothing is saved.

---

### Step 3

Call the repository.

```python
self.repository.save(...)
```

Notice the form **doesn't know how** to save.

It simply asks another object.

---

### Step 4

Receive the new ID.

The repository returns:

```python
implementation_id
```

The form remembers it.

---

### Step 5

Tell the user.

```
Record 2 saved successfully.
```

The form doesn't care how SQLite generated the ID.

It simply displays it.

---

# Why is this separation important?

Imagine one day you replace SQLite with PostgreSQL.

Which file changes?

**Only this one:**

```
ImplementationRepository
```

`ImplementationForm` doesn't need to change because it only knows:

```
repository.save(...)
```

That is one of the biggest benefits of the Repository pattern.

---

# Think of it this way

I think this mental model will help you.

## `main.py`

> Starts the application.

---

## `implementation_form.py`

> Talks to the user.

---

## `lookup_repository.py`

> Reads lookup tables.

---

## `implementation_repository.py`

> Reads and writes Implementations.

---

## `db.py`

> Opens the SQLite connection.

---

## `theraycode.db`

> Stores the data.

---

## What I'd like to do

I think this could become a regular part of our work.

For every `.py` file we examine, we'll answer the same questions:

1. **Why does this file exist?**
2. **Who creates it?**
3. **Who calls it?**
4. **What does it own?**
5. **What is it responsible for?**
6. **What should it never do?**

By the time we've gone through all the files, you'll understand the architecture of TRCStudio, not just the Python syntax. I think that's the understanding you're really aiming for.

================================================================

Excellent. This is the second repository, and together with `LookupRepository`, it forms the heart of TRCStudio's data access layer. 

Let's examine it the same way we did the first one.

---

# File: `implementation_repository.py`

## Purpose

This class is responsible for **all database operations involving the `Implementation` table**.

If `LookupRepository` answers the question:

> "What choices exist?"

then `ImplementationRepository` answers:

> "What Implementations exist, and how do we save and retrieve them?"

---

# Where does it fit?

```text
                     main.py
                        │
                        ▼
             ImplementationForm
                        │
                        ▼
          ImplementationRepository
                        │
                        ▼
                   SQLite Database
```

Notice something important:

The GUI **never** talks directly to SQLite.

Everything goes through this repository.

---

# Why does this file exist?

Imagine putting SQL inside `implementation_form.py`.

Your form would contain:

* Buttons
* Labels
* Combo boxes
* SQL statements

It would quickly become one large, difficult-to-maintain class.

Instead, all SQL lives here.

That means:

* The GUI displays information.
* The Repository stores information.

Each class has one responsibility.

---

# Constructor

```python
def __init__(self):

    self.connection = get_connection()
```

## Responsibility

When the repository is created, it opens a connection to the database.

Every method in this class uses that same connection.

Think of it as:

```text
Repository
      │
      ▼
Database Connection
```

The connection is created once and reused.

---

# save()

```python
def save(...)
```

This method performs the **Create** part of CRUD.

Its job is:

1. Receive information from the form.
2. Insert a new row into the `Implementation` table.
3. Commit the transaction.
4. Return the new `implementation_id`.

---

## Data Flow

```text
ImplementationForm

        │

language_id
category_id
pattern_id
version
title
notes

        │

        ▼

ImplementationRepository.save()

        │

        ▼

INSERT INTO Implementation

        │

        ▼

SQLite assigns

implementation_id

        │

        ▼

Return ID to the form
```

The repository does not know anything about buttons or text boxes.

It only knows how to insert records.

---

# search()

This method performs the **Read** part of CRUD.

Its purpose is:

> "Find every Implementation matching the selected Language, Category, and Pattern."

It receives three IDs:

```text
language_id

category_id

pattern_id
```

and executes a `SELECT`.

SQLite returns matching rows.

The repository simply passes those rows back to the form.

It does not decide what to display.

---

## Data Flow

```text
ImplementationForm

        │

Search button

        │

        ▼

repository.search()

        │

        ▼

SQLite

        │

Matching rows

        │

        ▼

ImplementationForm
```

Again, notice the separation of responsibilities.

---

# close()

```python
def close(self):
```

When TRCStudio exits, the repository closes its database connection.

That releases the SQLite file cleanly.

---

# What this class should eventually contain

Today you have:

```text
save()

search()

close()
```

Eventually it will become:

```text
save()

search()

get_by_id()

update()

delete()

close()
```

Those six methods will complete the CRUD cycle.

---

# What this class should NEVER contain

It should never contain:

* `QMessageBox`
* `QPushButton`
* `QComboBox`
* `QLineEdit`
* Any PySide6 widgets

Those belong to the user interface.

Likewise, it should never ask the user questions.

For example, it should **not** say:

> "Are you sure?"

That's the form's responsibility.

The repository only performs database operations.

---

# Relationship with `LookupRepository`

The two repositories have different jobs.

### LookupRepository

```text
READ ONLY

Language

Category

Pattern
```

It only performs `SELECT` statements.

---

### ImplementationRepository

```text
Business Data

INSERT

SELECT

UPDATE

DELETE
```

It manages the application's primary data.

---

# The Big Picture

At this point, TRCStudio has a clean separation of responsibilities:

```text
main.py
    │
    ▼
ImplementationForm
    │
    ├──────────────┐
    ▼              ▼
LookupRepository   ImplementationRepository
    │              │
    └──────┬───────┘
           ▼
       SQLite Database
```

This is one of the strengths of your design. Each class has a clear purpose, which will make the application easier to extend as you add Clips, Vimeo videos, YouTube videos, and the rest of your workflow.

I also like the way you're documenting each file with a consistent header. As the project grows, those headers will make it much easier to understand the purpose of each class months or even years later.

