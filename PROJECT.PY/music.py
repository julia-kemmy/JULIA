#the essence of this is basically dertimining who can sing and their vocal range

class Singer:
    def __init__(self,name,vocal_range):
        self.name = name
        self.vocal_range = vocal_range
    def can_sing(self,song_range):
        if self.vocal_range >=song_range:
            return f"{self.name}can sing this song."
        else:
            return f"{self.name}should not sing the song."
   # the main function creates a list of singers
def main():
    singers = [                                                     
        Singer ("Julia", 4),# Julia has a vocal of 5 octaves
        Singer("Makori", 2.5),# Makori has a vocal of 2.5 octaves
        Singer ("Pheel", 1), #Pheel has a vocal of 1 octaves
        Singer("Mwakideu", 3), # Mwakideu has a vocal of 3 octaves 
    ]  

    song_range = 3.5 #the actual range of the song   

    #iterating through each singing to dertimine who can sing   
    for singer in singers:
        print(singer.can_sing(song_range))  
        if __name__ == "_main_":
            main()