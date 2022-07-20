# AYOMI-project-work

En local:

Le dossier profile.app contient:
- un fichier python app.py
- la base de données data.db
- un dockerfile
- un fichier texte avec les dépendances
- un dossier templates avec des fichiers html:
  * display
  * index
  * login
  * register
  * update

Lancer l'invit de commande: 
Assurer vous que vous etes dans le bon repertoire ..\profile_app
$flask run
L'application tourne sur http://127.0.0.1:5000/

Le système d'autentification ne fonctionne pas correctement , c'est possible de se connecter sans être enregistrer :(

1- Page login : http://127.0.0.1:5000/login
Entrer le pseudo et le mot de passe ensuite cliquer sur login

2- Une page avec des onglets : index , display , update et log out s'affichera

3- Pour afficher les données utilisateurs : appuyer sur Display

4- Pour éditer les donéees utilisateurs : appuyer sur Update

5- Pour vérifier le changements des données , revenir à Display

6- Pour se déconnecter appuyer sur log out 
