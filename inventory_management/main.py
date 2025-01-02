from inventory_manager import InventoryManager
from search import Search
from report import Report


def menu():
    print("1. Consolider les fichiers CSV")
    print("2. Rechercher un produit")
    print("3. Générer un rapport")
    print("4. Quitter")
    choice = input("Choisissez une option: ")
    if choice == '1':
        inventory_manager = InventoryManager()
        inventory_manager.consolidate_files()
    elif choice == '2':
        search = Search()
        search.run_search()
    elif choice == '3':
        report = Report()
        report.generate_report()
    elif choice == '4':
        print("Au revoir!")
        exit()
    else:
        print("Choix invalide, essayez encore.")
        menu()


if __name__ == "__main__":

    while True:
        menu()
