from django.urls import path
from .views import (TaskList, LoginPage, RegisterPage, TodoCreateView, TaskUpdate, TaskDelete, UserProfileUpdate,
                    UserProfileDelete)
from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)
urlpatterns = [
    path('', TaskList.as_view(), name='main-page'),
    path('accounts/login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name='register'),
    path('todo_create/', TodoCreateView.as_view(), name='todo_create'),
    path("task-update/<int:pk>", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>", TaskDelete.as_view(), name="task-delete"),
    path("user-detail/<pk>[0-9]", UserProfileUpdate.as_view(), name="user_detail"),
    path("user-delete/<pk>[0-9]", UserProfileDelete.as_view(), name="user_delete"),
    # password reset
    path('password-reset', PasswordResetView.as_view(template_name='demo_app/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='demo_app/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='demo_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='demo_app/password_reset_complete.html'),
         name='password_reset_complete'),
]