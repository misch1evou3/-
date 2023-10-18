# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

players = ['A','B','C','D']
matches = [(player1, player2) for player1 in players for player2 in players if player1 != player2]
for match in matches:
    if match[0] != match[1]:
        print(f"{match[0]} VS. {match[1]}")
        
    
