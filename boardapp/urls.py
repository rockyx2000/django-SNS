from django.urls import path
from .views import deletefunc, signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, profilefunc, readfunc, BoardCreate, deletefunc, BoardEdit
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('logout/', logoutfunc, name="logout"),
    path('', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name="read"),
    path('profile/<int:pk>', profilefunc, name='profile'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('delete/<int:pk>', deletefunc, name='delete'),
    path('edit/<int:pk>', BoardEdit.as_view(), name='edit')
]

urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)