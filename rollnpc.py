#!/usr/bin/env python

"""Simple CLI tool for generating NPCs."""

import click

from loreroll.npc import generate_npc


@click.command()
@click.option('--age-allowed', '-a', 'ages_yes', multiple=True,
              help="Allowed age(s).")
@click.option('--age-disallowed', '-A', 'ages_no', multiple=True,
              help="Disallowed age(s).")
@click.option('--class-allowed', '-c', 'classes_yes', multiple=True,
              help="Allowed class(es).")
@click.option('--class-disallowed', '-C', 'classes_no', multiple=True,
              help="Disallowed class(es).")
@click.option('--number', '-n', default=1,
              help="Number of NPCs to generate.")
@click.option('--race-allowed', '-r', 'races_yes', multiple=True,
              help="Allowed race(s).")
@click.option('--race-disallowed', '-R', 'races_no', multiple=True,
              help="Disallowed race(s).")
def generate(number=1, ages_yes=None, ages_no=None, classes_yes=None,
             classes_no=None, races_yes=None, races_no=None):
    """Generate 'number' of NPCs and print them."""
    for _ in range(number):
        npc = generate_npc(ages_yes=ages_yes, ages_no=ages_no,
                           classes_yes=classes_yes, classes_no=classes_no,
                           races_yes=races_yes, races_no=races_no)
        print(f'Age: {npc.age}')
        print(f'Race: {npc.race}')
        print(f'Class: {npc.class_}')
        print(f'Appearance: {", ".join(npc.physical)}')
        print(f'Personality: {", ".join(npc.personality)}')
        print()


if __name__ == '__main__':
    generate()
