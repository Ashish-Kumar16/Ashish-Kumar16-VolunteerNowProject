from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# # Swagger/OpenAPI schema view configuration
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Volunteer Now API",
#         default_version='v1',
#         description="API documentation for Volunteer Now platform",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@volunteernow.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),                     # Admin panel
    path('api/', include('opportunities.urls')),         # Opportunities app endpoints
    path('auth/', include('accounts.urls')),             # Accounts app endpoints
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),   # Swagger UI
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),            # Redoc UI
    
]
