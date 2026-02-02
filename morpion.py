case_vide=""
plateau = [case_vide for i in range(9)]

choix_jouer = 0

symboles = ("❌", "⭕")
placeholder = ("1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ")
jouer = symboles[0]

def afficher_plateau():
        print(" ----+----+----")
        for i in range(9):
            print("|",plateau[i] if plateau[i]!= case_vide else placeholder[i], end=" ")
            if i  % 3 == 2:
                print("|")
                print(" ----+----+----")

while True:
    afficher_plateau()
    while choix_jouer < 1 or choix_jouer > 9 or plateau[choix_jouer-1] != case_vide:
        print("valeur incorrecte, recommencez")
        choix_jouer = int(input("entrez une valeur entre 1 et 9 :"))

    plateau[choix_jouer-1] = jouer

    if (plateau[0] == plateau[1] == plateau[2] != case_vide) \
    or (plateau[3] == plateau[4] == plateau[5] != case_vide) \
    or (plateau[6] == plateau[7] == plateau[8] != case_vide) \
    or (plateau[0] == plateau[3] == plateau[6] != case_vide) \
    or (plateau[1] == plateau[4] == plateau[7] != case_vide) \
    or (plateau[2] == plateau[5] == plateau[8] != case_vide) \
    or (plateau[0] == plateau[4] == plateau[8] != case_vide) \
    or (plateau[2] == plateau[4] == plateau[6] != case_vide):
        print("le joueur", jouer, "gagné la partie")
        afficher_plateau()
        break
    if case_vide not in plateau:
        print("malheureusement match nul !!!!")
        afficher_plateau()
        break  

    jouer = symboles[1] if jouer == symboles[0] else symboles[0]    