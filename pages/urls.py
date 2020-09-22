from django.urls import path, include
from .views import home, Thanks
urlpatterns = [
    path('', home, name='home'),
    path('thanks/', Thanks.as_view(), name='thanks')
]
