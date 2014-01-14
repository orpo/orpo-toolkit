import json
import urllib2

def get_vimeo_thumbnail(vimeo_video_id, size='large'):
	"""Fetches a thumbnail URL for a given video (and size) from Vimeo metadata API"""

	assert size in ['small', 'medium', 'large'], 'You must specify a valid size! small/medium/large'

	req = urllib2.urlopen('http://vimeo.com/api/v2/video/%s.json' % vimeo_video_id)

	try:
		data = json.loads(req.read())[0]
	except (ValueError, IndexError):
		return None

	key = 'thumbnail_%s' % size

	if not key in data:
		return None

	return data[key]
