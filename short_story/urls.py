from django.urls import path
from . import views

app_name = 'short_story'


urlpatterns = [
    path('', views.short_story_list_view, name='shortstory_list'),
]
