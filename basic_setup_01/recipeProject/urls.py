from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('user/<username>', views.userReceipe, name='userReceipe'),
    path('add-receipe', views.addReceipe, name='addReceipe'),
    path('delete-receipe/<int:id>', views.deleteReceipe, name='deleteReceipe'),
    path('update-receipe/<int:id>', views.updateReceipe, name='updateReceipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
