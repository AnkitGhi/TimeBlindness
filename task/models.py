from django.db import models
from django import forms
from django.contrib.auth.models import User

class Task_register(models.Model):
    task_choices = (
        (1,"Personal"),
        (2,"Study"),
        (3,"Work")
    )
    task_type = models.IntegerField(choices=task_choices,verbose_name="Recording tasks")
    task_name = models.CharField(verbose_name="Name of the taks", max_length = 100)
    est_time = models.IntegerField(verbose_name="Estimated time")
    moti = models.IntegerField(verbose_name="Motivation(0-10)")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='regstered_tasks')
    
class Task_complete(models.Model):
    task_bridge = models.OneToOneField(Task_register,on_delete=models.CASCADE)
    finished_choices = (
        (1,"Morning"),
        (2,"Day"),
        (3,"Night")
    )
    actual_time = models.IntegerField(verbose_name="Actual Time Taken")
    num_of_seatings = models.IntegerField(verbose_name="Number of seatings")
    percent_completed = models.IntegerField(verbose_name="Percentage completion")
    finished_time = models.IntegerField(choices=finished_choices, verbose_name="Recording completed tasks")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_tasks',null=True)

    def save(self, *args, **kwargs):
        TaskSummary.objects.create(
                task_type= self.task_bridge.task_type,
                task_name= self.task_bridge.task_name,
                est_time= self.task_bridge.est_time,
                moti= self.task_bridge.moti,
                actual_time= self.actual_time,
                num_of_seatings= self.num_of_seatings,
                percent_completed= self.percent_completed,
                finished_time= self.finished_time,
                user= self.user
        )
        task_register_instance = self.task_bridge
        task_register_instance.delete()  # Delete corresponding Task_register


class TaskSummary(models.Model):
    task_type = models.IntegerField(choices=Task_register.task_choices)
    task_name = models.CharField(max_length=100)
    est_time = models.IntegerField()
    moti = models.IntegerField()
    
    actual_time = models.IntegerField()
    num_of_seatings = models.IntegerField()
    percent_completed = models.IntegerField()
    finished_time = models.IntegerField(choices=Task_complete.finished_choices)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task_name} - {self.user.username}"
    
class Analytics(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    average_time_completion = models.IntegerField()
    average_time_estimated = models.IntegerField()
    no_task_completed = models.IntegerField()
    no_task_remaining = models.IntegerField()
    average_motivation = models.IntegerField()
    average_seatings = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}"



    
    




    
   