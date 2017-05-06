from AvayaApp.models import Patient

def loginPatient(self,request,format = None):
    if (Patient.objects.filter(UserName = request['UserName']).values('Password')[0]['Password']==request['Password']):
        return Patient.objects.filter(UserName = request['UserName'])