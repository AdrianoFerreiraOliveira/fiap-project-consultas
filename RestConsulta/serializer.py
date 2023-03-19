from rest_framework import serializers
from RestConsulta.models import Medico, Paciente

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields= '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields= '__all__'