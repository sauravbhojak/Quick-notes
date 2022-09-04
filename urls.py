from django.urls import path,include
from .import views

urlpatterns = [
  path('',views.indexpage,name='indexpage'),
  path('notes/',views.notes,name='notes'),
  path('up_note/<int:pk>',views.edit,name='up_note')
]
