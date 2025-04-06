from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
hepatitis_file_path = "HepatitisCdata.csv"
df = pd.read_csv(hepatitis_file_path)

# Define relevant symptoms based on dataset columns
hepatitis_symptoms = {
    "ALB": "Masukkan kadar albumin Anda:",
    "ALP": "Masukkan kadar alkaline phosphatase Anda:",
    "ALT": "Masukkan kadar alanine aminotransferase Anda:",
    "AST": "Masukkan kadar aspartate aminotransferase Anda:",
    "BIL": "Masukkan kadar bilirubin Anda:"
}

def evaluate_hepatitis_risk(responses):
    """Evaluasi risiko hepatitis berdasarkan nilai numerik."""
    score = 0
    
    try:
        alb = float(responses.get("ALB", 0))
        alp = float(responses.get("ALP", 0))
        alt = float(responses.get("ALT", 0))
        ast = float(responses.get("AST", 0))
        bil = float(responses.get("BIL", 0))
        
        if alb < 3.5:
            score += 2
        if alp > 120:
            score += 1
        if alt > 40:
            score += 2
        if ast > 40:
            score += 2
        if bil > 1.2:
            score += 2
    except ValueError:
        return "Input tidak valid. Harap masukkan angka yang benar."
    
    if score >= 5:
        return "Risiko tinggi hepatitis. Disarankan segera konsultasi dengan dokter."
    elif score >= 3:
        return "Risiko sedang. Sebaiknya periksa lebih lanjut ke tenaga medis."
    else:
        return "Risiko rendah. Tetap jaga pola makan dan lakukan pemeriksaan rutin."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        responses = {key: request.form.get(key) for key in hepatitis_symptoms}
        kesimpulan = evaluate_hepatitis_risk(responses)
        return render_template('jawaban.html', responses=responses, kesimpulan=kesimpulan)
    return render_template('form2.html', gejala_list=hepatitis_symptoms)

if __name__ == '__main__':
    app.run(debug=True)