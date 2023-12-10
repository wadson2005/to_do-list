from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

# tasks/views.py
from django.http import JsonResponse

def complete_task(request, task_id):
    try:
        task = get_object_or_404(Task, pk=task_id)
        task.completed = True
        task.save()

        
        sound = Howl(sources=[static('tasks/audios/completed.mp3')])  # Substitua pelo caminho real do seu arquivo de som
        sound.play()

        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
