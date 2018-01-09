from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.template import loader
from .models import User


# Create your views here.
def list(request):
    All_users = User.objects.all()
    template = loader.get_template("list.html")
    context = {"All_users": All_users}
    return HttpResponse(template.render(context,request))


def add(request):
    template = loader.get_template("add.html")
    form = UserCreation(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.name is not None and instance.email is not None:
            instance.save()


    context = {"form": form }
    return HttpResponse(template.render(context,request))


def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context,request))


class UserCreation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']