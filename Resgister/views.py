from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def list(request):
    All_users = User.objects.all()

    html = "<h1>User List:</h1>"

    for i in All_users:
        html += "<p>Username:" + i.name + " Email:" + i.email + "</p>"

    return HttpResponse(html)

def index(request):
    html = ""
    html += "<a href='/list/'>List Users</a>"
    return HttpResponse(html)
