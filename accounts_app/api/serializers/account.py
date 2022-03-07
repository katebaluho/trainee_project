from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ('password', )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password', 'birth_date', 'gender']
        extra_kwargs = {
            'name':{'write_only': True},
            'birth_date':{'write_only': True},
            'gender':{'write_only': True},
        }

    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def create(self, validated_data):
        user = UserModel.objects.create_user(email=validated_data['email'],
                                             password=validated_data['password'],
                                             name=validated_data['name'],
                                             birth_date=validated_data['birth_date'],
                                             gender=validated_data['gender'])
        return user
