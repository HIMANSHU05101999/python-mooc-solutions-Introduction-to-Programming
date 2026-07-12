# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genre: list):
        self.title=title
        self.seasons=seasons
        self.genre=genre
        self.ratings=[]

    def rate(self, rating: int):
        self.ratings.append(rating)

    def grade(self):
        if self.ratings:
            return sum(self.ratings)/len(self.ratings)
        else:
            return 0
         
    def __str__(self):
        avg=(f"{len(self.ratings)} ratings, average {self.grade():.1f} points" if self.ratings else 'no ratings')
        return (f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genre)}\n{avg}")
    
def minimum_grade(rating: float, series_list: list):
    return_list=[]
    for item in series_list:
         if item.grade()>=rating:
            return_list.append(item)
    return return_list
            
def includes_genre(genre: str, series_list: list):
    return_list=[]
    for item in series_list:
        if genre in item.genre:
            return_list.append(item)
    return return_list

def main():
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    print(s1)
    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

if __name__=="__main__":
    main()