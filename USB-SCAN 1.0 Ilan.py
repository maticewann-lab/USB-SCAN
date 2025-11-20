# Bibliothèque standard pour ouvrir un navigateur par défaut
import webbrowser

# Biblothèque standard pour rajouter la date et l'heure 
from datetime import datetime
date_heure = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Biblothèque pour connaître toutes les informations d'un système
import wmi 
def get_usb_devices():
    usb_devices = []
    c = wmi.WMI() # Crée un objet WMI qui va permettre de récupérer des informations sur les périphériques connectés à l'ordinateur
    for device in c.Win32_PnPEntity(): # Parcourt chacun des périphériques Plug and Play de l'ordinateur reconnu par Windows
        if device.PNPClass == "USB": # Filtre les péréphériques pour garder que les USB
            usb_devices.append({ 
                "name": device.Name,
                "manufacturer": device.Manufacturer,
                "device_id": device.DeviceID,
                "description": device.Description
            })
    return usb_devices # Renvoie la liste complète des périphériques USB détectés avec leur informations

# Liste pour stocker les réponses
reponses_utilisateur = []

# Crée une boucle
continu = True
while continu:

    # Demander le nom de l'utilisateur
    prenom = input("Quel est votre prénom ?")

    # Demander le prénom de l'utilisateur
    nom = input("Quel est votre nom ?")

    # Afficher le message de bienvenue
    print(f"Bonjour, {prenom} {nom} !")

    # Demander si l'utilisateur souhaite continuer
    reponse = input("Souhaitez-vous continuer ? (oui/non) ").strip().lower()

    # Stocker la réponse
    reponses_utilisateur.append({"nom": nom,"prenom": prenom,"reponse": reponse,"date": date_heure})
    
    if reponse == "non":
        continu = False # Arrête la boucle
        print("Au revoir !")

# Générer le contenu HTML
contenu_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Réponses de l'utilisateur</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Historique des réponses</h1>
    <table>
        <tr>
            <th>Prénom</th>
            <th>Nom</th>
            <th>Réponse</th>
            <th>Date/Heure</th>
        </tr>
"""

# Ajouter les réponses au HTML
for reponse in reponses_utilisateur:
    contenu_html += f"""
        <tr>
            <td>{reponse['prenom']}</td>
            <td>{reponse['nom']}</td>
            <td>{reponse['reponse']}</td>
            <td>{reponse['date']}</td>
        </tr>
    """

contenu_html += """
    </table>
    <h1>Périphériques USB détectés</h1>
    <table>
        <tr>
            <th>Nom</th>
            <th>Fabricant</th>
            <th>Description</th>
            <th>ID Matériel</th>
        </tr>
"""

for usb in get_usb_devices():
    contenu_html += f"""
        <tr>
            <td>{usb['name']}</td>
            <td>{usb['manufacturer']}</td>
            <td>{usb['description']}</td>
            <td>{usb['device_id']}</td>
        </tr>
    """

# Fermer le HTML
contenu_html += """
    </table>
</body>
</html>
"""

# Écrire le contenu dans un fichier HTML
with open("reponses_utilisateur.html", "w", encoding="utf-8") as fichier:
    fichier.write(contenu_html)

# Ouvrir le fichier dans le navigateur
webbrowser.open("reponses_utilisateur.html")
