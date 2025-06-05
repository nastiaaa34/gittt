import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''



CREATE TABLE IF NOT EXISTS students (    id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
               age INTEGER,
               major TEXT)''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (  course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_name TEXT,
               instructor TEXT)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses (
                student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY (student_id) REFERENCES students(id),
               FOREIGN KEY (course_id) REFERENCES courses(course_id),
               PRIMARY KEY (student_id, course_id))''')

while True:
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. View Students")
    print("5. View Courses")
    print("6. View Enrollments")
    print("7. Exit")

    choice = input("Оберіть опцію (1-7): ")

    if choice == '1':
        name = input("Введіть ім'я студента: ")
        age = int(input("Введіть вік студента: "))
        major = input("Введіть спеціальність студента: ")
        cursor.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', (name, age, major))
        conn.commit()
        print("Student added successfully.")

    elif choice == '2':
        course_name = input("Введіть назву курсу: ")
        instructor = input("Введіть ім'я викладача: ")
        cursor.execute('INSERT INTO courses (course_name, instructor) VALUES (?, ?)', (course_name, instructor))
        conn.commit()
        print("Course added successfully.")

    elif choice == '3':
        student_id = int(input("Введіть ID студента: "))
        course_id = int(input("Введіть ID курсу: "))
        cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
        conn.commit()
        print("Enrollment successful.")

    elif choice == '4':
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        for student in students:
            print(student)

    elif choice == '5':
        cursor.execute('SELECT * FROM courses')
        courses = cursor.fetchall()
        for course in courses:
            print(course)

    elif choice == '6':
        cursor.execute('SELECT s.name, c.course_name FROM students s JOIN student_courses sc ON s.id = sc.student_id JOIN courses c ON sc.course_id = c.course_id')
        enrollments = cursor.fetchall()
        for enrollment in enrollments:
            print(enrollment)

    elif choice == '7':
        break

    else:
        print("Invalid choice. Please try again.")