# RollTheLore
An *unseen servant* providing an *advantage* to DMs/GMs while creating their worlds.

[![Build Status](https://travis-ci.com/geckon/rollthelore.svg?branch=master)](https://travis-ci.com/geckon/rollthelore)

As a DM, have you ever needed to lower the *DC* for the world building skill
check? Did you need to create the right NPC for your players to interact with
and thought you could use a *divine intervention*? Were you out of ideas and
felt like an *inspiration die* or a bit of *luck* was all that you needed? This
tool will probably not fulfill all your *wish*es but it can at least provide
*guidance*.

RollTheLore is a tool from a DM to other DMs out there but it can also help
players as it's supposed to inspire you while not only creating your world,
a shop or a random NPC encounter but it can also be used to help with your
backstories.

As of now it can only randomly create NPCs but I have some ideas for generating
towns as well and who knows? Maybe there will be even more. RollTheLore is not
meant to be a perfect tool but rather a simple one that still can provide very
valuable ideas for your campaigns and stories. At least for me personaly it
works very well as I often need a few simple points I can use as inspiration
and build more fluff around it with both imagination and improvisation.

Sometimes the generated character doesn't make much sense but often that is
exactly the fun part. When I need an NPC for a story I like to *roll* a few of
them and pick one as a basis, then I build on that. It can also be used to
pre-roll a few NPCs in advance and then use them e.g. when your players decide
to enter a shop or address a person you hadn't planned beforehand.

Primarily RollTheLore is intended to be used with DnD 5e but it can very well
serve for other game systems as well. The imagination is what matters the most.

Please note that the tool is under development. Ideas, comments and bug reports are
welcome!

## Installation

```
pip install rollthelore
```

## Usage

```
$ rollnpc --help
Usage: rollnpc.py [OPTIONS]

  Generate 'number' of NPCs and print them.

Options:
  --adventurers / --no-adventurers
                                  Generate adventurers or civilians?
  -a, --age-allowed TEXT          Allowed age(s).
  -A, --age-disallowed TEXT       Disallowed age(s).
  -c, --class-allowed TEXT        Allowed class(es).
  -C, --class-disallowed TEXT     Disallowed class(es).
  --names-only                    Generate only NPC names
  -n, --number INTEGER            Number of NPCs to generate.
  -r, --race-allowed TEXT         Allowed race(s).
  -R, --race-disallowed TEXT      Disallowed race(s).
  -s, --seed TEXT                 Seed number used to generate NPCs. The same
                                  seed will produce the same results.
  -t, --traits INTEGER RANGE      Number of traits generated.  [0<=x<=9]
  --help                          Show this message and exit.
```

## Examples

```
$ rollnpc
Seed used: '3625060903250429453'. Run with '-s 3625060903250429453' to get the same result.

Name: Anfar
Age: older
Race: tabaxi
Class: barbarian
Appearance: artificial ear, subtle ring(s)
Personality: materialistic, dishonest
```

```
$ rollnpc -n3
Seed used: '3098691926526726649'. Run with '-s 3098691926526726649' to get the same result.

Name: Towerlock
Age: middle aged
Race: human
Class: cleric
Appearance: artificial finger(s), bruise(s)
Personality: wretched, bitter

Name: Leska
Age: young
Race: half-elf
Class: sorcerer
Appearance: visible Adam's apple, different leg length
Personality: scary, unreliable

Name: Marius
Age: old
Race: kobold
Class: warlock
Appearance: sexy, distinctive jewelry
Personality: tireless, decadent
```

```
$ rollnpc -n2 -r elf
Seed used: '8069506022788287187'. Run with '-s 8069506022788287187' to get the same result.

Name: Zerma
Age: older
Race: elf (dark - drow)
Class: rogue
Appearance: ugly, dreadlocks
Personality: gruesome, emotional

Name: Ryfar
Age: adult
Race: elf (wood)
Class: cleric
Appearance: light, horn(s)
Personality: childish, determined
```

```
$ rollnpc --traits 1
Seed used: '291255857363596163'. Run with '-s 291255857363596163' to get the same result.

Name: Enidin
Age: adult
Race: aasimar
Class: cleric
Appearance: receding hair
Personality: hardened
```

```
$ rollnpc -t 3
Seed used: '5732868273964053039'. Run with '-s 5732868273964053039' to get the same result.

Name: Letor
Age: older
Race: dragonborn
Class: sorcerer
Appearance: plump, abnormally short, short hair
Personality: bitter, scornful, sloppy
```

```
$ rollnpc --no-adventurers -n 2 -t 1
Seed used: '5305197205526584553'. Run with '-s 5305197205526584553' to get the same result.

Name: Yorjan
Age: adult
Race: tiefling
Appearance: big eyes
Personality: foolish

Name: Nalfar
Age: adult
Race: dragonborn
Appearance: dreadlocks
Personality: perverse

```

### Seeding

Let's say you generated this lovely duo and you want to keep it for the future.

```
$ rollnpc -n2
Seed used: '6095344300345411392'. Run with '-s 6095344300345411392' to get the same result.

Name: Macon
Age: older
Race: half-elf
Class: bard
Appearance: big eyes, muttonchops
Personality: intellectual, secretive

Name: Sirius
Age: very old
Race: human
Class: cleric
Appearance: different hand size, dimple in chin
Personality: speaks silently, hypochondriac
```

You can either save the whole text or just the seed and generate the same
data again like this:

```
$ rollnpc -n2 -s 6095344300345411392
Seed used: '6095344300345411392'. Run with '-s 6095344300345411392' to get the same result.

Name: Macon
Age: older
Race: half-elf
Class: bard
Appearance: big eyes, muttonchops
Personality: intellectual, secretive

Name: Sirius
Age: very old
Race: human
Class: cleric
Appearance: different hand size, dimple in chin
Personality: speaks silently, hypochondriac
```
