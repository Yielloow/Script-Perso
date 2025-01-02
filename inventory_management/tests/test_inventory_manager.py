import unittest
import os
import sys
from inventory_manager import InventoryManager

# Ajout du répertoire parent pour accéder à inventory_manager.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        """Configuration des fichiers nécessaires aux tests."""
        self.manager = InventoryManager()
        # Utiliser les fichiers existants
        self.test_file_1 = "empty.csv"
        self.test_file_2 = "inventory.csv"

        # S'assurer que les fichiers existent
        if not os.path.exists(self.test_file_1):
            raise FileNotFoundError(
                f"{self.test_file_1} non trouvé."
            )
        if not os.path.exists(self.test_file_2):
            raise FileNotFoundError(
                f"{self.test_file_2} non trouvé."
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


if __name__ == "__main__":
    unittest.main()
