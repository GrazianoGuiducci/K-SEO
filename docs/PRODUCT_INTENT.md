# Il prodotto che stiamo formando

## Direzione scelta

K-SEO è **LLM-first**. Parte dalla direzione scelta dall'operatore: nel prossimo campo della scoperta online, una parte crescente della relazione tra fonte e persona sarà mediata da LLM e agenti che cercano su siti, piattaforme e altre fonti, confrontano ciò che trovano, formano una risposta, consigliano una scelta o compiono un'azione per l'utente finale.

Questa è una direzione di prodotto e un orizzonte da osservare, non la dichiarazione che la ricerca umana sia già scomparsa o che tutti i sistemi si comportino allo stesso modo. L'umano resta il beneficiario, il proprietario dell'intento e spesso il decisore finale. Cambia però il destinatario intermedio: **l'informazione deve poter essere compresa e usata correttamente anche da un modello che decide che cosa recuperare, quale fonte considerare pertinente, che cosa citare, come confrontarlo e quando suggerirlo**.

K-SEO deve quindi dare a chi possiede un sito un gestore che comprende ciò che il sito offre, a chi si rivolge e quali informazioni permettono a persone, motori, LLM e agenti di trovarlo, comprenderlo e usarlo. Dopo una prima configurazione automatica, il gestore continua a osservare e migliorare la situazione senza richiedere ogni volta una nuova consegna.

La direzione è stata scelta da Graziano Guiducci il 6 ottobre 2026. La formazione procede tra ChatGPT, GPT-Pro e Codex usando le competenze e i kernel già disponibili. Il prodotto entrerà nel catalogo MAIOS. Queste intenzioni sono determinate; la forma concreta resta da sviluppare attraverso conoscenza e lavoro.

Il prodotto si applica principalmente ai siti, perché il sito è la superficie controllabile in cui identità, offerta, fonti, informazioni e azioni possono essere mantenute con continuità. Ma il campo che un LLM ricostruisce è distribuito: può includere articoli, piattaforme, profili, repository, recensioni, notizie, documentazione e altre fonti esterne. Quando queste cambiano materialmente la rappresentazione dell'entità, K-SEO deve saperle osservare e collegare al nucleo del sito senza appropriarsi delle competenze o degli effetti di altri owner.

### Il nuovo oggetto della SEO

La SEO classica tende a osservare una catena come:

~~~text
query -> indice/ranking -> risultato -> clic -> sito
~~~

K-SEO deve poter operare anche sulla catena mediata da LLM:

~~~text
intento dell'utente
-> LLM/agente formula o espande la ricerca
-> recupera fonti da più superfici
-> interpreta entità, affermazioni, prove e alternative
-> seleziona ciò che ritiene utile/affidabile
-> sintetizza, cita, consiglia o agisce
-> l'utente riceve il risultante
-> eventuale visita/azione/risultato per l'attività
~~~

Il lavoro non è “scrivere per convincere il bot” in modo artificiale. È rendere la fonte **semanticamente forte**: chiara sull'entità e sull'offerta, specifica, verificabile, aggiornata, coerente tra superfici, facile da attribuire, utile nelle comparazioni e capace di fornire all'LLM il materiale necessario per una risposta o un'azione corretta.

Per questo K-SEO deve comprendere non soltanto parole chiave, pagine e link ma anche:

- **entity clarity** — chi/che cosa è la fonte e quali relazioni la definiscono;
- **claim clarity** — che cosa afferma davvero, con quali limiti e condizioni;
- **evidence/provenance** — perché una risposta dovrebbe considerarla affidabile o citabile;
- **answerability** — se le informazioni necessarie a una domanda reale sono presenti e recuperabili;
- **comparison readiness** — se differenze, requisiti, prezzi/condizioni quando pubblici, capacità e limiti sono distinguibili senza inferenze arbitrarie;
- **freshness** — quali informazioni sono correnti e quali appartengono a un altro periodo/versione;
- **machine legibility** — struttura semantica, accessibilità e segnali che aiutano retrieval e agenti senza creare contenuto parallelo nascosto;
- **actionability** — se un agente può comprendere e, quando autorizzato, usare correttamente i percorsi d'azione disponibili.

Contenuti esterni, reputazione, canali pubblici e fonti citate diventano quindi parte del campo osservabile quando cambiano ciò che un LLM può recuperare o concludere. Le azioni sulle superfici esterne restano ai rispettivi owner e alle relative autorità.

## Conoscenza e capacità da rendere operative

Il gestore deve poter conoscere il sito e la sua attività: pagine, offerta reale, pubblico, lingue, domande delle persone, fonti affidabili, percorsi di contatto o acquisto, strumenti già in uso e modalità con cui un cambiamento arriva online. Una fotografia iniziale deve poter evolvere mentre cambiano contenuti, obiettivi e ambiente.

L'indagine può rendere pertinenti accessibilità ai motori e agli agenti, indicizzazione, collegamenti, canonical e redirect, qualità tecnica, struttura dei contenuti, dati strutturati coerenti, chiarezza delle entità e delle affermazioni. Le relazioni con ricerca AI, risposte, citazioni e azioni degli agenti devono essere comprese attraverso fonti e comportamento reale. Le [fonti iniziali](SOURCES.md) avviano questa conoscenza senza esaurirla.

Il gestore collega osservazioni e possibilità a interventi utili: correggere una risorsa irraggiungibile, far emergere una pagina utile rimasta isolata, rendere chiara un'offerta, migliorare una risposta incompleta, collegare fonti o aggiornare informazioni diventate inesatte. Può anche approfondire prima di intervenire, o conservare una situazione che non trae beneficio da modifiche.

