#Finding topper student
import pandas as pd
df=pd.read_csv('Student.csv')
topper = df.loc[df['Marks'].idxmax()]
print(topper['Name'], topper['Marks'])
