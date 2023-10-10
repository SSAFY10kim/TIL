from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs = {
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 255,
            }
        )
    )
    summary = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs = {
                'class' : 'my-summary',
                'placeholder' : 'Enter the summary',
                'row' : 5,
                'cols' : 50,
            }
        )
    )

    image = forms.ImageField(label="포스터")

    class Meta:
        model = Movie
        fields = '__all__'