from task5 import*
def analyse_movies_language(movies_detail_list):
	languages = {}
	for language in range(len(movies_detail_list)):
		for lang in range(len(movies_detail_list[language]['Language'])):
			if movies_detail_list[language]['Language'][lang] in languages:
				languages[movies_detail_list[language]['Language'][lang]] +=1 
			else:
				languages[movies_detail_list[language]['Language'][lang]] = 1
        return languages        
print analyse_movies_language(top10_data)                
		
