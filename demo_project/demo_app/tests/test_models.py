from datetime import datetime

from django.test import TestCase
from ..models import (User,
                      NotificationMassages,
                      Category, Todo, Notification)


class TestUser(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username="viral",
                                             email="viralpy1@gmail.com",
                                             mobile_number="9228110541",
                                             password="123"
                                             )

        self.category = Category.objects.create(
            category_name='general',
            create_time=datetime.now(),
        )

        self.todo = Todo.objects.create(
            user=self.user,
            category=self.category,
            title='todo app',
            description='working on it',
            deadline_time='2019-07-16 22:24',
            is_important=False,
            is_completed=False,
        )

    def test_should_create_user(self):
        user = User.objects.create(username="viren", email="viren@gmail.com",
                                   mobile_number="9228110541", password="123")
        self.assertEqual(str(user), user.username)

    def test_notification_messages(self):
        notification_messages = NotificationMassages.objects.create(
            massage_title='alert',
            massage_description='deadline is over'
        )
        self.assertEqual(str(notification_messages), notification_messages.massage_title)

    def test_notification(self):
        notification_messages = NotificationMassages.objects.create(
            massage_title='register',
            massage_description='register successfully'
        )
        notification = Notification.objects.create(
            todo=self.todo,
            user=self.user,
            notification_massage=notification_messages,
            is_send=True,
            sand_datetime=datetime.now()
        )
        self.assertEqual(str(notification), notification.user.username)
