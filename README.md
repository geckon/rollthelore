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
Usage: rollnpc [OPTIONS]

  Generate 'number' of NPCs and print them.

Options:
  -a, --age-allowed TEXT       Allowed age(s).
  -A, --age-disallowed TEXT    Disallowed age(s).
  -c, --class-allowed TEXT     Allowed class(es).
  -C, --class-disallowed TEXT  Disallowed class(es).
  -d, --detail-level INTEGER   Amount of details generated (one or higher).
  -n, --number INTEGER         Number of NPCs to generate.
  -r, --race-allowed TEXT      Allowed race(s).
  -R, --race-disallowed TEXT   Disallowed race(s).
  --help                       Show this message and exit.
```

## Examples

```
$ rollnpc
Name: Zaniel
Age: older
Race: tabaxi
Class: monk
Appearance: deaf, blind
Personality: discouraging, disrespectful
```

```
$ rollnpc -n3
Name: Iseult
Age: old
Race: dragonborn
Class: fighter
Appearance: cain, moustache
Personality: courteous, foolish

Name: Nyssa
Age: adult
Race: dragonborn
Class: barbarian
Appearance: hook instead of a hand, underbite
Personality: miserable, suspicious

Name: Briallan
Age: older
Race: human
Class: wizard
Appearance: skinny, tall
Personality: honorable, stylish
```

```
$ rollnpc -n2 -r elf
Name: Evadne
Age: young
Race: elf (wood)
Class: ranger
Appearance: silent voice, cute
Personality: dependable, honorable

Name: Ianthe
Age: young
Race: half-elf
Class: warlock
Appearance: handlebar beard, fire-burnt skin
Personality: witty, organized
```

```
$ rollnpc --detail-level 1
Name: Séverin
Age: young
Race: tiefling
Appearance: mute
Personality: happy
```

```
$ rollnpc --detail-level 3
Name: Korbin
Age: adult
Race: gnome (forest)
Class: ranger
Appearance: big nose, scarred, sinewy
Personality: grim, regretful, naive

```

### Seeding

Let's say you generated this lovely duo and you want to keep it for the future.

```
$ rollnpc.py -n2
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
$ rollnpc.py -n2 -s 6095344300345411392
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
