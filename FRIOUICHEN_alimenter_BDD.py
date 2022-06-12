# -*- coding: utf-8 -*-


"""
FRIOUICHEN Mohammed (BUT Info 1A)(Groupe1)
Ce  script permet de générer un fichier .sql qui contient des requêtes d'insertion des enregistrements générer aléatoirement.
Important : Ce script permet l’alimentation ET la création des tables donc on peut directement importer le .sql sans créer les tables préalablement
Ce script permet l’alimentation de la base de données suivante :  
LVAC(IDLieux, Batiment, Creneaux, NbPersoMax, nbDoses)
Patients(NumSecu, maladieChronique, Grossesse, IDLieux, Nom, age, sexe, adresse, profession)
Personnels(IDPerso, nb_Patient, Nom, age, sexe, profession)
INSCRIRE(date, heure)
Affecter(IDLieux, IDPerso)
"""

from random import randrange
from datetime import timedelta
from random import randint
import datetime
fichier = open("data.sql", "a")



def random_date(start, end):
    # Cette fonction permet de générer une date aléatoire 
    date=str(randint(start,end))+'-'+str(randint(1,12))+"-"+str(randint(1,28))
    return date

def adresse(ville):
    # Cette fonction permet de générer une adresse aléatoirement 
    index=randint(0,len(ville)-1)   
    adresse=ville[index]+" France"
    return adresse

def formaterlesdonnees(attribut):
    # Cette fonction pour ajouter les séparateur entre les attributs pour créer une requête type INSERT
    sep="`, `" #séparateur
    Attribut=""
    comp=0
    for i in attribut:  
        if(comp!=len(attribut)-1):
            Attribut=Attribut+i+sep
        else:
            Attribut=Attribut+i
        comp=comp+1

    return Attribut

def genererCreneaux():
    # Cette fonction permet de générer le nb de créneaux
    nb_creneaux=randint(0,100)
    return nb_creneaux

def genererNb():
    # Cette fonction permet de générer nb aléatoire
    nb_creneaux=randint(10,70)
    return nb_creneaux

def genererSexe():
    # Cette fonction permet de générer sexe 1 ou 2
    sexe=randint(1,2)
    return sexe

def genererNumSecu(sexe):
    # Cette fonction permet de générer Num Secu
    if (sexe==1) :
        NumSecu=str(1)+str(randint(100000000000,999999999999))
    else :
        NumSecu=str(2)+str(randint(100000000000,999999999999))
    return NumSecu

#==================================================Génerer des enregistrements pour la table LVAC
# LVAC(IDLieux, Batiment, Creneaux, NbPersoMax, nbDoses)
E="'" # un séparteur 
ListAttribTableLVAC=['IDLieux', 'Batiment', 'Creneaux', 'NbPersoMax', 'nbDoses']
Nom_Table='LVAC'
N=40
ExempleNomBatiment=['Mairie' ,'Pharmacie', 'Laboratoire']
Exemplelocalisation=['Paris' ,'Nancy', 'Metz', 'St-Dié']
Enregistrements1=[]
create1=[]
cleetrangere1=[]
alter1=[]
for i in range(N):
    #=================================Les valeurs générer automatiquement
    IDLieux=i+1 # la clé
    cleetrangere1.append(IDLieux)
    index=randint(0,len(ExempleNomBatiment)-1)
    index2=randint(0,len(Exemplelocalisation)-1)
    Batiment=ExempleNomBatiment[index]+" " +Exemplelocalisation[index2]
    Creneaux=genererCreneaux()
    NbPersoMax=genererNb()
    nbDoses=genererNb()
    #==== créer la requet sql 
    Values=str(IDLieux)+","+E+Batiment+E+","+E+str(Creneaux)+E+","+E+str(NbPersoMax)+E+","+E+str(nbDoses)+E
    #====================================Les attributs
    Attribut=formaterlesdonnees(ListAttribTableLVAC)
    #print(Attribut)
    #====================================la requette 
    Rq="INSERT INTO `"+Nom_Table+"`(`"+Attribut+"`) VALUES ("+Values+");"
    print(Rq)
    Enregistrements1.append(Rq)
    
create="CREATE TABLE `LVAC` ( `IDLieux` text NOT NULL, `Batiment` text NOT NULL, `Creneaux` text NOT NULL, `NbPersoMax` text NOT NULL, `nbDoses` text NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
print(create)
create1.append(create)

T='\n'.join(create1)
fichier.write(T)

