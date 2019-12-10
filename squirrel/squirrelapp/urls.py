from django.urls import path

from . import views

urlpatterns = [ 
                path('views/',views.View),
                path('',views.home),
                path('map/',views.coordinates),
                path('add/', views.add_squirrel),
                path('views/<str:Squirrel_Id>/edit/',views.edit_squirrel),
                path('stats/',views.stats),
]
