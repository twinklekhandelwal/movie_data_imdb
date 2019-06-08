from task5 import*
def analyse_movies_language(movies_language_list):
    language_list = []
    for movie in movies_language_list:
        # json_lang =  json.loads(movie)
        lang = movie['Language']
        language_list.extend(lang)
        language_dic = {}
        for langu in language_list:
            if langu not in language_dic:
                language_dic[langu] = 1
            else:
                language_dic[langu] += 1
    return language_dic

movies_language_count = analyse_movies_language(top10_data)
pprint.pprint (movies_language_count )

