from task1 import*
years=[]
def scrape(movies):

	for i in movies:
		year=i["year"] 
	 	if year not in years:
			years.append(year)
	
	dic={i:[]for i in years}
	for	y in movies:
		year=y["year"]

		for z in years:
			if(year==z):
				dic[z].append(y)
	return (dic)
# print scrape(top_movies)	
