from django.urls import path

from users.views import signup,userlogout,userlogin,home

app_name = 'users'
urlpatterns = [
    path('',home,name="home"),
    path('signup/',signup,name="signup"),
    path('logout/',userlogout,name="userlogout"),
    path('login/',userlogin,name="userlogin"),
]