#!/bin/bash

rm -f theraycode.db

sqlite3 theraycode.db < sql/001_create_lookup_tables.sql
sqlite3 theraycode.db < sql/002_lookup_data.sql
sqlite3 theraycode.db < sql/003_create_business_tables.sql
