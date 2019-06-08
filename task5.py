from task4 import*
movie_details_list=[]
def scrape_top_list1(top_list):
	#movie_details_list=[]
	random_sleep=random.randint(1,3)
	
	m=time.sleep(random_sleep)
	print random_sleep
	
	for i in top_list[:50]:
		url=i["url"]
		store_movies=movie_details(url)
		movie_details_list.append(store_movies)
	return movie_details_list
		
top10_data =scrape_top_list1(top_movies)
print top10_data