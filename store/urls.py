from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomePage,name='store/home/'),
    path('view-product/<int:product_id>',views.view_product, name='view_product'),
    # path('add-to-cart/', views.add_to_cart, name='store/add_to_cart/'),
    # path('get-cart-count/', views.get_cart_count, name='/get_cart_count/'),
    # path('view-cart/', views.view_cart, name='store/view_cart/'),
    # path('remove-from-cart/', views.remove_from_cart, name='store/remove_from_cart/'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)