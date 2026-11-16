from django import forms
from movies.models import Movie, Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Documentary, Mystery...'}),
        }


class MovieBaseForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter movie title...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description...'}),
            'release_year': forms.NumberInput(attrs={'placeholder': 'Movie release year...'}),
            'poster_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'genres': forms.CheckboxSelectMultiple(),
        }


class MovieCreateForm(MovieBaseForm):
    ...


class MovieEditForm(MovieBaseForm):
    ...


class MovieDeleteForm(MovieBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
