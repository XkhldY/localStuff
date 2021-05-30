from django.urls import path
from .views import home, welwel,  new_invitation
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'home', home, name='player_home'),
    path(r'welwel', welwel),
    path(r'login', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path(r'logout', LogoutView.as_view(), name='player_logout'),
    path(r'new_invitation$', new_invitation, name='player_new_invitation')
]
