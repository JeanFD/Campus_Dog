from rest_framework import serializers
from app.models import Animal, CustomUsuario, Desenvolvedor

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ['criado_por']

    #def create(self, validated_data):
    #    request = self.context['request']
    #   validated_data['criado_por'] = request.user
    #    return super().create(validated_data)

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUsuario
        fields = ['id', 'email', 'first_name', 'last_name', 'fone', 'password']

    def create(self, validated_data):
        user = CustomUsuario.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],  
            last_name=validated_data['last_name'],    
            fone=validated_data['fone'],              
            password=validated_data['password']
        )
        return user
    
class DesenvolvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desenvolvedor
        fiedls = '__all__'

