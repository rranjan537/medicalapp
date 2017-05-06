import xmltodict, json

def ConvertXMLtoJSON(self, request, format=None):
    recievedData = request['XMLData']
    recievedData = recievedData[39:]
    data = (xmltodict.parse(recievedData))
    print (json.dumps(data))
    sendData = (json.dumps(data))
    
    return (sendData)