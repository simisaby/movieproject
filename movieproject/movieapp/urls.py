from . import views
from django.urls import path

app_name='movieapp'    #namespace
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update_movie,name='update'),
    path('delete/<int:id>/',views.delete_movie,name='delete'),
]