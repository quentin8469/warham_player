from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account.views import SignUpView, LogoutView, connexion

app_name = 'account'

urlpatterns = [
    path('', connexion, name='connexion'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)