from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length = 100)
    info = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    datecompleted = models.DateTimeField(null = True, blank = True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE) # key for connection todo_list with user


    def __str__(self):
        return self.title