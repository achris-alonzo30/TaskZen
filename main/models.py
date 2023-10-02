from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ProjectFolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_folder_name = models.CharField(max_length=256, null=True, blank=True, verbose_name="Project Folder Name")
    project_folder_created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.project_folder_name is not None:
            return str(self.project_folder_name)
        else:
            return "No title"


class TodoItem(models.Model):
    CATEGORY_CHOICES = (
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('school', 'School'),
        ('social', 'Social'),
        ('health', 'Health'),
        ('finances', 'Finances'),
        ('hobbies', 'Hobbies'),
        ('miscellaneous', 'Miscellaneous'),
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    project_folder = models.ForeignKey(ProjectFolder, on_delete=models.PROTECT, null=True, blank=True)
    todo_title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Title")
    description = models.TextField(blank = True, null = True)
    completed = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='', null=True, blank=True)
    due_date = models.DateField(blank = True, null = True, verbose_name="Due Date")
    due_time = models.TimeField(blank = True, null = True, verbose_name="Due Time")

    def __str__(self):
        if self.todo_title is not None:
            return str(self.todo_title)
        else:
            return "No title"


class CompletedTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_folder = models.ForeignKey(ProjectFolder, on_delete=models.PROTECT, null=True, blank=True)
    completed_task_title = models.CharField(max_length=256, null=True, blank=True, verbose_name="Title")
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(blank=True, null=True, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    category = models.CharField(max_length=20, choices=TodoItem.CATEGORY_CHOICES, default='', null=True, blank=True)
    due_date = models.DateField(blank=True, null=True, verbose_name="Due Date")
    due_time = models.TimeField(blank=True, null=True, verbose_name="Due Time")

    def __str__(self):
        if self.completed_task_title is not None:
            return str(self.completed_task_title)
        else:
            return "No title"

