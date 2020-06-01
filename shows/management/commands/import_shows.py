from django.core.management.base import BaseCommand, CommandError
from shows.models import Show, Theme
import datetime
import requests
import json

class Command(BaseCommand):
    help = '''
    Used to import shows and themes from the themes.moe API (e.g. https://themes.moe/api/seasons/2018 or https://themes.moe/api/seasons/60s)
    '''

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            '--all',
            help="Get all themes until current year."
        )

    def handle(self, *args, **options):
        feed_url = 'https://themes.moe/api/seasons/'
        current_year = datetime.datetime.now().year
        years = [str(current_year)]

        message = 'Getting data for current year.'

        if options['all']:
            message = 'Getting data for every year.'
            years = ['60s', '70s', '80s', '90s']
            # Append all current years to list
            for n in range(2000, current_year + 1):
                years.append(str(n))

        print(message)

        show_count = 0
        theme_count = 0
            
        # Retrieve all data from each endpoint
        for year in years:
            current_url = feed_url + year
            r = requests.get(current_url)
            data = r.json()
            for show in data:
                mal = int(show['malID'])
                name = show['name']
                year = int(show['year'])
                season = show['season']
                themes = show['themes']

                show, created = Show.objects.get_or_create(
                    mal_id = mal,
                    defaults = {
                        'mal_id': mal,
                        'name': name,
                        'year': year,
                        'season': season
                    }
                )

                show_count = show_count + 1

                for theme in themes:
                    theme_type = theme['themeType']
                    theme_name = theme['themeName']
                    theme_mirror_url = theme['mirror']['mirrorURL']
                    theme_priority = theme['mirror']['priority']
                    theme_notes = theme['mirror']['notes']

                    theme, created = Theme.objects.get_or_create(
                        name=theme_name,
                        theme_type=theme_type,
                        show=show,
                        defaults = {
                            'name': theme_name,
                            'show': show,
                            'theme_type': theme_type,
                            'url': theme_mirror_url,
                            'priority': theme_priority,
                            'notes': theme_notes
                        }
                    )

                    theme_count = theme_count + 1

        print('----------------------------------------------------------')
        print('Show Count: ' + str(show_count))
        print('Theme Count: ' + str(theme_count))
        print('Successfully updated.')











