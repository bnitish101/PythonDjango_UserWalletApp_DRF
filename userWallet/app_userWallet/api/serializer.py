from rest_framework.serializers import ModelSerializer
from app_userWallet.models import User, UserTransactionHistory

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class UserTransactionHistorySerializer(ModelSerializer):
    
    class Meta:
        model = UserTransactionHistory
        fields = '__all__'
