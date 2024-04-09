from django.urls import path
from . import views


app_name = 'front'


urlpatterns = [
    # ----- urlpatterns -----
    path('', views.index, name='index'),
    path('product/<str:code>/', views.product_detail, name='product_detail'),
    path('product_list', views.product_list, name='product_list'),
    path('category/<str:code>/', views.category_list, name='category_list'),
    
    #------ Cart ------------------

    path('carts/', views.carts, name='carts'),
    path('cart/<str:code>/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<str:code>', views.add_to_cart, name='add_to_cart'),
    path('active/cart/', views.active_cart, name='active_cart'),
    path('cart_product_delete/<int:id>/', views.cart_product_delete, name='cart_product_delete'),
    path('add_cart_product/<str:code>/', views.add_cart_product, name='add_cart_product'),
    # -- product --
    path('product_delete/<int:id>/',views.product_delete, name='product_delete'),
    
    # -- Wishlist --
    path('wishlist',views.list_wishlist, name='wishlist'),
    path('wishlist_delete/<str:code>/', views.wishlist_delete, name='wishlist_delete'),
    path('remove-wishlist/<str:code>',views.remove_wishlist, name='remove_wishlist'),
    path('add-wishlist/<str:code>', views.add_wishlist, name='add_wishlist'),
    path('order-list',views.order_list, name='order_list'),

]