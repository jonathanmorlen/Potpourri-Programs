import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# globals
scope = 'playlist-modify-private playlist-modify-public user-library-read playlist-read-private'
sp = spotipy.Spotify()


def credentials():
    global sp, scope
    client_id = '********'      # client id from Spotify API here
    client_secret = '********'  # client secret from Spotify API here
    redirect_uri = 'https://google.com'
    cache = '.cache'
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            cache_path=cache
        )
    )


# returns all playlist information available on all public, private, and collaborative playlists
def get_playlists():
    user_id = sp.current_user()['display_name']
    results = sp.user_playlists(user=user_id)
    playlists = results['items']
    while results['next']:
        results = sp.next(results)
        playlists.extend(results['items'])
    return playlists


# returns a list of all playlist names
def get_playlist_names():
    return [playlist['name'] for playlist in get_playlists()]


# given a playlist name, returns the id of a playlist
def get_playlist_id_by_name(playlist_name):
    for playlist in get_playlists():
        if playlist['name'] == playlist_name:
            return playlist['uri']


# creates a private playlist with a given name
def create_playlist(playlist_name):
    sp.user_playlist_create(
        user=sp.current_user()['display_name'],
        name=playlist_name,
        public=True,
        description=f"Playlist of all liked tracks. Last updated: {datetime.today().strftime('%m/%d/%Y @ %I:%M%p')}"
    )


# clear playlist of all tracks
def clear_playlist(pid):
    sp.playlist_replace_items(pid, [])


# get playlist ID, creating a new playlist if one does not exist
def get_playlist_id(playlist_name):
    if playlist_name not in get_playlist_names():
        create_playlist(playlist_name)
    else:
        choice = input("Are you sure you want to completely overwrite playlist '" + playlist_name + "'? (Y/N):\t")
        if choice not in ['Y', 'y', 'yes']:
            print("Quitting...")
            exit()
    return get_playlist_id_by_name(playlist_name)


def get_liked_tracks():
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def populate_playlist(pid, tracks):
    clear_playlist(pid)
    sp.playlist_change_details(
        playlist_id=pid.split(':')[2],
        description=f"Playlist of all liked tracks. Last updated: {datetime.today().strftime('%m/%d/%Y @ %I:%M%p')}"
    )
    split_tracks = [[track['track']['uri'] for track in tracks[i:i + 100]] for i in range(0, len(tracks), 100)]
    for split in split_tracks:
        sp.playlist_add_items(playlist_id=pid, items=split)


if __name__ == '__main__':
    credentials()
    name = input('What would you like to name the playlist? Or if you would like to update an existing playlist, what is it\'s name?:\t')
    playlist_id = get_playlist_id(name)
    liked_tracks = get_liked_tracks()
    populate_playlist(playlist_id, liked_tracks)
