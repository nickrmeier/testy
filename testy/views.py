from django.shortcuts import render
from .models import CardCollection, FlashCard


def collection_list(request):
    collections = CardCollection.objects.all()
    return render(request, 'testy/collection_list.html', {'collections': collections})


def collection_detail(request, pk):
    collection = CardCollection.objects.get(id=pk)
    return render(request, 'testy/collection_detail.html', {'collection': collection})


def flashcard_detail(request, pk):
    card = FlashCard.objects.get(id=pk)
    return render(request, 'testy/flashcard_detail.html', {'card': card})
