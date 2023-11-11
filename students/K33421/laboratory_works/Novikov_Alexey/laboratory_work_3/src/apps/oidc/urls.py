from django.urls import path
from dj_rest_auth.jwt_auth import get_refresh_view

from apps.oidc.views import ItmoIdLogin, ItmoIdAuth, ItmoIdAuthUrl, ItmoIdProfileGroupView

urlpatterns = [
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("auth/url/", ItmoIdAuthUrl.as_view(), name="itmo_id_auth_url"),
    path("auth/", ItmoIdAuth.as_view(), name="itmo_id_auth"),
    path("login/", ItmoIdLogin.as_view(), name="itmo_id_login"),
    path("group/", ItmoIdProfileGroupView.as_view(), name="itmo_id_group"),
]
