import os
import pandas as pd
from utils import read_csv, save_to_csv


class InventoryManager:
    def __init__(self):
        self.inventory = pd.DataFrame()

    def consolidate_files(self):
        files = self.get_files()
        for file in files:
            print(f"Consolidation du fichier : {file}")
            # Vérification si le fichier est vide
            # Vérifie si la taille du fichier est nulle
            if os.stat(file).st_size == 0:
                print(f"Avertissement : Le fichier {file}"
                      f"est vide et a été ignoré.")
                continue
            # Lecture des données
            data = read_csv(file)
            # Vérification si le fichier contient uniquement des en-têtes
            if data.empty:
                print(f"Avertissement : Le fichier {file} contient"
                      f"uniquement des en-têtes et a été ignoré.")
                continue
            # Ajouter les données au DataFrame de l'inventaire
            self.inventory = pd.concat([self.inventory, data], ignore_index=True)
        # Suppression des doublons et sauvegarde du fichier consolidé
        self.inventory.drop_duplicates(inplace=True)
        save_to_csv(self.inventory, "consolidated_inventory.csv")
        print(f"Consolidation terminée, fichier sauvegardé"
              f"sous 'consolidated_inventory.csv'.")

    def get_files(self):
        # Retourne une liste de fichiers CSV présents dans le répertoire courant
        files = [f for f in os.listdir() if f.endswith('.csv')]
        return files
