from django.shortcuts import render
from django.http import HttpResponse
from djangoIntroduction.todo_app.models import Task


# Create your views here.

def my_view(request):
    return HttpResponse("<h1>Обичам те! <3!</h1>") #MIME type text/html


def add_view(request):
    return HttpResponse("<h1> Add </h1>")

def delete_view(request):
    return HttpResponse("<h1> Delete </h1>")




def index(request):

    title_filter = request.GET.get('title_filter', '')

    # if title_filter:
    tasks = Task.objects.filter(name__icontains=title_filter)
    # else:
    #     tasks = Task.objects.all()

    # result = [
    #     '<h1>TASKS</h1>',
    #     '<ul>',
    #     *[f"<li>{task.name} => {task.description}; Date: {task.created_at}</li>" for task in tasks],
    #     '</ul>',
    # ]

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context=context)