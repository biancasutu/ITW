from django.urls import path

from cart import views

urlpatterns = [
    path('cart-add-clothes/<int:item_id>', views.create_cart_product, name='cart_add_clothes'),
    path('cart-add-accesories/<int:item_id>', views.create_cart_accesory_item, name='cart_add_accesories'),
    path('show-cart/', views.CartListView.as_view(), name='show_cart'),
    path('edit-cart/<int:pk>', views.CartUpdateView.as_view(), name='update_cart'),
    path('delete-cart-clothes/<int:clothes_id>', views.delete_cart_cloth_item, name='delete_cart_clothes'),
    path('delete-cart-accessories/<int:accessory_id>', views.delete_cart_accesory_item, name='delete_cart_accesories')
]
