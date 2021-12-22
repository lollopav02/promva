#calcolo densità popolazione

fp_area=open("country_area.txt", "r", encoding="utf-8")
fp_pop=open("country_pop.txt", "r", encoding="utf-8")

list_area=[]
list_pop=[]

for line in fp_area:
    list_area.append(line.split())

for line in fp_pop:
    list_pop.append(line.split())

fp_area.close()
fp_pop.close()

for country in list_area:
    for i in range(len(list_pop)):
        if country[0]==list_pop[i][0]:
            print(country[0],float(list_pop[i][1])/float(country[1])*1000)