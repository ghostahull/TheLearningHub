from django.shortcuts import render
from .helpers import syncCourses
from .models import Course

from difflib import SequenceMatcher

def home(request):
    return render(request, "main/home.html")

def index(request):
    return render(request, "main/index.html", {
        "courses": Course.objects.order_by("key")
    })

def courses(request):
    context = {}

    if request.method == "POST":
        query = request.POST.get("search").lower()

        if not query:
            return render(request, "main/home.html")

        if query.isdigit() and Course.objects.filter(key=int(query)).exists():
            return render(request, "main/home.html", {
                "courses": [Course.objects.get(key=int(query))]
            })

        ratios = {}

        for course in Course.objects.all():
            link_as_text = course.link.lower().split("/")[-1].replace("_", " ").replace("+", " ")

            match = SequenceMatcher(None, course.title.lower(), query).ratio()
            desc_match = SequenceMatcher(None, course.desc.lower(), query).ratio()
            link_match = SequenceMatcher(None, link_as_text, query).ratio()

            if desc_match > match:
                match = desc_match

            if link_match > match:
                match = link_match

            ratios[course.key] = match

        len(ratios)
        context["courses"] = sorted(
            Course.objects.all(),
            key=lambda x: ratios[x.key],
            reverse=True)[:10]

    return render(request, "main/home.html", context)
