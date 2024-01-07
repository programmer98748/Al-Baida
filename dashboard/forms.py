from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
##
class LoginForm(forms.Form):
    username = forms.CharField(
         widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
##
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
##


class PhotosForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {
            'description' :" الوصف",
            'image': 'الصور',
            'category_id': 'الفئة',
        }
##

##    
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
##
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image' : 'رفع الصورة الشخصية'
        }
##
class InformaionSiteForm(forms.ModelForm):
    class Meta:
        model = InformaionSite
        fields = '__all__'
        labels = {
            'name': 'اسم الموقع',
            'address': 'العنوان',
            'image_icon':' ايقونة الموقع',
            'image':'خلفية الموقع',
            'title_name': 'العنوان الوصفي الظاهر علي الخلفية',
            'email': 'البريد الالكتروي الرئيسي للموقع',
            'telephone': ' رقم الهاتف',
            'facebook': 'رابط فيسبوك',
            'twitter': 'رابط تويتر',
            'instagram': 'رابط انستجرام',
            'whatsapp': 'رابط وتساب',
            'maps': 'رابط الخريطة',
            'description' : 'وصف الموقع',
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': ' الاسم',
            'image' : ' الصورة المعروضة',
            'description':' الوصف',
            'slug':'العنوان-كارابط-وصف',

        }

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = '__all__'
        labels = {
            'title': 'عنوان المقال',
            'image' : ' الصورة المعروضة',
            'description':' نص المقال'
        }
        exclude = ('',)


class PageAboutForm(forms.ModelForm):
    class Meta:
        model =PageAbout
        fields = '__all__'
        labels = {
            'description':'  الوصف',
            'title_head': 'مهمتنا',
            'title_goal' : 'رؤيتنا',
        }
