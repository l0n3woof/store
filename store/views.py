from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import UserDetails
import json
# Create your views here.

class CustomerDetails(APIView):
    def get(self, request):
        queryset = list(UserDetails.objects.values())
        return Response({'cutomers': queryset})

class EditCustomerDetails(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        phone = body.get('phone_number', '')
        name = body.get('full_name', '')
        email = body.get('email', '')
        store_name = body.get('store_name', '')
        address_line1 = body.get('address_line1', '')
        address_line2 = body.get('address_line2', '')
        pin_code = body.get('pin_code', '')
        district = body.get('district', '')
        state = body.get('state', '')
        pan_number = body.get('pan_number', '')
        gst_number = body.get('gst_number', '')
        userobject = []
        if phone:
            phonenumbers = list(UserDetails.objects.values_list('phone_number', flat=True))
            if phone in phonenumbers:
                userobject = UserDetails.objects.filter(phone_number=phone)
        else:
            names = list(UserDetails.objects.values_list('full_name', flat=True))
            if name in names:
                userobject = UserDetails.objects.filter(full_name=name)
        detail_list = {'phone':phone, 'name':name, 'email':email, 'store_name':store_name, 'address_line1':address_line1,\
                'address_line2':address_line2, 'pin_code': pin_code, 'district':district, 'state':state,\
                'pan_number':pan_number, 'gst_number':gst_number}
        if userobject:
            userobject.update(phone_number=phone,full_name=name,email=email,store_name=store_name,address_line1=address_line1,\
                address_line2=address_line2,pin_code=pin_code,district=district,state=state,pan_number=pan_number,gst_number=gst_number)
        else:
            newuser = UserDetails.objects.create(phone_number=phone,full_name=name,email=email,store_name=store_name,\
                    address_line1=address_line1,address_line2=address_line2,pin_code=pin_code,district=district,\
                    state=state,pan_number=pan_number,gst_number=gst_number)
        return Response(detail_list)

        

