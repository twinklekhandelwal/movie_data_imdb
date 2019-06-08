# #Twelth task---------------------------------
from task1 import*


def scrape_movie_cast(movie_url,movie_caste_url ):
	url_id=movie_url.split("/")
	url_data=url_id[4]
	url_data_store="cast/"+url_data+"_cast.json"
	filepath=pathlib.Path(url_data_store)
	if filepath.exists():
	
		with open(url_data_store,"r") as json_data:
			f=json_data.read()
			f2=json.loads(f)
	
		return f2
	else:	
	
		url2=movie_caste_url+"fullcredits?ref_=tt_cl_sm#cast"
		response=requests.get(url2)
		from bs4 import BeautifulSoup
		soup = BeautifulSoup(response.text,"html.parser")
		main=soup.find('table', class_='cast_list')
		find_td=main.find_all('td',class_='')
		for actor in find_td:
			dec={}
            
			
			id_cast= actor.find('a').get("href")[6:15]
			# cast_split=id_cast.split("/")
			name=actor.get_text().strip()
			dec["imdb_id"]=id_cast
			dec["name"]=name
			lis.append(dec)
			with open(url_data_store,"w") as data:
				data.write(json.dumps(lis))
        return lis
			
for i in top_movies	:
	url=i["url"]	
	url1=url
	lis=[]
			
	print scrape_movie_cast(url,url1)
