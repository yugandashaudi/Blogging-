from django.shortcuts import render

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from accounts.serializers import ChangePasswordSerializer, UserLoginSerailizer, UserResgisterationSerilaizer, UserResgisterationSerilaizer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class ResgiterUserView(APIView):
    def post(self,request,format=None):
        serializer = UserResgisterationSerilaizer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response('The user has been registered sucessfully')

class LoginUserView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerailizer(data=request.data)   
        serializer.is_valid(raise_exception=True)   
        username = serializer.data.get('username')
        password = serializer.data.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            tokens = get_tokens_for_user(user)
            return Response({'msg':'the user has been sucessfully logged in','tokens':tokens})
    
class ChangePasswordView(APIView):
    def post(self,request,format=None):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_password = serializer.data.get('password')
        new_password = serializer.data.get('new_password')
        user = request.user
        password_checking = user.check_password(current_password)
        if password_checking:
            user.set_password(new_password)
            return Response('The password has been changed sucessfully')

        else:
            return Response('The current password doesnot match')







class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

    def post(self,request,*args,**kwargs):
        super().post(request,*args,**kwargs)
        user =self.user
        tokens = get_tokens_for_user(user)
        return Response({'msg':'the user was logged in through facebook','tokens':tokens})

class GithubLogin(SocialLoginView):
    
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/accounts/github/login/callback/"
    client_class = OAuth2Client

