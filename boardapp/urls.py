from django.urls import path
from .views import signupfunc, loginfunc, listfunc
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('list/', listfunc, name='list'),
]

urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)