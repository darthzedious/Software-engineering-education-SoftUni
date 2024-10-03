from datetime import datetime
from django.shortcuts import render


def index(request):
    context = {
        "my_form": "",
    }

    return render(request, 'base.html', context)


def dashboard(request):


    context = {

    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    pass


def edit_post(request):
    pass

def  details_page(request):
    pass

def delete_post(request):
    pass
