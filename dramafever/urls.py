from django.urls import path

from . import views

app_name = 'dramafever'
urlpatterns = [
    path('', views.topics, name='topics'),
    path('<int:topic_id>/', views.topics_detail, name='topics_details'),
]