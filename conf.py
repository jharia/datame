import os

class Config(object):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    FBAPI_APP_ID = os.environ.get('FACEBOOK_APP_ID')
    FBAPI_APP_SECRET = os.environ.get('FACEBOOK_SECRET')
    FBAPI_SCOPE = [
	    'user_about_me',
	    'user_actions.books',
	    'user_actions.fitness',
	    'user_status',
	    'user_friends', 
	    'user_likes',
	    'user_photos',
	    'user_photo_video_tags',
	    'read_friendlists']
