from task5 import*
def  analyse_movies_directors(movies_detail_list):
    movie_directors_list=[]
    for movieDirector in movies_detail_list:
            
        direct = movieDirector["director"] 
        
        movie_directors_list.extend(direct)
        
        movie_directors_dic = {}
        for direc in  movie_directors_list:
            if direc not in  movie_directors_dic:
                movie_directors_dic[direc]= 1
            else:
                movie_directors_dic[direc] +=1
        
    return movie_directors_dic

movieDirectorCount =  analyse_movies_directors(top10_data)
print movieDirectorCount
