import pandas as pd
import math

df = pd.read_excel('healthcare-dataset-stroke-data.xlsx')
kolom = ["id", "gender", "age", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"]
df = pd.DataFrame(df, columns= kolom)

df['bmi'] = df['bmi'].astype(str)
df['avg_glucose_level'] = df['avg_glucose_level'].astype(str)

kolom = 'avg_glucose_level'
for i in range(len(df[kolom])):
	val = float(df[kolom][i])
	if df['age'][i] < 6:
		if val >= 100 and val <= 200:
			# atr = 'normal'
			df.at[i,kolom] = 'normal'
		elif val < 100:
			# atr = 'rendah'
			df.at[i,kolom] = 'rendah'
		elif val > 200:
			# atr = 'tinggi'
			df.at[i,kolom] = 'tinggi'
	elif df['age'][i] >= 6 and df['age'][i] <= 12:
		if val >= 70 and val <= 150:
			# atr = 'normal'
			df.at[i,kolom] = 'normal'
		elif val < 70:
			# atr = 'rendah'
			df.at[i,kolom] = 'rendah'
		elif val > 150:
			# atr = 'tinggi'
			df.at[i,kolom] = 'tinggi'
	elif df['age'][i] > 12:
		if val < 100:
			# atr = 'normal'
			df.at[i,kolom] = 'normal'
		elif val >= 100:
			# atr = 'tinggi'
			df.at[i,kolom] = 'tinggi'

kolom = 'bmi'
for i in range(len(df[kolom])):
	val = float(df[kolom][i])
	try:
		val = float(val)
		if val < 18.5:
			# atr = 'underwight'
			df.at[i,kolom] = 'underwight'
		elif val >= 18.5 and val <= 24.99:
			# atr = 'healty weight'
			df.at[i,kolom] = 'healty weight'
		elif val > 24.99 and val <= 29.99:
			# atr = 'overweight'
			df.at[i,kolom] = 'overweight'
		elif val > 29.99:
			# atr = 'obese'
			df.at[i,kolom] = 'obese'
	except Exception as e:
		# atr = 'NaN'
		df.at[i,kolom] = 'lain'

df['age'] = df['age'].astype(str)
kolom = 'age'
for i in range(len(df[kolom])):
	val = float(df[kolom][i])
	if val <= 11:
		# atr = 'anak'
		df.at[i,kolom] = 'anak'
	elif val > 11 and val <= 25:
		# atr = 'remaja'
		df.at[i,kolom] = 'remaja'
	elif val > 25 and val <= 45:
		# atr = 'dewasa'
		df.at[i,kolom] = 'dewasa'
	elif val > 45:
		# atr = 'lansia'
		df.at[i,kolom] = 'lansia'

df.to_excel('stroke_classified.xlsx')