alter="ALTER TABLE `LVAC` ADD PRIMARY KEY (`IDLieux`(255));"
print(alter)
alter1.append(alter)

T='\n'.join(alter1)
fichier.write(T) 

    
T='\n'.join(Enregistrements1)
fichier.write(T) 




#==================================================Génerer des enregistrements pour la table Patients
# Patients(NumSecu, maladieChronique, Grossesse, IDLieux, Nom, age, sexe, adresse, profession)
E="'" # un séparteur
Nom={}
ListAttribTablePatients=['NumSecu', 'maladieChronique', 'Grossesse', 'IDLieux', 'Nom', 'age', 'sexe', 'adresse', 'profession']
Nom_Table='Patients'
N=40
Noms=["Allen","Ward","Jones","Martin","scott"]
ville=['Nancy', 'Metz', 'St-Dié']
Professions=['pilote' ,'etudiant', 'enseignant', 'avocat','technicien']
Enregistrements2=[]
cleetrangere2=[]
create2=[]
alter2=[]
for i in range(N):
    #=================================Les valeurs générer automatiquement
    adresses=adresse(ville)
    sexe=genererSexe()
    NumSecu=genererNumSecu(sexe)# la clé
    cleetrangere2.append(NumSecu)
    maladieChronique=randint(0,1)
    if (sexe==2):
        Grossesse=randint(0,1)
    else :
        Grossesse=0
    IDLieux=i+1
    
    index=randint(0,len(Noms)-1)
    print(index)
    Nom=Noms[index]
    profession=Professions[index]

    age=randint(22,80)
    

    #==== créer la requet sql 
    Values=NumSecu+","+E+str(maladieChronique)+E+","+E+str(Grossesse)+E+","+E+str(IDLieux)+E+","+E+Nom+E+","+E+str(age)+E+","+E+str(sexe)+E+","+E+adresses+E+","+E+profession+E
    #====================================Les attributs
    Attribut=formaterlesdonnees(ListAttribTablePatients)
    #print(Attribut)
    #====================================la requette 
    Rq="INSERT INTO `"+Nom_Table+"`(`"+Attribut+"`) VALUES ("+Values+");"
    print(Rq)
    Enregistrements2.append(Rq)

create="CREATE TABLE `Patients` ( `NumSecu` text NOT NULL, `maladieChronique` text NOT NULL, `Grossesse` text NOT NULL, `IDLieux` text NOT NULL, `Nom` text NOT NULL, `age` text NOT NULL, `sexe` text NOT NULL, `adresse` text NOT NULL, `profession` text NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
print(create)
create2.append(create)

T='\n'.join(create2)
fichier.write(T)

alter="ALTER TABLE `Patients` ADD PRIMARY KEY (`NumSecu`(255));"
print(alter)
alter2.append(alter)

T='\n'.join(alter2)
fichier.write(T) 

T='\n'.join(Enregistrements2)
fichier.write(T) 







#==================================================Génerer association INSCRIRE
# INSCRIRE(date, heure)
E="'" # un séparteur
ListAttribAssoINSCRIRE=['date', 'heure']
Nom_Asso='INSCRIRE'
N=40
Enregistrements3=[]
create3=[]

for i in range(N):
    #=================================Les valeurs générer automatiquement

    date=random_date(1, 30)
    heure=randint(8,19)

    
    #==== créer la requet sql 
    Values="'"+date+"'"+","+E+str(heure)+E
    #====================================Les attributs
    Attribut=formaterlesdonnees(ListAttribAssoINSCRIRE)
    #print(Attribut)
    #====================================la requette 
    Rq="INSERT INTO `"+Nom_Asso+"`(`"+Attribut+"`) VALUES ("+Values+");"
    print(Rq)
    Enregistrements3.append(Rq)

create="CREATE TABLE `INSCRIRE` ( `date` text NOT NULL, `heure` text NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
print(create)
create3.append(create)

T='\n'.join(create3)
fichier.write(T)

T='\n'.join(Enregistrements3)
fichier.write(T) 









#==================================================Génerer des enregistrements pour la table Personnels
# Personnels(IDPerso, nb_Patient, Nom, age, sexe, profession)
Nom={}

E="'" # un séparteur 
ListAttribTablePersonnels=['IDPerso', 'nb_Patient', 'Nom', 'age', 'sexe', 'profession']
Nom_Table='Personnels'
N=40
Noms=["Allen","Ward","Jones","Martin","scott"]


