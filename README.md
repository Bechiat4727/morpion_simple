# Tic-Tac-Toe (XO) en Python

## Description

Ceci est un jeu simple de **Tic-Tac-Toe (XO)** en console, développé en Python.  
Deux joueurs s'affrontent pour aligner trois symboles identiques (`❌` ou `⭕`) sur une grille de 3x3.  
Les cases sont numérotées de 1 à 9 pour faciliter le choix des joueurs.

---

## Fonctionnalités

- Grille 3x3 affichée en console avec cases numérotées.
- Deux symboles : ❌ pour le joueur 1 et ⭕ pour le joueur 2.
- Détection automatique :
  - victoire d’un joueur,
  - match nul.
- Validation des entrées : impossible de jouer sur une case déjà occupée ou hors limites (1–9).

---

## Comment jouer

1. Lancez le programme Python :

```bash
python morpion.py
```
2. Le plateau s’affiche avec les numéros des cases :

|1️⃣ |2️⃣ |3️⃣ |
 ----+----+----
|4️⃣ |5️⃣ |6️⃣ |
 ----+----+----
|7️⃣ |8️⃣ |9️⃣ |
 ----+----+----

3. Chaque joueur choisit une case libre en entrant un nombre entre 1 et 9.

4. Le symbole du joueur est placé dans la case choisie.

5. Le jeu continue jusqu'à ce qu’un joueur gagne ou que toutes les cases soient remplies (match nul).

## Installation

- Python 3.x requis.

- Pas de dépendances externes.

- Clonez le dépôt ou téléchargez le fichier morpion.py et lancez-le avec Python.

## Auteur

- Islam BECHIAT