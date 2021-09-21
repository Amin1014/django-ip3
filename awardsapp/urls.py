from django.urls import path,re_path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [

    path('', views.home_projects, name='homePage'),
    # path('search/', views.search_projects, name='search_projects'),
    re_path('image', views.project, name='project'),
    path('users/', views.user_list, name='user_list'),
    path('new/image', views.new_image, name='new_image'),
    path('profile/', views.profile, name='profile'),
    path('upload/profile', views.upload_profile, name='upload_profile'),
    path('post/', views.post_project, name = 'post'),
    # path('new/project', views.new_project, name='new_project'),
    # path('edit/profile', views.edit_profile, name='edit_profile'),
    # re_path('profile/',
    #     views.individual_profile_page, name='individual_profile_page'),
    # path('project', views.project_list, name='project_list'),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), {"next_page": '/'}),
    path('accounts/',include('django_registration.backends.one_step.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)