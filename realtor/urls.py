from django.urls import path, include

from .views import index, EstateCreateView, ShowEstate, EstatesList, EstateCreateView2

app_name = 'realtor'


urlpatterns = [
    # path('', index, name='home'),
    path('', EstatesList.as_view(), name='home'),
    path('create/', EstateCreateView.as_view(), name='create'),
    path('create2/', EstateCreateView2.as_view(), name='create2'),
    path('estate/<slug:estate_slug>/', ShowEstate.as_view(), name='estate'),
]