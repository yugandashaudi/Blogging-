from rest_framework import serializers 
from django.contrib.auth.models import User 


class UserResgisterationSerilaizer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100,write_only=True)

    class Meta:
        model = User 
        feilds=['username','email','password','confirm_password']


    def create(self,validated_data):
        validated_data.pop('confirm_password')
        registered_user =User.objects.create(username=validated_data['username'],email=validated_data['email'])
        registered_user.set_password(validated_data['password'])
        return registered_user
class UserLoginSerailizer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    class Meta:
        model = User 
        fields=['username','password']
   
class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=100)
    confirm_new_password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['password','new_password','confrim_new_password']

    def validate(self,attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError('The new_password and confirm password doesnot match')