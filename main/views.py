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

        context["courses"] = sorted(
            Course.objects.all(),
            key=lambda x: SequenceMatcher(None, x.title.lower(), query).ratio(),
            reverse=True
        )[:10]

    return render(request, "main/home.html", context)
