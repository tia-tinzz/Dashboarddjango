from django.urls import path
from.import views as v 


urlpatterns = [
    path('',v.login,name="loginpage"),  
    path('logoutform/',v.logoutfn,name="logoutformpage"),
    path('register/',v.registration,name="registerpage"),
    path('main/',v.index,name="mainpage"),
]