require 'active_support/all'

MINE_HP = 50
MINE_MANA = 500
BOSS_HP = 71
BOSS_DAMAGE = 10

# MINE_HP = 10
# MINE_MANA = 250
# BOSS_HP = 14
# BOSS_DAMAGE = 8

# battle class
class Battle
  attr_accessor :hp, :mana, :boss_hp, :effects, :mana_used, :result, :stack, :use

  def starting
    self.hp = MINE_HP
    self.mana = MINE_MANA
    self.boss_hp = BOSS_HP
    self.effects = {}
    self.mana_used = 0
    self.result = nil
    self.stack = []
    self.use = []
  end

  def boss_damage
    BOSS_DAMAGE
  end

  def armor
    result = 0
    effects.each do |_key, effect|
      result += effect[:armor] if effect[:armor].present?
    end
    result
  end

  def can_cast?(name, spell)
    return false if use.first.present? && use.first != name
    return false if mana < spell[:cost]
    return false if effects[name].present?
    true
  end

  def cast(name, spell)
    use.shift if use.present?
    stack << name
    self.mana -= spell[:cost]
    self.mana_used += spell[:cost]
    self.boss_hp -= spell[:damage] if spell.key?(:damage)
    update_result
    self.hp += spell[:heal] if spell.key?(:heal)
    effects[name] = spell[:effect].dup if spell[:effect].present?
  end

  def update_result
    self.result ||= :won if boss_hp <= 0
    self.result ||= :lost if hp <= 0
  end

  def turn
    effects.each do |_key, effect|
      self.boss_hp -= effect[:damage] if effect[:damage].present?
      update_result
      self.mana += effect[:mana] if effect[:mana].present?
      effect[:turns] -= 1
    end
    effects.delete_if { |_name, effect| effect[:turns] == 0 }
  end

  def boss_turn
    turn
    self.hp -= [1, boss_damage - armor].max
    update_result
  end

  def penalty
    self.hp -= 1
    update_result
  end

  def dup
    duplicate = self.class.new
    duplicate.hp = hp
    duplicate.mana = mana
    duplicate.boss_hp = boss_hp
    duplicate.effects = effects.deep_dup
    duplicate.mana_used = mana_used
    duplicate.result = result
    duplicate.stack = stack.dup
    duplicate.use = use.dup
    duplicate
  end
end

@spells = {}
@spells[:missile] = { cost: 53, damage: 4 }
@spells[:drain] = { cost: 73, damage: 2, heal: 2 }
@spells[:shield] = { cost: 113, effect: { turns: 6, armor: 7 } }
@spells[:poison] = { cost: 173, effect: { turns: 6, damage: 3 } }
@spells[:recharge] = { cost: 229, effect: { turns: 5, mana: 101 } }

@min_mana_kill = nil
@min_mana_stack = nil

def self.recursive(battle)
  battle.penalty
  battle.turn
  return if won_test(battle)
  return if battle.result == :lost
  return if @min_mana_kill.present? && @min_mana_kill < battle.mana_used

  @spells.each do |key, spell|
    next unless battle.can_cast?(key, spell)
    # print "#{key}\n"
    new_battle = battle.dup
    new_battle.cast(key, spell)
    new_battle.boss_turn
    recursive(new_battle)
  end
end

def self.won_test(battle)
  return false unless battle.result == :won
  if @min_mana_kill.nil? || @min_mana_kill > battle.mana_used
    @min_mana_kill = battle.mana_used
    @min_mana_stack = battle.stack
  end
  true
end

battle = Battle.new
battle.starting
# battle.use = [:recharge, :shield, :drain, :poison, :missile]

recursive(battle)
print "#{@min_mana_stack}\n"
print "#{@min_mana_kill}\n"
