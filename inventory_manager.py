import os
import pandas as pd
from utils import read_csv, save_to_csv


class InventoryManager:
    def __init__(self):
        self.inventory = pd.DataFrame()

    def consolidate_files(self):
        files = self.get_files()
        for file in files:
            if file == "inventory_report.csv":
                print(f"Le fichier {file} a été ignoré.")
                continue

            print(f"Consolidation du fichier : {file}")
            # Vérifie si le fichier est vide
            if os.stat(file).st_size == 0:
                print(f"Avertissement : Le fichier {file} est vide et a été ignoré.")
                continue

            # Lecture des données
            data = read_csv(file)

            # Vérifie si le fichier contient uniquement des en-têtes
            if data.empty:
                print(f"Avertissement : Le fichier {file} contient uniquement des en-têtes et a été ignoré.")
                continue

            # Filtrer les données pour exclure les lignes de totaux (si applicable)
            if 'product_name' in data.columns:
                data = data[data['product_name'].str.lower() != 'total']  # Exclure les totaux

            # Ajouter les données au DataFrame de l'inventaire
            self.inventory = pd.concat([self.inventory, data], ignore_index=True)

        # Suppression des doublons et sauvegarde du fichier consolidé
        self.inventory.drop_duplicates(inplace=True)
        save_to_csv(self.inventory, "consolidated_inventory.csv")
        print("Consolidation terminée, fichier sauvegardé sous 'consolidated_inventory.csv'.")

    def get_files(self):
        # Retourne une liste de fichiers CSV présents dans le répertoire courant
        files = [f for f in os.listdir() if f.endswith('.csv')]
        return files
