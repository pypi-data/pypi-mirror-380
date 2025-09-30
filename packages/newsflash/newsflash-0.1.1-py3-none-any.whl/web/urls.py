from django.urls import path, include


urlpatterns = [
    path("", include("web.app.urls")),
    path("accounts/", include("web.accounts.urls")),
]
