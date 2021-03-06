from forms import InstagramScraper
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from glasses import *
import matplotlib
#from igDataCompiler import GetUrl

def instagram_scraper(word):
	base_url = "https://api.instagram.com/v1"
	query=word
	url = '{0}/tags/{1}/media/recent?client_id={2}&count=30'.format(base_url, query, client_id)	
	#get_pages(url, 2)
	df = json_normalize(requests.get(url).json()['data'])
	total_posts = len(df)
	total_comments = df['comments.count'].sum()
	total_likes = df['likes.count'].sum()
	return total_likes, 'people like',total_posts, 'recent posts containing #'+word+'!'
	return str(float(total_comments)/float(total_likes))[:5]+'% of Instagram users who have liked posts containing #'+word, 'have commented on a post.'

    #df = df[['user.username','caption.text','tags','comments.count','likes.count',
    #         'filter','type','created_time','user.full_name','user.id','link','location.latitude',
    #         'location.longitude']]
    
    #df.rename(columns={'user.username':'user_name',
    #               'caption.text':'caption_text',
    #               'tags':'hashtags',
    #               'comments.count':'comments_count',
    #               'likes.count':'likes_count',
    #               'filter':'filter',
    #               'created_time':'created_time',
    #               'user.full_name':'full_name',
    #               'user.id':'user_id',
    #               'type':'type',
    #               'link':'link',
    #               'location.latitude':'latitude',
    #               'location.longitude':'longitude'},
    #      inplace=True)
    
    #return df

