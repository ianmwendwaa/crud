from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import Taskform


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_details.html', {'tasks': task})


def task_create(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = Taskform()
    return render(request, 'task_form.html', {'form': form})


def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', id=task.id)
    else:
        form = Taskform(instance=task)
    return render(request, 'task_form.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect("task_list")
    return render(request, 'task_c_d.html', {'task': task})
