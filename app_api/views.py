from rest_framework import generics
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from app_api import serializers
from patients import models as PatientModals


class CustomListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


class PatientAPIViews(generics.GenericAPIView):
    queryset = PatientModals.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    lookup_field = "patient_id"

class PatientListView(generics.ListAPIView, PatientAPIViews):
    pagination_class = CustomListPagination

class PatientCreateView(generics.CreateAPIView, PatientAPIViews):
    pass

class PatientUpdateView(generics.UpdateAPIView, PatientAPIViews):
    pass

class PatientRetrieveView(generics.RetrieveAPIView, PatientAPIViews):
    pass

class NextOfKinViews(generics.GenericAPIView):
    queryset = PatientModals.NextOfKin.objects.all()
    serializer_class = serializers.PatientNokSerializer
    lookup_field = "pk"

    
class NextOfKinRetrieveView(generics.RetrieveAPIView, NextOfKinViews):
    def get(self, request, pk):
        patient = PatientModals.Patient.objects.filter(pk=pk)
        if patient:
            nok = patient.first().next_of_kin.all().first()
            serializer = self.get_serializer(nok)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class PatientNokCreateView(generics.CreateAPIView, NextOfKinViews):
    pass

class NextOfKinUpdateView(generics.UpdateAPIView, NextOfKinViews):
    pass