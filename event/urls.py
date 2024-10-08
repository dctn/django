from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.index,name="index"),
    path("base",views.base),
    path("detail/<int:id>",views.detail,name="detail"),
    path("add/",views.add,name="add")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)