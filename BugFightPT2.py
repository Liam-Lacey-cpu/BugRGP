#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:53:28 2024

@author: liaml
"""
class BugCharacter():
    name = ""
    health = 1.0
    stamina = 1.0
    attack = (1,2)
    defe = 1
    HeatResistance = 0
    force_res = 0
    water_resistance = 0
    is_alive = True
    
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def mit(self, value, dtype = 'later'):
        return value - self.defe
        
    def dmg(self, value, dtype = 'later'):
        result = self.mit(value, dtype)
        self.health = self.health - result
        if not self.is_alive():
            self.die
    def is_alive(self):
        return 0 < self.health
    
    def die(self):
        is_alive = False
        self.health = 0
        
Mantis = BugCharacter('Manny', 100)

Mantis.dmg(10)

print(Mantis.__dict__)