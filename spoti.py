import sys
import spotipy
import spotipy.util as util

client_id = "your-client-id"
client_secret = "your-client-secret"
redirect_uri = "http://localhost/"
username = "your-spotify-username"
scope = "user-read-currently-playing user-modify-playback-state"

if len(sys.argv) > 1:
	if sys.argv[1] == "-i" or sys.argv[1] == "--init":
		token = spotipy.util.prompt_for_user_token(
			username, scope, client_id, client_secret, redirect_uri)

		if token:
			sp = spotipy.Spotify(auth=token)
			print("Successfully connected")
			sys.exit(0)
		else:
			print("Can't connect to this account (Username: )", username)
			sys.exit(1)
