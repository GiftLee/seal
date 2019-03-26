from django.urls import path
from system.views import login_view, UserPasswordUpdateView, logout_view, GetInfo

app_name = "system"

urlpatterns = [
    path('login', login_view, name="login"),
    path('password_update', UserPasswordUpdateView.as_view(), name="password_update"),
    path('logout', logout_view, name="logout"),
    path('get_info', GetInfo.as_view()),
]