L'esperienza SEO già maturata fornisce alcune relazioni operative da generalizzare nel prodotto:

- ogni misura conserva fonte, periodo, unità e copertura; un dato assente non diventa zero;
- richieste, persone, sessioni, impressioni, clic, citazioni e risultati dell'attività mantengono significati diversi;
- le visite generate dai controlli del gestore sono riconoscibili e separate dall'attività esterna;
- il nome dichiarato da un client non basta a provare la sua identità;
- i risultati di una singola ispezione non rappresentano automaticamente l'intero sito;
- una correlazione osservata orienta un approfondimento senza diventare prova della causa;
- contenuti e suggerimenti rispettano l'offerta e le fonti reali; volumi, promesse e risultati non vengono inventati.

Sono metodi da incarnare nei dati e negli strumenti scelti per K-SEO. Le prove svolte in un altro ambiente restano attribuite a quell'ambiente.

## Configurazione e autonomia

La prima configurazione dovrebbe ricostruire quanto possibile dal sito e dall'ambiente disponibile, riconoscere gli accessi già presenti e proporre soltanto le informazioni o le scelte che mancano davvero. Il proprietario deve poter capire quali interventi il gestore può svolgere e quali effetti ha autorizzato.

Occorre formare insieme il sapere SEO e i mezzi che lo fanno agire: acquisizione dei dati, strumenti per modificare il sito, esecuzione programmata o attivata da eventi, persistenza, recupero dopo interruzioni, conservazione del lavoro concorrente e verifica del risultato online. Un testo di istruzioni da solo non fornisce queste capacità. L'ambiente scelto può già offrirne alcune; le altre vanno integrate o costruite.

Il prodotto deve poter scegliere un intervento pertinente, portarlo fino al risultato consentito, leggere le conseguenze e apprendere. Una modifica sorgente e una modifica online hanno effetti distinti: il gestore deve conoscerne il percorso reale. Per gli interventi materiali conserva una possibilità di recupero proporzionata al cambiamento.

Il sapere del prodotto, i mezzi con cui viene eseguito e il contesto privato di ogni sito hanno funzioni diverse e devono rimanere collegati. Questa relazione permette adattamenti a CMS, repository, servizi e assistenti senza decidere ora un ambiente universale. Frequenza, costi, priorità e comunicazione all'utente si formano dal caso concreto; il lavoro programmato non deve produrre notifiche prive di un cambiamento utile.

Il gestore conserva ragioni, fonti, risultati, correzioni e possibilità aperte. Quando l'uso produce un miglioramento riutilizzabile, quel sapere cambia il metodo che deve agire meglio. Al rientro raggiunge il punto corrente e le fonti pertinenti. Se una capacità utile esiste ma resta scollegata, la riconnette al lavoro che deve usarla.

## Collaborare con altri kernel

K-SEO deve poter offrire valore da solo e comporre un lavoro quando altre competenze lo migliorano. Editoriali, quando diventerà pubblico, potrà contribuire alla scrittura e revisione; Social Kernel al campo pubblico e alle relazioni; Business Manager alle priorità e al valore per l'attività. Ulteriori collaborazioni possono emergere dalle necessità reali.

La collaborazione porta la domanda, il contesto necessario, le fonti, il risultato atteso e gli effetti consentiti al soggetto che sa svolgere quel lavoro. Il ritorno conserva le ragioni e il risultato realmente prodotto. La disponibilità di una repository o di un nome non dimostra che esista già un collegamento eseguibile. I prodotti mantengono il proprio sapere, stato, strumenti e responsabilità; i dati privati condivisi sono quelli necessari alla collaborazione autorizzata.

## Due situazioni per formare la prima realizzazione

Un sito di servizi ha una guida utile che i visitatori raggiungono con difficoltà. Il gestore ricostruisce domanda, pagina, collegamenti e accesso dei motori; sceglie un miglioramento sostenuto dalle fonti, lo applica nel percorso autorizzato, controlla ciò che è online e osserva gli effetti successivi senza contaminare le misure con i propri test.

Un'offerta viene interpretata in modo incompleto nelle risposte AI. Il gestore raccoglie esempi attribuiti e limitati al contesto osservato, verifica le fonti del sito e individua dove nasce l'ambiguità. Può coinvolgere la competenza di scrittura, portare la correzione fino al sito e conservare ciò che le osservazioni successive rendono comprensibile. La nuova formulazione non garantisce una citazione o un comportamento uniforme di tutti i sistemi.

Queste situazioni aiutano a capire cosa serve per funzionare. La ricerca può far emergere una prima realizzazione più utile e ulteriori capacità.

## Possibilità da approfondire

ChatGPT può ampliare la ricerca su come persone e agenti scoprono, interrogano, confrontano e usano i siti; su quali dati sono realmente ottenibili; su quanto cambiano i risultati tra sistemi, lingue, contesti e periodi; e su come riconoscere un miglioramento significativo per il proprietario.

Sono aperte la forma del gestore, i mezzi di configurazione automatica, le integrazioni iniziali, la persistenza e l'esecuzione, il modello di collaborazione tra kernel, la distribuzione, i costi e la forma dell'offerta. Una possibilità sufficientemente compresa può diventare un progetto e poi una capacità esercitata. La formazione deve produrre sapere utilizzabile e una direzione concreta, lasciando che le nuove relazioni cambino la proposta.
