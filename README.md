# rag-N-box

La Rag'n box est une cage à Ragondins equipée d'une caméra et d'un capteur de fermeture. 
Lorqu'un animal est capturé, la caméra prend une photo qui est ensuite analysée par une IA.
Un message accompagné d'une image est ensuite envoyé au piégeur qui lui indique une prise et si celle-ci est un ragondin.
L'objectif de ce système est de faciliter la capture d'espèces invasives tout en évitant aux piégeurs de devoir vérifier l'entièreté de leurs cages tous les jours.

# Matériel requis :
- Un raspberry Pi3
- Une caméra
- Un capteur logique
- Une carte memoire de 32GB
- Un module GSM
- Une carte SIM valide
- Un écran
- Un clavier
- Une souris
- Un câble HDMI
- Un câble d'alimentation pour le raspberry 
- Un câble USB-MicroUSB pour faire la data entre le GSM et le raspberry
- Un générateur (non utilisé pour le moment)
- Deux câbles permettants de lier le générateur et le GSM (non utilisé pour le moment)
- Une cage à ragondin avec un aimant sur la trappe
- Deux fils liaisons
- Une breadbord

# Installation
Pour commencer, sur le raspberry, il faut : 
    - brancher le capteur qui se trouve sur la breadbord au raspberry via les fils liaisons,
    - brancher la caméra,
    - brancher le GSM via le câble USB-MicroUSB et mettre la carte SIM dans le module GSM,
    - brancher le clavier et la souris aux ports USB,
    
Ensuite pour démarrer le raspberry, il suffit de le brancher avec le câble d'alimentation.
Pour lancer le programme, il faut ouvrir Thonny et ouvrir main.py, n'oublier pas de vérifier si c'est le bon port USB, auquel est branché le GSM, qui est renseigné (à la ligne 23 du code).

Pour faire ce projet, nous avons créé l'integralitée des programmes utilisés dans le projet.
Des tests de commandes AT (qui permettent l'envoi d'un messaege) ont étés effectués à l'aide du logiciel PUTTY, qui permet l'utilisation de commandes AT à travers un terminal.

# Créateurs du projet 
- Malo TESSE
- Célian QUILLARD
- Martin DESCOMBES 
- Cassiopée FLAMANT-VIETTE

# Licence 
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

