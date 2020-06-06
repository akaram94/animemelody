from django.core.management.base import BaseCommand, CommandError
from shows.models import Show, Theme
import datetime
import requests
import json
import time

class Command(BaseCommand):
    help = '''
    Used to import english show names from the Jikan API (rate limit of 2s)
    '''

    def handle(self, *args, **options):
        feed_url = 'https://api.jikan.moe/v3/anime/'

        message = 'Getting english names...'

        shows = Show.objects.filter(english_name='')

        print(message)

        show_count = 0
            
        # Retrieve all data from each endpoint
        for show in shows:
            current_url = feed_url + str(show.mal_id)
            time.sleep(2)
            r = requests.get(current_url)
            data = r.json()
            if data['title_english']:
                title_english = str(data['title_english'])
            else:
                title_english = None
            show.english_name = title_english
            show.save()
            show_count = show_count + 1
            print(show_count)

        print('----------------------------------------------------------')
        print('Show Count: ' + str(show_count))
        print('Successfully updated.')











