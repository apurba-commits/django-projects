from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponse
# Create your views here.
def task(request):
    tasks=Task.objects.all()
    return render(request,'index.html',{'tasks':tasks})

def create_tasks(request):
    if request.method == "POST":
        title=request.POST.get('title')
        due_date=request.POST.get('due_date')

        if title and due_date:
            task=Task(title=title , due_date=due_date)
            task.save()
            return redirect('task')
        return HttpResponse("Please provide both title and due date.", status=400)
    return render(request, 'add_task.html')