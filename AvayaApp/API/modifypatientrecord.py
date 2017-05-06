from AvayaApp.models import Patient
import ast

def modifyData(self, request, format=None):

    try:
        ob = Patient.objects.get(UID = request['UID'])
        testarray = ast.literal_eval(ob.HospitalId)
        if request['HospitalId'] in testarray:
            ob.save()
        else:
            testarray.append(request['HospitalId'])
            ob.HospitalId = testarray
            ob.save()
        return '200'


    except Patient.DoesNotExist:                #UID is not present
        return ('400')

    except SyntaxError:                         #array is empty
        ob = Patient.objects.get(UID=request['UID'])
        testarray = []
        testarray.append(request['HospitalId'])
        ob.HospitalId = testarray
        ob.save()
        return '201'