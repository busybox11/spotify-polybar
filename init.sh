#!/bin/sh
python3 spoti.py -i

if [ $? -eq 0 ]
then
	echo "Successfully logged in."
	cp .cache-<YOUR-USERNAME> .cache-spotipy
	rm init.sh
else
	echo "Could not connect to Spotify. Check your credentials."
fi
