from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
diabetes_file_path = "diabetes.csv"
df = pd.read_csv(diabetes_file_path)

# Define relevant symptoms based on dataset columns
diabetes_symptoms = {
    "Glucose": "Masukkan kadar glukosa Anda:",
    "BloodPressure": "Masukkan tekanan darah Anda:",
    "SkinThickness": "Masukkan ketebalan kulit Anda:",
    "Insulin": "Masukkan kadar insulin Anda:",
    "BMI": "Masukkan indeks massa tubuh Anda:"
}

def evaluate_diabetes_risk(responses):
    """Evaluasi risiko diabetes berdasarkan nilai numerik."""
    score = 0
    
    try:
        glucose = float(responses.get("Glucose", 0))
        blood_pressure = float(responses.get("BloodPressure", 0))
        skin_thickness = float(responses.get("SkinThickness", 0))
        insulin = float(responses.get("Insulin", 0))
        bmi = float(responses.get("BMI", 0))
        
        if glucose > 140:
            score += 2
        if blood_pressure > 80:
            score += 1
        if skin_thickness > 32:
            score += 1
        if insulin > 100:
            score += 2
        if bmi > 30:
            score += 2
    except ValueError:
        return "Input tidak valid. Harap masukkan angka yang benar."
    
    if score >= 5:
        return "Risiko tinggi diabetes. Disarankan konsultasi dengan dokter."
    elif score >= 3:
        return "Risiko sedang. Sebaiknya periksa lebih lanjut ke tenaga medis."
    else:
        return "Risiko rendah. Tetap jaga pola makan dan gaya hidup sehat."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        responses = {key: request.form.get(key) for key in diabetes_symptoms}
        kesimpulan = evaluate_diabetes_risk(responses)
        return render_template('jawaban.html', responses=responses, kesimpulan=kesimpulan)
    return render_template('form1.html', gejala_list=diabetes_symptoms)

if __name__ == '__main__':
    app.run(debug=True)