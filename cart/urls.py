from django.urls import path

from cart import views

urlpatterns = [
    path('add-to-cart/', views.CartCreateView.as_view(), name='add_to_card'),
    path('show-cart/<int:pk>', views.CartDetailView.as_view(), name='show_cart'),
    path('edit-cart/', views.CartUpdateView.as_view(), name='update_cart'),

]
