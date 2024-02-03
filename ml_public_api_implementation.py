# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:06:30 2022

@author: siddhardhan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:16:26 2022

@author: siddhardhan
"""

import json
import requests


url = 'http://05ca-34-83-94-130.ngrok.io/diabetes_prediction'

40,3,165,65,1,1,1,4,4,125,75,180,45,135,90,150
input_data_for_model = {
    
    'Age' : 40,
    'BloodGroup' : 3,
    'Height' : 165,
    'Weight' : 65,
    'Gender' : 1,
    'Allergies' : 1,
    'Medications' : 1,
    'Surgeries' : 4,
    'MedicalHistory' : 4,
    'SystolicBP' : 125,
    'DiastolicBP' : 75,
    'TotalCholesterol' : 180,
    'HDL' : 45,
    'LDL' : 135,
    'FastingBloodSugar' : 90,
    'PostprandialBloodSugar' : 150
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)

