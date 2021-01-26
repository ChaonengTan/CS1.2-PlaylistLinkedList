from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    newSong = Song(title)
    newSong.set_next_song = self.__first_song
    self.__first_song = newSong


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_node = self.__first_song
    counter = 0 
    while current_node.get_next_song != None:
      counter = counter + 1
      if current_node.get_title == title:
        return counter
      current_node = current_node.get_next_song
      


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    pass



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    current_node = self.__first_song
    counter = 0 
    while current_node.get_next_song != None:
      counter = counter + 1
      current_node = current_node.get_next_song
    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_node = self.__first_song
    counter = 0 
    while current_node.get_next_song != None:
      counter = counter + 1
      print(f'{counter}. {current_node.get_title}')
      current_node = current_node.get_next_song

  