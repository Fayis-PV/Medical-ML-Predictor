import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def generate_feature_vector(row, unique_prescribed_medicines):
    return [1 if med in row['Prescribed Medicines'] else 0 for med in unique_prescribed_medicines]

def healthcare_instruction_prediction(dataset_path):
    # Load dataset
    data = pd.read_csv(dataset_path)

    # Step 2: Feature Engineering
    # Replace 'None' with NaN
    categorical_columns = ["Gender", "Blood Group", "Allergies", "Medications", "Surgeries", "Medical History"]
    print(data[categorical_columns])
    # Convert categorical variables into numerical representations
    for col in categorical_columns:
        data[col] = data[col].astype("category").cat.codes
    # Combine prescribed medicines into a single column
    data = data.replace('None', 0.0)
    data["Prescribed Medicines"] = data[["Prescribed Medicine 1", "Prescribed Medicine 2", "Prescribed Medicine 3"]].values.tolist()

    # Flatten and unique list of prescribed medicines
    unique_prescribed_medicines = set(med for sublist in data["Prescribed Medicines"] for med in sublist)

    # Filter unique prescribed medicines list to remove empty strings
    unique_prescribed_medicines = [med for med in unique_prescribed_medicines if isinstance(med, str)]

    # Indexing instructions
    data["Prescribed Medicines Index"] = data["Prescribed Medicines"].apply(lambda x: [unique_prescribed_medicines.index(instr) for instr in x if instr in unique_prescribed_medicines])

    # Generate binary vectors for each row
    data["Feature Vector"] = data.apply(lambda row: generate_feature_vector(row, unique_prescribed_medicines), axis=1)

    # Split dataset into features and target
    X = pd.DataFrame(data["Feature Vector"].tolist(), columns=unique_prescribed_medicines)
    # print(data)
    y = X.values  # Convert to numpy array for RandomForestClassifier
    # print(y)
    X = data.drop(columns=["Prescribed Medicine 1", "Prescribed Medicine 2", "Prescribed Medicine 3", "Prescribed Medicines", "Prescribed Medicines Index", "Feature Vector"])
    # print(X)
    # change NaN to 0
    X = X.fillna(0)
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model selection and training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)
    print('y_pred',y_pred,'y_test',y_test)
    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

# Call the function with the dataset path
accuracy = healthcare_instruction_prediction("finished_edge_dataset.csv")
print("Model Accuracy:", accuracy)
