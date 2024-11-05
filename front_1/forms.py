from django import forms
from django.core import validators

# 留言板的表单
class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=20,min_length=2,label='标题',error_messages={"min_length":'标题长度不能小于2个字符'})
    content = forms.CharField(widget=forms.Textarea,label='内容')
    email = forms.EmailField(label='邮箱')

class RegisterForm(forms.Form):
    telephone = forms.CharField(
        validators=[
            validators.RegexValidator(regex='^1[3-9]\d{9}$',
                                      message='手机号格式错误')]
    )
    pwd1 = forms.CharField(max_length=100,min_length=6)
    pwd2 = forms.CharField(max_length=100,min_length=6)

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码输入不一致')
        else:
            return cleaned_data