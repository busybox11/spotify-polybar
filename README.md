# spotify-polybar

The polybar theme used here is a slightly modified version of the 2nd theme of [adi1090x/polybar-themes](https://github.com/adi1090x/polybar-themes).

## **Dependencies**
- python3 (pip3)
- spotipy (`pip3 install spotipy`)

## **What modifications are required ?**

You should have a declared app in Spotify's developer dashboard to obtain a `Client ID`.

*How to do it :*
As I said, the first thing is to create a Client ID (`Create a Client ID` button) on [Spotify's developer dashboard](https://developer.spotify.com/dashboard/applications).
Type your app's name in the `App or Hardware name` text field, and its description on the `App or Hardware description` text field. In the `What are you building ?` section, indicate the platform which you are building the app for, then click on the `NEXT` button. Answer to the commercial integration question, and continue. If necessary, fill the form and check all the boxes at the 3rd stage and you're ready to go. Your app is declared in Spotify's developer dashboard !

Now that you have your app, you have some modifications to do in one file : `scripts/spoti.py`.

Edit those values :

- `your-client-id` by your Client ID available on your app's panel,
- `your-client-secret` by your `Client Secret` available by clicking on the `Show Client Secret` button situated on the same webpage as your client ID,
- `your-spotify-username` by your Spotify Username. ([How to find it?](https://community.spotify.com/t5/Accounts/How-do-i-find-my-username-when-using-Facebook-login/m-p/1268764#M183681))

Let's go back in our app's panel. Click on the green `Edit settings` button situated on the top of the page, then in the `Redirect URIs` text field, add `http://localhost/`. ***ATTENTION*** : this field is case sensitive, you should **IMPERATIVELY** write the exact same thing ! Then click on the `SAVE` button on the very bottom of the form. Your app is declared and ready to use !

Now it's time to test your changes. Run the `init.sh` (in `scripts` folder). If your credentials are good, you're ready to rock. If they're not, check and edit them.

Now that the script is working, you have to tell your OS to run the `cron.sh` every hour.
We're going to do this with `crontab`, but use whatever method you want, as long as it runs the script every hour.
Run this command : `crontab -e`, then choose your favorite text editor (just follow the instrictions).
Now that you're in the file, add this line at the bottom of it : `@hourly ~/.config/polybar/scripts/cron.sh` (change the script location if needed).
Run it once to make sure that everything works, if it does, the setup is finished. You can now use this polybar config !

(Tip / reminder : launch polybar using the `launch.sh` script located in `~/.config/polybar` (the location may not be the same as yours depending of your configuration).
