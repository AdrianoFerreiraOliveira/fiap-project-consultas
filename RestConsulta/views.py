from rest_framework import viewsets
from RestConsulta.models import Medico, Paciente
from RestConsulta.serializer import MedicoSerializer, PacienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class MedicosViewSet(viewsets.ModelViewSet):
    """Exibindo a lista de médicos"""

    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PacientesViewSet(viewsets.ModelViewSet):
    """Exibindo a lista de pacientes"""

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
