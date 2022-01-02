
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('cf_app/', include('cf_app.urls')),
    path('', RedirectView.as_view(pattern_name='car_changelist'), name='home'),
    path('admin/', admin.site.urls),
]
