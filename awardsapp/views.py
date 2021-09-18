from django.shortcuts import render

from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image,Location,tags, Profile, Review, NewsLetterRecipients, Like, Project
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .forms import NewImageForm, UpdatebioForm, ReviewForm, NewProjectForm
from .email import send_welcome_email
from .forms import NewsLetterForm



