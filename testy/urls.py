from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection_list, name='collection_list'),
    # path('cards/', views.flashcard_list, name='flashcard_list'),
    path('cards/<int:pk>', views.collection_detail, name='collection_detail'),
    path('card/<int:pk>', views.flashcard_detail, name='flashcard_detail'),

]
