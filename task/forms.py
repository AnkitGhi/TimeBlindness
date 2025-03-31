from django import forms
from .models import Task_register, Task_complete

class Data_provide(forms.ModelForm):
    class Meta:
        model = Task_register
        fields = ['task_type','task_name','est_time','moti']

class Submission_Provide(forms.ModelForm):
    
    class Meta:
        model = Task_complete
        fields = ['actual_time','num_of_seatings','percent_completed','finished_time']


  