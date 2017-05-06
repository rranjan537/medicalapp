# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Hospital, Patient
from rest_framework.views import APIView
from rest_framework.response import Response
# import AvayaApp.API
from AvayaApp.API import addpatient,hospitallogin,modifypatientrecord,patientlogin,searchhospital,convertxmltojson
from .serializers import HospitalSerializer,PatientSerializer
from django.forms.models import model_to_dict

class AddPatientDetails(APIView):
    def post(self, request, format=None):
        print request.data
        data = addpatient.addData(self, request.data)
        if data == '200':
            return Response('200')

class LoginHospital(APIView):
    def post(self, request, format = None):
        data = hospitallogin.loginHospital(self, request.data)
        serializeddata = HospitalSerializer(data, many=True)

        return Response(serializedData.data)
        # return '200'

class ModifyPatientRecordData(APIView):
    def post(self, request, format=None):
        # print request.data
        data = modifypatientrecord.modifyData(self, request.data)
        if data == '200':
            return Response('200')
        if data == '201':
            return Response('201')
        if data == '400':
            return Response('400')

class LoginPatient(APIView):
    def post(self, request, format=None):
        data = patientlogin.loginPatient(self, request.data)
        serializedData = PatientSerializer(data, many=True)
        return Response(serializedData.data)

class SearchHospital(APIView):
    def post(self, request, format=None):
        data = searchhospital.SearchHospital(self, request.data)
        serialzedData = HospitalSerializer(data, many=True)
        return Response(serialzedData.data)

class XMLtoJSON(APIView):
    def post(self, request, format=None):
        data = (convertxmltojson.ConvertXMLtoJSON(self, request.data))
        return Response(data)