from . import views
from django.urls import path

urlpatterns = [
    path('', views.trialList, name='trial'),
    path('detail/<str:pk>/',views.trailDetail, name='detail'),
    path('create',views.trialCreate, name='create'),
    path('update/<str:pk>/',views.trialUpdate, name='update'), 
    path('delete/<str:pk>/',views.trialDelete, name='delete'),
]
