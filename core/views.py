# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Account, Destination,IncomingData
# from .serializers import AccountSerializer, DestinationSerializer,IncomingDataSerializer
# import requests
# from django.shortcuts import get_object_or_404

# class AccountViewSet(viewsets.ModelViewSet):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

# class DestinationViewSet(viewsets.ModelViewSet):
#     queryset = Destination.objects.all()
#     serializer_class = DestinationSerializer

# @api_view(['GET'])
# def get_destinations(request, account_id):
#     account = get_object_or_404(Account, account_id=account_id)
#     destinations = account.destinations.all()
#     serializer = DestinationSerializer(destinations, many=True)
#     return Response(serializer.data)

# # @api_view(['POST'])
# # def incoming_data(request):
# #     app_secret_token = request.headers.get('CL-X-TOKEN')
# #     if not app_secret_token:
# #         return Response({"error": "Un Authenticate"}, status=401)

# #     if request.method != 'POST' or not isinstance(request.data, dict):
# #         return Response({"error": "Invalid Data"}, status=400)

# #     account = get_object_or_404(Account, app_secret_token=app_secret_token)
# #     destinations = account.destinations.all()

# #     for destination in destinations:
# #         if destination.http_method == 'GET':
# #             requests.get(destination.url, params=request.data, headers=destination.headers)
# #         else:
# #             requests.request(destination.http_method.lower(), destination.url, json=request.data, headers=destination.headers)

# #     return Response({"message": "Data processed successfully"})

# @api_view(['POST'])
# def incoming_data(request):
#     app_secret_token = request.headers.get('CL-X-TOKEN')
#     if not app_secret_token:
#         return Response({"error": "Un Authenticate"}, status=401)

#     if request.method != 'POST' or not isinstance(request.data, dict):
#         return Response({"error": "Invalid Data"}, status=400)

#     account = get_object_or_404(Account, app_secret_token=app_secret_token)
#     destinations = account.destinations.all()

#     # Log the incoming data
#     IncomingData.objects.create(account=account, data=request.data)

#     for destination in destinations:
#         if destination.http_method == 'GET':
#             requests.get(destination.url, params=request.data, headers=destination.headers)
#         else:
#             requests.request(destination.http_method.lower(), destination.url, json=request.data, headers=destination.headers)

#     return Response({"message": "Data processed successfully"})

# @api_view(['GET'])
# def view_incoming_data(request, account_id):
#     account = get_object_or_404(Account, account_id=account_id)
#     incoming_data = IncomingData.objects.filter(account=account).order_by('-timestamp')
#     serializer = IncomingDataSerializer(incoming_data, many=True)
#     return Response(serializer.data)



from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Destination, IncomingData
from .serializers import AccountSerializer, DestinationSerializer, IncomingDataSerializer
import requests
from django.shortcuts import get_object_or_404
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows destinations to be viewed or edited.
    """
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@swagger_auto_schema(
    method='get',
    operation_description="Get all destinations for a specific account",
    responses={200: DestinationSerializer(many=True)}
)
@api_view(['GET'])
def get_destinations(request, account_id):
    """
    Get all destinations for a specific account
    """
    account = get_object_or_404(Account, account_id=account_id)
    destinations = account.destinations.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    operation_description="Receive incoming data and forward to destinations",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'key': openapi.Schema(type=openapi.TYPE_STRING, description='Any key-value pair')
        }
    ),
    responses={200: openapi.Response('Data processed successfully'),
               400: 'Invalid Data',
               401: 'Un Authenticate'}
)
@api_view(['POST'])
def incoming_data(request):
    """
    Receive incoming data and forward to destinations
    """
    app_secret_token = request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        return Response({"error": "Un Authenticate"}, status=401)

    if request.method != 'POST' or not isinstance(request.data, dict):
        return Response({"error": "Invalid Data"}, status=400)

    account = get_object_or_404(Account, app_secret_token=app_secret_token)
    destinations = account.destinations.all()

    # Log the incoming data
    IncomingData.objects.create(account=account, data=request.data)

    for destination in destinations:
        if destination.http_method == 'GET':
            requests.get(destination.url, params=request.data, headers=destination.headers)
        else:
            requests.request(destination.http_method.lower(), destination.url, json=request.data, headers=destination.headers)

    return Response({"message": "Data processed successfully"})

@swagger_auto_schema(
    method='get',
    operation_description="View incoming data for a specific account",
    responses={200: IncomingDataSerializer(many=True)}
)
@api_view(['GET'])
def view_incoming_data(request, account_id):
    """
    View incoming data for a specific account
    """
    account = get_object_or_404(Account, account_id=account_id)
    incoming_data = IncomingData.objects.filter(account=account).order_by('-timestamp')
    serializer = IncomingDataSerializer(incoming_data, many=True)
    return Response(serializer.data)