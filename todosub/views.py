from django.shortcuts import render,redirect

from todosub.models import Todoapp,DeleteTodoApp

# Create your views here.

def sample(request):
    
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        Todoapp.objects.create(task=task,description=description)
   
    return render(request,'index.html')

def list(request):
    data = Todoapp.objects.all()
    context = {
        'data' : data
    }
    return render(request,'todo.html',context)

def details(request,pk):
    data = Todoapp.objects.get(id=pk)
    if request.method == 'POST' and 'delete' in request.POST:
        DeleteTodoApp.objects.create(task=data.task,description=data.description)
        data.delete()
        return redirect('list')
    context = {
        'data' : data
    }
    return render(request,'details.html',context)

def edit(request,pk):
    data = Todoapp.objects.get(id=pk)
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        data.task = task
        data.description = description
        data.save()
        return redirect('home')
    context = {
        'data' : data
    }
    return render(request,'edit.html',context)
    
def update(request,pk):
    data = Todoapp.objects.get(id = pk)
    context = {
        'data' : data
    }
    return render(request,'edit.html',context)

def history(request):
    
    if request.method == 'POST' and 'delete' in request.POST:
        DeleteTodoApp.objects.all().delete()
        return redirect('history')
    data = DeleteTodoApp.objects.all()
    context = {
        'data' : data
    }
    return render(request,'history.html',context)

