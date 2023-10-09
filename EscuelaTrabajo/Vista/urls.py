from django.urls import path
from  .views import ProcessOrder
urlpatterns = [
    
    path('order_P/',ProcessOrder,name='order_P')
]
