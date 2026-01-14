from django.urls import path
from app1 import views

urlpatterns = [
    path ('<int:pk>/', views.employee_detail, name='employee_detail'),
]
