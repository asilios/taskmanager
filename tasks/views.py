from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q
from .models import Task, Category, Tag
from .forms import TaskForm, CategoryForm, TagForm, RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(owner=request.user)
    total = tasks.count()
    pending = tasks.filter(status='pending').count()
    in_progress = tasks.filter(status='in_progress').count()
    completed = tasks.filter(status='completed').count()
    recent_tasks = tasks[:5]
    context = {
        'total': total, 'pending': pending,
        'in_progress': in_progress, 'completed': completed,
        'recent_tasks': recent_tasks,
    }
    return render(request, 'tasks/dashboard.html', context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks, 'query': query, 'status': status, 'priority': priority
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form.save_m2m()
            messages.success(request, 'Task created!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Update'})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def category_list(request):
    categories = Category.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.created_by = request.user
            cat.save()
            messages.success(request, 'Category created!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/category_list.html', {'categories': categories, 'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted!')
    return redirect('category_list')


@login_required
def tag_list(request):
    tags = Tag.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.created_by = request.user
            tag.save()
            messages.success(request, 'Tag created!')
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'tasks/tag_list.html', {'tags': tags, 'form': form})

# test