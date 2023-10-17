from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        modle = get_user_model()
    
    username = forms.CharField(label="아이디", widget=forms.TextInput())
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput())

    error_messages = {
        'invalid_login': (
            '올바른 아이디와 비밀번호를 입력해주세요'
        ),
    }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    first_name = forms.CharField(max_length=32, label="이름", widget=forms.TextInput())
    last_name = forms.CharField(max_length=32, label="성", widget=forms.TextInput())
    email = forms.EmailField(max_length=64, label="이메일 주소", widget=forms.EmailInput())

    username = forms.CharField(
        max_length=255,
        label = "사용자명",
        widget= forms.TextInput(),
    )

    password1 = forms.CharField(
        label = "비밀번호",
        widget= forms.PasswordInput(),
    )

    password2 = forms.CharField(
        label = "비밀번호 확인",
        widget = forms.PasswordInput(),
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
    
    first_name = forms.CharField(max_length=32, label="이름", widget=forms.TextInput())
    last_name = forms.CharField(max_length=32, label="성", widget=forms.TextInput())
    email = forms.EmailField(max_length=64, label="이메일 주소", widget=forms.EmailInput())

    username = forms.CharField(
        max_length=255,
        label = "사용자명",
        widget= forms.TextInput(),
    )
    password = None

class CustomPasswordChangeForm(PasswordChangeForm):
    # class Meta(PasswordChangeForm.Meta):
    #     model = get_user_model()
    old_password = forms.CharField(
        label='기존 비밀번호',
        widget=forms.PasswordInput()
    )

    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput()
    )
    
    new_password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput()
    )
    
    error_messages = {
        'password_incorrect' : "기존 패스워드가 잘못됬습니다",
        'password_mismatch' : "비밀번호 확인이 틀렸습니다"
    }