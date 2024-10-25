from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import pandas as pd

model_logreg = r'E:\Assignments\Evaluation\Models\best_logreg_model.pkl'
model_label = r'E:\Assignments\Evaluation\Models\label_encoders.pkl'
model_scaler = r'E:\Assignments\Evaluation\Models\scaler.pkl'

logreg_model = joblib.load(model_logreg)
label_encoder_model = joblib.load(model_label)
scaler_model = joblib.load(model_scaler)

features = ['Num_Children', 'Gender', 'Income', 'Own_Car', 'Own_Housing']
categorical_features = ['Gender', 'Own_Car', 'Own_Housing']
numerical_features = ['Income', 'Num_Children']
required_features = features

@csrf_exempt
def predict_credit_approval(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            df = pd.DataFrame(data)

            for feature in required_features:
                if feature not in df.columns:
                    return JsonResponse({'error': f'Missing feature: {feature}'}, status=400)

            for col in categorical_features:
                le = label_encoder_model[col]
                try:
                    df[col] = le.transform(df[col])
                except ValueError as ve:
                    # Handle unseen categories
                    return JsonResponse({'error': f'Invalid category in {col}: {ve}'}, status=400)

            df[numerical_features] = scaler_model.transform(df[numerical_features])

            df = df[features]

            predictions = logreg_model.predict(df)

            prediction_labels = [int(pred) for pred in predictions]

            # Return the predictions
            return JsonResponse({'predictions': prediction_labels})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Please send a POST request.'}, status=400)
