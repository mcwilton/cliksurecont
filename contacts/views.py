import contacts
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def contacts_list(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            contacts = contacts.filter(title__icontains=title)
        
        contacts_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contacts_serializer.data, safe=False)
 
    elif request.method == 'POST':
        contacts_data = JSONParser().parse(request)
        contacts_serializer = ContactSerializer(data=contacts_data)
        if contacts_serializer.is_valid():
            contacts_serializer.save()
            return JsonResponse(contacts_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(contacts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Contact.objects.all().delete()
        return JsonResponse({'message': '{} Contacts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def contacts_detail(request, pk):
    try: 
        contacts = Contact.objects.get(pk=pk) 
    except Contact.DoesNotExist: 
        return JsonResponse({'message': 'The Contact does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        contacts_serializer = ContactSerializer(contacts) 
        return JsonResponse(contacts_serializer.data) 
 
    elif request.method == 'PUT': 
        contacts_data = JSONParser().parse(request) 
        contacts_serializer = ContactSerializer(contacts, data=contacts_data) 
        if contacts_serializer.is_valid(): 
            contacts_serializer.save() 
            return JsonResponse(contacts_serializer.data) 
        return JsonResponse(contacts_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        contacts.delete() 
        return JsonResponse({'message': 'Contacts was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def contacts_list_published(request):
    contacts= Contact.objects.filter(published=True)
        
    if request.method == 'GET': 
        contacts_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contacts_serializer.data, safe=False)
