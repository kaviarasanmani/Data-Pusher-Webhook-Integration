from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AccountViewSet, DestinationViewSet, get_destinations, incoming_data, view_incoming_data
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Data Pusher API",
      default_version='v1',
      description="API for managing accounts, destinations, and incoming data",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kavim1996@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/account/<uuid:account_id>/destinations/', get_destinations, name='get_destinations'),
    path('server/incoming_data/', incoming_data, name='incoming_data'),
    path('api/account/<uuid:account_id>/incoming-data/', view_incoming_data, name='view_incoming_data'),
    
    # Swagger URLs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]