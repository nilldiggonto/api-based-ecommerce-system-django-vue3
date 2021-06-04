from django.urls import path
from .views import LatesProductView,ProductDetail,CategoryDetail

urlpatterns = [
    path('latest-products/',LatesProductView.as_view(),name='latest-product'),
    path('products/<slug:category_slug>/<slug:product_slug>/',ProductDetail.as_view(),name='product-detail'),
    path('products/<slug:category_slug>/',CategoryDetail.as_view(),name='category-detail')
]