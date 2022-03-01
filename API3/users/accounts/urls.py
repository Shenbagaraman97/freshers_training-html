
from django.urls import path
# from knox import views as knox_views

# from .views import LoginAPI
# from accounts import views
from accounts.views import Register,Signin

urlpatterns = [
   
    path('signup/',Register.as_view(), name="signup"),
    path('signin/',Signin.as_view(),name="signin")
    
]