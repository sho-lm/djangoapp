from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import User
from .serializers import LoginSerializer, UserSerializer


# これとルーターの登録だけで、一覧取得(GET:/accounts/users/)、作成(POST:/accounts/users/)などのURLが作成される
# 上記はDefaultRouterの登録できている場合の説明
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=request,
            account_id=serializer.validated_data["account_id"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return JsonResponse(
                data={"msg": "アカウントIDまたはパスワードが間違っています"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            login(request, user)
            return JsonResponse(data={"user": user})

    @action(methods=["POST"], detail=False)
    def logout(self, request):
        logout(request)
        return HttpResponse()
