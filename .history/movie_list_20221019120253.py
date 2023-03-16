movies=[]

class Movie:
    def __init__(self,movie_line):
        size=None
        movie_dat=movie_line.split(sep=',')
        self.id=movie_dat[0]
        size=movie_dat[1].index('(')
        
                