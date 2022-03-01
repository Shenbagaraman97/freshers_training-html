from django.urls import path
from employee import views

urlpatterns = [
    path('employee/', views.queryset_list),
    path('employee/<int:pk>/', views.queryset_detail),
]