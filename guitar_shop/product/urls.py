from django.urls import path
from .views import LatesProductView,ProductDetail

urlpatterns = [
    path('latest-products/',LatesProductView.as_view(),name='latest-product'),
    path('products/<slug:category_slug>/<slug:product_slug>/',ProductDetail.as_view(),name='product-detail')
]