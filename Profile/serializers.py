from rest_framework import serializers

#--------------------- MODELOS ----------------------
from Profile.models import ProfileModel

class ProfileModelSerializer(serializers.ProfileModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('_all_')
