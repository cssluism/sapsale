import os
import pandas as pd

# Variables
DATA_PATH = '/app/data/data_transfort.csv'
CLASS_LABEL= int(os.getenv('CLASS_LABEL'))
KERNEL= os.getenv('KERNEL')
MODEL_PATH = '/app/model/model.pkl'

# Load Datasets
import pandas as pd
df = pd.read_csv(DATA_PATH)


y = df[['product_sale_per_month']]
X = df[['YEAR_SALEHD','MONTH_SALEHD', 'CURRENCY_SALEHD', 'YEAR_SALEIT','MONTH_SALEIT', 'PARTNERID_CLIENT_SO', 'CURRENCY_SALEITEM', 'PRODUCTID', 'PRODCATEGORYID']]



#X = df.drop('target', axis=1)
#y = df['target']

# Partition into Train and test dataset
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3)

# Init model
from sklearn import svm
model = svm.SVC(C=CLASS_LABEL, kernel=KERNEL)
# model = svm.SVC(C=1, kernel="rbf")

# Train model
model.fit(train_x, train_y)

# Test model
score = model.score(test_x, test_y)
# Output will be available in logs of SAP AI Core.
# Not the ideal way of storing /reporting metrics in SAP AI Core, 
print(f"Test Data Score: {score}")

# Save model
import pickle
pickle.dump(model, open(MODEL_PATH, 'wb'))