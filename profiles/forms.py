from django import forms
from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['activated_at']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...'}),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell us about yourself...',
                'rows': 3,
            }),
            'profile_picture': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class ProfileCreateForm(ProfileBaseForm):
    ...


class ProfileEditForm(ProfileBaseForm):
    ...


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
