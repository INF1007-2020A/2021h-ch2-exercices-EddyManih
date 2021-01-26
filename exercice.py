#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nouveau_mot = ""

    for letter in range(len(mot)):
        code_letter = ord(mot[letter]) - 32
        nouveau_mot += chr(code_letter)

    return nouveau_mot

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
