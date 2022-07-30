from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('details/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add'),
    path('update/<int:movie_id>/',views.update,name='update'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),

]
