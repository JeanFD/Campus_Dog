from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from app.models import Animal, Desenvolvedor, CustomUsuario
from .serializer import AnimalSerializer, UsuarioSerializer, DesenvolvedorSerializer

class AnimalListCreateView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAdminUser()]

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user)

class AnimalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

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