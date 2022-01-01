import pandas as pd
import numpy as np
import math

def MemilihNode(kolom, df):
	for kol in kolom:
		for i in range(len(df[kol])):
			 
			atr = df[kol][i]

			if atr not in globals()[kol]:
				if df['stroke'][i] == 1:	# change stroke to your last column/result
					globals()[kol][atr] = {'ya':1, 'tidak':0}
				else:
					globals()[kol][atr] = {'ya':0, 'tidak':1}
			else:
				if df['stroke'][i] == 1:	# change stroke to your last column/result
					globals()[kol][atr]['ya'] += 1
				else:
					globals()[kol][atr]['tidak'] += 1

def EntropyKecil(kolom, df):
	Ekecil = [100]
	for kol in kolom:
		E = 0
		for i in globals()[kol]:
			ya = globals()[kol][i]['ya']
			tidak = globals()[kol][i]['tidak']
			p = ya/(ya+tidak)
			n = tidak/(ya+tidak)
			try:
				r1 = (-p)*(math.log(p,2))
			except Exception as e:
				r1 = 0
			try:
				r2 = (-n)*(math.log(n,2))
			except Exception as e:
				r2 = 0
			Etmp = round(((ya+tidak)/len(df[kol]))*(r1+r2),2)
			E += Etmp
		if E < Ekecil[0]:
			Ekecil = [E,kol]
	return Ekecil

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def Run(E, df, kolom):
	for j in globals()[E[1]].keys():
		if globals()[E[1]][j]['ya'] == 0:
			globals()[E[1]+'Tree'].add_child(TreeNode((str(j)+"->TIDAK")))
			continue
		elif globals()[E[1]][j]['tidak'] == 0:
			globals()[E[1]+'Tree'].add_child(TreeNode((str(j)+"->YA")))
			continue
		if len(kolom) <= 3:
			if globals()[E[1]][j]['tidak'] > globals()[E[1]][j]['ya']: 			# can be changed if the results still require expert judgment
				globals()[E[1]+'Tree'].add_child(TreeNode((str(j)+"->TIDAK")))
				continue
			else:
				globals()[E[1]+'Tree'].add_child(TreeNode((str(j)+"->YA")))
				continue
		df2 = df[df[E[1]] == j]
		df2 = pd.DataFrame(df2, columns=kolom)
		df2.to_excel('tmp.xlsx')
		df2 = pd.read_excel('tmp.xlsx')
		df2 = pd.DataFrame(df2, columns=kolom)
		for i in kolom:
			globals()[i] = {}
		MemilihNode(kolom, df2)
		E2 = EntropyKecil(kolom[1:-1], df2)
		globals()[E2[1]+'Tree'] = TreeNode((str(j)+'->'+str(E2[1])))
		globals()[E[1]+'Tree'].add_child(globals()[E2[1]+'Tree'])
		for i in range(len(kolom)):
			if kolom[i] == E2[1]:
				kolom2 = np.delete(kolom,i)
		Run(E2, df2, kolom2)

# change according to your need
# please remain that :
# 	1. first column and last column must be id/name/unique and result(in this case is stroke)
# 	2. please classify your columns first, source code is in klasifikasi.py
kolom = ["id", "gender", "age", "hypertension", "heart_disease", "ever_married", "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status", "stroke"]
nama_file = 'stroke_classified.xlsx'
# !change according to your need


for i in kolom:
	globals()[i] = {}

df = pd.read_excel(nama_file)
df = pd.DataFrame(df, columns=kolom)
MemilihNode(kolom, df)
E = EntropyKecil(kolom[1:-1], df)
globals()[E[1]+'Tree'] = TreeNode(E[1])


kolom = np.array(kolom)
for i in range(len(kolom)):
	if kolom[i] == E[1]:
		kolom2 = np.delete(kolom,i)
Run(E,df,kolom2)

# print decision tree
# globals()[E[1]+'Tree'].print_tree() 	# uncomment to get decision_tree.txt

predict = []
for i in range(len(df['stroke'])):		# change stroke to your last column/result
	ambilData = globals()[E[1]+'Tree']
	kol = E[1]
	df_index = df.iloc[i]
	j = 1
	while j:
		for i in range(len(ambilData.children)):
			tes = ambilData.children[i].data
			tes = tes.split('->')
			if tes[0] == str(df_index[kol]):
				if tes[1] == 'YA':
					# print('1/YA')
					predict.append(1)
					j = 0
				elif tes[1] == 'TIDAK':
					# print('0/TIDAK')
					predict.append(0)
					j = 0
				ambilData = ambilData.children[i]
				kol = tes[1]
				break

# print(predict)
df['Prediksi'] = predict
df.to_excel('hasil_prediksi.xlsx')

e = 0
for i in range(len(df['stroke'])):
	if df['stroke'][i] != df['Prediksi'][i]:	# change stroke to your last column/result
		e+=1

hitung = (e/len(df['stroke']))*100				# change stroke to your last column/result
print(hitung)