from django.urls import path
from . import views
app_name='movieapp'


urlpatterns=[
    path('',views.movie,name='movie'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name="add_movie"),
    path('update/<int:id>/', views.update,name='update'),
    path('dele/<int:id>/',views.delete,name='delete')
]