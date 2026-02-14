from django.shortcuts import render

def index(request):
    context = {
        "title": "Periwinkle Punk Offical",
    }
    return render(request, "index.html", context)

def mybooks(request):
    context = {
        "title": "My Books",
    }
    return render(request, "mybooks.html", context)

def moodboard(request):
    context = {
        "title": "Mood Board",
    }
    return render(request, "moodboard.html", context)

def updates(request):
    context = {
        "title": "Author's Note",
    }
    return render(request, "updates.html", context)

def about(request):
    context = {
        "title": "About the Author",
    }
    return render(request, "about.html", context)