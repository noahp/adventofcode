import re, sys, itertools, copy

shop = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''

def parseShop(shopList):
    parsedShop = {'Weapons':[], 'Armor':[], 'Rings':[]}
    for cat in shopList.split('\n\n'):
        for line in cat.splitlines():
            m = re.match(r'([A-Za-z \+0-9]+?) {2,}([0-9]+) {2,}([0-9]+) {2,}([0-9]+)', line)
            if m:
                if cat.find('Weapons') == 0:
                    parsedShop['Weapons'].append(m.groups())
                elif cat.find('Armor') == 0:
                    parsedShop['Armor'].append(m.groups())
                elif cat.find('Rings') == 0:
                    parsedShop['Rings'].append(m.groups())

    return parsedShop

def battle(player, boss, test=False):
    turn = 0
    while player['hp'] > 0 and boss['hp'] > 0:
        if turn == 0:
            # player
            boss['hp'] -= max(1, player['dmg'] - boss['armor'])
            turn = 1
            if test:
                print boss
        else:
            # boss
            player['hp'] -= max(1, boss['dmg'] - player['armor'])
            turn = 0
            if test:
                print player

    if player['hp'] > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    # 1. get puzzle input
    boss = {'hp':None, 'dmg':None, 'armor':None}
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

    # get parsed shop contents
    parsedShop = parseShop(shop)

    # # test battle
    # testPlayer = {'hp':8, 'dmg':5, 'armor':5}
    # testBoss = {'hp':12, 'dmg':7, 'armor':2}
    # testPlayer = {'hp':100, 'dmg':4, 'armor':0}
    # testBoss = {'hp':100, 'dmg':8, 'armor':2}
    # print battle(testPlayer, testBoss, True)
    # exit(0)

    # for each combination of gear, run the battle
    s = {}
    s1 = {}
    # 1 weapon
    for w in itertools.combinations(parsedShop['Weapons'], 1):
        # 0-1 armor
        for a in list(itertools.combinations(parsedShop['Armor'] + [('None', '0', '0', '0')], 1)):
            # 0-2 rings
            for r in list(itertools.combinations(parsedShop['Rings'] + [('None1', '0', '0', '0'),('None2', '0', '0', '0'),], 2)):
                # compute stats
                cost = sum([int(c[1]) for c in w]) + sum([int(c[1]) for c in a]) + sum([int(c[1]) for c in r])
                player = {
                    'hp':100,
                    'dmg':sum([int(c[2]) for c in w]) + sum([int(c[2]) for c in a]) + sum([int(c[2]) for c in r]),
                    'armor':sum([int(c[3]) for c in w]) + sum([int(c[3]) for c in a]) + sum([int(c[3]) for c in r])
                }
                # execute battle
                battleBoss = copy.deepcopy(boss)
                if battle(player, battleBoss):
                    s[cost] = (player,(w,a,r))
                else:
                    s1[cost] = (player,(w,a,r))

    # print s[min(s.keys())]
    print 'Answer to part 1: ' + str(min(s.keys()))
    print 'Answer to part 2: ' + str(max(s1.keys()))
