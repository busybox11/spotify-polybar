import sys
import spotipy
import spotipy.util as util
import spoti as cred

token = spotipy.util.prompt_for_user_token(
    cred.username, cred.scope, cred.client_id, cred.client_secret, cred.redirect_uri)

def return_song():
    if current_song != None and current_song != "Spotify":
        print(current_song['item']['name'] + ' - ' + current_song['item']['artists'][0]['name'])
    else:
        if current_song == None:
            print('No song currently playing')
        else:
            print(current_song)

if token:
    sp = spotipy.Spotify(auth=token)
    try:
        current_song = sp.currently_playing()
    except:
        current_song = "Spotify"
    return_song()
else:
    print("Can't get token for", username)
