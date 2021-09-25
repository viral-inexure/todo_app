from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from ..models import (User, Category,
                      Todo)
from constants import (REGISTER, LOGIN)


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="admin",
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

    def tearDown(self):
        self.user.delete()
        self.todo.delete()
        self.category.delete()

    def test_project_register(self):
        response = self.client.post(reverse(REGISTER), {
            'username': 'viralmalaviya',
            'email': 'viralmalaviya@gmail.com',
            'mobile_number': '9409562030',
            'password1': 'mytodoapp',
            'password2': 'mytodoapp',
        })
        self.assertEquals(response.status_code, 302)

    def test_login_function(self):
        response = self.client.post(reverse(LOGIN), {
            'username': self.user.username,
            'password': '123'
        })
        self.assertEquals(response.status_code, 302)

    def test_login_function_email(self):
        response = self.client.post(reverse(LOGIN), {
            'username': self.user.email,
            'password': '123'
        })
        self.assertEquals(response.status_code, 302)

    def test_project_create_todo_get(self):
        self.client.post(reverse(LOGIN), {
            'username': self.user.username,
            'password': '123'
        })
        response = self.client.post(reverse('todo_create'), {
            'user': self.user,
            'category': self.category,
            'title': 'todo app',
            'description': 'working on it',
            'deadline_time': '2019-07-16 22:24',
            'is_important': False,
            'is_completed': False,
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'demo_app/task_form.html')

    def test_project_delete_todo_data(self):
        self.client.post(reverse(LOGIN), {
            'username': self.user.username,
            'password': '123'
        })
        response = self.client.delete(reverse('task-delete', args=(self.todo.id,)))
        self.assertEquals(response.status_code, 302)

    def test_project_update_todo_data(self):
        self.client.post(reverse(LOGIN), {
            'username': self.user.username,
            'password': '123'
        })

        response = self.client.post(reverse('task-update', args=(self.todo.id,)),
                                    {
                                        'user': self.user,
                                        'category': self.category,
                                        'title': 'todo app',
                                        'description': 'working on it',
                                        'deadline_time': '2019-07-16 22:23',
                                        'is_important': False,
                                        'is_completed': False,
                                    })

        self.assertEquals(response.status_code, 200)

    def test_should_update_profile(self):
        user1 = User.objects.create_user(username="viren",
                                         email="viral@gmail.com",
                                         mobile_number="9228110541",
                                         password="123"
                                         )
        self.client.post(reverse(LOGIN), {
            'username': 'viren',
            'password': '123'
        })
        response = self.client.post(
            reverse('user_detail', kwargs={'pk': user1.id}), context=
            {'username': "viren_cjange",
             'email': "viral@gmail.com",
             'mobile_number': "9409563987",
             'password1': "mytodoapp",
             'password2': "mytodoapp"})
        self.assertEqual(response.status_code, 200)

    def test_project_delete_user_data(self):
        self.client.post(reverse(LOGIN), {
            'username': self.user.username,
            'password': '123'
        })
        response = self.client.delete(reverse('user_delete', args=(self.user.id,)))
        self.assertEquals(response.status_code, 302)

    def test_reset_password(self):
        response = self.client.post(reverse('password_reset'))
        self.assertEquals(response.status_code, 200)