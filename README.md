# Vincere a Flappy Bird grazie all'IA      <img src="https://unibs.coursecatalogue.cineca.it/img/unibs/logo.png" alt= “” width="10%" height="10%">

***Breve spiegazione***

Il progetto ha l'obbiettivo di utilizzare l'algoritmo genetico ***NEAT*** per imparare a giocare a ***Flappy Bird***.

Il gioco è stato ricreato in Python ed è stata utilizzata la libreria ***NEAT-Python*** per implementare l'algoritmo genetico.

>**NB** è necessario installare le seguenti librerie per avviare il programma: 
> - NEAT-Python <https://neat-python.readthedocs.io/en/latest/installation.html> 
> - ...



## Avviare il programma
***comandi base solo per far partire il programma***


## NEAT
***Breve spiegazione di NeuroEvolution of Augmenting Topologies*** \
***NeuroEvolution of Augmenting Topologies*** (**NEAT**) è un *algoritmo genetico* (GA) per la generazione di *reti neurali evolutive artificiali*. La sua unicità è data dalla  capaità di creare una sua struttura sempre più complessa e nel contempo sempre più ottimale (analoga all'evoluzione naturale). 
L'alogritmo è stato originariamente sviluppato Kenneth Stanley e Risto Miikkulainen nel 2002 all'Università del Texas ad Austin. 

A partire da reti estremamente semplici, in quanto completamente prive di neuroni intermedi, NEAT ha generalmente performance più elevate nella ricerca di soluzioni  efficaci e robuste rispetto ad algoritmni di *reinforcement leaening* o a tecniche neuro-evolutive analoghe che però partono da topologie predeterminate o comunque casuali. 

L'algorimo si basa su tre princìpi fondamentali:

1. **OMOLOGIA**: NEAT codifica ciascun nodo e ciascuna connessione della rete attraverso un gene. Ogni volta che una mutazione strutturale sfocia nella creazione di un nuovo gene, quel gene riceve un contrassegno numerico che lo rende permanentemente rintracciabile. Tale marcatura storica è utilizzata in seguito per verificare la conciliabilità di geni omologhi durante l'operazione di crossover, e per definire un operatore di compatibilità;

2. **PROTEZIONE DELL'INNOVAZIONE**: L'operatore precedente di compatibilità divide la popolazione composta da reti neurali in specie differenti, allo scopo di proteggere le soluzioni innovative da un'eliminazione prematura, e di prevenire l'incrocio di materiale genetico incompatibile. Tali innovazioni strutturali presentano una significativa possibilità di raggiungere il loro pieno potenziale, in quanto protette dal resto della popolazione attraverso la suddivisione in specie, ovvero la creazione di nicchie o spazi riservati;

3. **STRUTTURA MINIMA**: da ultimo, il principio secondo cui la ricerca di una soluzione dovrebbe avvenire nel più piccolo spazio possibile (inteso come numero di dimensioni), da espandere poi in maniera graduale. Cominciando il processo evolutivo da una popolazione di elementi a struttura minima, le successive mutazioni topologiche comportano l'aggiunta di nuovi nodi e connessioni alle reti, conducendo pertanto ad una crescita incrementale della popolazione stessa. Dal momento che solo le modifiche strutturali vantaggiose tendono a sopravvivere nel lungo termine, le topologie che vengono raffinate tendono ad essere le minime necessarie alla soluzione del problema assegnato.


## FLAPPY BIRD IA
***Spiegazione del codice per intero (solo le parti essenziali)***


## Avvia il codice in Gitpod
[![Avvia in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MattsSalv/Flappy-Bird)
