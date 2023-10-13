from django import forms
from .models import Movie, Comment

GENRE_CHOICES = (
    ('판타지', '판타지'),
    ('코미디' , '코미디'),
    ('로맨스', '로맨스'),
)


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

    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        label="장르",
        widget=forms.Select()
    )

    score = forms.DecimalField(
        label="평점",
        max_value=5,
        min_value=0,  
        decimal_places=1,  
        max_digits=3,
    )

    image = forms.ImageField(required=False, label="포스터")

    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(label="댓글", widget=forms.TextInput())