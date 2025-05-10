from rest_framework import serializers
from .models import User


# APIでデータをやり取りするために必要なのがserializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'account_id',
            'password'
        )


class LoginSerializer(serializers.Serializer):
    account_id = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    def validate(self, data):
        account_id = data.get('account_id')
        password = data.get('password')
        user = User.objects.get(account_id=account_id)
        if (account_id != user.account_id
            or password != user.password):
                raise serializers.ValidationError('アカウントIDまたはパスワードが間違っています')
        
        return data