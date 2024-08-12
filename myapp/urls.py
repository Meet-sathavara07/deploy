"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loadindex),
    path('loadabout/',views.loadabout),
    path('loadservice/',views.loadservice),
    path('pcba/', views.pcba),
    path('smt/', views.smt),
    path('thole/', views.thole),
    path('bga/', views.bga),
    path('turnkey/', views.turnkey),
    path('boxb/', views.boxb),
    path('cem/', views.cem),
    path('pcbspacegrade/', views.pcbspacegrade),
    path('pcbaerospacedefence/',views.pcbaerospacedefence),
    path('loadinfrastructure/',views.loadinfrastructure),
    path('projectcompleted/', views.projectcompleted),
    path('spacequalified/',views.spacequalified),
    path('emvariousindus/',views.emvariousindus),
    path('achievement/',views.achievement),
    path('awardscertificate/',views.awardscertificate),
    path('careers/',views.careers),
    path('testimonial/',views.testimonial),
    path('loadcontact/',views.loadcontact),
    path('contact/', views.loadcontact, name='contact'),
    path('success/', views.success, name='success'),  # Add a success view and template

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)