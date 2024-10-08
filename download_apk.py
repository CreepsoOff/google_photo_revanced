import os
import requests
from apkpure.apkpure import ApkPure

def download_google_photos_apk():
    # Initialiser l'API
    api = ApkPure()
    
    # Télécharger la dernière version de Google Photos
    download_path = api.download("com.google.android.apps.photos")
    
    if download_path:
        print(f"APK téléchargé à : {download_path}")
    else:
        print("Échec du téléchargement de l'APK.")

def download_latest_release(url):
    response = requests.get(url)
    response.raise_for_status()  # Vérifier si la requête a réussi
    return response.json()

def get_latest_revanced_cli():
    url = "https://api.github.com/repos/ReVanced/revanced-cli/releases/latest"
    release_data = download_latest_release(url)
    
    # Récupérer le lien de téléchargement du fichier .jar
    for asset in release_data['assets']:
        if asset['name'].endswith('-all.jar'):
            download_url = asset['browser_download_url']
            print(f"Téléchargement de ReVanced CLI depuis : {download_url}")
            response = requests.get(download_url)
            with open('revanced-cli.jar', 'wb') as f:
                f.write(response.content)
            print("ReVanced CLI téléchargé.")

def get_latest_revanced_patches():
    url = "https://api.github.com/repos/ReVanced/revanced-patches/releases/latest"
    release_data = download_latest_release(url)
    
    # Récupérer le lien de téléchargement du fichier .jar
    for asset in release_data['assets']:
        if asset['name'].endswith('.jar'):
            download_url = asset['browser_download_url']
            print(f"Téléchargement de ReVanced Patches depuis : {download_url}")
            response = requests.get(download_url)
            with open('revanced-patches.jar', 'wb') as f:
                f.write(response.content)
            print("ReVanced Patches téléchargé.")

def get_latest_revanced_integrations():
    url = "https://api.github.com/repos/ReVanced/revanced-integrations/releases/latest"
    release_data = download_latest_release(url)
    
    # Récupérer le lien de téléchargement de l'APK des intégrations
    for asset in release_data['assets']:
        if asset['name'].endswith('.apk'):
            download_url = asset['browser_download_url']
            print(f"Téléchargement de ReVanced Integrations depuis : {download_url}")
            response = requests.get(download_url)
            with open('revanced-integrations.apk', 'wb') as f:
                f.write(response.content)
            print("ReVanced Integrations téléchargé.")

if __name__ == "__main__":
    download_google_photos_apk()
    get_latest_revanced_cli()
    get_latest_revanced_patches()
    get_latest_revanced_integrations()
