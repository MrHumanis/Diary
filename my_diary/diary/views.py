from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
  if request.method == 'POST':
    selected_status = request.POST.get('status')
    if selected_status:
      tasks = Task.objects.filter(status=selected_status)
    else:
      tasks = Task.objects.exclude(status='completed')
  else:
    tasks = Task.objects.exclude(status='completed')
  return render(request, 'diary/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
  task = get_object_or_404(Task, pk=pk)
  return render(request, 'diary/task_detail.html', {'task': task})

def task_create(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('task_list')
  else:
    form = TaskForm()
  return render(request, 'diary/task_form.html', {'form': form})


def task_update(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('task_list')
  else:
    form = TaskForm(instance=task)
  return render(request, 'diary/task_form.html', {'form': form, 'update': True})

def task_delete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  if request.method == 'POST':
    task.delete()
    return redirect('task_list')
  return render(request, 'diary/task_confirm_delete.html', {'task': task})
