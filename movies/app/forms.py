from cProfile import label

from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watch_again'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Review
        fields = ['text', 'watch_again']
        labels = {'text': 'Обзор', 'watch_again': 'Посмотреть снова'}
        widgets = {
            'text': Textarea(attrs={'rows': 4})
        }
