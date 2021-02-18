import datetime
import spotipy
import spotipy.oauth2 as oauth2
import numpy as np

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

today = datetime.date.today()
start_time = str(today)

client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')

auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

token = auth.get_access_token()
spotify = spotipy.Spotify(auth=token)

artists = ['6LACK', 'blink-182', 'Sum 41', 'Flume', 'Glass Animals', 
			'Dave', 'Jimi Hendrix', 'Zanksi', 'Freddie Gibbs']

def get_artist(name):
	artist_detail = spotify.search(
		artist, 
		limit=1, 
		offset=0, 
		type='artist', 
		market=None
	)

	artist_id = artist_detail['artists']['items'][0]['id']
	artist_name = artist_detail['artists']['items'][0]['name']
	score = artist_detail['artists']['items'][0]['popularity']

	if not artist_name == artist:
		print('exact match not found')
		frauds = spotify.search(
			artist, 
			limit=5, 
			offset=0, 
			type='artist', 
			market=None
		)
		for fraud in frauds['artists']['items']:
			name = fraud['name']
			if name == artist:
				artist_id = fraud['id']
				artist_name = fraud['name']
				score = fraud['popularity']
				break

	return artist_id, artist_name, score

def get_artist_albums(artist_id):
	return spotify.artist_albums(
		artist_id, 
		album_type='album', 
		limit=10, offset=0
	)

def get_album_tracks(album_id):
	return spotify.album_tracks(
		album_id, 
		limit=15, 
		offset=0, 
		market=None
	)

def get_track_details(track_id):
	return spotify.track(track_id)

def get_top_three_tracks(album_tracks):
	ranks = []
	top_three = []

	for album_track in album_tracks['items']:
		track = get_track_details(album_track['id'])
		popularity = track['popularity']
		ranks.append(popularity)

	arr = np.array(ranks)
	output = arr.argsort()[-3:][::-1]

	for pos in output:
		track_id = album_tracks['items'][pos]['id']
		track = spotify.track(track_id)
		track_name = track['name']
		track_pop = track['popularity']
		track_data =  {
			'popularity': track_pop,
			'id': track_id,
			'name': track_name
		}
		top_three.append(track_data)

	return top_three















