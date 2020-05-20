from django.urls import path
from apiapp.views import DatasetList

urlpatterns = [
    path('data', DatasetList.as_view(),name='data'),
   
]