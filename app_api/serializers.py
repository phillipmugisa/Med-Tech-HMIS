import datetime
from rest_framework import serializers
from patients import models as PatientModals

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModals.Patient
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["fullname"] = instance.getFullName()
        
        visit = PatientModals.Visit.objects.filter(patient=instance, complete=False)
        if visit:
            representation["visit"] = True
        else:
            representation["visit"] = False
            
        return representation

class PatientNokSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientModals.Patient.objects.all())

    class Meta:
        model = PatientModals.NextOfKin
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["fullname"] = instance.getFullName()
        return representation


class VisitSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=PatientModals.Visit.objects.all())

    class Meta:
        model = PatientModals.Visit
        fields = "__all__"