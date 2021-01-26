class Song:

  def __init__(self, title):
      self._title = title
      self._next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self._title
    
  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self._title = title


  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self._next_song


  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self._next_song = next_title


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return str(self._title)


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return str(f'{self.get_title} -> {self.get_next_song.get_title}')

song = Song('yes')
print(song._title)
print(song.get_title)