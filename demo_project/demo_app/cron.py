import os

from .models import Todo, NotificationMassages, Notification
from django.core import mail
from datetime import datetime, timedelta


def cron_test():
    todo_data = Todo.objects.all()
    notification_alert = NotificationMassages.objects.filter(massage_title="Alert").first()
    for todo_details in todo_data:
        if not todo_details.is_completed:
            naive = todo_details.deadline_time.replace(tzinfo=None) + timedelta(hours=5.50)
            updated_time = datetime.now().replace(tzinfo=None)
            if (updated_time.hour == naive.hour) and (updated_time.minute == naive.minute) and \
                    (naive.day == updated_time.day) and (naive.month == updated_time.month) \
                    and (updated_time.year == naive.year):
                connection = mail.get_connection()
                connection.open()
                email2 = mail.EmailMessage(
                    f'remind your deadline time for - {todo_details.title}-{notification_alert}',
                    f'{notification_alert.massage_description} -- Thank you',
                    os.environ.get('EMAIL_HOST_USER'),
                    [todo_details.user.email],
                    connection=connection,
                )
                email2.send()

                notification_update = Notification(todo=todo_details, user=todo_details.user
                                                   , notification_massage=notification_alert
                                                   , is_send=True, sand_datetime=datetime.now())
                notification_update.save()
