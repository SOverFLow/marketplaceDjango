from django import forms
from .models import Item

CLASS_TAILWIND = 'w-full px-4 py-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category' : forms.Select(attrs={
                'class' : CLASS_TAILWIND
            }),
            'name' : forms.TextInput(attrs={
                'class' : CLASS_TAILWIND
            }),
            'description' : forms.Textarea(attrs={
                'class' : CLASS_TAILWIND
            }),
            'price' : forms.TextInput(attrs={
                'class' : CLASS_TAILWIND
            }),
            'image' : forms.FileInput(attrs={
                'class' : CLASS_TAILWIND
            }),

            

        }