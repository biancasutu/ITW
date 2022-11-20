from django.urls import path

from cart import views

urlpatterns = [
    path('add-to-cart/', views.create_cart_product, name='add_to_card'),
    path('show-cart/', views.CartListView.as_view(), name='show_cart'),
    path('edit-cart/<int:pk>', views.CartUpdateView.as_view(), name='update_cart'),
    path('delete-cart/<int:pk>', views.CartDeleteView.as_view(), name='delete_cart')
]
