# -*- coding: utf-8 -*-
"""
Hieroglyphe - Librairie de traduction français → hiéroglyphes

Fonctions disponibles :
- fr_to_hg(texte) : traduit le texte en hiéroglyphes
- reverse_text(texte) : renverse le texte
- repeat_text(texte, times=2) : répète le texte
- shout_hg(texte) : met en majuscules et traduit
- fancy_hg(texte, sep=" ") : stylise avec séparateurs
"""

transcription = {
    "A": "𓄿", "B": "𓃀", "C": "𓎡", "D": "𓂧", "E": "𓇋",
    "F": "𓆑", "G": "𓎼", "H": "𓉔", "I": "𓇋", "J": "𓆓",
    "K": "𓎡", "L": "𓃭", "M": "𓅓", "N": "𓈖", "O": "𓂝",
    "P": "𓊪", "Q": "𓎡", "R": "𓂋", "S": "𓋴", "T": "𓏏",
    "U": "𓅱", "V": "𓆑𓅱", "W": "𓅱", "X": "𓐍", "Y": "𓇋",
    "Z": "𓊃",
    "É": "𓇋", "È": "𓇋", "Ê": "𓇋", "À": "𓄿", "Ç": "𓎡"
}

def fr_to_hg(texte):
    """Traduit un texte français en hiéroglyphes."""
    resultat = ""
    for lettre in texte.upper():
        resultat += transcription.get(lettre, lettre)
    return resultat

def reverse_text(texte):
    """Renverse le texte donné."""
    return texte[::-1]

def repeat_text(texte, times=2):
    """Répète le texte un nombre de fois donné."""
    return texte * times

def shout_hg(texte):
    """Met le texte en majuscules et traduit en hiéroglyphes."""
    return fr_to_hg(texte.upper())

def fancy_hg(texte, sep=" "):
    """Stylise le texte en séparant chaque hiéroglyphe par un séparateur."""
    return sep.join(fr_to_hg(texte))
