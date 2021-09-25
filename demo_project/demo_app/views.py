import os
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from .models import User, Todo, NotificationMassages, Notification
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View
from .forms import LoginForm, RegisterUserForm, TodoListCreate
from django.core import mail
from datetime import datetime, timedelta, timezone
from plyer import notification
from constants import (REGISTER, LOGIN, TODO,
                       MAIN_PAGE, TODO_APP)


class RegisterPage(CreateView):
    model = User
    template_name = 'demo_app/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy(MAIN_PAGE)

    def form_valid(self, form):
        notification_register = NotificationMassages.objects.filter(massage_title=REGISTER).first()
        form.save()
        send_email_function(form, notification_register)
        return redirect(MAIN_PAGE)


class TaskList(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'demo_app/home_page.html'
    context_object_name = TODO
    ordering = ['is_completed']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TODO] = context[TODO].filter(user=self.request.user)
        context['count'] = context[TODO].filter(is_completed=False).count()

        search_input = self.request.GET.get('search-area', '')
        if search_input:
            context[TODO] = context[TODO].filter(title__contains=search_input)

        context['search_input'] = search_input
        context['massages'] = get_notification_data(self.request)
        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoListCreate
    template_name = 'demo_app/task_form.html'

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user
        todo.create_time = datetime.now(tz=timezone.utc) + timedelta(hours=5.50)
        notification_update_obj = NotificationMassages.objects.filter(massage_title="create").first()

        title = notification_update_obj.massage_title
        message = notification_update_obj.massage_description
        app_name = TODO_APP
        popup_notification(title, message, app_name)
        todo.save()
        return redirect(MAIN_PAGE)


class TaskUpdate(UpdateView):
    model = Todo
    template_name = 'demo_app/task_form.html'
    form_class = TodoListCreate
    success_url = reverse_lazy(MAIN_PAGE)

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user
        todo_data = Todo.objects.all()
        notification_update_obj = NotificationMassages.objects.filter(massage_title="update").first()
        for todo_details in todo_data:
            notification_update = Notification(todo=todo_details, user=todo_details.user
                                               , notification_massage=notification_update_obj
                                               , is_send=True, sand_datetime=datetime.now())
            notification_update.save()
        todo.save()
        notification_alert = NotificationMassages.objects.filter(massage_title="update").first()
        title = notification_alert.massage_title
        message = notification_alert.massage_description
        app_name = TODO_APP
        popup_notification(title, message, app_name)
        return redirect(MAIN_PAGE)


class TaskDelete(DeleteView):
    model = Todo
    template_name = 'demo_app/task_confirm_delete.html'
    fields = "__all__"
    success_url = reverse_lazy(MAIN_PAGE)


class UserProfileUpdate(UpdateView):
    model = User
    template_name = 'demo_app/user_detail.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy(MAIN_PAGE)

    def form_valid(self, form):
        todo_user = form.save(commit=False)
        todo_user.user = self.request.user
        todo_user.user.update_time = datetime.now()
        todo_user.save()
        return redirect(MAIN_PAGE)


class UserProfileDelete(DeleteView):
    model = User
    template_name = 'demo_app/task_confirm_delete.html'
    context_object_name = "todo-delete"
    fields = "__all__"
    success_url = reverse_lazy(LOGIN)


class LoginPage(View):
    template_name = 'demo_app/login.html'
    success_url = MAIN_PAGE

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                messages.info(request, "Please enter correct Username/Email and Password")
                return render(request, self.template_name, {'form': form})
        if user.check_password(password):
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Success: You have login successfully.")
            return redirect(MAIN_PAGE)
        return render(request, self.template_name, {'form': form, 'success':True})


def get_notification_data(request):
    massages = []
    all_data = Notification.objects.select_related('notification_massage').select_related(TODO).filter(
        user=request.user.id).all()

    for date_get in all_data:
        msg_target = NotificationMassages.objects.filter(massage_title=date_get.notification_massage).first()
        todo_target = Todo.objects.filter(title=date_get.todo).first()
        massage = f"{todo_target.title} task {msg_target.massage_description} "
        massages.append(massage)

    return massages


def send_email_function(form, notification_detail):
    try:
        connection = mail.get_connection()
        connection.open()
        email1 = mail.EmailMessage(
            f'{notification_detail.massage_title}',
            f'{notification_detail.massage_description}-- Thank you',
            os.environ.get('EMAIL_HOST_USER'),
            [form.cleaned_data['email']],
            connection=connection,
        )
        email1.send()
    except AttributeError:
        pass


def popup_notification(title, message, app_name):
    notification.notify(title=title,
                        message=message,
                        app_name=app_name,
                        timeout=5,
                        toast=False)
