class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
        print "\n A new Song is adding..."

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday=Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])

bulls_on_parade=Song(["They rally around the family","With pockets full of shells"])

little_star=Song(["little star","How I count out many you are"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

little_star.sing_me_a_song()