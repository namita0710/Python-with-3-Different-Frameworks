from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from todoList.models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request,"base.html",{"todos":todos})

def index(request):
    todos = Todo.objects.all()
    for n in todos:
       print(n) 
    print("hi")
    return render(request,"base.html",{"todos":todos})

@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    todo = Todo(title = title) 
    todo.save()
    return redirect("index")

def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

def delete(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")


