from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile_number = models.IntegerField(default=123)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    deadline_time = models.DateTimeField(null=True, blank=True)
    is_important = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class NotificationMassages(models.Model):
    massage_title = models.CharField(max_length=200)
    massage_description = models.TextField(max_length=300)

    def __str__(self):
        return self.massage_title


class Notification(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_massage = models.ForeignKey(NotificationMassages, on_delete=models.CASCADE)
    is_send = models.BooleanField(default=False)
    sand_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