Professions=['Medecin' ,'infirmer-e', 'aide-soignant-e']

Enregistrements4=[]
create4=[]

cleetrangere3=[]
alter3=[]
for i in range(N):
    #=================================Les valeurs générer automatiquement
    IDPerso=i+1 # la clé
    cleetrangere3.append(IDPerso)
    nb_Patient=randint(0,13)
    index=randint(0,len(Noms)-1)
    print(index)
    Nom=Noms[index]
    profession=Professions[randint(0,len(Professions)-1)]
    age=randint(22,80)
    sexe=genererSexe()

    #==== créer la requet sql 
    Values=str(IDPerso)+","+E+str(nb_Patient)+E+","+E+Nom+E+","+E+str(age)+E+","+E+str(sexe)+E+","+E+profession+E
    #====================================Les attributs
    Attribut=formaterlesdonnees(ListAttribTablePersonnels)
    #print(Attribut)
    #====================================la requette 
    Rq="INSERT INTO `"+Nom_Table+"`(`"+Attribut+"`) VALUES ("+Values+");"
    print(Rq)
    Enregistrements4.append(Rq)

create="CREATE TABLE `Personnels` ( `IDPerso` text NOT NULL, `nb_Patient` text NOT NULL, `Nom` text NOT NULL, `age` text NOT NULL, `sexe` text NOT NULL, `profession` text NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
print(create)
create4.append(create)

T='\n'.join(create4)
fichier.write(T)

alter="ALTER TABLE `Personnels` ADD PRIMARY KEY (`IDPerso`(255));"
print(alter)
alter3.append(alter)

T='\n'.join(alter3)
fichier.write(T) 

T='\n'.join(Enregistrements4)
fichier.write(T) 






#==================================================Génerer association Affecter
# Affecter(IDLieux, IDPerso)
E="'" # un séparteur
ListAttribAssoAffecter=['IDLieux', 'IDPerso']
Nom_Asso='Affecter'
N=40
Enregistrements5=[]
create5=[]

for i in range(N):
    #=================================Les valeurs générer automatiquement

    IDLieux=cleetrangere1[randint(1,len(cleetrangere3)-1)]
    IDPerso=cleetrangere3[randint(1,len(cleetrangere1)-1)]

    
    #==== créer la requet sql 
    Values=str(IDLieux)+","+E+str(IDPerso)+E
    #====================================Les attributs
    Attribut=formaterlesdonnees(ListAttribAssoAffecter)
    #print(Attribut)
    #====================================la requette 
    Rq="INSERT INTO `"+Nom_Asso+"`(`"+Attribut+"`) VALUES ("+Values+");"
    print(Rq)
    Enregistrements5.append(Rq)
    
create="CREATE TABLE `Affecter` ( `IDLieux` text NOT NULL, `IDPerso` text NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
print(create)
create5.append(create)



T='\n'.join(create5)
fichier.write(T)



T='\n'.join(Enregistrements5)
fichier.write(T) 




#==================================================Génerer association VACCINER
# VACCINER(IDPerso, NumSecu)
E="'" # un séparteur
ListAttribAssoVACCINER=['IDPerso', 'NumSecu']
Nom_Asso='VACCINER'
N=40
Enregistrements6=[]
create6=[]
commit1=[]

for i in range(N):
    #=================================Les valeurs générer automatiquement

    IDPerso=cleetrangere3[randint(1,len(cleetrangere2)-1)]
    NumSecu=cleetrangere2[randint(1,len(cleetrangere3)-1)]

    
    #==== créer la requet sql 
    Values=str(IDPerso)+","+E+str(NumSecu)+E
    #====================================Les attributs
    Attribut=formaterlesdonnees(ListAttribAssoVACCINER)
    #print(Attribut)
    #====================================la requette 
    Rq="INSERT INTO `"+Nom_Asso+"`(`"+Attribut+"`) VALUES ("+Values+");"
    print(Rq)
    Enregistrements6.append(Rq)


#Sauvgarder les requetts dans un fichiier
create="CREATE TABLE `VACCINER` ( `IDPerso` text NOT NULL, `NumSecu` text NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
print(create)
create6.append(create)

T='\n'.join(create6)
fichier.write(T)

    
T='\n'.join(Enregistrements6)
fichier.write(T)

commit="COMMIT;"
print(commit)
commit1.append(commit)
T='\n'.join(commit1)
fichier.write(T)


fichier.close()

