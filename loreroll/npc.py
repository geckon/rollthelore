"""Module for generating NPCs."""

import random
# from collections import namedtuple

from strictyaml import load, Map, Str, Seq


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
    print(random.choice(NPC_DATA['races']))
    print(random.choice(NPC_DATA['classes']))
    print(random.choice(NPC_DATA['age']))
    print(random.choice(NPC_DATA['physical']))
    print(random.choice(NPC_DATA['personality']))
