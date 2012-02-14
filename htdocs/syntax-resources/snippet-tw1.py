""" The most basic form with ToscaWidgets 1

Stable, but no new development. """

import tw.forms as twf

movie_form = twf.TableForm(
    'movie_form',
    action='save_movie',
    children=[
        twf.HiddenField('id'),
        twf.TextField('title'),
        twf.TextField('year', size=4),
        twf.CalendarDatePicker('release_date'),
        twf.SingleSelectField('genera', options=[
            '', 'Action', 'Comedy', 'Other'
        ]),
        twf.TextArea('description'),
    ]
)
