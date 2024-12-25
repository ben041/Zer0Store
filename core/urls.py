from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("cart", views.cart, name="cart-page"),
    path("product", views.product, name="product-page"),
]

# Add the following line to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
