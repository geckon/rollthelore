"""Tests for npc.py"""

from loreroll.npc import (
    _filter_string_data,
    _filter_structured_data,
    _weighted_random,
    generate_npc,
    generate_npcs,
    NPC_DATA,
)


def _ignore_weights(data_set):
    """Take only 'v' values from the given weighted data set."""
    return [x['v'] for x in data_set]


# Lists of all RollTheLore data
ALL_NAMES = NPC_DATA['names']
ALL_RACES = _ignore_weights(NPC_DATA['races'])
ALL_CLASSES = NPC_DATA['classes']
ALL_AGES = _ignore_weights(NPC_DATA['age'])
ALL_PHYSICAL = NPC_DATA['physical']
ALL_PERSONALITY = NPC_DATA['personality']

# Fellowship of the Ring members as a data set with probabilities
LOTR_DATA_SET = [
    {'v': 'Gandalf', 'w': '1'},
    {'v': 'Frodo', 'w': 42},
    {'v': 'Sam', 'w': 11.0},
    {'v': 'Aragorn', 'w': '4.2'},
    {'v': 'Legolas', 'w': 5.1},
    {'v': 'Gimli', 'w': '6.0'},
    {'v': 'Pippin', 'w': 7},
    {'v': 'Merry', 'w': '11'},
    {'v': 'Boromir', 'w': '1.0'},
    {'v': 'Sauron', 'w': 0},
    {'v': 'Saruman', 'w': '0'},
]

# Fellowship of the Ring members as a list
LOTR_LIST = [
    'Gandalf',
    'Frodo',
    'Sam',
    'Aragorn',
    'Legolas',
    'Gimli',
    'Pippin',
    'Merry',
    'Boromir',
]

# Only hobbit members of the Fellowship of the Ring as a data set
HOBBITS_DATA_SET = [
    {'v': 'Frodo', 'w': 42},
    {'v': 'Sam', 'w': 11.0},
    {'v': 'Pippin', 'w': 7},
    {'v': 'Merry', 'w': '11'},
]
# Only hobbit members of the Fellowship of the Ring
HOBBITS_LIST = ['Frodo', 'Sam', 'Pippin', 'Merry']


def test_weighted_random_foo_only():
    """Test _weighted_random() function."""
    # All the following data sets should only give 'foo' while passed to
    # _weighted_random() but they may also contain other data.
    FOO_ONLY_DATA_SETS = (
        (
            {'v': 'foo', 'w': '1'},
            {'v': 'bar', 'w': '0'},
        ),
        (
            {'v': 'foo', 'w': '1.0'},
            {'v': 'bar', 'w': '0'},
        ),
        (
            {'v': 'foo', 'w': '1'},
            {'v': 'bar', 'w': '0.0'},
            {'v': 'foobar', 'w': '0'},
        ),
        (
            {'v': 'foo', 'w': '1'},
        ),
        (
            {'v': 'foo', 'w': '1.0'},
        ),
        (
            {'v': 'foo', 'w': '5'},
            {'v': 'foo', 'w': '17'},
        ),
        (
            {'v': 'bar', 'w': 0},
            {'v': 'foo', 'w': 1},
            {'v': 'foo', 'w': '2'},
        ),
    )

    for data_set in FOO_ONLY_DATA_SETS:
        for _ in range(100):
            assert _weighted_random(data_set) == 'foo'


def test_weighted_random_lotr():
    """Test _weighted_random() function."""
    for _ in range(100):
        assert _weighted_random(LOTR_DATA_SET) in LOTR_LIST


def test_filter_string_data():
    """Test _filter_string_data() function."""
    # Trivial filters
    assert _filter_string_data(LOTR_LIST) == LOTR_LIST
    assert _filter_string_data(LOTR_LIST, (), ()) == LOTR_LIST
    assert _filter_string_data(LOTR_LIST, None, ()) == LOTR_LIST
    assert _filter_string_data(LOTR_LIST, (), None) == LOTR_LIST
    assert _filter_string_data(LOTR_LIST, LOTR_LIST) == LOTR_LIST
    assert _filter_string_data(LOTR_LIST, LOTR_LIST, LOTR_LIST) == []
    assert _filter_string_data((), LOTR_LIST) == []

    # Non-members
    assert _filter_string_data(LOTR_LIST, (), ('Sauron',)) == LOTR_LIST
    assert _filter_string_data(LOTR_LIST, ('Sauron',)) == []

    # Limit to some members only
    assert _filter_string_data(LOTR_LIST, ('Frodo',)) == ['Frodo']
    assert _filter_string_data(LOTR_LIST, HOBBITS_LIST) == HOBBITS_LIST

    # Allowing and disallowing counts as disallowing
    assert _filter_string_data(
        LOTR_LIST, HOBBITS_LIST + ['Gimli'], ('Gimli',)
    ) == HOBBITS_LIST


