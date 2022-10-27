from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import SocialLoginSerializer

from accounts.models import Usuario

import datetime, jwt
from datetime import timedelta

class SocialLoginView(APIView):
    
    def post(self, request, format=None):
        serializer = SocialLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            if not Usuario.objects.filter(email=request.data.get('email')).exists():
                usuario = serializer.save()
            else:
                usuario = Usuario.objects.get(email=request.data.get('email'))
                if usuario.metodo_ingreso !=  request.data.get('metodo_ingreso'):
                    raise AuthenticationFailed(detail="Este email ya ha sido registrado")

            payload = {
                'id': usuario.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {'jwt': token }
            response.status_code = status.HTTP_200_OK
            return response
        else:
            raise AuthenticationFailed(detail="Los campos enviados no son validos", code=status.HTTP_400_BAD_REQUEST)

            
            
            
                