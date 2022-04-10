from unicodedata import decimal
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import User, UserTransactionHistory
from .form import MyUserCreationForm
# Create your views here.
# def apiOverview(request):
#     context = {}
#     api_urls = {
#         'Wallet':'/wallet',
#         'Transaction History':'/transaction-history',
#         'Enable Wallet':'/creat-wallet',
#         'Get Wallet':'/get-wallet-balance',
#         'Add Wallet Balance':'/add-wallet-balance',
#         'Remove Wallet Balance':'/remove-wallet-balance',   
#     }
#     return render(request, 'app_userWallet/main.html')

def register(request):
    context = {}
    return render(request, 'app_userWallet/register.html')

def loginPage(request):
    # context = {}
    # return render(request, 'app_userWallet/login_register.html', context) # do not make login() method because already created one by django admin
    page = 'login'
    # ----------- cb+ s (check is user already logged in) ----------- #
    if request.user.is_authenticated:
        return redirect('wallet')
    # ----------- cb+ e (check is user already logged in) ----------- #

    if request.method == 'POST':
        print(request.POST)
        # username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            # user = User.objects.get(username=username)
            user = User.objects.get(username=email)
        except:
            print('User does not exist')

        # user = authenticate(request, username=username, password=password)
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user) # this will set the session id data
            return redirect('wallet')
        else:
            print('Username or Password does not exist')

    context = {'page':page}
    return render(request, 'app_userWallet/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = MyUserCreationForm()
    print('-----------------')
    print(request.POST)
    print('-----------------')
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('wallet')
        else:
            print('An error encounterd during the registration!')
            context = {'resorce':'register','data':'An error encounterd during the registration!'}
            return render(request, 'app_userWallet/errorPage.html', context)

    context = {'form':form}
    return render(request, 'app_userWallet/login_register.html', context)

@login_required(login_url='login')
def walletPage(request):
    user_id = request.user.id
    userTransactionHistory = UserTransactionHistory.objects.filter(userWallet_id=user_id)
    sum_updateAmount = userTransactionHistory.aggregate(Sum('updateAmount'))
    
    # print(len(userTransactionHistory))
    # print('sum_updateAmount: ',sum_updateAmount)
    # print('userTransactionHistory: ', userTransactionHistory.query)

    context = {'userTransactionHistory':userTransactionHistory, 'sum_updateAmount':sum_updateAmount}
    return render(request, 'app_userWallet/wallet.html', context)
    

def submitWallet(request):
    if request.method == 'POST':
        get_updateAmount = request.POST.get('updateAmount')
        submitType = request.POST.get('fund')
        print(submitType)
        print(request.POST.get)
        if submitType == 'Add':
            updateAmount = float(get_updateAmount)
            # print('Add pdateAmount: ', updateAmount)
            
            UserTransactionHistory.objects.create(
                userWallet_id = request.user.id,
                updateAmount = updateAmount,
                added_by = request.user.email,
            )
        elif submitType == 'Remove':
            updateAmount = -abs(float(get_updateAmount))
            # print('Remove updateAmount: ', updateAmount)
            
            UserTransactionHistory.objects.create(
                userWallet_id = request.user.id,
                updateAmount = updateAmount,
                added_by = request.user.email,
            )
        return redirect('wallet')