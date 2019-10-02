from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('new/', views.new),
    path('create/', views.create),
    # Read
    path('', views.index,),
    path('<int:page_id>/', views.detail),
    # Update
    path('<int:page_id>/edit/', views.edit),
    path('<int:todo_id>/update/', views.update),
    # Delete
    path('<int:page_id>/delete/', views.delete),
]