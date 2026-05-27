from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    return Response({"message": "Login endpoint ready", "token": "demo-token"})


@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    return Response({"message": "Register endpoint ready"})


@api_view(["GET"])
def profile_view(request):
    return Response({"user": "demo@bank.com", "role": "esg_analyst"})
