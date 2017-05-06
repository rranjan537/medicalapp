from AvayaApp.models import Hospital
def loginHospital(self,request,format = None):
    if (Hospital.objects.filter(UserName = request['UserName']).values('Password')[0]['Password']==request['Password']):
        return Hospital.objects.filter(UserName = request['UserName'])



        # Hospital.objects.filter(UserName = request['UserName']).values('Password')[0]['Password']
        # To make the above statement first filter the username then get its password value
        # (is is of the form {"Password":"value"})
        # then take its 0th element and get the value corresponding to the password key


        # Note the statement assumes UserName to be Unique