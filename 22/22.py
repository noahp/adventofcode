import re, sys, itertools, copy

# name, cost, damage, heal, manaCharge, armor, effectLength
spells = [
    ('MagicMissle',      53, 4, 0, 0, 0, 0)
    ('Drain',            53, 4, 0, 0, 0, 0)
    ('Shield',           53, 4, 0, 0, 0, 0)
    ('Poison',           53, 4, 0, 0, 0, 0)
    ('Recharge',         53, 4, 0, 0, 0, 0)
]


def battle(player, boss, turn, activeEffects, manaSpent, winCosts, test=False):
    # apply active effects and decrement timers
    pass

    # check for end conditions
    if player['hp'] <= 0 or player['mana'] < :
        # loss
        return winCosts
    if boss['hp'] <= 0:
        # win
        return winCosts + [manaSpent]

    # execute turn
    if turn == 0:
        # player; recurse over allowed options, to test each path the battle
        # can take.
        turn = 1
        for s in spells:
            if canCast(s, player, activeEffects):
                pass

        if test:
            print boss
    else:
        # boss
        turn = 0
        player['hp'] -= max(1, boss['dmg'] - player['armor'])
        if test:
            print player

    battle(player, boss, turn, activeEffects, manaSpent, winCosts, test)

if __name__ == '__main__':
    # 1. get puzzle input
    boss = {'hp':None, 'dmg':None, 'armor':0}
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            m = re.match(r'Hit Points: ([0-9]+)', line)
            if m:
                boss['hp'] = int(m.group(1))
            m = re.match(r'Damage: ([0-9]+)', line)
            if m:
                boss['dmg'] = int(m.group(1))
            m = re.match(r'Armor: ([0-9]+)', line)
            if m:
                boss['armor'] = int(m.group(1))

    player = {'hp':50, 'mana':500, 'armor':0}

    # # test battle
    # testPlayer = {'hp':8, 'dmg':5, 'armor':5}
    # testBoss = {'hp':12, 'dmg':7, 'armor':2}
    # testPlayer = {'hp':100, 'dmg':4, 'armor':0}
    # testBoss = {'hp':100, 'dmg':8, 'armor':2}
    # print battle(testPlayer, testBoss, True)
    # exit(0)

    print 'Answer to part 1: ' + ''
    print 'Answer to part 2: ' + ''
