from django import forms
from .models import CardCollection, FlashCard

class CollectionForm(forms.ModelForm):

    class Meta:
        model = CardCollection
        fields = ('title',)