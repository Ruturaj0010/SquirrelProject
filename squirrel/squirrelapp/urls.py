from django.urls import path

from . import views

urlpatterns = [ 
                path('home/views/',views.View),
                path('home/',views.home),
                path('home/map/',views.coordinates),
                path('home/add/', views.add_squirrel),
                path('home/<str:Unique_Squirrel_ID>/edit/',views.edit_squirrel),
                path('home/stats/',views.stats),
]
