from django import forms
from django.contrib.auth.models import User
from iFood.models import UserProfile, Feedback, Comments, Product, Restaurant
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'E-Mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"8+ characters and please don't use your username as password"}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '1234 Food Street'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'https://facebook.com/your-name'}))
    twitter = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'https://twitter.com/your-twitter-name'}))
    class Meta:
        model = UserProfile
        fields = ('address','facebook','twitter')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address','facebook','twitter')

class UserDetailsForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','last_name','email','is_active')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment','created_at')

ratings = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
class RestaurantFeedbackForm(forms.ModelForm):
    rating = forms.CharField(label='How many stars would you give this restaurant?',
                             widget=forms.RadioSelect(choices=ratings))
    class Meta:
        fields = ('rating',)
        model = Restaurant



