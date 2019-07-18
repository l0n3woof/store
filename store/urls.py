from django.urls import path
from .views import CustomerDetails, EditCustomerDetails

urlpatterns = [
    path('customers/', CustomerDetails.as_view(), name='custdetails'),
    path('edit/', EditCustomerDetails.as_view(), name='editcustdetails')
]
