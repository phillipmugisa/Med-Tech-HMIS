from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.urls import resolve, reverse_lazy
from django.test import Client

from patients import models as PatientModels
from manager import models as ManagerModels
from finance import models as FinanceModels

class PatientTest(TestCase):
    def setUp(self):
        pass
    
    def test_patient_creation(self):
        test_patient = PatientModels.Patient.objects.create(
            firstname = "mark",
            middlename = "alex",
            lastname = "peter",
            nin = "NIOV234923F9VNEVWE",
            gender = "Male",
            telnumber = "+256786273721",
            email = "markalex@test.com",
            address = "Kampala",
            age = 22
        )
        self.assertEqual(test_patient.getFullName(), "mark alex peter")

        # test adding a next of kin to a patient
        n_o_k = PatientModels.NextOfKin.objects.create(
            firstname = "mugalu",
            lastname = "flex",
            nin = "NVWOEI23820232039",
            gender = "Male",
            telnumber = "+256703273322",
            email = "flex.mugalu@test.com",
            address = "Jinja",
            relationship="Father",
            age = 40
        )
        test_patient.next_of_kin.add(n_o_k)
        self.assertEqual(n_o_k.patient, test_patient)
        test_patient.save()

        self.assertEqual(test_patient, n_o_k.patient)

    def test_patients_visits(self):
        test_patient = PatientModels.Patient.objects.create(
            firstname = "mark",
            lastname = "peter",
            nin = "NIOV234923F9VNEVWE",
            gender = "Male",
            telnumber = "+256786273721",
            address = "Kampala",
            age = 22
        )

        speciality = ManagerModels.DoctorSpeciality.objects.create(
            name="Cardiology"
        )

        test_doctor = ManagerModels.Doctor.objects.create(
            firstname = "mugalu",
            lastname = "flex",
            nin = "NVWOEI23820232039",
            gender = "Male",
            telnumber = "+256703273322",
            email = "flex.mugalu@test.com",
            address = "Jinja",
        )
        test_doctor.speciality.add(speciality)

        billingtype = FinanceModels.BillingType.objects.create(
            name = "Cash"
        )

        billing = FinanceModels.Billing.objects.create(
            btype = billingtype,
            amount = 1000000,
            paid = False
        )

        visit = PatientModels.Visit.objects.create(
            patient = test_patient,
            doctor = test_doctor,
            speciality = test_doctor.speciality.first(),
            billing = billing,
        )
        # visit.services.add(lab)

        self.assertEqual(visit, PatientModels.Visit.objects.filter(patient=test_patient).first())

    def test_patients_triage(self):
        test_patient = PatientModels.Patient.objects.create(
            firstname = "mark",
            lastname = "peter",
            nin = "NIOV234923F9VNEVWE",
            gender = "Male",
            telnumber = "+256786273721",
            address = "Kampala",
            age = 22
        )
        visit = PatientModels.Visit.objects.create(
            patient = test_patient
        )

        traige = PatientModels.Triage(
            visit = visit,
            blood_pressure="test",
            heart_rate="test",
            respiratory_rate="test",
            temperature="test",
            sign_symptoms = "this is a test",
            injury_details = "this is a test"
        )

    def test_patient_allergies(self):
        test_patient = PatientModels.Patient.objects.create(
            firstname = "mark",
            lastname = "peter",
            nin = "NIOV234923F9VNEVWE",
            gender = "Male",
            telnumber = "+256786273721",
            address = "Kampala",
            age = 22
        )
        visit = PatientModels.Visit.objects.create(
            patient = test_patient
        )

        traige = PatientModels.Allergy(
            visit = visit,
            name="flue",
            comments = "This is a test"
        )
