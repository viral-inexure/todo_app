# import os
#
# for i in os.environ:
#     if i == 'EMAIL_HOST_USER':
#         print("d")
#
# # print('deadline_time---->', form.cleaned_data['deadline_time'])
# # print(type(form.cleaned_data['deadline_time']))
# # todo_time = Todo.objects.filter(deadline_time=form.cleaned_data['deadline_time']).first()
# # c_time = todo_time.create_time
# # print('time_diff ---->', form.cleaned_data['deadline_time'] > c_time)
# # print('time_diff ---->', form.cleaned_data['deadline_time'] - c_time)
# # print(type(form.cleaned_data['deadline_time'] - c_time))
# # if form.cleaned_data['deadline_time'] > c_time:
# #     time.sleep(form.cleaned_data['deadline_time'] - c_time)
#
#
#
#  # SELECT dn.notification_massage_id, du.username, dnm.massage_title, dnm.massage_description FROM
#     # demo_app_notification dn LEFT JOIN demo_app_user du ON dn.user_id = du.id LEFT JOIN demo_app_notificationmassages
#     # dnm ON dn.notification_massage_id = dnm.id WHERE user_id = 19
#
# ***** firebase generate accoutnt information
# import firebase_admin
# from firebase_admin import credentials
#
# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
#
# *****************
#
# // Import the functions you need from the SDKs you need
# import { initializeApp } from "firebase/app";
# import { getAnalytics } from "firebase/analytics";
# // TODO: Add SDKs for Firebase products that you want to use
# // https://firebase.google.com/docs/web/setup#available-libraries
#
# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
# const firebaseConfig = {
#   apiKey: "AIzaSyB3Jdp3kZWHUQP_suV7k4sTDW7USLO9ZXM",
#   authDomain: "todo-app-3eeab.firebaseapp.com",
#   projectId: "todo-app-3eeab",
#   storageBucket: "todo-app-3eeab.appspot.com",
#   messagingSenderId: "113654336372",
#   appId: "1:113654336372:web:791924a5a93491aa1bba21",
#   measurementId: "G-PWKGJ0VQWW"
# };
#
# // Initialize Firebase
# const app = initializeApp(firebaseConfig);
# const analytics = getAnalytics(app);
#
#
#
# # for notification
# import subprocess
#
#
# def sub_process():
#     subprocess.Popen(['notify-send', 'deadline time over'])
#
# sub_process()


# def LoginPage(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             try:
#                 user = User.objects.get(email=username)
#             except User.DoesNotExist:
#                 messages.info(request, "Please enter correct Username/Email and Password")
#                 return render(request, 'demo_app/login.html', {'form': form})
#         if user.check_password(password):
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect(MAIN_PAGE)
#     else:
#         form = LoginForm()
#         messages.success(request, "Success: You have login successfully.")
#     return render(request, 'demo_app/login.html', {'form': form})

# pip install pywhatkit
# import os
import pywhatkit
# print(os.environ.get('EMAIL_HOST_USER'))

utc = datetime
