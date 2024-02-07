from django.db.models import Q

from rest_framework import generics
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from app_api import serializers
from app_api import lab_serializers

from patients import models as PatientModals
from lab import models as LabModels
from lab import models as LabModels
from doctor import models as DoctorModels


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
    pass

class PatientAllergyListView(generics.ListAPIView, AllergyViews):
    def get(self, request, patient_id):
        allergies = PatientModals.Allergy.objects.filter(patient__patient_id=patient_id)
        try:
            serializer = self.get_serializer(allergies, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# ------------------------------- General finding ----------------------------------------
class GeneralFindingsViews(generics.GenericAPIView):
    queryset = PatientModals.GeneralFinding.objects.all()
    serializer_class = serializers.GeneralFindingsSerializer
    lookup_field = "pk"

class GeneralFindingsListView(generics.ListAPIView, GeneralFindingsViews):
    pass

class GeneralFindingsRetrieveView(generics.RetrieveAPIView, GeneralFindingsViews):
    pass

class GeneralFindingsUpdateView(generics.UpdateAPIView, GeneralFindingsViews):
    pass

class GeneralFindingsCreateView(generics.CreateAPIView, GeneralFindingsViews):
    pass

class PatientGeneralFindingsListView(generics.ListAPIView, GeneralFindingsViews):
    def get(self, request, patient_id):
        results = PatientModals.GeneralFinding.objects.filter(visit__patient__patient_id=patient_id)
        try:
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class VisitGeneralFindingsListView(generics.ListAPIView, GeneralFindingsViews):
    def get(self, request, visit_id):
        results = PatientModals.GeneralFinding.objects.filter(visit__id=visit_id)
        try:
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Paedeatrics
class PaedeatricsNoteViews(generics.GenericAPIView):
    queryset = PatientModals.PaedeatricNote.objects.all()
    serializer_class = serializers.PaedeatricNoteSerializer
    lookup_field = "pk"

class PaedeatricsNotesListView(generics.ListAPIView, PaedeatricsNoteViews):
    pass

class PaedeatricsNotesRetrieveView(generics.RetrieveAPIView, PaedeatricsNoteViews):
    pass

class PaedeatricsNotesUpdateView(generics.UpdateAPIView, PaedeatricsNoteViews):
    pass

class PaedeatricsNotesCreateView(generics.CreateAPIView, PaedeatricsNoteViews):
    pass

class PatientPaedeatricsNotesListView(generics.ListAPIView, PaedeatricsNoteViews):
    def get(self, request, patient_id):
        results = PatientModals.PaedeatricNote.objects.filter(visit__patient__patient_id=patient_id)
        try:
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class VisitPaedeatricsNotesListView(generics.ListAPIView, PaedeatricsNoteViews):
    def get(self, request, visit_id):
        results = PatientModals.PaedeatricNote.objects.filter(visit__id=visit_id)
        try:
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Gyn
class GynNoteViews(generics.GenericAPIView):
    queryset = PatientModals.GynNote.objects.all()
    serializer_class = serializers.GynNoteSerializer
    lookup_field = "pk"

class GynNotesListView(generics.ListAPIView, GynNoteViews):
    pass

class GynNotesRetrieveView(generics.RetrieveAPIView, GynNoteViews):
    pass

class GynNotesUpdateView(generics.UpdateAPIView, GynNoteViews):
    pass

class GynNotesCreateView(generics.CreateAPIView, GynNoteViews):
    pass

class PatientGynNotesListView(generics.ListAPIView, GynNoteViews):
    def get(self, request, patient_id):
        results = PatientModals.GynNote.objects.filter(visit__patient__patient_id=patient_id)
        try:
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class VisitGynNotesListView(generics.ListAPIView, GynNoteViews):
    def get(self, request, visit_id):
        results = PatientModals.GynNote.objects.filter(visit__id=visit_id)
        try:
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class LabRequestViews(generics.GenericAPIView):
    queryset = LabModels.Request.objects.all()
    serializer_class = lab_serializers.LabRequestSerializer
    lookup_field = "pk"

class LabRequestListView(generics.ListAPIView, LabRequestViews):
    pass
class LabRequestRetrieveView(generics.RetrieveAPIView, LabRequestViews):
    pass
class LabRequestUpdateView(generics.UpdateAPIView, LabRequestViews):
    def patch(self, request, *args, **kwargs):
        lab_request = LabModels.Request.objects.filter(pk=request.data.get("request"))
            
        try:
            if not request:
                return Response({"status" : status.HTTP_404_NOT_FOUND})
            else:
                lab_request = lab_request.first()

            for test in request.data.get("selectedTests"):
                existing_assigned_test = LabModels.AssignedTest.objects.filter(
                    pk=test.get("id"),
                    request=lab_request
                )
                if existing_assigned_test:
                    existing_assigned_test.first().price = test.get("price")
                    existing_assigned_test.first().save()
                else:
                    lab_test = LabModels.LabTest.objects.filter(id=test.get("id"))
                    test = LabModels.AssignedTest.objects.create(
                        request = lab_request,
                        test = lab_test.first(),
                        price = test.get("price"),
                    )

            # detect deleted tests
            if len(LabModels.AssignedTest.objects.filter(request=lab_request)) > len(request.data.get("selectedTests")):
                tests_to_keep = [test.get("id") for test in request.data.get("selectedTests")]
                tests_to_delete = LabModels.AssignedTest.objects.filter(Q(request=lab_request), ~Q(pk__in=tests_to_keep))
                for test in tests_to_delete:
                    test.delete()
                
            return Response({"status" : status.HTTP_201_CREATED})
        except Exception as err:
            return Response({"status" : status.HTTP_400_BAD_REQUEST})
class LabRequestCreateView(generics.CreateAPIView, LabRequestViews):
    def post(self, request, *args, **kwargs):
        try:
            visit = PatientModals.Visit.objects.filter(visit_id=request.data.get("visit_id"))
            lab_request = LabModels.Request.objects.filter(visit=visit.first())
            if not lab_request:
                request_category = LabModels.RequestCategory.objects.filter(name=request.data.get("category"))

                # TODO: Set request doctor
                # doctor = DoctorModels.Doctor.objects.
                lab_request = LabModels.Request.objects.create(
                    visit=visit.first(),
                    category=request_category.first(),
                    # doctor=doctor.first()
                )
            else:
                lab_request = lab_request.first()

            for test in request.data.get("selectedTests"):
                lab_test = LabModels.LabTest.objects.filter(id=test.get("id"))
                test = LabModels.AssignedTest.objects.create(
                    request = lab_request,
                    test = lab_test.first(),
                    price = test.get("price"),
                )
            return Response({"status" : status.HTTP_201_CREATED})
        except Exception as err:
            lab_request.delete()
            return Response({"status" : status.HTTP_400_BAD_REQUEST})

class PatientLabRequestListView(generics.ListAPIView, LabRequestViews):
    def get(self, request, patient_id):
        patient = PatientModals.Patient.objects.filter(patient_id=patient_id)
        if not patient:
            return Response(status=status.HTTP_404_NOT_FOUND)

        results = LabModels.Request.objects.filter(visit__in=patient.first().visit_set.all())
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
    
class VisitLabRequestListView(generics.ListAPIView, LabRequestViews):
    def get(self, request, pk):
        results = LabModels.Request.objects.filter(visit__id=pk)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class CategoryLabRequestListView(generics.ListAPIView, LabRequestViews):
    def get(self, request, category):
        self.queryset = LabModels.Request.objects.filter(visit__id=category)
        return self.list(request, category)


class LabTestViews(generics.GenericAPIView):
    queryset = LabModels.LabTest.objects.all()
    serializer_class = lab_serializers.LabTestSerializer
    lookup_field = "pk"

class LabTestListView(generics.ListAPIView, LabTestViews):
    pass

class LabTestRetrieveView(generics.RetrieveAPIView, LabTestViews):
    pass

class LabTestUpdateView(generics.UpdateAPIView, LabTestViews):
    pass

class LabTestCreateView(generics.CreateAPIView, LabTestViews):
    pass

class CategoryLabTestListView(generics.ListAPIView, LabTestViews):
    def get(self, request, category):
        self.queryset = LabModels.LabTest.objects.filter(category__name__icontains=category)

        search_keyword = request.GET.get("s")
        if search_keyword:
            self.queryset = self.queryset.filter(
                name__icontains=search_keyword
                # Q(description__icontains=search_keyword)
            )
        return self.list(request, category)

class RequestLabTestListView(generics.ListAPIView):
    serializer_class = lab_serializers.AssignedLabTestSerializer

    def get(self, request, pk):
        queryset = LabModels.AssignedTest.objects.filter(request__pk=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)