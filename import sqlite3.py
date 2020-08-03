import sqlite3 as lite
con = lite.connect('students.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute("CREATE TABLE students(sid TEXT, fname TEXT, lname TEXT, grade INT, email TEXT)")
    cur.execute("INSERT INTO students VALUES('S00001', 'John', 'Johnson', 12, 'john.johnson@school.edu')")
    cur.execute("INSERT INTO students VALUES('S00002', 'Jane', 'Jackson', 9, 'jane.jackson@school.edu')")
    cur.execute("INSERT INTO students VALUES('S00003', 'Andrew', 'Jerkface', 2, 'andrew.jerkface@school.edu')")
    #last_row_id = cur.lastrowid
    #print("The last Id of the inserted row is {}".format(last_row_id))
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print("{} {} {}".format(row["sid"], row["fname"], row["lname"]))