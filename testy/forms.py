from django import forms
from .models import CardCollection, FlashCard

class CollectionForm(forms.ModelForm):

    class Meta:
        model = CardCollection
        fields = ('title',)

class FlashCardForm(forms.ModelForm):

    class Meta:
        model = FlashCard
        fields = ('collection', 'question', 'answer',)
