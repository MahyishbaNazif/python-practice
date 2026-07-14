#Average Marks
import pandas as pd
df=pd.read_csv('Student.csv')
ave=df['Marks'].mean()
print(ave)