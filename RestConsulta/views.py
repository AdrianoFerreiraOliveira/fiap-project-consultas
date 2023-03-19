from rest_framework import viewsets
from RestConsulta.models import Medico, Paciente
from RestConsulta.serializer import MedicoSerializer, PacienteSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    """ Exibindo a lista de médicos"""
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    """ Exibindo a lista de pacientes"""
    queryset = Paciente.objects.all()
    serializer_class =PacienteSerializer 
