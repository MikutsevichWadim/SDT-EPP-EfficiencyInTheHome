import json
import os

from config import *




class Data:

    template = {
        'levels_successes': [.0,.0,.0],
        'game': {
            'completed': False,
            'show_thanks': False,
            'started': False,
        },
    }

    def load(self):
        
        if not os.path.exists(DATA_FILE):
            self.create_file(self)

        self.data = json.load(open(DATA_FILE, 'r'))

        self.fill_levels_data(self)
    
    def fill_levels_data(self):
        successes = self.data['levels_successes']
        self.passed = list(map(lambda success: success >= LEVEL_SUCCES_TO_PASS, successes))
        self.available = [True,] + self.passed[:-1]

    def save(self):

        json.dump(self.data, open(DATA_FILE, 'w'))

    def level_completed(self, level_i, success):

        self.data['levels_successes'][level_i] = max(
            self.data['levels_successes'][level_i],
            success,
        )
        self.passed[level_i] = (
            self.data['levels_successes'][level_i] >= LEVEL_SUCCES_TO_PASS
            or success >= LEVEL_SUCCES_TO_PASS
        )
        if level_i+1 != LEVELS_COUNT:
            self.available[level_i+1] = self.passed[level_i]

        if (not self.data['game']['completed']
            and self.passed[level_i]
            and level_i+1 == LEVELS_COUNT
        ):
            self.data['game']['completed'] = True
            self.data['game']['show_thanks'] = True

    def reset_progress(self):
        self.data = self.template
        self.fill_levels_data(self)

    def create_file(self):

        json.dump(
            self.template,
            open(DATA_FILE, 'w'),
        )

Data.load(Data)