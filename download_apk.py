import requests
import os

def download_apk(app_id):
    url = f"https://d.apkpure.com/b/APK/{app_id}?version=latest"
    
    # Suivre les redirections pour obtenir le lien direct
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        apk_url = response.url
        apk_response = requests.get(apk_url)

        # Vérifier que le téléchargement a réussi
        if apk_response.status_code == 200:
            with open(f"{app_id}.apk", 'wb') as apk_file:
                apk_file.write(apk_response.content)
            print(f"Downloaded {app_id}.apk successfully.")
        else:
            print(f"Failed to download APK from {apk_url}: {apk_response.status_code}")
    else:
        print(f"Failed to fetch APK page: {response.status_code}")

def download_latest_release(repo, file_pattern):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        assets = response.json().get('assets', [])
        for asset in assets:
            if file_pattern in asset['name']:
                download_url = asset['browser_download_url']
                download_file(asset['name'], download_url)
                return
        print(f"No assets found matching {file_pattern} in {repo}.")
    else:
        print(f"Failed to fetch releases from {repo}: {response.status_code}")

def download_file(filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename} successfully.")
    else:
        print(f"Failed to download {filename} from {url}: {response.status_code}")

if __name__ == "__main__":
    download_apk("com.google.android.apps.photos")
    
    # Télécharger les dernières releases de ReVanced
    download_latest_release("ReVanced/revanced-cli", "revanced-cli")
    download_latest_release("ReVanced/revanced-patches", "revanced-patches")
    download_latest_release("ReVanced/revanced-integrations", "revanced-integrations")
