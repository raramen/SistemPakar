from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load dataset
file_path = "heart_cleveland_upload.csv"
df = pd.read_csv(file_path)

# Define categorical and numerical features
categorical_features = {
    "sex": "Jenis Kelamin",
    "cp": "Jenis Nyeri Dada",
    "fbs": "Kadar Gula Darah Puasa Tinggi",
    "restecg": "Hasil Elektrokardiografi Abnormal",
    "exang": "Angina Saat Berolahraga",
    "slope": "Kemiringan Segmen ST",
    "thal": "Thalassemia",
    "ca": "Jumlah Pembuluh Darah Terdeteksi"
}

# ✅ Ganti trestbps dengan sistol dan diastol
numerical_features = {
    "age": "Usia (tahun)",
    "sistol": "Tekanan Darah Sistol (mmHg)",
    "diastol": "Tekanan Darah Diastol (mmHg)",
    "chol": "Kadar Kolesterol (mg/dL)",
    "thalach": "Detak Jantung Maksimal",
    "oldpeak": "Depresi ST akibat olahraga"
}

# Mapping categorical options
categorical_options = {
    "sex": {0: "Perempuan", 1: "Laki-laki"},
    "cp": {0: "Tidak ada nyeri", 1: "Angina ringan", 2: "Angina sedang", 3: "Angina berat"},
    "fbs": {0: "Tidak", 1: "Ya"},
    "restecg": {0: "Normal", 1: "Kelainan ST-T", 2: "Hipertrofi ventrikel kiri"},
    "exang": {0: "Tidak", 1: "Ya"},
    "slope": {0: "Menanjak", 1: "Datar", 2: "Menurun"},
    "thal": {1: "Normal", 2: "Fixed Defect", 3: "Reversible Defect"},
    "ca": {0: "0", 1: "1", 2: "2", 3: "3"}
}

def fuzzy_logic(data):
    # Step 1: Fuzzification
    age = int(data.get("age", 0))
    chol = int(data.get("chol", 0))
    oldpeak = float(data.get("oldpeak", 0))

    if age < 40:
        age_fuzzy = "Muda"
    elif 40 <= age <= 60:
        age_fuzzy = "Dewasa"
    else:
        age_fuzzy = "Lansia"

    if chol < 200:
        chol_fuzzy = "Normal"
    elif 200 <= chol <= 240:
        chol_fuzzy = "Borderline"
    else:
        chol_fuzzy = "Tinggi"

    if oldpeak < 1:
        oldpeak_fuzzy = "Rendah"
    elif 1 <= oldpeak <= 2:
        oldpeak_fuzzy = "Sedang"
    else:
        oldpeak_fuzzy = "Tinggi"

    # Step 2: Inference
    risk = "Rendah"
    if age_fuzzy == "Lansia" and chol_fuzzy == "Tinggi" and oldpeak_fuzzy == "Tinggi":
        risk = "Tinggi"
    elif (age_fuzzy == "Dewasa" and chol_fuzzy == "Tinggi") or (oldpeak_fuzzy == "Sedang"):
        risk = "Sedang"

    # Step 3: Defuzzification
    if risk == "Tinggi":
        return "Risiko tinggi penyakit jantung. Segera konsultasikan ke dokter."
    elif risk == "Sedang":
        return "Risiko sedang. Disarankan melakukan pemeriksaan lebih lanjut."
    else:
        return "Risiko rendah. Tetap jaga kesehatan dan lakukan pemeriksaan rutin."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Tangkap semua input numerik dan kategorikal
        responses = {}
        for key in numerical_features.keys():
            responses[key] = request.form.get(key)
        for key in categorical_features.keys():
            responses[key] = request.form.get(key)

        kesimpulan = fuzzy_logic(responses)

        return render_template(
            'newoutput.html',
            responses=responses,
            kesimpulan=kesimpulan,
            categorical_features=categorical_features,
            numerical_features=numerical_features,
            categorical_options=categorical_options
        )
    
    return render_template(
        'newform.html',
        categorical_features=categorical_features,
        numerical_features=numerical_features,
        categorical_options=categorical_options
    )

if __name__ == '__main__':
    app.run(debug=True)