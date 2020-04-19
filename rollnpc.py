#!/usr/bin/env python

"""Simple CLI tool for generating NPCs."""

import click

from loreroll.npc import generate_npc


@click.command()
@click.option('--number', '-n', default=1,
              help="Number of NPCs to generate.")
@click.option('--race-allowed', '-r', 'races_yes', multiple=True,
              help="Allowed race(s).")
@click.option('--race-disallowed', '-R', 'races_no', multiple=True,
              help="Disallowed race(s).")
def generate(number=1, races_yes=None, races_no=None):
    """Generate 'number' of NPCs and print them."""
    for _ in range(number):
        npc = generate_npc(races_yes=races_yes, races_no=races_no)
        print(f'Age: {npc.age}')
        print(f'Race: {npc.race}')
        print(f'Class: {npc.class_}')
        print(f'Appearance: {", ".join(npc.physical)}')
        print(f'Personality: {", ".join(npc.personality)}')
        print()


if __name__ == '__main__':
    generate()
