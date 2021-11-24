from django.urls.conf import path,include
from rest_framework import urlpatterns,routers

app_name = 'customers'

router = routers.DefaultRouter

urlpatterns = [
    path('',include(router.urls))
]
