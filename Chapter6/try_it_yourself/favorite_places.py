# Storing people names and their favorite places.
favorite_places = {
    'sawah': ['al falah', 'princess', 'karam al sham'],
    'alaa': ['anwar masoud', 'balbaa', 'zafir'],
    'habiba': ['al falah', 'nutopia', 'al maqam'],
    }

# Looping through people and their favorite places.
for name , places_list in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places_list:
        print(f"\t {place.title()}")
