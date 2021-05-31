from django.urls import path
from .views import LatesProductView

urlpatterns = [
    path('latest-products/',LatesProductView.as_view(),name='latest-product'),
]