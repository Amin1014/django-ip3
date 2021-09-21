from .models import Image, Review, Profile, Project
from django import forms
from django.forms import Textarea


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user',]

class PostProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ["profile", "post_date"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating' , 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')


class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']
