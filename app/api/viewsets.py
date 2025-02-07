from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Animal, Desenvolvedor, CustomUsuario
from .serializer import AnimalSerializer, UsuarioSerializer, DesenvolvedorSerializer

class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user)

class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]

class CadastroUsuarioView(generics.CreateAPIView):
    queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()

class DesenvolvedorListView(generics.ListAPIView):
    queryset = Desenvolvedor.objects.all()
    serializer_class = DesenvolvedorSerializer
    permission_classes = [permissions.AllowAny]

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_animal_api(request):
#     try:
#         data = request.data  # O corpo da requisição será processado automaticamente pelo Django REST Framework.
#         animal = Animal.objects.create(
#             nome=data['nome'],
#             raca=data['raca'],
#             genero=data['genero'],
#             idade=data['idade'],
#             vacinado=data['vacinado'],
#             descricao=data['descricao'],
#             descricao_completa=data['descricao_completa'],
#             criado_por=request.user  # Aqui associamos o usuário autenticado.
#         )
#         return JsonResponse({'message': 'Animal cadastrado com sucesso!', 'animal_id': animal.id}, status=201)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)