from django.urls import path
from poll import views

app_name = 'poll'

urlpatterns = [
    path('index/', views.index, name="index")
]