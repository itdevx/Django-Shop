from django.urls import path
from Account.views import *

app_name = 'account'

urlpatterns = [
    path(
        'sign-in', SignInView.as_view(), name='sign-in'
    ),
    path(
        'sign-up', SignUpView.as_view(), name='sign-up'
    ),
    path(
        'sign-out', SignOutRequest.as_view(), name='sign-out'
    )
]