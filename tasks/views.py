from django.shortcuts import render

tasks = ["hello/", "AllSaintsDay/", "tasks/"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    } )