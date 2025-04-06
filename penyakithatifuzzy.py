from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('formfuzzy.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Ambil data dari form
        age = int(request.form['age'])
        chol = int(request.form['chol'])
        oldpeak = float(request.form['oldpeak'])

        # Fuzzy Logic untuk usia
        if age < 40:
            age_category = "Muda"
            age_class = "badge bg-success"  # Hijau
        elif age <= 60:
            age_category = "Dewasa"
            age_class = "badge bg-warning"  # Kuning
        else:
            age_category = "Lansia"
            age_class = "badge bg-danger"  # Merah

        # Fuzzy Logic untuk kadar kolesterol
        if chol < 200:
            chol_category = "Normal"
            chol_class = "badge bg-success"  # Hijau
        elif chol <= 240:
            chol_category = "Borderline"
            chol_class = "badge bg-warning"  # Kuning
        else:
            chol_category = "Tinggi"
            chol_class = "badge bg-danger"  # Merah

        # Fuzzy Logic untuk Depresi ST
        if oldpeak < 1:
            oldpeak_category = "Rendah"
            oldpeak_class = "badge bg-success"  # Hijau
        elif oldpeak <= 2:
            oldpeak_category = "Sedang"
            oldpeak_class = "badge bg-warning"  # Kuning
        else:
            oldpeak_category = "Tinggi"
            oldpeak_class = "badge bg-danger"  # Merah

        # Penentuan risiko berdasarkan fuzzy logic sederhana
        if age_category == "Lansia" or chol_category == "Tinggi" or oldpeak_category == "Tinggi":
            risk_class = "high"
            risk_message = "Risiko Tinggi! Harap konsultasi ke dokter."
        elif age_category == "Dewasa" or chol_category == "Borderline" or oldpeak_category == "Sedang":
            risk_class = "medium"
            risk_message = "Risiko Sedang. Perlu perhatian lebih lanjut."
        else:
            risk_class = "low"
            risk_message = "Risiko Rendah. Tetap jaga kesehatan!"

        return render_template(
            'resultfuzzy.html',
            age=age, age_category=age_category, age_class=age_class,
            chol=chol, chol_category=chol_category, chol_class=chol_class,
            oldpeak=oldpeak, oldpeak_category=oldpeak_category, oldpeak_class=oldpeak_class,
            risk_class=risk_class, risk_message=risk_message
        )

    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)