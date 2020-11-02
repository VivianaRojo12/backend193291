from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView

#--------------------- MODELOS ----------------------
from Profile.models import ProfileModel

#--------------------- SERIALIZER -------------------
from Profile.serializers import ProfileModelSerializers

# Create your views here.
class ProfileView(APIView):
    def (self, request, format = None):
        serializer = ProfileModelSerializers(data = request.data, context = {'request': request}) #Invocara una clase de tipo serializador
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.date)
