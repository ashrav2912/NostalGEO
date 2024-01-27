import geocoder

def get_curr_loc():
    g = geocoder.ip('me')
    return g.latlng

print(get_curr_loc())