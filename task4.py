from task1 import*
def movie_details(url):
	
	url_id=url.split("/")
	url_data=url_id[4]

	url_data_store="file1/"+url_data+".json"

	


	filepath=pathlib.Path(url_data_store)
	if filepath.exists():
	
			
		with open(url_data_store,"r") as json_data:
			f=json_data.read()
			f2=json.loads(f)
	
		return f2
		
			
	else:
		data_store={"name":"","director":"","Language":"","Country":"","genre": "","bio":"","poster_image_url":"","runtime":"","cast1":""}
	
		response=requests.get(url)

		out = BeautifulSoup(response.text,"html.parser")
		main1=out.find('div',class_="title_wrapper").h1.get_text().strip()
	
		movies_name=""
		for i in main1:
			if "(" not in i:
				movies_name=movies_name+i.strip()
			
			else:
				break		
		plot=out.find('div',class_='plot_summary')
		summary=plot.find('div',class_='credit_summary_item')
		director1=summary.find_all("a")
		director_name= [i.get_text().strip() for i in director1]
		gen=out.find('div',class_="title_block")
		dra=gen.find('div',class_='subtext')
		boi=out.find('div',class_="plot_summary")
		boi_data=boi.find('div',class_='summary_text').get_text().strip()
		genre=dra.find_all("a")
		genre_name=[i.get_text().strip() for i in genre]
		
		link_data=out.find('div',class_='poster').a["href"]
		url="https://www.imdb.com"+link_data
		time=out.find('div',class_="title_block")
		run_time=time.find('div',class_='subtext')
		run_time_data=run_time.find("time").get_text().strip()
		st=str(run_time_data)
		minut=int(st[0])*60
		if "min" in time:
			min1=int(i[3:].strip("min"))
			minut1= minut+min1
		else:
			minut1=minut
		
		coun=out.find('div',{"id":"titleDetails"})
		country=coun.find_all('div',class_='txt-block')
		for i in country:
			h1=i.find_all("h4",class_="inline")
			for j in h1:
				if "Language:" in j:
				
					language_name=i.find_all("a")
					language_de=[j.get_text() for j in language_name]
				elif "Country:" in j:
					country_name=i.find("a")
		 			country_de	=[k for k in country_name]
		# data_store={"name":"","director":"","Language":"","Country":"","genre": "","bio":"","poster_image_url":"","runtime":"","cast1":""}
		
		data_store["name"]=str(movies_name)
		data_store["director"]=director_name
		data_store["Language"]=str(language_de)
		data_store["Country"]=country_de
		data_store["genre"]=str(genre_name)
		data_store["bio"]=boi_data
		data_store["poster_image_url"]=str(url)
		data_store["runtime"]=int(minut)
		data_store["runtime"]=int(minut)
		# data_store["cast1"]=scrape_movie_cast(url,url1)
		


		with open(url_data_store,"w") as data:
			data.write(json.dumps(data_store))
        return data_store
for i in top_movies[:25]:
	url=i["url"]
	print movie_details(url)		
    # print store_movies