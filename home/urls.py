from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('loginform/', views.login_page, name="loginform"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_page, name='logout'),
    path('product/', views.product, name='product'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('jobs/', views.jobs, name='jobs'),
    path('viewcontact/', views.viewcontact, name='viewcontact'),
    path('addjob/', views.addjob, name='addjob'),
    path('addnotification/', views.addnotification, name='notiification'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    path('viewcomplain/', views.viewcomplain, name='viewcomplain'),
    path('viewemployee/', views.viewemployee, name='viewemployee'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('feedback/', views.feedback, name='feedback'),
    path('complain/', views.complain, name='complain'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('subscriber/', views.subscriber, name='subscriber'),


]




if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
