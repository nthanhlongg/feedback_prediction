# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import ExcelFile
from imblearn.over_sampling import SMOTE
import pickle

# Importing dataset 
df = pd.read_excel('feedback-mci-2.xlsx')
df = df.drop(columns="#")

# Coverting string to integer
continued_rpl = {'Tiếp tục': 1,
            'Dừng hợp tác': 0}
df.continued = df.continued.map(continued_rpl)

study_abr = {'Yes': 1,
            'No': 0}
df.study_abroad = df.study_abroad.map(study_abr)

# Label Encoding
le = LabelEncoder()
lecturer_label = le.fit_transform(df['lecturer_name'])
lecturer_mappings = {index: label for index, label in 
                  enumerate(le.classes_)}
df.lecturer_name = le.transform(df.lecturer_name)

understanding_label = le.fit_transform(df['understanding_level'])
understanding_mappings = {index: label for index, label in 
                  enumerate(le.classes_)}
df.understanding_level = le.transform(df.understanding_level)

course_label = le.fit_transform(df['course_name'])
course_mappings = {index: label for index, label in 
                  enumerate(le.classes_)}
df.course_name = le.transform(df.course_name)

# Removing unnecessary columns
df = df.drop(columns=['timestamp','name','class_code','feedback_time','understanding_comment','unsatisfaction_thing','building_comment','study_abroad'])

X = df.drop(columns = ['continued'])
Y = df.continued

# Upsampling
smote = SMOTE()
X, Y = smote.fit_resample(X, Y)

# Splitting train and test set
xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size = 0.2, random_state=42)

# Fitting model with Decision Tree algorithm
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(X, Y)

# Saving model to disk
pickle.dump(tree, open('model.pkl','wb'))
