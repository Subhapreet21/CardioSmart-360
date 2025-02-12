import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import SelectKBest, f_classif

# Load data
heart_data = pd.read_csv('heart_with_smoker_cleaned.csv')

# Check for missing values
if heart_data.isnull().sum().any():
    print("Dataset has missing values. Please address them.")
    heart_data = heart_data.dropna()

# Separate features and target
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Feature selection
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X_scaled, Y)

# Handle class imbalance
smote = SMOTE(random_state=42)
X_resampled, Y_resampled = smote.fit_resample(X_selected, Y)

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X_resampled, Y_resampled, test_size=0.2, stratify=Y_resampled, random_state=42
)

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42)
}

# Train and evaluate models
best_model = None
best_accuracy = 0
for name, model in models.items():
    print(f"Training {name}...")
    
    # Cross-validation
    cv_scores = cross_val_score(model, X_train, Y_train, cv=5)
    print(f"{name} - Mean CV Score: {cv_scores.mean():.4f}")
    
    # Train the model
    model.fit(X_train, Y_train)
    
    # Evaluate on test set
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"{name} - Test Accuracy: {accuracy:.4f}")
    print(f"{name} - Classification Report:\n{classification_report(Y_test, Y_pred)}")
    
    # Save the best model
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Final model
print("Test Accuracy:", best_accuracy)

# Function for prediction
def predict_heart_disease(input_data):
    # Scale and select features
    input_data_scaled = scaler.transform(np.asarray(input_data).reshape(1, -1))
    input_data_selected = selector.transform(input_data_scaled)

    # Predict
    prediction = best_model.predict(input_data_selected)
    probabilities = best_model.predict_proba(input_data_selected)
    
    if prediction[0] == 1:
        return f"The Person has Heart Disease (Probability: {probabilities[0][1]:.2f})"
    else:
        return f"The Person does not have Heart Disease (Probability: {probabilities[0][0]:.2f})"
