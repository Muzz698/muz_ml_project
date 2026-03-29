import joblib
from sklearn.preprocessing import StandardScaler

# Example preprocessor
preprocessor = StandardScaler()
preprocessor.fit(X_train)

# Save it in artifacts folder
joblib.dump(preprocessor, "artifacts/preprocessor.pkl")
import joblib
from sklearn.preprocessing import StandardScaler

# Example preprocessor
preprocessor = StandardScaler()
preprocessor.fit(X_train)

# Save it in artifacts folder
joblib.dump(preprocessor, "artifacts/preprocessor.pkl")