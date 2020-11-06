from rest_framework import serializers

#--------------------- MODELOS ----------------------
from Profile.models import ProfileModel
from Profile.models import ProfileUser

class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class ProfileModelUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('__all__')