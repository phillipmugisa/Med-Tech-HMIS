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
    queryset = PatientModals.Visit.active.all()
    serializer_class = serializers.VisitSerializer
    lookup_field = "pk"

class VisitsListView(generics.ListAPIView, VisitsViews):
    pagination_class = CustomListPagination

class VisitsRetrieveView(generics.RetrieveAPIView, VisitsViews):
    pass
class VisitCreateView(generics.CreateAPIView, VisitsViews):
    def post(self, request, *args, **kwargs):
        print("\n"*5)
        print(request.data.get("patient"))
        print(PatientModals.Visit.objects.filter(patient__pk=request.data.get("patient"), complete=False))
        print("\n"*5)
        if PatientModals.Visit.objects.filter(patient__pk=request.data.get("patient"), complete=False):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return self.create(request, *args, **kwargs)

class VisitsUpdateView(generics.UpdateAPIView, VisitsViews):
    pass

class PatientVisitListView(generics.ListAPIView, VisitsViews):
    def get(self, request, patient_id):
        patient = PatientModals.Patient.objects.filter(patient_id=patient_id)
        if patient:
            visit = PatientModals.Visit.objects.filter(patient=patient.first(), complete=False)
            serializer = self.get_serializer(visit, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class VisitPatientListView(generics.RetrieveAPIView):
    queryset = PatientModals.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    
    def get(self, request, pk):
        visit = PatientModals.Visit.objects.filter(pk=pk)
        if visit:
            serializer = self.get_serializer(visit.first().patient)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

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
            triage = PatientModals.Triage.objects.filter(visit=visit.first()).first()
            serializer = self.get_serializer(triage)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PatientTriageListView(generics.ListAPIView, TriageViews):
    def get(self, request, patient_id):
        visits = PatientModals.Visit.objects.filter(patient__patient_id=patient_id)
        if visits:
            # loop through visits
            triages = []
            for visit in visits:
                triage = PatientModals.Triage.objects.filter(visit=visit)
                if triage:
                    triages.append(triage.first())
            serializer = self.get_serializer(triages, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)



# allergies
class AllergyViews(generics.GenericAPIView):
    queryset = PatientModals.Allergy.objects.all()
    serializer_class = serializers.AllergySerializer
    lookup_field = "pk"
    
class AllergyListView(generics.ListAPIView, AllergyViews):
    pass
class AllergyRetrieveView(generics.RetrieveAPIView, AllergyViews):
    pass
class AllergyUpdateView(generics.UpdateAPIView, AllergyViews):
    pass
class AllergyCreateView(generics.CreateAPIView, AllergyViews):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PatientAllergyListView(generics.ListAPIView, AllergyViews):
    def get(self, request, patient_id):
        allergies = PatientModals.Allergy.objects.filter(patient__patient_id=patient_id)
        if allergies:
            serializer = self.get_serializer(allergies, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
