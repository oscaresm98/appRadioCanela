from rest_framework import serializers

from django.utils.crypto import get_random_string

from accounts.models import Usuario


def crear_username(username_social: str):
    '''
    Crea un nuevo nombre de usuario basandose en el username_social que se le pase
    '''

    nuevo_username = None
    if username_social.count(' ') >= 1: # Contamos si el username tiene 1 o mas nombres
        nombres_sep = username_social.split(' ')
        if len(nombres_sep) > 1:
            nuevo_username = '-'.join(nombres_sep[:2]) # Solo usamos los 2 primeros nombres
        else:
            nuevo_username = nombre_sep[0] 
    else:
        nuevo_username = username_social

    nuevo_username += '-' + get_random_string(length=3, allowed_chars='0123456789')
    return nuevo_username

def verificar_username(username: str):
    '''
    Verifica si el username que se le pasa como parametro es unico y si no lo es genera uno nuevo
    '''
    nuevo_username = username
    while True:
        if not Usuario.objects.filter(username=nuevo_username).exists():
            return '-'.join(nuevo_username.split(' ')[0:2])
        else:
            nuevo_username = crear_username(nuevo_username)
            print(nuevo_username)


def obtener_nombre_apellido(username: str):
    return username.split(' ')[:2]

class SocialLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ['username', 'email', 'metodo_ingreso']
        model = Usuario
        extra_kwargs = { 
            'username': { 'validators': [] }, 
            'email': { 'validators': [] }
        }
    
    def create(self, validated_data):
        username = validated_data.get('username')
        nombre_usuario = verificar_username('-'.join(username.split(' ')[0:2]))
        nombre, apellido = obtener_nombre_apellido(validated_data.get('username'))
        usuario = Usuario( 
            first_name =nombre,
            last_name = apellido, 
            username = nombre_usuario, 
            email = validated_data.get('email'),
            metodo_ingreso= validated_data.get('metodo_ingreso')
        )
        usuario.set_unusable_password()
        usuario.save()
        return usuario
