# Defining a function that accepts
def make_album(artist, title, num_of_songs = None):
    """This function builds a dictionary that describes a music album"""
    album_dic = {'artist': artist, "album title": title}
    if num_of_songs:
        album_dic['num_of_songs'] = num_of_songs

    return album_dic
# Filling all arguments with values.
print(make_album('adele', '25', 11))
print(make_album('frank sinatra', 'my way'))