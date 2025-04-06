def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def process_inputs(responses):
    # Dummy prediction
    prediction = 1 if to_float(responses.get('age', 0)) > 50 else 0

    fuzzy_results = {}
    
    for key, value in responses.items():
        v = to_float(value)
        if v is None:
            continue

        if key == 'age':
            if v < 40:
                fuzzy_results[key] = ('Muda', 'fuzzy-baik')
            elif 40 <= v <= 60:
                fuzzy_results[key] = ('Dewasa', 'fuzzy-sedang')
            else:
                fuzzy_results[key] = ('Lansia', 'fuzzy-buruk')
        
        elif key == 'chol':
            if v < 200:
                fuzzy_results[key] = ('Normal', 'fuzzy-baik')
            elif 200 <= v <= 240:
                fuzzy_results[key] = ('Borderline', 'fuzzy-sedang')
            else:
                fuzzy_results[key] = ('Tinggi', 'fuzzy-buruk')

        elif key == 'oldpeak':
            if v < 1.0:
                fuzzy_results[key] = ('Sedikit', 'fuzzy-baik')
            elif 1.0 <= v < 2.5:
                fuzzy_results[key] = ('Sedang', 'fuzzy-sedang')
            else:
                fuzzy_results[key] = ('Tinggi', 'fuzzy-buruk')

        elif key == 'thalach':
            if v < 60:
                fuzzy_results[key] = ('Rendah', 'fuzzy-buruk')
            elif 60 <= v <= 100:
                fuzzy_results[key] = ('Normal', 'fuzzy-baik')
            else:
                fuzzy_results[key] = ('Tinggi', 'fuzzy-baik')

        elif key == 'sistol':
            if v < 90:
                fuzzy_results[key] = ('Rendah', 'fuzzy-buruk')
            elif 90 <= v <= 120:
                fuzzy_results[key] = ('Normal', 'fuzzy-baik')
            else:
                fuzzy_results[key] = ('Tinggi', 'fuzzy-buruk')

        elif key == 'diastol':
            if v < 60:
                fuzzy_results[key] = ('Rendah', 'fuzzy-buruk')
            elif 60 <= v <= 80:
                fuzzy_results[key] = ('Normal', 'fuzzy-baik')
            else:
                fuzzy_results[key] = ('Tinggi', 'fuzzy-buruk')

    return prediction, fuzzy_results