from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection_list, name='collection_list'),
    path('cards/<int:pk>', views.collection_detail, name='collection_detail'),
    path('card/<int:pk>', views.flashcard_detail, name='flashcard_detail'),
    path('collection/new', views.collection_create, name='collection_create'),
    path('card/new', views.flashcard_create, name='flashcard_create'),
    path('collection/<int:pk>/edit', views.collection_edit, name='collection_edit'),
    path('collection/<int:pk>/delete',
         views.collection_delete, name='collection_delete'),
    path('card/<int:pk>/delete', views.flashcard_delete, name='flashcard_delete'),

]
