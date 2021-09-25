from django.contrib import admin
from .models import User, Category, Todo, NotificationMassages, Notification

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(NotificationMassages)
admin.site.register(Notification)
