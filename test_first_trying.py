from first_trying import Character, Ork, Elf
import pytest


def test_character_init():
    ork = Ork(level=5)
    assert ork.health_point == Ork.base_health_point * 5
    assert ork.attack_power == Ork.base_attack_power * 5

def test_attack():
    elf = Elf(level=7)
    elf.healh_point = 29
    target = Ork(level=1)
    original_damage = elf.attack_power
    elf.attack(target=target)
    
    assert target.health_point < target.max_health_point - original_damage * 2