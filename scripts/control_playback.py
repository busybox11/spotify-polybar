import sys
import spotipy
import spotipy.util as util
import spoti as cred

token = spotipy.util.prompt_for_user_token(
    cred.username, cred.scope, cred.client_id, cred.client_secret, cred.redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    try:
        if sys.argv[1] == '-n' or sys.argv[1] == '--next':
            sp.next_track()
        elif sys.argv[1] == '-p' or sys.argv[1] == '--previous':
            sp.previous_track()
    except:
        sys.exit("Cannot control playback")
else:
    print("Can't get token for", username)
