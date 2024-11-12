import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "AllSaintsDay/index.html", {
        "AllSaintsDay": now.month ==10 and now.day == 30
    })