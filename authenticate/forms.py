from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Feedback,Quiz




class EditProfileForm(UserChangeForm):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ'}))
    student_code = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mã Sinh viên'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        #excludes private information from User
        fields = ('username', 'first_name', 'last_name', 'email','password','student_code')
    

class DeleteUser(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DeleteUser, self).__init__(*args, **kwargs)

class FeedbackUser(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('user_send','messages',)

class addQuestionform(forms.ModelForm):
    class Meta:
        model=Quiz
        fields="__all__"

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), )
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tên'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Họ'}))
    student_code = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mã Sinh viên'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','student_code', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Yêu cầu 150 ký tự trở xuống, chỉ bao gồm chữ cái, chữ số và các kí tự @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn</li><li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu của bạn không được là mật khẩu thường được sử dụng.</li><li>Mật khẩu phải bao gồm cả chữ cái và số</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Nhập mật khẩu giống như trên để xác minh.</small></span>'