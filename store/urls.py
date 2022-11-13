from django.urls import path
from store import views

urlpatterns = [
    path('', views.get_all_products, name='all_products'),
    path('', views.StoreClothesListView.as_view(), name='all_gender_clothes'),
    path('<str:gender>', views.StoreClothesListView.as_view(), name='clothes'),
    path('<str:gender>/<str:prod_type>', views.StoreClothesListView.as_view(), name='filtered_products'),
    path('add-clothes/', views.ClothesCreateView.as_view(), name='create_clothes'),
    path('update-clothes/<int:pk>/', views.ClothesUpdateView.as_view(), name='update_clothes'),
    path('delete-clothes/<int:pk>/', views.ClothesDeleteView.as_view(), name='delete-clothes')
]
