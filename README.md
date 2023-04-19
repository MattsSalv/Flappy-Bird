# Vincere a Flappy Bird grazie all'IA  <img src="https://www.unidformazione.com/wp-content/uploads/2017/10/unibs-universita-di-brescia.jpg" style="background-color:white;" alt= “error” width="20%" height="20%" align="right"> 
<p align="center" ><b><i>di Mattia Salvatti e Claudio Onorati </b></i></p>

<br> <br>

Il progetto ha l'obbiettivo di utilizzare l'algoritmo genetico ***NEAT*** per imparare a giocare a ***Flappy Bird***.

Il gioco è stato ricreato in Python ed è stata utilizzata la libreria ***NEAT-Python*** per implementare l'algoritmo genetico.

<br>

<p align="center">
 <img src="https://github.com/MattsSalv/Flappy-Bird/blob/master/images/Cover.png" alt= “” width="40%" height="40%">
</p>

<br> 
 


>**NB** è necessario installare le seguenti librerie per avviare il programma: 
> - NEAT-Python <https://neat-python.readthedocs.io/en/latest/installation.html> 
> - PyGame <http://www.pygame.org/downloads.shtml>
> - ...



<br> <br>



## Avviare il programma
***comandi base  per avviare il programma (DA CANCELLARE)***



<br> <br>



## NEAT
***NeuroEvolution of Augmenting Topologies*** (**NEAT**) è un *algoritmo genetico* (GA) per la generazione di *reti neurali evolutive artificiali*, per la risoluzione di attività di *Reinforcement Learning*, in particolare in presenza di informazioni *Hidden State*. La sua unicità è data dalla  capaità di creare una sua struttura sempre più complessa e nel contempo sempre più ottimale (analoga all'evoluzione naturale). 
L'alogritmo è stato originariamente sviluppato Kenneth Stanley e Risto Miikkulainen nel 2002 all'Università del Texas ad Austin. 

A partire da reti estremamente semplici, in quanto completamente prive di neuroni intermedi, NEAT ha generalmente performance più elevate nella ricerca di soluzioni  efficaci e robuste rispetto ad algoritmi di *reinforcement leaening* o a tecniche neuro-evolutive analoghe che però partono da topologie predeterminate o comunque casuali. Ciò è possibile grazie all'uso di strutture iniziali minime che sono facili da ottimizzare e rendono l'algoritmo estremamente veloce nella ricerca di soluzioni.

L'algorimo si basa su tre princìpi fondamentali:

1. **OMOLOGIA**: NEAT codifica ciascun nodo e ciascuna connessione della rete attraverso un gene. Ogni volta che una mutazione strutturale sfocia nella creazione di un nuovo gene, quel gene riceve un contrassegno numerico che lo rende permanentemente rintracciabile. Tale marcatura storica è utilizzata in seguito per verificare la conciliabilità di geni omologhi durante l'operazione di crossover, e per definire un operatore di compatibilità;

2. **PROTEZIONE DELL'INNOVAZIONE**: L'operatore precedente di compatibilità divide la popolazione composta da reti neurali in specie differenti, allo scopo di proteggere le soluzioni innovative da un'eliminazione prematura, e di prevenire l'incrocio di materiale genetico incompatibile. Tali innovazioni strutturali presentano una significativa possibilità di raggiungere il loro pieno potenziale, in quanto protette dal resto della popolazione attraverso la suddivisione in specie, ovvero la creazione di nicchie o spazi riservati;

3. **STRUTTURA MINIMA**: da ultimo, il principio secondo cui la ricerca di una soluzione dovrebbe avvenire nel più piccolo spazio possibile (inteso come numero di dimensioni), da espandere poi in maniera graduale. Cominciando il processo evolutivo da una popolazione di elementi a struttura minima, le successive mutazioni topologiche comportano l'aggiunta di nuovi nodi e connessioni alle reti, conducendo pertanto ad una crescita incrementale della popolazione stessa. Dal momento che solo le modifiche strutturali vantaggiose tendono a sopravvivere nel lungo termine, le topologie che vengono raffinate tendono ad essere le minime necessarie alla soluzione del problema assegnato.

L'utilizzo dell'algoritmo porta i seguenti vantaggi rispetto ad analoghi GA:

1. **Velocità**: Strutture più piccole si ottimizzano più velocemente. Inoltre, anche se nel tempo aumenta la complessità, la maggior parte delle strutture preesistenti sono già ottimizzate.
2. **Fuga da un'optima locale**: Non solo NEAT attraverso l'*accoppiamento* e la *mutazione* può cercare la forma del suo ambiente, ma può anche alterare l'ambiente stesso con nuove strutture. Così, quando una specie in NEAT si trova su un optimum locale, è possibile che aggiungendo una nuova connessione, si possa aprire una nuova dimensione di libertà, che porta a un percorso di allontanamento dall'optimum locale.

<br> <br>

**DIZIONARIO NEAT:**
- **Gene Nodo**: Rappresenta il nodo vero e proprio, ognuno di essi trasporta l'informazione di *Numero di Nodo*, *Tipologia di Nodo* intesa come Input/Hidden/Output e altre informazioni.
- **Gene di Connessione**: Collegamento tra due *Geni Nodo*, ognuno di essi trasposta l'informazione di *Nodo d'Ingresso*, *Nodo d'Uscita*, *Peso della Connessione*, un *Enable Bit* per l'espressione o non del gene, e un *Numero di Innovazione*
- **Genotipo**: Singolo insieme di *Geni Nodo* e *Geni di Connessione*.
- **Fenotipo**: Singola rappresentazione della topologia di una singola rete di *Geni Nodo* e *Geni di Connessione*
- **Specie**:
- **crossover**:
- **Accoppiamento**:
- **Mutazione strutturale**: evento che può cambiare sia il *Peso della connessione* che la *Topologia della Rete*, avviene in 2 modalità, *aggiungendo una connessione* tra due nodi non connessi precedentemente oppure *aggiungendo un nodo* in una connessione preesistente 



<br> <br>

## COME VIENE USATO NEAT IN FLAPPY BIRD
 ***Spiegazione di come neat è stato implementanto nel gioco (DA CANCELLARE)***
 
<br> <br>


## FLAPPY BIRD IA CODE
***Spiegazione del codice per intero (solo le parti essenziali) (DA CANCELLARE)***



<br> <br>



## Avvia il codice in Gitpod
[![Avvia in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MattsSalv/Flappy-Bird)
