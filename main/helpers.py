from django import forms
from .models import Course
import sqlite3

def syncCourses():
    db = sqlite3.connect("db.sqlite3")
    c = db.cursor()
    c.execute("select * from main_course")

    for row in c.fetchall():
        Course.objects.create(
            key=row[4],
            title=row[1],
            link=row[3],
            desc=row[2]
        )
