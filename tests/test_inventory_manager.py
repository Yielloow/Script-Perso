import unittest
import os


import sys

# Ajout du répertoire parent pour accéder à inventory_manager.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from inventory_manager import InventoryManager


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        """Configuration des fichiers nécessaires aux tests."""
        self.manager = InventoryManager()
        # Utiliser les fichiers existants
        self.test_file_1 = os.path.join(os.path.dirname(__file__), "empty.csv")
        self.test_file_2 = os.path.join(os.path.dirname(__file__), "inventory.csv")
        self.test_file_3 = os.path.join(os.path.dirname(__file__), "invalid_structure.csv")

        # S'assurer que les fichiers existent
        if not os.path.exists(self.test_file_1):
            raise FileNotFoundError(
                f"{self.test_file_1} non trouvé."
            )
        if not os.path.exists(self.test_file_2):
            raise FileNotFoundError(
                f"{self.test_file_2} non trouvé."
            )
        if not os.path.exists(self.test_file_3):
            raise FileNotFoundError(
                f"{self.test_file_3} non trouvé."
            )

    def tearDown(self):
        """Nettoyage après chaque test."""
        # Pas besoin de supprimer car des fichiers fixes
        pass

    def test_consolidate_files(self):
        """Test pour vérifier la consolidation des fichiers CSV."""
        self.manager.consolidate_files()
        self.assertFalse(
            self.manager.inventory.empty,
            "L'inventaire ne devrait pas être vide après consolidation."
        )
        self.assertIn(
            "product_name",
            self.manager.inventory.columns,
            "La colonne 'product_name' devrait exister dans l'inventaire."
        )

    def test_empty_file_ignored(self):
        """Test pour s'assurer qu'un fichier vide est ignoré."""
        self.manager.get_files = lambda: [self.test_file_1]
        self.manager.consolidate_files()
        self.assertTrue(self.manager.inventory.empty, "L'inventaire devrait être vide pour un fichier vide.")

    def test_non_empty_file_processed(self):
        """Test pour vérifier qu'un fichier non vide est traité."""
        self.manager.get_files = lambda: [self.test_file_2]
        self.manager.consolidate_files()
        self.assertFalse(self.manager.inventory.empty, "L'inventaire ne devrait pas être vide pour un fichier valide.")

    def test_ignored_inventory_report(self):
        """Test pour vérifier que le fichier inventory_report.csv est ignoré."""
        self.manager.get_files = lambda: ["inventory_report.csv"]
        self.manager.consolidate_files()
        self.assertTrue(self.manager.inventory.empty, "Le fichier inventory_report.csv devrait être ignoré.")

    def test_invalid_file_structure_ignored(self):
        """Test pour vérifier qu'un fichier avec une colonne manquante est ignoré."""
        self.manager.get_files = lambda: [self.test_file_3]
        self.manager.consolidate_files()
        self.assertTrue(self.manager.inventory.empty, "Un fichier avec une colonne manquante devrait être ignoré.")
    

if __name__ == "__main__":
    unittest.main()
