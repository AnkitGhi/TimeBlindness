from django.shortcuts import render, redirect, get_object_or_404
from .forms import Data_provide, Submission_Provide
from .models import Task_register, Task_complete
from django.contrib.auth .decorators import login_required

@login_required
def profile(request):
    return render(request,"task/home.html")


@login_required
def task_register(request):
    if request.method == 'POST':
        form = Data_provide(request.POST)
        if form.is_valid():
            # Associate task with current user
            task = form.save(commit=False)
            task.user = request.user  # 👈 Critical line
            task.save()
            return redirect('take_me_home') 
        else:
            print(form.errors)
    else:
        form = Data_provide()
    return render(request, 'task/create_task.html', {'form': form})


@login_required
def task_completion(request,task_id):
    task = get_object_or_404(Task_register, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = Submission_Provide(request.POST)
        if form.is_valid():
            task_complete = form.save(commit=False)
            task_complete.user = request.user
            task_complete.task_bridge = task
            task_complete.save()
            return redirect('view tasks')
    else:
        # Display the form to complete the task
        form = Submission_Provide()
    return render(request, 'task/submit.html', {'form': form, 'task': task})
    

    # Get only current user's tasks
    # user_tasks = Task_register.objects.filter(user=request.user)
    
    # if request.method == 'POST':
    #     form = Submission_Provide(request.POST)
    #     # Limit task choices to user's tasks
    #     form.fields['task'].queryset = user_tasks  # 👈 Security critical
    #     if form.is_valid():
    #         submission = form.save()
    #         return redirect('view_tasks')
    # else:
    #     form = Submission_Provide()
    #     # Initialize form with filtered tasks
    #     form.fields['task'].queryset = user_tasks  # 👈 User-specific choices
    
    # return render(request, "task/submit.html", {'form': form})



@login_required
def view_tasks(request):
    # Get all tasks from the database
    tasks = Task_register.objects.filter(user=request.user)
    
    return render(request, 'task/view_tasks.html', {'tasks': tasks})
