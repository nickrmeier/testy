from django.shortcuts import render, redirect
from .models import CardCollection, FlashCard
from.forms import CollectionForm, FlashCardForm


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


def flashcard_create(request):
    if request.method == 'POST':
        form = FlashCardForm(request.POST)
        if form.is_valid():
            flashcard = form.save()
            return redirect('collection_list')
    else:
        form = FlashCardForm()
    return render(request, 'testy/flashcard_form.html', {'form': form})


def collection_edit(request, pk):
    collection = CardCollection.objects.get(pk=pk)
    if request.method == "POST":
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            collection = form.save()
            return redirect('collection_detail', pk=collection.pk)
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'testy/collection_form.html', {'form': form})


def collection_delete(request, pk):
    CardCollection.objects.get(id=pk).delete()
    return redirect('collection_list')

def flashcard_delete(request, pk):
    card = FlashCard.objects.get(id=pk).delete()
    return redirect('collection_list')
