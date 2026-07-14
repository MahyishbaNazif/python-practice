#Average marks per subject
import pandas as pd
df=pd.read_csv('Student.csv')
a=df.groupby('Subject')['Marks'].mean()
print(a)