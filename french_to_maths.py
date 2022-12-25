def translate_to_maths(txt):
    french_to_maths = {
        
    "a": "(pour tout à l'envers)",
    "b": "(Bijection)",
    "c": "(ensemble nbr complexes)",
    "d": "(ensemble nbr décimaux)",
    "e": "(nombre de néper)",
    "f": "(fonction)",
    "g": "(facteur multiplicatif par 1 000 000 000 (giga))",
    "h": "(ensemble nbr hypercomplexes)",
    "i": "(indice de sigma)",
    "j": "(nombre complexe tel que: j^3 = 1)",
    "k": "(souvent pris pour représenter un réel)",
    "l": "(franchement représente rien en maths)",
    "m": "(pente)",
    "n": "(ensemble nbr naturels)",
    "o": "(précédé de petit)",
    "p": "(ordonneée à l'origine)",
    "q": "(ensemble nbr rationnels)",
    "r": "(ensemble nbr réels)",
    "s": "(symbole de sommation)",
    "t": "(tau)",
    "u": "(union deux ensembles)",
    "v": "(vecteur)",
    "w": "(j'ai jamais vu cette lettre en maths)",
    "x": "(variable axe abscisses)",
    "y": "(variable axe ordonnées)",
    "z": "(ensemble nbr entiers)"
}
    translated = ""
    for char in txt.lower():
        translated += french_to_maths[char]
    return translated