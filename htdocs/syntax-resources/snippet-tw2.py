""" The most basic form with ToscaWidgets 2 """

import tw2.core as twc
import tw2.forms as twf

class MovieForm(twf.FormPage):
    title = 'Movie'
    class child(twf.TableForm):
        id = twf.HiddenField()
        title = twf.TextField(validator=twc.Required)
        director = twf.TextField()
        genres = twf.CheckBoxList(options=[
            'Action', 'Comedy', 'Romance', 'Sci-fi'
        ])
        class cast(twf.GridLayout):
            extra_reps = 5
            character = twf.TextField()
            actor = twf.TextField()
