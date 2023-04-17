from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from patients import models as PatientModels
from manager import models as ManagerModels
from finance import models as FinanceModels

class PatientTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_patient_create(self):
        url = reverse('app_api:patient_create')
        data = {
            "firstname" : "mark",
            "middlename" : "alex",
            "lastname" : "peter",
            "nin" : "NIOV234923F9VNEVWE",
            "gender" : "Male",
            "telnumber" : "+256786273721",
            "email" : "markalex@test.com",
            "address" : "Kampala",
            "age" : 22
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PatientModels.Patient.objects.count(), 1)

        # fetch data
        url = reverse('app_api:patient_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        patient = PatientModels.Patient.objects.filter(patient_id = response.data[0].get("patient_id")).first()
        self.assertEqual(f'{data["firstname"]} {data["middlename"]} {data["lastname"]}', patient.getFullName())

        # test update
        url = reverse('app_api:patient_update', kwargs={"patient_id": patient.patient_id})
        response = self.client.patch(url, data={"email" : "alexmarkp@test.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("alexmarkp@test.com", response.data.get("email"))

        # retrieve patients
        url = reverse('app_api:patients_retrieve', kwargs={"patient_id": patient.patient_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(patient.patient_id, response.data.get("patient_id"))

        # add next of kin
        url = reverse('app_api:patient_create_nok')
        data = {
            "firstname" : "mugalu",
            "lastname" : "flex",
            "nin" : "NVWOEI23820232039",
            "gender" : "Male",
            "telnumber" : "+256703273322",
            "email" : "flex.mugalu@test.com",
            "address" : "Jinja",
            "relationship" :"Father",
            "age" : 40,
            "patient" : patient.id
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(patient.next_of_kin.all().last().nin, data.get("nin"))
