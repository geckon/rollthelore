"""Simple CLI tool for generating NPCs."""

import click

from loreroll.npc import generate_npc


@click.command()
@click.option('--number', '-n', default=1, help="Number of NPCs to generate.")
def generate(number=1):
    """Generate 'number' of NPCs and print them."""
    for _ in range(number):
        npc = generate_npc()
        print(f'Age: {npc.age}')
        print(f'Race: {npc.race}')
        print(f'Class: {npc.class_}')
        print(f'Appearance: {", ".join(npc.physical)}')
        print(f'Personality: {", ".join(npc.personality)}')
        print()


if __name__ == '__main__':
    generate()
