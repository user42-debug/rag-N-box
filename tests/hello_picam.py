import os
"""
Ce test a pour but de verifier le fonctionnement de la caméra.
rpicam-hello lance une fenetre qui affiche ce que voitla caméra.
Ici, on le regle pour qu'il dure 5 secondes
"""
os.system("rpicam-hello --timeout 0")