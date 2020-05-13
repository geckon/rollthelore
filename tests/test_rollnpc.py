"""Tests for rollnpc.py"""

from loreroll.npc import NPC
from rollnpc import print_npc

NPCS = (
    NPC(
        'Sirius',
        'old',
        'dwarf (hill)',
        'barbarian',
        ('spots', 'hook instead of a hand'),
        ('funny', 'rude')
    ),
    NPC(
        'Ryfar',
        'middle aged',
        'dragonborn',
        'bard',
        ('leg missing', 'sinewy', 'subtle circlet'),
        ('tense', 'opportunistic', 'articulate')
    ),
    NPC(
        'Yve',
        'very old',
        'aasimar',
        None,
        ('tall',),
        ('desperate',)
    )
)

NPCS_TEXT = (
    (
        'Name: Sirius\n'
        'Age: old\n'
        'Race: dwarf (hill)\n'
        'Class: barbarian\n'
        'Appearance: spots, hook instead of a hand\n'
        'Personality: funny, rude\n\n'
    ),
    (
        'Name: Ryfar\n'
        'Age: middle aged\n'
        'Race: dragonborn\n'
        'Class: bard\n'
        'Appearance: leg missing, sinewy, subtle circlet\n'
        'Personality: tense, opportunistic, articulate\n\n'
    ),
    (
        'Name: Yve\n'
        'Age: very old\n'
        'Race: aasimar\n'
        'Appearance: tall\n'
        'Personality: desperate\n\n'
    )
)


def test_print_npc(capsys):
    """Test the printing function with a few examples."""
    for npc in zip(NPCS, NPCS_TEXT):
        print_npc(npc[0])
        out, err = capsys.readouterr()
        assert out == npc[1]
