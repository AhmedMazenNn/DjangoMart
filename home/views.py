from django.shortcuts import render


def get_home_page(request):
    return render(request, "index.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")

def welcome(request):
    return render(request, "welcome.html")


