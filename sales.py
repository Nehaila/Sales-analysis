import pandas as pd
import os 
import xlsxwriter
import openpyxl
import re
#Check what is the directory here:
pd.set_option('display.max_columns',9)
print(os.getcwd())
#Change the directory:
os.chdir('C:/Users/32466/Desktop/python3')
#Check what is the new directory
print(os.getcwd())
directory = os.getcwd()
df=pd.DataFrame()
i=1
listt={}
for file in os.listdir(directory):
	df_sec = pd.read_csv(file)
	df_sec.columns=['Order_ID', 'Product', 'Quantity_Ordered', 'Price_Each', 'OrderDate',
   'Purchase_Address']
	df_sec["city"] = ''
	df_sec=df_sec.dropna()
	df_sec= df_sec.drop(df_sec.loc[df_sec.OrderDate =='Order Date'].index, axis=0)

	#Add Sales column, first convert to numeric: 
	df_sec['Price_Each']= pd.to_numeric(df_sec['Price_Each'])
	df_sec['Quantity_Ordered']=pd.to_numeric(df_sec['Quantity_Ordered'])
	df_sec['Sales']= df_sec['Price_Each']*df_sec['Quantity_Ordered']
	df_sec['city'] = [re.search(',(.+?),', str(x)).group(1) for x in df_sec['Purchase_Address']]
	df_sec=df_sec.reset_index(drop=True)
	listt[int(df_sec['Sales'].sum())] = int(df_sec['OrderDate'][0:1].str[0:2])
	i=i+1
	df=df.append(df_sec)

df=df.sort_values(by=['OrderDate'])
df=df.reset_index(drop=True)

#printing the dataframe:
print(df)
#What is the best month for sales? Doing it with dictionnaries
print(listt) #December 
#What city sold the most product?
sum_per_city=df.groupby(['city']).sum()
print(sum_per_city) #San Francisco 