from django.urls import path
from store import views
from .views import get_filtered

urlpatterns = [
    path('<str:acc_name>', get_filtered, name='accessories_by_name')
]
