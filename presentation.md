## Présentation du projet "Rag'n Box"

Le ragondin, venu d'Amérique du Nord, est reconnu comme espèce nuisible en France en raison de sa tendance à dégrader les berges et les cultures, sa capture est donc autorisée et réglementée. Or, selon la réglementation, tous les pièges doivent être vérifiés chaque jour, ce qui limite la quantité de pièges utilisables par une seule personne.
Pour remédier à ce problème, nous avons décidé de créer la **Rag'n box**.

L'idée initiale était d'adapter une cage à ragondins et d'y ajouter une caméra et un capteur afin de détecter une prise.
En cas de capture, la caméra prend une photo de l'intérieur de la cage puis un message et une image sont envoyées au piégeur via un module GSM. Pour améliorer cette idée, nous avons dévelopée un modèle d'I.A. qui analyse la photo de l'animal capturé et indique s'il s'agit d'un ragondin ou non. Cette solution permet au piègeur de ne pas devoir vérifier ses pièges tous les jours mais seulement lorsqu'il reçoit un message. Grâce à cela, le piègeur peut donc poser plus de pièges et permettre un contrôle plus efficace des espèces nuisibles.

## Présentation de l'équipe : 

Notre équipe, composée de 4 élèves de NSI, est avant tout un groupe d'amis. Malo Tesse, développeur expérimenté, a développé l'IA utilisée dans notre projet. Martin Descombes, s'est quant à lui occupé de la communication sans fil grâce au module GSM. Célian Quillard a participé à la programmation du module GSM et à l'électronique du Raspberry Pi. Enfin, Cassiopée Flamant-Viette a réalisé la partie hardware et l'installation des capteurs et modules (Conception et impression 3D). Nous avons réalisé ce projet au cours d'un mois de travail.

## Avancement du projet 
Nous avons tout d'abord commencé par la mise en place de la caméra et du capteur logique ainsi que la création de leur programme et le début de quelques tests afin de vérifier leur bon fonctionnement. Ensuite, nous avons commencé la partie autour de l'envoi de SMS par le module GSM, cela se fait par l'utilisation de commandes AT, elles permettent d'envoyer un message en rentrant la numéro du téléphone qui doit recevoir le message. C'est au niveau de l'envoi de MMS, donc d'images que certains problèmes sont arrivés, en effet, notre module GSM ne permet pas l'envoi de MMS, nous avons donc trouvé un autre moyen d'accèder à l'image. Nous avons fait en sorte que l'image soit envoyée sur serveur externe (couldinari) et que le message envoyé au trappeur soit accompagné de l'URL de l'image pour qu'il puisse y accèder facilement. Un autre problème s'est déclaré : l'I.A. n'est pas compatible avec le raspberry, comme solution nous avons décidé d'en créer une autre mais par manque de temps, nous n'avons pas réussi à l'aboutir. De noubreux tests ont étés effectués notamment au niveau de l'envoi de message à un numéro de téléphone mais aussi des tests pour vérifier le bon fonctionnement de l'I.A..  

## Problèmes rencontrés lors du développement du projet :
De nombreux problèmes sont survenus lors de la création du projet :
    - Problème de connexion du Raspberry Pi, réglé car il y avait un problème de cohabitation pour se connecter au WiFi, en effet, le module GSM prennait le dessus sur le raspberry.
    - Problème de mémoire, réglé en changeant la carte mémoire, passage de 8GB à 32GB.
    - Difficultés pour envoyer des images à l'aide du module GSM, le GSM ne pouvant pas envoyer de MMS, nous avons décider d'envoyer l'image prise par la caméra sur un serveur externe (couldinarie) et d'envoyer au trappeur un message contenant l'URL pour accèder à l'image de la cage.
    - Problème avec la caméra, la caméra n'était pas détectée par le raspberry, problème réglé en débranchant et en rebranchant la caméra.
    - Problème de compatibilité entre le raspberry et l'I.A., non réglé actuellement, la création d'une nouvelle I.A. pourrait peut-être résoudre le problème.

## Ouveture 
L'implémentation d'une I.A., compatible avec le raspberry et capable de calculer une probabilité que l'animal capturé soit un ragondin, permetterais de faire gagner encore plus de temps aux trappeurs. Notre projet est une bonne idée mais n'est pas parfait, en effet, il nécessite une carte SIM par cage avec un forfait valable pour l'envoi de SMS, ce qui revient à devoir payer un prix assez conséquent et sûrement au dessus des primes pour les ragondins. Ce projet nous a permis d'en apprendre plus sur les commandes AT et l'envoi de SMS par un module GSM ainsi que sur l'électronique du raspberry.