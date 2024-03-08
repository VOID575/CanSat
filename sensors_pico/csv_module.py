import time

# Définition du chemin du fichier CSV
fichier_csv = 'blackbox.csv'

# Fonction pour ajouter une nouvelle valeur au fichier CSV
def ajouter_valeur(valeur):
   
    # Ouvrir le fichier CSV en mode ajout
    with open(fichier_csv, 'a') as fichier:
        
        # Écrire la nouvelle valeur dans le fichier
        fichier.write(str(valeur) + '\n')

# Fonction pour maintenir un maximum de 30 valeurs dans le fichier CSV
def gerer_limitation_valeurs():
    # Lire toutes les valeurs du fichier CSV dans une liste
    valeurs = []
    with open(fichier_csv, 'r') as fichier:
        for ligne in fichier:
            valeurs.append(ligne.strip())
            
    
    # Si le nombre de valeurs dépasse 85, supprimer les premières valeurs
    if len(valeurs) >= 80:
        valeurs = valeurs[-80:]
    
    # Réécrire le fichier CSV avec les valeurs mises à jour
    with open(fichier_csv, 'w') as fichier:
        for valeur in valeurs:
            fichier.write(str(valeur) + '\n')

"""
# Simuler l'ajout de valeurs
while True :
    ajouter_valeur('oui')
    gerer_limitation_valeurs()
    time.sleep(0.1)
"""

