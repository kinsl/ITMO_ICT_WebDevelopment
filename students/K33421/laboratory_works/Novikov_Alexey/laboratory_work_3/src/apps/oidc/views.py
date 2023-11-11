from urllib.parse import urlencode, quote

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.openid_connect.views import OpenIDConnectAdapter
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from django.http import HttpResponseRedirect
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiParameter
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

BE_BASE_URL = settings.BE_BASE_URL
FE_BASE_URL = settings.FE_BASE_URL


class ItmoIdAuthUrl(APIView):
    @extend_schema(
        summary="Return ITMO.ID authentication URL",
        responses=inline_serializer(
            name="ItmoIdAuthUrl",
            fields={"url": serializers.URLField()},
        ),
    )
    def get(self, request: Request):
        query_params = {
            "client_id": settings.ITMO_ID_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": f"{BE_BASE_URL}/oidc/auth",
            "scope": "openid name edu",
        }

        url = f"https://id.itmo.pro/auth/realms/itmo/protocol/openid-connect/auth?{urlencode(query_params)}"

        return Response({"url": url}, status=status.HTTP_200_OK)


class ItmoIdAuth(APIView):
    @extend_schema(
        summary="Get 'code' from ITMO.ID and return it with redirect to FE app",
        parameters=[OpenApiParameter(name="code", type=OpenApiTypes.STR)],
        responses={
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="ItmoIdAuthError",
                fields={"detail": serializers.CharField()},
            ),
        },
    )
    def get(self, request: Request):
        auth_code = request.query_params.get("code")
        if not auth_code:
            return Response({"detail": "Missing 'code' parameter"}, status=status.HTTP_400_BAD_REQUEST)

        redirect_url = f"{FE_BASE_URL}/login?code={quote(auth_code)}"
        return HttpResponseRedirect(redirect_url)


class ItmoIdAdapter(OpenIDConnectAdapter):
    def __init__(self, request: Request):
        provider_id = "itmo_id"
        super().__init__(request, provider_id)


class ItmoIdLogin(SocialLoginView):
    """Get 'code' and request ITMO.ID for access token and userinfo. Create new User and ITMO.ID Profile"""

    adapter_class = ItmoIdAdapter
    callback_url = f"{BE_BASE_URL}/oidc/auth"
    client_class = OAuth2Client


class ItmoIdProfileGroupView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get user's education group from ITMO.ID",
        responses={
            status.HTTP_400_BAD_REQUEST: inline_serializer(
                name="ItmoIdProfileGroup",
                fields={"group": serializers.CharField()},
            ),
            status.HTTP_404_NOT_FOUND: inline_serializer(
                name="ItmoIdProfileGroupNotFound", fields={"error": serializers.CharField()}
            ),
        },
    )
    def get(self, request: Request):
        user = request.user
        if not hasattr(user, "profile"):
            return Response({"error": "Profile does not exist"}, status.HTTP_404_NOT_FOUND)

        group = user.profile.group
        return Response({"group": group})
