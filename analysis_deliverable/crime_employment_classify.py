import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline


data = pd.read_csv('../final_final_csv.csv')

feature_cols = data[['Violent Total Rate', 'Murder Rate', 'Rape Rate', 'Robbery Rate', 
               'Agg Assault Rate', 'Property Total Rate', 'Burglary Rate', 
               'Larceny Rate', 'MV Theft Rate']]

pred_col = pd.qcut(data['Unemployment_rate'], q=4, labels=['low', 'medium', 'high', 'very high'])

X_train, X_test, y_train, y_test = train_test_split(feature_cols, pred_col, test_size=0.3, random_state=18)

pipeline = make_pipeline(StandardScaler(), SVC(kernel='rbf'))

pipeline.fit(X_train, y_train) # train model

y_unemployment_pred = pipeline.predict(X_test) # make predictions on test data

# evaluate
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_unemployment_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_unemployment_pred))