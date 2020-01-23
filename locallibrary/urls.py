from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

admin.site.site_header = "Mozilla Django Tutorial Admin"
admin.site.site_title = "Mozilla Django Tutorial Portal"
admin.site.index_title = "Mozilla Django Tutorial Portal"
