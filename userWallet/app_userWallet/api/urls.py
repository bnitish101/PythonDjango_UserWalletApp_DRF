from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('get-wallet/<str:user_id>/', views.getWallet),
    path('transaction-history/<str:user_id>/', views.getTransactionHistory),
    path('update-wallet/', views.updateWallet),
    path('create-user/', views.createUser),
    # path('room/<str:pk>/', views.getRoom)
]

