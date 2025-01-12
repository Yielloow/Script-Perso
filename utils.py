import pandas as pd

def read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {file_path}: {e}")
        return pd.DataFrame()

def save_to_csv(df, file_path):
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du fichier {file_path}: {e}")
