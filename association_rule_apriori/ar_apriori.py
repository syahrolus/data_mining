import pandas as pd
from itertools import combinations
from itertools import permutations
import itertools
import threading
import time
import sys

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c + ' datanya banyak sih:(')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)

t.start()


namaFile = 'basket_analysis.csv'
df = pd.read_csv(namaFile)
kolom = ['Apple', 'Bread', 'Butter', 'Cheese', 'Corn', 'Dill', 'Eggs', 'Ice cream', 'Kidney Beans', 'Milk', 'Nutmeg', 'Onion', 'Sugar', 'Unicorn', 'Yogurt','chocolate']
# kolom = ['Apple', 'Bread', 'Butter', 'Cheese', 'Corn']
df = pd.DataFrame(df, columns=kolom)

support = 9
confidence = 23

# ===========
data_rekap = []

def Cek(cek):
	count = 0
	c = len(cek)
	for i in range(len(df)):
		st = 0
		for j in cek:
			if df[j][i]:
				st += 1
		if st == c:
			count += 1
	return count

def Apriori(row1, data, k):
	data_new = []
	row2 = []
	if len(data) == 0:
		return
	for i in combinations(row1, k):
		tmp = []
		for j in i:
			tmp.append(j)
		count = Cek(tmp)
		sprt = round(count/len(df),2)*100
		if sprt > support:
			for kol in tmp:
				if kol not in row2: 
					row2.append(kol)
			data_new.append([tmp, count, sprt])
			data_rekap.append([tmp, count, sprt])
	Apriori(row2, data_new, k+1)

data = []
row1 = []
for i in kolom:
	cnt = 0
	for j in range(len(df)):
		if df[i][j]:
			cnt += 1
	sprt = round(cnt/len(df),2)*100
	if sprt > support:
		row1.append(i)
		data.append([i, cnt, sprt])

Apriori(row1, data, 2)
# data_total = pd.DataFrame(data_rekap, columns=['itemset', 'support count', 'support %'])
# print(data_total)

data_confidence = []
for i in range(len(data_rekap)):
	for j in permutations(data_rekap[i][0]):
		sprtxy = Cek(j)
		sprtx = Cek([j[-1]])
		conf = round(sprtxy/sprtx,2)*100
		if conf > confidence:
			data_confidence.append([str(j[:-1])+'=>'+str(j[-1]),round(sprtxy/len(df),2)*100,round(sprtx/len(df),2)*100,conf])

print()
hasil_akhir = pd.DataFrame(data_confidence, columns=['Aturan', 'Support XuY %', 'Support X %', 'Confidence %'])
print(hasil_akhir)
hasil_akhir.to_csv('hasil_akhir.csv')
#long process here

done = True



