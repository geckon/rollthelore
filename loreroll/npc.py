"""Module for generating NPCs."""

import random
from collections import namedtuple

from strictyaml import Float, load, Map, MapPattern, Seq, Str


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


def generate_npc():
    """Generate and print an NPC."""
    return NPC(    # nosec
        race=str(_weighted_random(NPC_DATA['races'])),
        class_=str(random.choice(NPC_DATA['classes'])),
        age=str(_weighted_random(NPC_DATA['age'])),
        physical=[str(random.choice(NPC_DATA['physical'])),
                  str(random.choice(NPC_DATA['physical']))],
        personality=[str(random.choice(NPC_DATA['personality'])),
                     str(random.choice(NPC_DATA['personality']))]
    )
