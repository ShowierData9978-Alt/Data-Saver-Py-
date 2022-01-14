import json
def Write():	
    dict1 = {}
    print(dict1)
    dict1['normal']['Users'].update({'name':'Showierdata9978'})
    f = open('Testing.json','r+')
    print(dict1)
    json.dump(dict1,f)


Write()