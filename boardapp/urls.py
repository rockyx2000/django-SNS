from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, profilefunc
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('logout/', logoutfunc, name="logout"),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('profile/<int:pk>', profilefunc, name='profile'),
]

urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)