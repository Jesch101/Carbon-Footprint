
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('cf_app/', include('cf_app.urls')),
    path('', RedirectView.as_view(pattern_name='home_view'), name='home'),
    path('admin/', admin.site.urls),
]
