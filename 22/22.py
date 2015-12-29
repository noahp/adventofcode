import re, sys, copy, random

# name, cost, damage, heal, manaCharge, armor, effectLength
spells = [
    ('MagicMissle',      53, 4, 0, 0, 0, 0),
    ('Drain',            73, 2, 2, 0, 0, 0),
    ('Shield',           113, 0, 0, 0, 7, 6),
    ('Poison',           173, 0, 0, 0, 0, 6),
    ('Recharge',         229, 0, 0, 101, 0, 5),
]
minspellcost = min([c[1] for c in spells])

class state(object):
    def __init__(self, player, boss, effects={}, manaspent=0, playerturn=True):
        self.player = copy.deepcopy(player)
        self.boss = copy.deepcopy(boss)
        self.effects = copy.deepcopy(effects)
        self.manaspent = manaspent
        self.playerturn = playerturn

    def canCast(self, spell):
        '''' Can the player cast the specified spell at this time?'''
        if spell[0] not in self.effects:
            if spell[1] <= self.player['mana']:
                return True
        return False

    def spellsAvailable(self):
        return [c for c in spells if self.canCast(c)]

    def cast(self, spell):
        # print spell
        self.player['mana'] -= spell[1]
        self.manaspent += spell[1]
        # activate effect
        if spell[6] > 0:
            self.effects[spell[0]] = spell[6]
        # apply damage to boss
        if spell[2] > 0:
            self.boss['hp'] -= spell[2]
        # apply healing to player
        if spell[3] > 0:
            self.player['hp'] += spell[3]

    def __str__(self):
        return ''.join(map(str, (self.player, self.boss, self.effects, self.playerturn)))

def runEffects(thisState):
    # apply active effects and decrement timers
    if 'Shield' in thisState.effects:
        thisState.player['armor'] = 7
        thisState.effects['Shield'] -=1
        if thisState.effects['Shield'] == 0:
            del thisState.effects['Shield']
    if 'Poison' in thisState.effects:
        thisState.boss['hp'] -= 3
        thisState.effects['Poison'] -=1
        if thisState.effects['Poison'] == 0:
            del thisState.effects['Poison']
    if 'Recharge' in thisState.effects:
        thisState.player['mana'] += 101
        thisState.effects['Recharge'] -=1
        if thisState.effects['Recharge'] == 0:
            del thisState.effects['Recharge']

    # check for end conditions
    if thisState.player['hp'] <= 0 or thisState.player['mana'] < minspellcost:
        # loss
        # print player,boss
        # print 'loss'
        return float('inf')
    if thisState.boss['hp'] <= 0:
        # win
        # print thisState.manaspent
        return thisState.manaspent

    return 0

def battle(thisState, winCost=float('inf')):
    ''' Fight until player dies, boss dies, or player mana is all spent.'''
    while True:
        # execute effects at start of turn
        result = runEffects(thisState)
        if result:
            # game over
            if result < winCost:
                # print winCost
                return result
            else:
                return winCost

        if thisState.playerturn:
            # execute player turn
            thisState.playerturn = False
            # cast a random spell
            thisState.cast(random.choice(thisState.spellsAvailable()))

        else:
            # boss turn
            thisState.playerturn = True
            thisState.player['hp'] -= max(1, thisState.boss['dmg'] - thisState.player['armor'])
            if thisState.player['hp'] <= 0:
                # game over
                break

    return winCost

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
    manaspent = float('inf')
    for i in xrange(1000000):
        s = state(player, boss)
        w = battle(s)
        if w < manaspent:
            print w
            manaspent = w

    print 'Answer to part 1: ' + str(manaspent)




    # print 'Answer to part 2: ' + ''
