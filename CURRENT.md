# K-SEO — punto corrente

Aggiornato: 6 ottobre 2026.

Graziano Guiducci ha selezionato K-SEO come prodotto pubblico da sviluppare e aggiungere al catalogo MAIOS: un'entità per gestire la presenza online di siti nella ricerca umana e agentica, con prima configurazione automatica, autonomia e collaborazione con altri kernel.

Codex ha preparato la base conoscitiva iniziale: intento, relazioni operative da trasferire, prime fonti ufficiali, basi pubbliche raggiungibili e [input per ChatGPT](work/CHATGPT_INPUT.md). La repository inizialmente vuota contiene ora questo lavoro di formazione. Nessun gestore K-SEO, installazione, connettore o funzionamento autonomo è ancora implementato o provato. La licenza del nuovo prodotto è da scegliere.

Il seguito selezionato è il contributo di ChatGPT: approfondire le possibilità del settore e formare il sapere, le competenze e una proposta concreta del prodotto. GPT-Pro e Codex contribuiranno secondo ciò che il lavoro renderà utile, anche con progettazione e implementazione. L'architettura, l'ambiente di esecuzione e la distribuzione emergeranno da questa formazione.

La [guida del prodotto](docs/PRODUCT_INTENT.md) conserva direzione e possibilità; le [fonti](docs/SOURCES.md) qualificano le basi attuali. La prima realizzazione dovrà rendere possibile un movimento utile completo su un sito reale, con accessi e autorità scelti dal suo proprietario. Quel risultato formerà il seguito senza limitare il prodotto al primo caso.

Questo punto cambia quando un nuovo contributo dell'operatore, una fonte pertinente, un progetto sufficientemente formato o le conseguenze d'uso modificano materialmente il lavoro.

## ChatGPT product-formation pass — 6 ottobre 2026

Il contributo selezionato è stato svolto sul branch `work/chatgpt-product-formation-20261006`, senza modificare `main`.

Risultante candidata:

- K-SEO non viene ristretto a una serie di tattiche GEO: gestisce la reperibilità, comprensibilità e usabilità del sito tra ricerca umana e sistemi agentici;
- conserva separate almeno sei relazioni osservabili: accessibilità, scoperta/indicizzazione, comprensibilità, presenza/citazione, usabilità e risultato utile per l'attività;
- usa un contratto di evidenza con fonte, metodo, periodo, scope, unità e copertura invece di un unico punteggio AI opaco;
- separa il prodotto pubblico dallo stato privato di ogni sito;
- separa il sapere K-SEO dai provider che forniscono API, browser, CMS, repository, scheduler o altri controller;
- tratta Editoriali, Social Kernel e Business Manager come owner distinti che partecipano solo quando cambiano realmente il movimento;
- propone come prima prova un vertical slice completo: capire un sito reale, trovare una differenza supportata, intervenire attraverso un'autorità reale, verificare il risultato online, osservare le conseguenze e restituire apprendimento.

Fonte del contributo:
`work/CHATGPT_FORMATION_RETURN_2026-10-06.md`.

`docs/SOURCES.md` contiene il secondo giro di fonti ufficiali e di ricerca.

### Seguito candidato

Il prossimo movimento non è costruire una dashboard né fissare subito un SaaS. La proposta da sottoporre a GPT-Pro/Codex è realizzare il più piccolo reference slice che eserciti il ciclo causale completo e lasci stato/evidenza/receipt recuperabili.

Restano aperti, senza bloccare la progettazione: licenza K-SEO, primo sito controllato, host iniziale, prima fonte autenticata, primo controller di scrittura/pubblicazione, scheduler e forma economica.

Questa sezione descrive una proposta formata sul branch, non una decisione già integrata nel `main` e non una capacità K-SEO già esercitata.

## Direzione LLM-first selezionata — 6 ottobre 2026

Graziano ha reso centrale una relazione che il primo giro trattava ancora come una delle possibilità: **K-SEO deve nascere per il campo in cui LLM e agenti diventano sempre più spesso l'intermediario tra le fonti online e l'operatore finale**.

La previsione “a breve solo LLM” resta un orizzonte dell'operatore da osservare, non un fatto esterno già provato. Il prodotto però può e deve essere progettato ora per questa transizione.

La risultante del branch cambia quindi da “SEO + AI/agentic visibility” a:

~~~text
fonte/sito reale
+ campo pubblico distribuito recuperabile
+ chiarezza di entità / offerta / claim / prova / condizioni / freschezza
+ accessibilità e leggibilità per retrieval e agenti
+ evidenza provider-specifica
-> LLM può recuperare e comprendere la fonte
-> può attribuirla / citarla / confrontarla
-> può raccomandarla o usarla quando pertinente
-> operatore finale riceve una risposta/azione migliore
-> conseguenze ritornano a K-SEO
~~~

Il sito resta il nucleo controllabile. Piattaforme, articoli, profili, repository, recensioni, notizie e altre fonti diventano campo osservabile quando possono cambiare la rappresentazione che un LLM ricostruisce. Gli effetti su quelle superfici restano ai rispettivi owner (per esempio Social Kernel).

La prima implementazione deve quindi provare non soltanto crawl/indexing ma almeno una relazione di **machine comprehension**: K-SEO deve poter individuare un'informazione importante che un LLM potrebbe recuperare in modo ambiguo, incompleto o debole, formare una correzione source-faithful, applicarla sul sito se autorizzato e verificare poi sia lo stato live sia le evidenze successive disponibili.

Il linguaggio pubblico resta semplice. Termini come KA, FDLA, entity graph, retrieval o competence formation non sono prerequisiti per usare il prodotto.