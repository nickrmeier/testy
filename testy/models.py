from django.db import models

class CardCollection(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title

class FlashCard(models.Model):
    collection = models.ForeignKey(CardCollection, on_delete=models.CASCADE, related_name='cards')
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.question
