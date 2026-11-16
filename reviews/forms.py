from django import forms
from reviews.models import Review


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'placeholder': 'Rate from 1 to 5'}),
            'review_text': forms.Textarea(attrs={'placeholder': 'Write your thoughts about this movie...', 'rows': 5}),
        }


class ReviewCreateForm(ReviewBaseForm):
    pass


class ReviewEditForm(ReviewBaseForm):
    pass


class ReviewDeleteForm(ReviewBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
