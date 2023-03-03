import window

class Song:
    def __init__(self, name, file):
        self.name = name
        self.file = file
        self.next = None
        self.prev = None
        print("Song was added...")
        
    def PlaySong(self):
        pass
        
        
class Playlist:
    #конструктор
    def __init__(self):
        self.start_song = None
    
    #вставка песни в пустой плейлист
    def InsertEmptyPlaylist(self, name, file):
        if self.start_song is None:
            new_song = Song(name, file)
            self.start_song = new_song
            # print("First song was inserted!")
        else:
            pass
            # print("Playlist is not empty!")
        
    #вставка песни в начало плейлиста
    def MoveToStart(self, name, file):
        if self.start_song is None:
            self.InsertEmptyPlaylist(name, file)
            # print("First song was inserted in start!")
        else:
            new_song = Song(name, file)
            new_song.next = self.start_song
            self.start_song.prev = new_song
            self.start_song = new_song
            # print("You have inserted new song in start!")
    
    #вставка песни в конец плейлиста
    def AddSong(self, name, file):
        if self.start_song is None:
            self.InsertEmptyPlaylist(name, file)
            # print("First song was inserted in end!")
        else:
            current_song = self.start_song
            while current_song.next is not None:
                current_song = current_song.next
            new_song = Song(name, file)
            current_song.next = new_song
            new_song.prev = current_song
            # print("You have inserted new song in end!")
    
    #вывод песен, из которых состоит плейлист 
    def print_list(self):
        if self.start_song is None:
            pass
            # print("Playlist is empty")
        else:
            current_song = self.start_song
            while current_song is not None:
                # print(current_song.name, current_song.file)
                current_song = current_song.next
                
    def len(self):
        if self.start_song is None:
            # print("Playlist is empty")
            return 0
        else:
            l = 0
            current_song = self.start_song
            while current_song is not None:
                # print(current_song.name, current_song.file)
                current_song = current_song.next
                l = l + 1
            return l
            


        
