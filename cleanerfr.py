import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from send2trash import send2trash
import ctypes

def est_cache_ou_systeme(chemin_fichier):
    attributs = ctypes.windll.kernel32.GetFileAttributesW(chemin_fichier)
    if attributs == -1:
        return False
    return bool(attributs & 2) or bool(attributs & 4)

def nettoyer_dossier():
    try:
        dossier = entree_dossier.get()
        jours = int(entree_jours.get())
        demander_confirmation = var_confirmation.get()

        if not os.path.isdir(dossier):
            messagebox.showerror("Erreur", "Le dossier spécifié est invalide.")
            return

        limite = jours * 86400
        maintenant = time.time()
        fichiers_supprimes = 0

        for nom_fichier in os.listdir(dossier):
            chemin_fichier = os.path.abspath(os.path.join(dossier, nom_fichier))  # chemin absolu

            # Debug : afficher le fichier trouvé
            print("Fichier trouvé :", chemin_fichier)

            if est_cache_ou_systeme(chemin_fichier):
                print("Ignoré (caché/système) :", chemin_fichier)
                continue

            if os.path.isfile(chemin_fichier):
                age = maintenant - os.path.getmtime(chemin_fichier)
                if age > limite:
                    if demander_confirmation:
                        reponse = messagebox.askyesno("Confirmation", f"Supprimer {nom_fichier} ?")
                        if not reponse:
                            continue
                    try:
                        send2trash(chemin_fichier)
                        print("Envoyé à la corbeille :", chemin_fichier)
                        fichiers_supprimes += 1
                    except Exception as e:
                        print("send2trash a échoué, suppression définitive :", chemin_fichier, e)
                        try:
                            os.remove(chemin_fichier)
                            print("Supprimé définitivement :", chemin_fichier)
                            fichiers_supprimes += 1
                        except Exception as e2:
                            print("Échec de la suppression :", chemin_fichier, e2)

        messagebox.showinfo("Terminé", f"{fichiers_supprimes} fichier(s) supprimé(s).")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide pour les jours.")

def parcourir_dossier():
    dossier = filedialog.askdirectory()
    if dossier:
        entree_dossier.delete(0, tk.END)
        entree_dossier.insert(0, dossier)

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Nettoyeur de fichiers temporaires")

tk.Label(fenetre, text="Dossier à nettoyer :").grid(row=0, column=0, sticky="w")
entree_dossier = tk.Entry(fenetre, width=40)
entree_dossier.grid(row=0, column=1)
tk.Button(fenetre, text="Parcourir", command=parcourir_dossier).grid(row=0, column=2)

tk.Label(fenetre, text="Supprimer les fichiers plus vieux que (jours) :").grid(row=1, column=0, sticky="w")
entree_jours = tk.Entry(fenetre, width=10)
entree_jours.grid(row=1, column=1, sticky="w")

var_confirmation = tk.BooleanVar()
tk.Checkbutton(fenetre, text="Demander confirmation avant suppression", variable=var_confirmation).grid(row=2, columnspan=3, sticky="w")

tk.Button(fenetre, text="Lancer le nettoyage", command=nettoyer_dossier).grid(row=3, columnspan=3, pady=10)

fenetre.mainloop()
