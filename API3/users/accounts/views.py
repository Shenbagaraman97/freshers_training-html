from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from accounts.models import User
from accounts.serializers import RegisterSerializer,LoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.generics import GenericAPIView

class Register(GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self,request):
        serializer =  RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

class Signin(GenericAPIView):
    serializer_class=LoginSerializer

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.data['email']
            password=serializer.data['password']
            try:
                user = User.objects.get(email = email)
            except User.DoesNotExist:
                user= None
            if user:
                exist= check_password (password, user.password)
                if exist:
                    return JsonResponse({'message':"login success"},status=201)
                return JsonResponse({'messgage':"login failed"},status=400)
        return JsonResponse ({'message':"login not found"},status=400)
