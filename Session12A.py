"""
    LINKED LIST :)
        CIRCULAR DOUBLY LINKED LIST :)

    Use Case
        gaana.com
        Play List of Songs

        previous and next

    Object      : Song
    Attributes  : title, artist, duration, next, previous

"""

class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.previous = None

    def show_song(self):
        print("-----------------------------------------------")
        print("|  {}  |  {}  |  {}  |".format(self.title, self.artist, self.duration))
        print("-----------------------------------------------")
        print()



def main():
    song1 = Song("1. Kyon", "Payal", 4.23)
    song2 = Song("2. Dil Bechara", "Payal", 5.23)
    song3 = Song("3. Cute Song", "Payal", 4.15)
    song4 = Song("4. Ek Tarfa", "Dhipesh", 3.23)
    song5 = Song("5. Kurta Pajama", "Payal", 7.77)

    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song5
    song5.next = song1


    song1.previous = song5
    song2.previous = song1
    song3.previous = song2
    song4.previous = song3
    song5.previous = song4


    # Iterate in forward Direction
    temp = song1

    while temp.next != song1:
        temp.show_song()
        temp = temp.next

    temp.show_song()


    print()


    # Iterate in backward Direction
    temp = song5
    while temp.previous != song5:
        temp.show_song()
        temp = temp.previous

    temp.show_song()




if __name__ == '__main__':
    main()