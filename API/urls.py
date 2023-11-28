from django.urls import path
from .views import (create_vendor, get_all_vendors, get_vendor_by_id, 
                    update_vendor, delete_vendor, create_purchase_order, 
                    list_all_purchases,get_purchase_by_id , update_purchase_order,
                    delete_purchase_order, get_vendor_metrics
                )

urlpatterns = [
    
    # vendors
    path('create_vendors/', create_vendor, name='create_vendor'),
    path('all_vendors/', get_all_vendors, name='get_all_vendors'),
    path('vendors/<int:vendor_id>/', get_vendor_by_id, name='get_vendor_by_id'),
    path('update_vendor/<int:vendor_id>/', update_vendor, name='update_vendor'),
    path('delete_vendor/<int:vendor_id>/', delete_vendor, name='delete_vendor'),
    
    # puchasing things
    path('make_purchase_orders/', create_purchase_order, name='create_purchase_order'),
    path('purchase_orders/', list_all_purchases, name='list_all_purchases'), # get all the orders
    path('purchase_orders/<int:id>/', get_purchase_by_id, name='get_purchase_by_id'),
    path('update_purchase_orders/<int:id>/', update_purchase_order, name='update_purchase_order'),
    path('delete_purchase_orders/<int:id>/', delete_purchase_order, name='delete_purchase_order'),
    
    # performance
    path('vendors/<int:vendor_id>/performance/', get_vendor_metrics, name= 'vendor_performance'),

]