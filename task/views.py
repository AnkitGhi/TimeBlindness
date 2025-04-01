from django.shortcuts import render, redirect, get_object_or_404
from .forms import Data_provide, Submission_Provide
from .models import Task_register, Task_complete, TaskSummary, Analytics
from django.contrib.auth .decorators import login_required

@login_required
def profile(request):
    return render(request,"task/home.html")


@login_required
def task_register(request):
    if request.method == 'POST':
        form = Data_provide(request.POST)
        if form.is_valid():

            task = form.save(commit=False)
            task.user = request.user  
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

@login_required
def view_tasks(request):
    # Get all tasks from the database
    tasks = Task_register.objects.filter(user=request.user)
    
    return render(request, 'task/view_tasks.html', {'tasks': tasks})

def analytics(request):
    task_stored = TaskSummary.objects.filter(user=request.user)
    task_incomplete = Task_register.objects.filter(user=request.user)

    no_task_complete = task_stored.count()
    no_task_incomplete = task_incomplete.count()
    if no_task_complete > 0:
        average_actual_time = sum(tasks.actual_time for tasks in task_stored)/no_task_complete
        average_motivation = sum(tasks.moti for tasks in task_stored)/no_task_complete
        average_seatings = sum(taks.num_of_seatings for taks in task_stored)/no_task_complete
        average_esti_time = sum(tasks.est_time for tasks in task_stored)/no_task_complete
    else:
        average_esti_time = 0
        average_actual_time = 0
        average_motivation = 0
        average_seatings = 0
   
    if request.method=='POST':
        Analytics.objects.update_or_create(
            user=request.user,
            defaults={
                'average_time_completion':average_actual_time,
                'average_time_estimated': average_esti_time,
                'no_task_completed': no_task_complete,
                'no_task_remaining': no_task_incomplete,
                'average_motivation': average_motivation, 
                'average_seatings': average_seatings,
            }
        )



