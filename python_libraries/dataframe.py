import pandas as pd
std_data= [(1,'Mahyishba Nazif', 19,'female','Pakistan'),(2,'John',60,'male','India'), (3,'Ray', 40,'male','Turkey'),
           (4,'Sara', 20,'female','Afghanistan'), (5,'Daniel',37,'male','England')]
df=pd.DataFrame(std_data, columns=['Id','Name','Age','Gender','Country'])
print(df)