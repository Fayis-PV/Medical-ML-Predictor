# !pip install fastapi
# !pip install uvicorn
# !pip install pickle5
# !pip install pydantic
# !pip install scikit-learn
# !pip install requests
# !pip install pypi-json
# !pip install pyngrok
# !pip install nest-asyncio

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):

    Age : int
    BloodGroup : int
    Height : float
    Weight : float
    Gender : int
    Allergies : int
    Medications : int
    Surgeries : int
    MedicalHistory : int
    SystolicBP : int
    DiastolicBP : int
    TotalCholesterol : int
    HDL : int
    LDL : int
    FastingBloodSugar : int
    PostprandialBloodSugar : int

# loading the saved model
diabetes_model = pickle.load(open('c:/Users/fayis/Desktop/Farrago/working_area/predictor.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    age = input_dictionary['Age']
    blood_group = input_dictionary['BloodGroup']
    height = input_dictionary['Height']
    weight = input_dictionary['Weight']
    gender = input_dictionary['Gender']
    allergies = input_dictionary['Allergies']
    medications = input_dictionary['Medications']
    surgeries = input_dictionary['Surgeries']
    medical_history = input_dictionary['MedicalHistory']
    systolic_bp = input_dictionary['SystolicBP']
    diastolic_bp = input_dictionary['DiastolicBP']
    total_cholesterol = input_dictionary['TotalCholesterol']
    hdl = input_dictionary['HDL']
    ldl = input_dictionary['LDL']
    fasting_blood_sugar = input_dictionary['FastingBloodSugar']
    postprandial_blood_sugar = input_dictionary['PostprandialBloodSugar']



    input_list = [age,blood_group,height,weight,gender,allergies,medications,surgeries,medical_history,systolic_bp,diastolic_bp,total_cholesterol,hdl,ldl,fasting_blood_sugar,postprandial_blood_sugar ]

    prediction = diabetes_model.predict([input_list])

    print(prediction)

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)

