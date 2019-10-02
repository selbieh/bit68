from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializer import city_serializer
import requests
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

#GET for help and Post {"city":"city name"} to get weather
class weather(APIView):
    def get(self, request, format=None):
        return Response({'helpe':"please use post include data like {'city':'cairo'} to get response wtih weather"})
    def post(self ,request, format=None):
        #simple serializer for empty city string not accepted
        serializer=city_serializer(data=request.data)
        if serializer.is_valid():
            city=request.data['city']
            #consume weatherstack.com API endpoint
            weather_end_point='http://api.weatherstack.com/current?access_key=1748fbb0c28ed5d71abd6704de70ff7e&query={0}'.format(city)
            response = requests.get(weather_end_point)
            weather_resulte = response.json()
            return Response({'weather for {0}'.format(city):weather_resulte})
        return Response({'error':serializer.errors},status=HTTP_400_BAD_REQUEST)

#Template register user
class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

#Template render weather state
def get_whether_in_template(request):
    if request.method=="POST":
        city=request.POST.get('city',None)
        if city:
            weather_end_point = 'http://api.weatherstack.com/current?access_key=1748fbb0c28ed5d71abd6704de70ff7e&query={0}'.format(
                city)
            response = requests.get(weather_end_point)
            weather_resulte = response.json()
            #get the weathe icon from reponse
            weather_icons=weather_resulte['current']['weather_icons']
            #delete the resulte icon (bad render stuffe)
            del weather_resulte['current']['weather_icons']
            return render(request,'weatherView.html',{'weather_resulte':weather_resulte,'weather_icons':weather_icons,'city':city})
        else:
            return render(request,'home.html',context={'error':'city name can not be empty'})

