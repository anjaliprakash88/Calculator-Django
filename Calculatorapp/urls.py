from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name="calculator"),
    path('submit_query', views.submitquery, name="submit_query"),
 ]