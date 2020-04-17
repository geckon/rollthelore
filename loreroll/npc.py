"""Module for generating NPCs."""

import random
from collections import namedtuple

from strictyaml import load, Map, Str, Seq


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
    'races': Seq(Str()),
    'classes': Seq(Str()),
    'age': Seq(Str()),
    'physical': Seq(Str()),
    'personality': Seq(Str()),
})


def _read_data():
    """Read NPC data."""
    with open(NPC_FILENAME, 'r') as datafile:
        return load(datafile.read())


NPC_DATA = _read_data()


def generate_npc():
    """Generate and print an NPC."""
    return NPC(    # nosec
        race=str(random.choice(NPC_DATA['races'])),
        class_=str(random.choice(NPC_DATA['classes'])),
        age=str(random.choice(NPC_DATA['age'])),
        physical=[str(random.choice(NPC_DATA['physical'])),
                  str(random.choice(NPC_DATA['physical']))],
        personality=[str(random.choice(NPC_DATA['personality'])),
                     str(random.choice(NPC_DATA['personality']))]
    )
