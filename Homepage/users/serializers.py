from rest_framework import serializers
import datetime
from django.contrib.auth.hashers import make_password


from .models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    # #to give argument explicitly
    # name = serializers.CharField(read_only=True)
    # is_superuser = serializers.BooleanField(read_only=True)
    # password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = Profile
        # fields = ['id', 'name', 'roll', 'city']
        # fields = '__all__'
        exclude = ['date_joined','last_login','is_superuser','is_staff','groups','is_active', 'enrollment_status' ]
        # #to give arguments explicitly to multiple fields
        read_only_fields = ['is_superuser','is_staff','enrollment_status', 'user_level']
        # #multiple arguments
        # extra_kwargs = {'name': {'read_only': True}, 'roll': {'required': True}}

        #def validate_roll(self, value):
           # if value>=200:
            #    raise serializers.ValidationError
           # return

        def create(self, validated_data):
            if validated_data.get('password'):
                 validated_data['password'] = make_password(validated_data['password'])

            user = get_user_model().objects.create(**validated_data)
            #user = User(
            #email=validated_data['email'],
            #username=validated_data['username']
            #)
            #user.set_password(validated_data['password'])
            user.save()
            return user



class AdminSerializer(serializers.ModelSerializer):
    is_superuser = serializers.BooleanField(default=True)
 #   password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = Profile
        fields = '__all__'
