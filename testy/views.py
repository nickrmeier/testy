from django.shortcuts import render, redirect
from .models import CardCollection, FlashCard
from.forms import CollectionForm


def collection_list(request):
    collections = CardCollection.objects.all()
    return render(request, 'testy/collection_list.html', {'collections': collections})


def collection_detail(request, pk):
    collection = CardCollection.objects.get(id=pk)
    return render(request, 'testy/collection_detail.html', {'collection': collection})


def flashcard_detail(request, pk):
    card = FlashCard.objects.get(id=pk)
    return render(request, 'testy/flashcard_detail.html', {'card': card})

def collection_create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_detail', pk=collection.pk)
    else:
        form = CollectionForm()
    return render(request, 'testy/collection_form.html', {'form': form})