from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.index, name="main_page"),
    path('groups/<slug:slug>/', views.group_posts, name="groups_list"),
]
