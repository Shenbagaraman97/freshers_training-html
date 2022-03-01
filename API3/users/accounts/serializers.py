from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from accounts.models import User

class RegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=100)
    lastname  = serializers.CharField(max_length=100)
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField(max_length=8, write_only=True, required=True)
    password1 = serializers.CharField(max_length=8, write_only=True, required=True)

    def validate(self,validated_data):
        if validated_data['password'] != validated_data['password1']:
            raise ValidationError({"password":"password did not match"})
        return validated_data 

    def create(self, validated_data):
        # print("validated_data", validated_data['firstname'])
        # print("validated_data", validated_data['lastname'])
        # print("validated_data", validated_data['email'])
        # print("validated_data", validated_data['password'])
        # print("validated_data", validated_data['password1'])
        # # return User.objects.validated_data)

        user = User.objects.create(
            firstname= validated_data['firstname'],
            lastname =  validated_data['lastname'],
            email    = validated_data['email'],
            password = make_password(validated_data['password'])   
        )
        return validated_data
          
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=8, required=True)
    