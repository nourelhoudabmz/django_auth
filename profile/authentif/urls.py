from django.urls import path, include
from .views import ProfileView, SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
]
