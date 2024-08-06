from django.urls import path
from . import views

urlpatterns = [
    path('',views.sample,name='home'),
    path('1',views.list,name='list'),
    path('details/<int:pk>',views.details,name='details'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('update/<int:pk>',views.update,name='update'),
    path('history',views.history,name='history')
]