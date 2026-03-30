from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = '&#9825; BagLuxe Administration'
admin.site.site_title = 'BagLuxe Admin'
admin.site.index_title = 'Welcome to BagLuxe Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
