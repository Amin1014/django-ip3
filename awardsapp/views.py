# from sys import _ProfileFunc
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Image,Location,tags, Profile, Review, NewsLetterRecipients, Like, Project
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewImageForm, ReviewForm
from .email import send_welcome_email
from .forms import NewsLetterForm, ProfileUploadForm,PostProjectForm

@login_required(login_url='/accounts/login/')
def home_projects (request):
    # Display all projects here:

    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))

    else:
        projects = Project.objects.all()

    form = NewsLetterForm

    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_projects')

    return render(request, 'index.html', {'project':projects, 'letterForm':form})

def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})



@login_required(login_url='/accounts/login/')

# def new_project(request):

#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user = current_user
#             project.save()
#         return redirect('homePage')

#     else:
#         form = NewProjectForm()

#     return render(request, 'templates/new_project.html', {"form": form})

# Viewing a single picture

def user_list(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'user_list.html', context)

@login_required
def post_project(request):
  if request.method == 'POST':
    post_form = PostProjectForm(request.POST,request.FILES)
    if post_form.is_valid():
      new_post = post_form.save(commit = False)
      new_post.user = request.user
      new_post.save()
      return redirect('homePage')
  else:
    post_form = PostProjectForm()
  return render(request,'post_project.html',{"post_form":post_form})


# @login_required(login_url='/accounts/login/')
# def edit_profile(request):
#     current_user = request.user

#     if request.method == 'POST':
#         form = UpdatebioForm(request.POST, request.FILES, instance=current_user.profile)
#         print(form.is_valid())
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.user = current_user
#             image.save()
#         return redirect('homePage')

#     else:
#         form = UpdatebioForm()
#     return render(request, 'registration/edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def individual_profile_page(request, username=None):
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)

    return render (request, 'registration/user_image_list.html', {'images':images, 'username': username})

@login_required(login_url='/accounts/login/')
def create_project(request):
    if request.method == 'POST':
        form = PostProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user
            project.save()
            return redirect('index')
    else:
        form = PostProjectForm()
    

    return render(request, 'new_project.html')



def update_project(request):
    pass


def update_project(request):
    pass


def delete_project(request):
    pass
# def search_projects(request):

#     # search for a user by their username
#     if 'project' in request.GET and request.GET["project"]:
#         search_term = request.GET.get("project")
#         searched_projects = Project.search_projects(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html', {"message": message, "projects": searched_projects})

#     else:
#         message = "You haven't searched for any person"
#         return render(request, 'search.html', {"message": message})

# Search for an image
def search_image(request):

        # search for an image by the description of the image
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}"

            return render(request, 'search.html', {"message": message, "pictures": searched_images})

        else:
            message = "You haven't searched for any image"
            return render(request, 'search.html', {"message": message})


# @login_required(login_url='/accounts/login/')
# def individual_profile_page(request, username):
#     print(username)
#     if not username:
#         username = request.user.username
#     # images by user id
#     images = Image.objects.filter(user_id=username)
#     user = request.user
#     profile = Profile.objects.get(user=user)
#     userf = User.objects.get(pk=username)
#     latest_review_list = Review.objects.filter(user_id=username).filter(user_id=username)
#     context = {'latest_review_list': latest_review_list}
#     if userf:
#         print('user found')
#         profile = Profile.objects.get(user=userf)
#     else:
#         print('No such user')
#     return render (request, 'registration/user_image_list.html', context, {'images':images,
#                                                                   'profile':profile,
#                                                                   'user':user,
#                                                                   'username': username})
def review_list(request):
    latest_review_list = Review.objects.all()
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)


# def review_detail(request, review_id):
    # review = get_object_or_404(Review, pk=review_id)
    # return render(request, 'review_detail.html', {'review': review})


def project_list(request):
    project_list = Project.objects.order_by('-title')
    context = {'project_list':project_list}
    return render(request, 'project_list.html', context)


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)
            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                # requested_profile.username = form.cleaned_data[ 'username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)
            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect('')
        else:
            form = ProfileUploadForm()

    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	#  follower = Follow.objects.filter(user = profile)

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile})

