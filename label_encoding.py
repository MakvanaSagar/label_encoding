
#IMPORT ALL NEEDED LIBRARY
from sklearn.preprocessing import LabelEncoder
import pandas as pd



#LOAD DATASET
df = pd.read_csv("genders.csv")
print("Original Dataset...")
print(df)



#COPY METHOD USED TO - SAFE MY ORIGINAL TABLE
df_label = df.copy()



#ENCODING PORTION
le = LabelEncoder()
df_label["gender_Encoded"] = le.fit_transform(df_label["gender"])
print("\n One-hot Encoded Dataset...")
print(df_label[["name", "gender", "gender_Encoded"]])