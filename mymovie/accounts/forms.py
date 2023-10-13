from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="사용자 이름", widget=forms.TextInput())
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput())

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    first_name = forms.CharField(
        max_length=32, 
        label='이름',
        widget=forms.TextInput()
        )
    last_name = forms.CharField(max_length=32, label='성', widget=forms.TextInput())
    email = forms.EmailField(max_length=64, label='이메일 주소', widget=forms.EmailInput())
    username = forms.CharField(
        max_length=150, 
        label='사용자명',
        help_text='150자 이하 문자, 숫자, 그리고 @/./+/-/_만 가능합니다.',
        widget=forms.TextInput()
    )
    password1 = forms.CharField(
        label='비밀번호',  # 원하는 레이블로 설정
        widget=forms.PasswordInput(),
        help_text='<br><ul><li>다른 개인 정보와 유사한 비밀번호는 사용할 수 없습니다.</li><li>비밀번호는 최소 8자리 이상이어야 합니다.</li><li>통상적으로 자주 사용되는 비밀번호는 사용할수 없습니다.</li><li>숫자로만 이루어진 비밀번호는 사용할수 없습니다.</li></ul>',
    )
    
    password2 = forms.CharField(
        label='비밀번호 확인',  # 원하는 레이블로 설정
        widget=forms.PasswordInput(),
        help_text='확인을 위해 이전과 동일한 비밀번호를 입력하세요.',
    )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username')

    email = forms.CharField(
        max_length= 64,
        label = "이메일 주소",
        widget=forms.EmailInput(),
    )

    first_name = forms.CharField(
        max_length=32,
        label = "이름",
        widget=forms.TextInput(),
    )

    last_name = forms.CharField(
        max_length=32,
        label="성",
        widget=forms.TextInput(),
    )

    username = forms.CharField(
        max_length=150, 
        label='사용자명',
        help_text='150자 이하 문자, 숫자, 그리고 @/./+/-/_만 가능합니다.',
        widget=forms.TextInput()
    )

    password = None

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="기존 비밀번호",
        widget=forms.PasswordInput()
    )

    new_password1 = forms.CharField(
        label="새 비밀번호",
        widget=forms.PasswordInput(),
        help_text='<br><ul><li>다른 개인 정보와 유사한 비밀번호는 사용할 수 없습니다.</li><li>비밀번호는 최소 8자리 이상이어야 합니다.</li><li>통상적으로 자주 사용되는 비밀번호는 사용할수 없습니다.</li><li>숫자로만 이루어진 비밀번호는 사용할수 없습니다.</li></ul>'
    )

    new_password2 = forms.CharField(
        label="새 비밀번호(확인)",
        widget=forms.PasswordInput(),
    )
