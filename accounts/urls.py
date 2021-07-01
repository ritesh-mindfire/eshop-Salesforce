from django.urls import path
from accounts import views
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)