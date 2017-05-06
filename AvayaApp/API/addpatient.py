from AvayaApp.models import Patient

def addData(self, request, format = None):
	ob = Patient()
	# print request['Name']

	ob.Age = request['Age']
	ob.Name = request['Name']
	if(request['Age']<'18'):
		ob.AgeGroup = '1'
	elif(request['Age']>='18' and request['Age']<'40'):
		ob.AgeGroup = '2'
	elif(request['Age'] >= '40' and request['Age'] < '60'):
		ob.AgeGroup = '3'
	elif(request['Age']>='60'):
		ob.AgeGroup = '4'
	ob.UID = request['UID']
	ob.UserName = request['UserName']
	ob.Password = request['Password']
	ob.save()
	return('200')
