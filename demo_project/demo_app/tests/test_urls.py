from django.test import TestCase
from django.urls import reverse, resolve
from ..views import (TaskList, LoginPage, RegisterPage,
                     TodoCreateView, TaskUpdate, TaskDelete)

from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetCompleteView)
from ..models import User


class Test_url(TestCase):

    def setup(self):
        user = User.objects.create_user(username="admin",
                                        email="viralpy1@gmail.com",
                                        mobile_number="9228110541",
                                        password="123"
                                        )
        return user

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginPage)

    def test_main_page_url_is_resolved(self):
        url = reverse('main-page')
        self.assertEquals(resolve(url).func.view_class, TaskList)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterPage)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_todo_create_url_is_resolved(self):
        url = reverse('todo_create')
        self.assertEquals(resolve(url).func.view_class, TodoCreateView)

    def test_task_update_url_is_resolved(self):
        url = reverse('task-update', args='1')
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)

    def test_task_delete_url_is_resolved(self):
        url = reverse('task-delete', args='1')
        self.assertEquals(resolve(url).func.view_class, TaskDelete)

    def test_user_update_url_is_resolved(self):
        url = self.client.get(reverse('user_detail', args=(self.setup().id,)))
        self.assertEqual(url.status_code, 200)

    def test_password_reset_url_is_resolved(self):
        url = reverse('password_reset')
        self.assertEquals(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse('password_reset_done')
        self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse('password_reset_complete')
        self.assertEquals(resolve(url).func.view_class, PasswordResetCompleteView)
