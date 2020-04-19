"""Module for generating NPCs."""

import random
from collections import namedtuple

from strictyaml import Float, load, Map, Seq, Str


NPC = namedtuple(
    'NPC', [
        'age',
        'race',
        'class_',
        'physical',
        'personality',
    ]
)

NPC_FILENAME = 'data/npc.yaml'

NPC_SCHEMA = Map({
    'races': Seq(Map({'v': Str(), 'w': Float()})),
    'classes': Seq(Str()),
    'age': Seq(Map({'v': Str(), 'w': Float()})),
    'physical': Seq(Str()),
    'personality': Seq(Str()),
})


def _read_data():
    """Read NPC data."""
    with open(NPC_FILENAME, 'r') as datafile:
        return load(datafile.read(), NPC_SCHEMA)


NPC_DATA = _read_data()


def _weighted_random(data_set):
    """Returns a weighted random option from data_set.

    The data_set needs to be a sequence of dict-like objects with at
    least 'v' (value) and 'w' (weight) keys. Weights need to be
    convertible to float.
    """
    return random.choices(
        [x['v'] for x in data_set],
        [float(x['w']) for x in data_set]
    )[0]


def _filter_string_data(data_set, allowed=(), disallowed=()):
    """Filters the given weighted data according to given filters.

    The data_set needs to be a sequence of string values.
    The allowed and disallowed need to be sequences of strings and
    their contents will be used to filter the values in data_set.

    A data_set item will be a part of the result only if its value
    contains any of the allowed values as a substring unless it also
    contains any of the disallowed values as a substring.

    If allowed sequence is not provided, all items in data_set are
    allowed. If disallowed sequence is not provided, no items are
    filtered out.
    """
    if not allowed and not disallowed:
        return data_set

    if allowed:
        filtered = []
        for item in allowed:
            filtered += [x for x in data_set if item in x]
    else:
        filtered = data_set

    for item in disallowed:
        filtered = [x for x in filtered if item not in x]
    return filtered


def _filter_structured_data(data_set, allowed=(), disallowed=()):
    """Filters the given weighted data according to given filters.

    The data_set needs to be a sequence of dict-like objects with at
    least 'v' (value) key with string values.
    The allowed and disallowed need to be sequences of strings and
    their contents will be used to filter the values in data_set.

    A data_set item will be a part of the result only if its value
    contains any of the allowed values as a substring unless it also
    contains any of the disallowed values as a substring.

    If allowed sequence is not provided, all items in data_set are
    allowed. If disallowed sequence is not provided, no items are
    filtered out.
    """
    if not allowed and not disallowed:
        return data_set

    if allowed:
        filtered = []
        for item in allowed:
            filtered += [x for x in data_set if item in x['v']]
    else:
        filtered = data_set

    for item in disallowed:
        filtered = [x for x in filtered if item not in x['v']]
    return filtered


def generate_npc(ages_yes=None, ages_no=None, classes_yes=None,
                 classes_no=None, races_yes=None, races_no=None, ):
    """Generate and print an NPC."""
    ages = _filter_structured_data(NPC_DATA['age'], ages_yes, ages_no)
    classes = _filter_string_data(NPC_DATA['classes'], classes_yes,
                                  classes_no)
    races = _filter_structured_data(NPC_DATA['races'], races_yes, races_no)

    return NPC(    # nosec
        race=str(_weighted_random(races)),
        class_=str(random.choice(classes)),
        age=str(_weighted_random(ages)),
        physical=[str(random.choice(NPC_DATA['physical'])),
                  str(random.choice(NPC_DATA['physical']))],
        personality=[str(random.choice(NPC_DATA['personality'])),
                     str(random.choice(NPC_DATA['personality']))]
    )
