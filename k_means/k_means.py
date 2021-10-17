from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

fig = plt.figure()
# ax = fig.gca(projection='3d')
ax = fig.add_subplot(111,projection='3d')

df = pd.read_excel('data.xlsx')
df = pd.DataFrame(df, columns= ['FITUR X','FITUR Y', 'FITUR Z'])
print(df)

# 4 cluster, misal 1, 2, 3, 4

# akhir harus angka
dvn = ["cluster1", "cluster2", "cluster3", "cluster4"]
pil = [10, 20, 13, 3]
durasi = 2

pil = [i-1 for i in pil]
titik_tengah = []
for i in pil:
	titik_tengah.append([df['FITUR X'][i], df['FITUR Y'][i], df['FITUR Z'][i]])

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
		titik_tengah.append([x, y, z])
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

print(df)
# ind = 5
# print([df['FITUR X'][ind], df['FITUR Y'][ind], df['FITUR Z'][ind]])

clstr = []
for i in range(len(dvn)):
	clstr.append("clstr"+str(i))
	globals()[clstr[i]] = []

for i in range(len(dvn)):
	for j in range(len(Gtot[0])):
		if Gtot[i][j] == "1":
			globals()[clstr[i]].append(j+1)
		# print(Gtot[i][j],end=', ')

for i in range(len(dvn)):
	print("cluster",str(i),":",globals()[clstr[i]])

print()
clstr_new = []
for i in range(len(dvn)):
	clstr_new.append("clstr_new"+str(i))
	globals()[clstr_new[i]] = []


for i in range(len(clstr_new)):
	globals()[clstr_new[i]].append(globals()[init[i]])
	for j in globals()[clstr[i]]:
		ind = j-1
		tmp = [df['FITUR X'][ind], df['FITUR Y'][ind], df['FITUR Z'][ind]]
		globals()[clstr_new[i]].append(tmp)

# for i in range(len(clstr_new)):
# 	print(globals()[clstr_new[i]])

color = ["b", "g", "y", "c", "m", "y", "k"]

for o in range(0,len(titik_tengah),len(clstr)):
	for m in range(len(clstr_new)):
		tp = titik_tengah[m+o]
		ttps = globals()[clstr_new[m]][1:]

		for i in range(len(ttps)):
			x = np.array([tp[0],ttps[i][0]])
			y = np.array([tp[1],ttps[i][1]])
			z = np.array([tp[2],ttps[i][2]])

			plt.plot(x,y,z,c=color[m])
			ax.scatter(x,y,z,c=color[m],marker='o')
	if o <= len(titik_tengah)-len(clstr)-1:
		plt.pause(durasi)
		plt.cla()

plt.show()