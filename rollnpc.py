#!/usr/bin/env python

"""Simple CLI tool for generating NPCs."""

import random
import sys

import click

from loreroll.npc import generate_name, generate_npcs


def print_npc(npc):
    """Print the given NPC."""
    print(f'Name: {npc.name}')
    print(f'Age: {npc.age}')
    print(f'Race: {npc.race}')
    if npc.class_:
        print(f'Class: {npc.class_}')
    if npc.physical:
        print(f'Appearance: {", ".join(npc.physical)}')
    if npc.personality:
        print(f'Personality: {", ".join(npc.personality)}')
    print()


# pylint: disable=too-many-arguments
@click.command()
@click.option('--adventurers/--no-adventurers', default=True,
              help='Generate adventurers or civilians?')
@click.option('--age-allowed', '-a', 'ages_yes', multiple=True,
              help='Allowed age(s).')
@click.option('--age-disallowed', '-A', 'ages_no', multiple=True,
              help='Disallowed age(s).')
@click.option('--class-allowed', '-c', 'classes_yes', multiple=True,
              help='Allowed class(es).')
@click.option('--class-disallowed', '-C', 'classes_no', multiple=True,
              help='Disallowed class(es).')
@click.option('--names-only', is_flag=True, default=False,
              help='Generate only NPC names')
@click.option('--number', '-n', default=1,
              help='Number of NPCs to generate.')
@click.option('--race-allowed', '-r', 'races_yes', multiple=True,
              help='Allowed race(s).')
@click.option('--race-disallowed', '-R', 'races_no', multiple=True,
              help='Disallowed race(s).')
@click.option('--seed', '-s', 'seed', default=None,
              help='Seed number used to generate NPCs. The same seed will '
                   'produce the same results.')
@click.option('--traits', '-t', 'traits', type=click.IntRange(0, 9),
              default=2, help='Number of traits generated.')
def generate(adventurers, ages_yes, ages_no, classes_yes, classes_no,
             names_only, number, races_yes, races_no, seed, traits):
    """Generate 'number' of NPCs and print them."""
    filters = {
        'ages_no': ages_no,
        'ages_yes': ages_yes,
        'classes_no': classes_no,
        'classes_yes': classes_yes,
        'races_no': races_no,
        'races_yes': races_yes,
    }

    # Seed properly - use either the value from command line or seed randomly.
    if seed is None:
        # String needed instead of int because command line options are also
        # strings.
        seed = str(random.randrange(sys.maxsize))  # nosec
    random.seed(seed)
    print(f"Seed used: '{seed}'. Run with '-s {seed}' to get the same "
          f"result.\n")

    if names_only:
        for _ in range(number):
            print(generate_name())
        return

    npcs = generate_npcs(
        number,
        traits=traits,
        filters=filters,
        generate_adventurers=adventurers
    )

    for npc in npcs:
        print_npc(npc)
# pylint: enable=too-many-arguments


if __name__ == '__main__':
    generate()  # pylint: disable=no-value-for-parameter
