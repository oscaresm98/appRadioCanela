from rest_framework import serializers
from accounts.models import Usuario


class SocialLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ['username', 'email', 'metodo_ingreso']
        model = Usuario
        extra_kwargs = { 
            'username': { 'validators': [] }, 
            'email': { 'validators': [] }
        }
    
    def create(self, validated_data):
        usuario = Usuario( 
            username = validated_data.get('username'), 
            email = validated_data.get('email'),
            metodo_ingreso= validated_data.get('metodo_ingreso')
        )
        usuario.set_unusable_password()
        usuario.save()
        return usuario
