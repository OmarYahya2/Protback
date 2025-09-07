
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  


def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "Backend is running on Render 🚀"
    })

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("account.urls")),
]
