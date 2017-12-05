from django import forms
from .models import Course
import json


def syncCourses():
    conf = json.load(open("conf.json", "r"))

    for course in conf["#learninghub"]["courses"]:
        Course.objects.create(
            key=int(course["key"]),
            title=course["title"],
            link=course["link"],
            desc=course["desc"] if "desc" in course and course["desc"] != "" else "This course doesn't have a description."
        )
