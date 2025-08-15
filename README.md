# 🗑 File Cleaner / Nettoyeur de fichiers

A Python tool with a graphical interface (Tkinter) to clean a chosen folder by sending old files to the recycle bin.  
Un outil Python avec une interface graphique (Tkinter) pour nettoyer un dossier choisi en envoyant les fichiers anciens à la corbeille.

---

## 🇬🇧 English

### Features
- Choose a folder to clean.
- Set the number of days before files are deleted.
- Option to delete automatically or ask before each deletion.
- Files are sent to the recycle bin (can be recovered if needed).
- Language selection (English/French).

### Requirements
Install the dependencies before running:
```
py -m pip install send2trash
```

### How to Run
```
python cleanereng.py
```

---

## 🇫🇷 Français

### Fonctionnalités
- Choisir un dossier à nettoyer.
- Définir le nombre de jours avant que les fichiers soient supprimés.
- Option pour supprimer automatiquement ou demander confirmation à chaque suppression.
- Les fichiers sont envoyés à la corbeille (ils peuvent être récupérés si besoin).
- Sélecteur de langue (Français/Anglais).

### Prérequis
Installez les dépendances avant de lancer :
```
py -m pip install send2trash
```

### Lancement
```
python cleanerfr.py
```

---

## 📌 Notes
- Works on Windows.  
- The program will not delete the original files permanently; they will be in the recycle bin.
- Hidden system files like `desktop.ini` are ignored.


Sélectionnez le dossier à nettoyer.
Entrez le nombre de jours ; les fichiers plus anciens seront supprimés.
Cochez la case si vous voulez demander confirmation avant la suppression.
Cliquez sur Lancer le nettoyage.
