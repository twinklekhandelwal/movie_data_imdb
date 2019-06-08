#third task-----
from task1 import*
def group_decate(top_movie):
	movie_by_de = {}
	for movie_de in top_movies:
		year = movie_de['year'] % 10
		year_de = movie_de['year'] - year
		if year_de in movie_by_de:
			movie_by_de[year_de].append(movie_de)
		else:
			movie_by_de[year_de] =[movie_de]
	return (movie_by_de)
group=(group_decate(top_movies))
pprint.pprint(group)