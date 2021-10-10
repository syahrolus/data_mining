import pandas as pd
import math

df = pd.read_excel('data.xlsx')
df = pd.DataFrame(df, columns= ['FITUR X','FITUR Y', 'FITUR Z'])
print(df)

# 4 cluster, misal 1, 2, 3, 4

# akhir harus angka
dvn = ["cluster1", "cluster2", "cluster3", "cluster4"]
pil = [5, 2, 3, 4]

# pil = []
# for i in range(len(dvn)):
	# pil.append(int(dvn[i][-1]))

init = []
for i in range(len(dvn)):
	globals()[dvn[i]] = []
	init.append(dvn[i][0]+dvn[i][-1])
for i in range(len(init)):
	globals()[init[i]] = []

for i in range(len(init)):
	p = pil[i]-1
	globals()[init[i]] = [df['FITUR X'][p], df['FITUR Y'][p], df['FITUR Z'][p]]

# print(globals()[init[0]])
Gtmp = []

while True:
	for i in range(len(df)):
		for j in range(len(dvn)):
			c1x = df['FITUR X'][i] - globals()[init[j]][0]
			c1y = df['FITUR Y'][i] - globals()[init[j]][1]
			c1z = df['FITUR Z'][i] - globals()[init[j]][2]
			hitung = round(math.sqrt(pow(c1x,2)+pow(c1y,2)+pow(c1z,2)),3)
			globals()[dvn[j]].append(hitung)

	G = []
	for i in range(len(dvn)):
		G.append('G'+dvn[i][-1])
	for i in range(len(G)):
		globals()[G[i]] = []

	# print(globals()[dvn[0]])
	# print(globals()[dvn[1]])
	# print(globals()[dvn[2]])
	# print(globals()[dvn[3]])

	for i in range(len(globals()[dvn[0]])):
		print(i,end='\t')
		tmp = []
		for j in range(len(G)):
			tmp.append(globals()[dvn[j]][i])
		print(tmp,end='\t')
		# print(min(tmp),end='\t')
		tmp2 = []
		for k in range(len(G)):
			if k == tmp.index(min(tmp)): 
				tmp2.append('1')
			else:
				tmp2.append('0')
		for l in range(len(G)):
			globals()[G[l]].append(tmp2[l])
		print(tmp2)
		# print()

	# print(G1)
	# print(G2)
	# print(G3)
	# print(G4)
	# print(globals()[dvn[0]])

	# Pusat Baru

	# loop tiap G
	for i in range(len(G)):
		# loop tiap unit G
		tmpx = 0
		tmpy = 0
		tmpz = 0
		jml = 0
		for j in range(len(globals()[G[0]])):
			if globals()[G[i]][j] == '1':
				tmpx += df['FITUR X'][j]
				tmpy += df['FITUR Y'][j]
				tmpz += df['FITUR Z'][j]
				jml += 1
		x = round(tmpx/jml,3)
		y = round(tmpy/jml,3)
		z = round(tmpz/jml,3)
		globals()[init[i]] = [x, y, z]
		print(globals()[init[i]])

	Gtot = []
	for i in range(len(G)):
		Gtot.append(globals()[G[i]])
	if Gtot == Gtmp:
		break
	Gtmp = Gtot

	for i in range(len(dvn)):
		globals()[dvn[i]].clear()

print('\n================== HASIL ==================\n')
for i in range(len(dvn)):
	print(dvn[i], ":",end=' data ')
	for j in range(len(Gtot[0])):
		if Gtot[i][j] == "1":
			print(j+1,end=', ')
		# print(Gtot[i][j],end=', ')
	print()
