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


class VisitsViews(generics.GenericAPIView):
    queryset = PatientModals.Visit.objects.all()
    serializer_class = serializers.VisitSerializer
    lookup_field = "pk"

class VisitsListView(generics.ListAPIView, VisitsViews):
    pagination_class = CustomListPagination

class VisitsRetrieveView(generics.RetrieveAPIView, VisitsViews):
    pass
class VisitCreateView(generics.CreateAPIView, VisitsViews):
    pass

class VisitsUpdateView(generics.UpdateAPIView, VisitsViews):
    pass

class PatientVisitListView(generics.ListAPIView, VisitsViews):
    def get(self, request, patient_id):
        patient = PatientModals.Patient.objects.filter(patient_id=patient_id)
        if patient:
            visit = PatientModals.Visit.objects.filter(patient=patient.first(), complete=False).order_by("-id")
            serializer = self.get_serializer(visit, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class TriageViews(generics.GenericAPIView):
    queryset = PatientModals.Triage.objects.all()
    serializer_class = serializers.TriageSerializer
    lookup_field = "pk"

class TriageListView(generics.ListAPIView, TriageViews):
    pass

class TriageRetrieveView(generics.RetrieveAPIView, TriageViews):
    pass

class TriageUpdateView(generics.UpdateAPIView, TriageViews):
    pass

class TriageCreateView(generics.CreateAPIView, TriageViews):
    pass

class VisitTriageListView(generics.ListAPIView, TriageViews):
    def get(self, request, pk):
        visit = PatientModals.Visit.objects.filter(pk=pk)
        if visit:
            visit = PatientModals.Triage.objects.filter(visit=visit).first()
            serializer = self.get_serializer(triage)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)