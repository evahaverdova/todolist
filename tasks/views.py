# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskStatus
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def task_list(request):
    current_filter = request.GET.get('filter', 'all')
    if current_filter == 'all':
        tasks = Task.objects.filter(user=request.user).order_by('start_time')
    else:
        tasks = Task.objects.filter(user=request.user, status__name=current_filter).order_by('start_time')

    available_statuses = TaskStatus.objects.values_list('name', flat=True).distinct()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'current_filter': current_filter,
        'available_statuses': available_statuses
    })

@login_required
def task_create(request):
    current_filter = request.GET.get('filter', 'all')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            all_status, created = TaskStatus.objects.get_or_create(name='all')
            task.status.add(all_status)

            if current_filter != 'all':
                custom_status, created = TaskStatus.objects.get_or_create(name=current_filter)
                task.status.add(custom_status)

            task.save()
            return HttpResponseRedirect(f'/tasks/?filter={current_filter}')
    else:
        form = TaskForm()

    available_statuses = TaskStatus.objects.values_list('name', flat=True).distinct()
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'current_filter': current_filter,
        'available_statuses': available_statuses
    })

@csrf_exempt
def add_filter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        filter_name = data.get('name')
        if filter_name:
            TaskStatus.objects.get_or_create(name=filter_name)
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_filter(request):
    if request.method == 'POST':
        filter_name = request.GET.get('name')
        if filter_name:
            status = get_object_or_404(TaskStatus, name=filter_name)
            status.delete()
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if 'completed' in request.POST and request.POST['completed'] == 'on':
                task.delete()
                return redirect('task_list')
            else:
                form.save()
                return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    available_statuses = TaskStatus.objects.values_list('name', flat=True).distinct()
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'task': task,
        'current_filter': current_filter,
        'available_statuses': available_statuses
    })

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('task_list')

def index(request):
    return render(request, 'index.html')
