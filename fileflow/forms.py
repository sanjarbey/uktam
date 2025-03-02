from django import forms
from .models import Person, Friend

# Person uchun forma
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'surename', 'type', 'send', 'sendstatus',  'document', 'image']

# Friend uchun forma
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['firstname', 'lastname', 'surename', 'type', 'status']
