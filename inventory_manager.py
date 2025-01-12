import os
import pandas as pd
from utils import read_csv, save_to_csv


class InventoryManager:
    def __init__(self):
        self.inventory = pd.DataFrame()

    def consolidate_files(self):
        files = self.get_files()
        required_columns = {'product_name', 'category', 'price', 'quantity'}

        for file in files:
            if file == "inventory_report.csv":
                print(f"Le fichier {file} a été ignoré.")
                continue

            print(f"Consolidation du fichier : {file}")
            
            if os.stat(file).st_size == 0:
                print(f"Avertissement : Le fichier {file} est vide et a été ignoré.")
                continue

            data = read_csv(file)

            # Vérifie si le fichier a toutes les colonnes nécessaires
            if not required_columns.issubset(data.columns):
                print(f"Avertissement : Le fichier {file} a une structure invalide et a été ignoré.")
                continue

            self.inventory = pd.concat([self.inventory, data], ignore_index=True)

        self.inventory.drop_duplicates(inplace=True)
        save_to_csv(self.inventory, "consolidated_inventory.csv")
        print("Consolidation terminée, fichier sauvegardé sous 'consolidated_inventory.csv'.")


    def get_files(self):
        # Retourne une liste de fichiers CSV présents dans le répertoire courant
        files = [f for f in os.listdir() if f.endswith('.csv')]
        return files
