from django.shortcuts import render, redirect
from django.urls import reverse

from .models import TodoItem, CompletedTask
from .forms import TodoItemForm


def home(request):
    return render(request, 'main/home.html')


def todo_list(request):
    todos = TodoItem.objects.all().order_by('-created_at')
    form = TodoItemForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        completed_ids = request.POST.getlist('completed')

        if action == 'complete':
            for todo_id in completed_ids:
                todo_item = TodoItem.objects.get(id = todo_id)
                CompletedTask.objects.create(title = todo_item.title)
                todo_item.delete()
        elif action == 'delete':
            delete_id = request.POST.get('delete_id')
            TodoItem.objects.filter(id = delete_id).delete()
        else:
            form = TodoItemForm(request.POST)
            if form.is_valid():
                form.save()

        return redirect('main:todo_list')

    return render(request, 'main/todo_list.html', {'todos': todos, 'form': form})


def completed_list(request):
    completed_todos = CompletedTask.objects.all()

    return render(request, 'main/completed_list.html', {'completed_todos': completed_todos})
