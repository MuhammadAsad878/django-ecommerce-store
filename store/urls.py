from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),
    path('signup/',views.SignUp, name='signup'),
    path('loginPage/',views.LoginPage,name='loginPage'),
    path('login',views.Login,name='login'),
    path('logout',views.LogoutPage,name='logout'),
    path('home/',views.HomePage,name='home'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
