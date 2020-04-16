import click

from loreroll.npc import generate_npc

@click.command()
@click.option('--number', '-n', default=1, help="Number of NPCs to generate.")
def generate(number=1):
    """Generate 'number' of NPCs and print them."""
    for _ in range(number):
        generate_npc()
        print()

if __name__ == '__main__':
    generate()