def test_filter_structured_data():
    """Test _filter_structured_data() function."""
    # Trivial filters
    assert _filter_structured_data(LOTR_DATA_SET) == LOTR_DATA_SET
    assert _filter_structured_data(LOTR_DATA_SET, (), ()) == LOTR_DATA_SET
    assert _filter_structured_data(LOTR_DATA_SET, None, ()) == LOTR_DATA_SET
    assert _filter_structured_data(LOTR_DATA_SET, (), None) == LOTR_DATA_SET
    assert _filter_structured_data(LOTR_DATA_SET, LOTR_LIST, LOTR_LIST) == []
    assert _filter_structured_data((), LOTR_LIST) == []

    # Non-members
    assert _ignore_weights(
        _filter_structured_data(LOTR_DATA_SET, (), ('Sauron', 'Saruman'))
    ) == LOTR_LIST

    # Limit to some members only
    assert _filter_structured_data(
        LOTR_DATA_SET, HOBBITS_LIST
    ) == HOBBITS_DATA_SET
    assert _ignore_weights(
        _filter_structured_data(LOTR_DATA_SET, HOBBITS_LIST)
    ) == HOBBITS_LIST

    # Allowing and disallowing counts as disallowing
    assert _filter_structured_data(
        LOTR_DATA_SET, HOBBITS_LIST + ['Gimli'], ('Gimli',)
    ) == HOBBITS_DATA_SET


def _assert_npc_data_from_the_data_file(npc):
    """Test that the given NPC is generated from RollTheLore data set.

    Check that all the NPC values come from the RollTheLore data files.
    """
    assert npc.name in ALL_NAMES
    assert npc.age in ALL_AGES
    assert npc.race in ALL_RACES
    if npc.class_ is not None:
        assert npc.class_ in ALL_CLASSES
    for trait in npc.physical:
        assert trait in ALL_PHYSICAL
    for trait in npc.personality:
        assert trait in ALL_PERSONALITY


def test_generate_npcs():
    """Test generate_npcs() function."""
    npcs_count = 50

    # Defaults
    for npc in generate_npcs(npcs_count):
        _assert_npc_data_from_the_data_file(npc)

    # Detail level 1
    for npc in generate_npcs(npcs_count, detail_level=1):
        assert npc.class_ is None
        _assert_npc_data_from_the_data_file(npc)

    # Various default levels (incl. 1 to check the traits count)
    for detail_level in range(1, 5):
        for npc in generate_npcs(npcs_count, detail_level):
            assert len(npc.physical) == detail_level
            assert len(npc.personality) == detail_level
            _assert_npc_data_from_the_data_file(npc)


def test_generate_npcs_filters():
    """Test generate_npcs() function filters."""
    npcs_count = 50

    # Allow just one race to test positive filter
    for npc in generate_npcs(npcs_count,
                             filters={'races_yes': ['dragonborn']}):
        assert npc.race == 'dragonborn'
        _assert_npc_data_from_the_data_file(npc)

    # Allow two classes and disallow one of them to test negative filter
    for npc in generate_npcs(npcs_count,
                             filters={'classes_yes': ['bard', 'fighter'],
                                      'classes_no': ['fighter']}):
        assert npc.class_ == 'bard'
        _assert_npc_data_from_the_data_file(npc)

    # Filters work for substrings too
    for npc in generate_npcs(npcs_count,
                             filters={'ages_yes': ['young']}):
        assert npc.age == 'young' or npc.age == 'very young'
        _assert_npc_data_from_the_data_file(npc)

    # Negative filters as well respect substrings
    for npc in generate_npcs(npcs_count,
                             filters={'races_no': ['a']}):
        assert 'a' not in npc.race
        _assert_npc_data_from_the_data_file(npc)

    # Data not included in the RollTheLore data can't be added by filters
    for npc in generate_npcs(npcs_count,
                             filters={'races_yes': ['kobold', 'not-a-race']}):
        assert npc.race == 'kobold'
        _assert_npc_data_from_the_data_file(npc)
