from rest_framework import serializers
from base.models import *
from django.contrib.auth import login
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import TokenError
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['phonenumber','username', 'password']

        extra_kwargs = {
            'password':{'write_only':True,}
        }

        def validate(self, validated_data):
            validate_password(validated_data['password'])
            return validated_data

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def save(self, **kwargs):
        user = CustomUser(
            phonenumber=self.validated_data['phonenumber'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.is_active = False
        user.save()
        return user


class ResetPasswordSerializer(serializers.ModelSerializer):

    newpassword = serializers.CharField(style={"input_type":"password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 'newpassword']

        extra_kwargs = {
            'password':{'write_only':True,}
        }

    def validate(self, attrs):
        password = attrs.get('password', '')
        newpassword = attrs.get('newpassword', '')
        validate_password(password)
        validate_password(newpassword)
        
        if password != newpassword:
            raise serializers.ValidationError({'message_error':'The password and newpassword didnt matched.'})
        
        return attrs
    
    def save(self, **kwargs):
        request = self.context.get('request')
        user = CustomUser.objects.get(id=request.user.id)
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class UserLoginSerilizer(serializers.ModelSerializer):

    phonenumber = serializers.CharField()
    password = serializers.CharField(max_length=55, min_length=6,write_only = True)

    class Meta:
        model = CustomUser
        fields = ['phonenumber', 'password']

    def validate(self, data):

        phonenumber = data.get('phonenumber', )
        password = data.get('password',)

        if phonenumber is None:
                raise serializers.ValidationError({'message_error':'An phonenubmer address is required to log in.'})
        
        if password is None:
            raise serializers.ValidationError({'message_error':'A password is required to log in.'})
        
        user = authenticate(username= phonenumber, password= password)

        if user is None:
            raise serializers.ValidationError({'message_error':'A user with this phonenumber and password was not found.'})
        
        if not user.is_active:
            raise serializers.ValidationError({'message_error':'This user is not currently activated.'})
        
        return data

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'