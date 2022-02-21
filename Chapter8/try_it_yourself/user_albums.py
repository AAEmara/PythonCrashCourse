def make_album(artist, title, num_of_songs = None):
    """This function builds a dictionary that describes a music album"""
    album_dic = {'artist': artist, "album title": title}
    if num_of_songs:
        album_dic['num_of_songs'] = num_of_songs

    return album_dic

while True:
    print("\nHello, Please enter the your favorite artist and album:")
    print("(If you want to quit at any time enter 'q').")

    # Prompting user to enter artist name.
    a_name = input("\nArtist name: ")
    if a_name == 'q':
        break
    
    # Prompting user to enter album title name.
    t_name = input("Album title name: ")
    if t_name == 'q':
        break

    # Prompting use to enter no. of songs in the album.
    no_songs = input("Number of songs in the album: ")
    if no_songs == 'q':
        break

    dictionary_output = make_album(artist = a_name,
                                   title = t_name ,
                                   num_of_songs = no_songs)
    print(dictionary_output)
