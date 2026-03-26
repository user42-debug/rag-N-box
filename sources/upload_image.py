import requests 
import os


# dossier où se trouve ton script
script_dir = os.path.dirname(os.path.abspath(__file__))

# chemin complet vers ton image
image_path = os.path.join(script_dir, "can.jpg")

#print("Chemin complet :", image_path)
#print("Fichier existe ?", os.path.exists(image_path))

#with open(image_path, "rb") as file:
    #data = file.read()
    #print(len(data), "octets lus")
#reponse=requests.get("https://www.google.com")
#print (reponse.status_code)

# === CONFIG ===
cloud_name = "df1huukcm"
upload_preset = "uwuuwu"
#image_path = "can.jpg"  # chemin vers ton image

# === URL API Cloudinary ===
url = f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload"

# === Upload ===
#with open(image_path, "rb") as file:
#   response = requests.post(
#        url,
#        files={"file": file},
#        data={"upload_preset": upload_preset}
#    )

#data = response.json()

#if "secure_url" in data:
#    print("Image uploadée !")
#    print("URL de l'image :", data["secure_url"])
#else:
#    print("Erreur :", data)
def envoie_image(image_path,cloud_name,upload_preset,url):
    with open(image_path,"rb") as file:
        response= requests.post(
            url,
            files={"file":file},
            data={"upload_preset": upload_preset},
        )
    data= response.json() 
    if "secure_url" in data:
        print("image uploadé !")
        print("url de l'image:" , data["secure_url"])
        url_1 = data["secure_url"]
        print(url_1)

    else:
        print("erreur :", data)
envoie_image(image_path,cloud_name,upload_preset,url)