"""Module for generating NPCs."""

import hashlib
import json
import os
import random
from collections import namedtuple

from strictyaml import Float, load, Map, Seq, Str


NPC = namedtuple(
    'NPC', [
        'name',
        'age',
        'race',
        'class_',
        'physical',
        'personality',
    ]
)

NPC_FILENAME = os.path.join(os.path.dirname(__file__), 'data/npc.yaml')
NPC_JSON_FILENAME = os.path.join(os.path.dirname(__file__), 'data/npc.json')

NPC_SCHEMA = Map({
    'races': Seq(Map({'v': Str(), 'w': Float()})),
    'classes': Seq(Str()),
    'age': Seq(Map({'v': Str(), 'w': Float()})),
    'physical': Seq(Str()),
    'personality': Seq(Str()),
    'names': Seq(Str()),
})


def _read_data():
    """Read NPC data.

    Parsing StrictYAML turned out to be really slow -> The function attempts
    to read the pre-parsed JSON version. If that fails or if it has been
    generated for a different YAML data version, read the source YAML and try
    and store the data in JSON format for future runs.

    Note that this approach could theoretically cause trouble if the user
    didn't have write permission to the JSON file but if the appropriate JSON
    data is shipped along with YAML source data, this shouldn't be an issue.
    JSON will only be regenerated if YAML changes and if user can modify YAML,
    write permission to JSON should be available as well since these two are in
    the same directory. And even if that somehow isn't true, the consequence is
    "only" a performance drop.

    Still there probably is a better solution - see github issue #53:
    https://github.com/geckon/rollthelore/issues/53
    """
    def _handle_caching_error(operation, error):
        """Print just a warning.

        This is "caching" and we want to continue in any case."""
        print(
            f'WARNING: Could not {operation} the cache JSON file '
            f'("{NPC_JSON_FILENAME}"): {error}'
        )

    with open(NPC_FILENAME, 'r') as yaml_datafile:
        yaml_data = yaml_datafile.read()
        yaml_data_checksum = hashlib.sha512(yaml_data.encode()).hexdigest()

        # Try to read NPC_JSON_FILENAME ("cached"  version).
        try:
            with open(NPC_JSON_FILENAME, 'r') as json_datafile:
                npc_data = json.load(json_datafile)
                checksum = npc_data.pop('yaml_datafile_checksum')
                if checksum == yaml_data_checksum:
                    return npc_data
        except Exception as error:
            _handle_caching_error('read', error)

        # At this point we indeed need to parse the YAML data. Let's do so and
        # try and store the parsed data into a JSON file for future runs.
        npc_data = load(yaml_data, NPC_SCHEMA).data
        try:
            npc_data['yaml_datafile_checksum'] = yaml_data_checksum
            with open(NPC_JSON_FILENAME, 'w') as json_datafile:
                json.dump(npc_data, json_datafile)
        except Exception as error:
            _handle_caching_error('store', error)
        return npc_data


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

    if disallowed:
        for item in disallowed:
            filtered = [x for x in filtered if item not in x]
    return filtered


def _filter_structured_data(data_set, allowed=None, disallowed=None):
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

    if disallowed:
        for item in disallowed:
            filtered = [x for x in filtered if item not in x['v']]
    return filtered


def generate_name():
    return str(random.choice(NPC_DATA['names']))  # nosec


def generate_npc(traits, ages=None, classes=None, races=None):
    """Generate an NPC.

    Traits parameter determines how many physical and personality traits
    will be generated.

    Ages, classes and races are supposed to be sequences of allowed
    ages/classes/races. If None is passed instead of any of these,
    the default set of traits will be used.
    """
    age = str(_weighted_random(ages))

    if classes:
        class_ = str(random.choice(classes))  # nosec
    else:
        class_ = None

    name = generate_name()

    race = str(_weighted_random(races))

    physical = random.choices(NPC_DATA['physical'], k=traits)
    physical = [str(trait) for trait in physical]

    personality = random.choices(NPC_DATA['personality'], k=traits)
    personality = [str(trait) for trait in personality]

    return NPC(
        name=name,
        race=race,
        class_=class_,
        age=age,
        physical=physical,
        personality=personality,
    )


def generate_npcs(number=1, traits=2, filters=None,
                  generate_adventurers=True):
    """Generate a number of NPCs.

    Traits parameter affects how much detailed the generated NPCs will
    be. Non-negative integer is expected, higher number means more
    details. Default is meant to give the best results and with certain
    level of detail the NPCs tend to start getting contradictory traits
    (like fat and slim at the same time).

    Filters are expected to be a dictionary with string keys like
    'races_yes' and 'races_no' and sequence values with traits that are
    supposed to be included and excluded respectively while generating
    NPCs. Properties currently supporting filters are ages, classes and
    races.
    """
    # filter the data
    if filters is None:
        filters = {}

    ages = _filter_structured_data(NPC_DATA['age'],
                                   filters.get('ages_yes'),
                                   filters.get('ages_no'))

    # classes are only generated for adventurers
    if generate_adventurers:
        classes = _filter_string_data(NPC_DATA['classes'],
                                      filters.get('classes_yes'),
                                      filters.get('classes_no'))
    else:
        classes = []

    races = _filter_structured_data(NPC_DATA['races'],
                                    filters.get('races_yes'),
                                    filters.get('races_no'))

    npcs = []
    for _ in range(number):
        npcs.append(generate_npc(traits, ages, classes, races))
    return npcs
