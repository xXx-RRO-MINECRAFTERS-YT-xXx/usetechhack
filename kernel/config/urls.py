# -*- coding: utf-8 -*-

from graphene_django.views import GraphQLView

from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import TemplateView
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/<str:service>", include("pizda.services.urls")),
    path("password_reset/<str:token>", include("pizda.services.urls")),
    path("email_confirm/<str:token>", include("pizda.services.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'',
        ensure_csrf_cookie(TemplateView.as_view(template_name='index.html')),
        name='index',
    )
]
