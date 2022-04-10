from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_userWallet.models import User, UserTransactionHistory
from app_userWallet.api.serializer import UserSerializer, UserTransactionHistorySerializer
from django.db.models import Sum
from app_userWallet.form import MyUserCreationForm

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Get Wallet':'/get-wallet/<str:user_id>/',
        'Transaction History':'/transaction-history/<str:user_id>/',
        'Add/Remove Wallet Balance':{
            'url':'/update-wallet','param':{
                "submitType": "Add/Remove",
                "updateAmount": "25.00",
                "added_by": "bnitish103@gmail.com",
                "userWallet": 3
            }
        },
    }
    return Response(api_urls)

@api_view(['GET'])
def getWallet(request, user_id):
    userDetail = User.objects.get(pk=user_id)
    serializer = UserSerializer(userDetail, many=False)
    userTransactionHistory = UserTransactionHistory.objects.filter(userWallet_id=user_id)
    sum_updateAmount = userTransactionHistory.aggregate(Sum('updateAmount'))
    print('--------------')
    print(sum_updateAmount['updateAmount__sum'])
    print('--------------')
    wallet = {
        'userDetails': serializer.data,
        'walletAmount': sum_updateAmount['updateAmount__sum'],
    }
    return Response(wallet)
    
@api_view(['GET'])
def getTransactionHistory(request, user_id):
    userTransactionHistory = UserTransactionHistory.objects.filter(userWallet_id=user_id)
    serializer = UserTransactionHistorySerializer(userTransactionHistory, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def updateWallet(request):

    print('-------------')
    print('cb+ 1')
    print('-------------')
    if request.method == 'POST':
            
        print('-------------')
        print('cb+ 2')
        print(request.data['submitType'])
        print('-------------')
        submitType = request.data['submitType']
        get_updateAmount = request.data['updateAmount']
        if submitType == 'Add':
            
            print('-------------')
            print('cb+ 3')
            print('-------------')
            updateAmount = float(get_updateAmount)
            # print('Add pdateAmount: ', updateAmount)
            
            UserTransactionHistory.objects.create(
                userWallet_id = request.data['userWallet'],
                updateAmount = updateAmount,
                added_by = request.data['added_by'],
            )
            return Response(data=request.data, status=status.HTTP_201_CREATED)
        elif submitType == 'Remove':
            
            print('-------------')
            print('cb+ 4')
            print('-------------')
            updateAmount = -abs(float(get_updateAmount))
            # print('Remove updateAmount: ', updateAmount)
            
            UserTransactionHistory.objects.create(
                userWallet_id = request.data['userWallet'],
                updateAmount = updateAmount,
                added_by = request.data['added_by'],
            )
            return Response(data=request.data, status=status.HTTP_201_CREATED)

    
    print('-------------')
    print('cb+ 5')
    print('-------------')
    return Response(data=request.data, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def createUser(request):
    print('-------------')
    print('cb+ 1')
    print(request.data)
    print('-------------')
    form = MyUserCreationForm()
    if request.method == 'POST':
        print('-------------')
        print('cb+ 2')
        print('-------------')
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            print('-------------')
            print('cb+ 3')
            print('-------------')
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return Response(data=request.data, status=status.HTTP_201_CREATED)
    
    print('-------------')
    print('cb+ 4')
    print('-------------')
    return Response(data=request.data, status=status.HTTP_201_CREATED)