from django.urls import path 
from . import views

urlpatterns = [ 
    path('bird_list/', views.bird_list,name='bird_list'),
    path('bird_create/', views.bird_create,name='bird_create'),
    path('bird_update/<id>/', views.bird_edit,name='bird_edit'),
    path('bird_delete/<id>/', views.destroy,name='bird_destroy'),


    path('bird_family_list/', views.bird_family_list,name='bird_family_list'),
    path('bird_family_create/', views.bird_family_create,name='bird_family_create'),
    path('bird_family_update/<id>/', views.bird_family_edit,name='bird_family_edit'),
    path('bird_family_delete/<id>/', views.bird_family_destroy,name='bird_family_destroy')
]
