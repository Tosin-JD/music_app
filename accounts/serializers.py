from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


# get the user model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 
                  'website', 'profile_pic', 'password')
        extra_kwargs = {
            'username': {
                'required': False,
                'error_messages': {
                    'unique': 'A user with this username already exists.'
                }
            },
        }

    def validate_email(self, value):
        # Skip validation if no value provided
        if value is None:
            return value

        if User.objects.exists(email=value):
            raise serializers.ValidationError(
                'A user with this email address already exists.')

        # Note: it's important to return the value at the end of this method
        return value

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise serializers.ValidationError('Invalid email or password.')

            if not user.is_active:
                raise serializers.ValidationError('User account is disabled.')

        else:
            raise serializers.ValidationError('Email and password must be provided.')

        attrs['user'] = user
        return attrs


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
      required=True,
      validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
      write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 
            'password', 'password2')
        extra_kwargs = {
          'username': {'required': True},
          'email': {'required': True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
          raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email'],
          first_name=validated_data['first_name'],
          last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user