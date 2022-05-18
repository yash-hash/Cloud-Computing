from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

from .models import User
from .serializers import ProfileSerializer, AdminSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

class ProfileModelViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_class = [SessionAuthentication]
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


# Create your views here.
class AdminModelViewset(viewsets.ModelViewSet):
    queryset= Profile.objects.all()
    serializer_class = AdminSerializer

def loginUser(request):

    if(request.user.is_authenticated):
        return redirect ('profiles')

    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']

        try:
           user = User.objects.get(username=username)

        except:
         print("User does not Exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
          login(request, user)
          return redirect('level')

        else:
          print("Username OR password is incorrect")


    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')



def profiles(request):
    return render(request, 'users/profiles.html')
