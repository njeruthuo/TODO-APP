from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def index(request, *args, **kwargs):
    todos = Todo.objects.all()
    return render(request, 'index.html', context={
        'todos': todos
    })


@login_required(login_url='login')
def todo_view(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    return render(request, 'todo-view.html', context={
        'todo': todo
    })


@login_required(login_url='login')
def create_todo(request, *args, **kwargs):
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mytodo:index')
    return render(request, 'create-todo.html', context={
        'form': form
    })


@login_required(login_url='login')
def change_todo(request, pk, *args, **kwargs):
    todo = get_object_or_404(Todo, id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'change-form.html', context)


@login_required(login_url='login')
def delete_todo(request, pk, *args, **kwargs):
    todo = get_object_or_404(Todo, id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('mytodo:index')

    return render(request, 'delete-view.html', context={
        'todo': todo
    })
