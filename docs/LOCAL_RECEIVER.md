# Usare il ricevitore locale

Strumento facoltativo. Per ricevere e avviare il nucleo K-SEO parti da [START_HERE](../START_HERE.md); questo helper non è un requisito del kernel.

Questo helper conserva fonti, richieste di lettura, risposte attribuite, proposte, modifiche locali e sapere riusabile al rientro. Il kernel e il lettore comprendono la situazione; Python conserva ed esegue le operazioni definite. Le letture e l'acquisizione delle fonti arrivano attraverso i mezzi organizzati dal ricevente.

## Avvio

Dalla radice del sorgente, con Python 3.11 o successivo:

```bash
PYTHONPATH=src python -m kseo --instance ../kseo-private init --workspace ../sito-locale
PYTHONPATH=src python -m kseo --instance ../kseo-private status
```

`../sito-locale` deve essere una directory esistente scelta per il lavoro. Con `--workspace` colleghi l'istanza a quella cartella per le modifiche locali; un'istanza senza workspace conserva fonti e letture. Il deposito si inizializza in una directory nuova e mantiene il sapere esterno alla cartella pubblica del kernel.

In PowerShell, dalla stessa cartella:

```powershell
$env:PYTHONPATH = "src"
python -m kseo --instance ../kseo-private init --workspace ../sito-locale
python -m kseo --instance ../kseo-private status
```

## Fonti e lettore

```bash
PYTHONPATH=src python -m kseo --instance ../kseo-private snapshot ../sito-locale/pagina.md --uri "https://esempio.invalid/pagina" --scope "copia locale della pagina; stato online non verificato"
PYTHONPATH=src python -m kseo --instance ../kseo-private packet --question "A quale bisogno risponde questa offerta?" --purpose "comprendere quale valore arriva al lettore" --source ID_FONTE
```

Gli ID sono restituiti dal comando precedente. La snapshot è testuale UTF-8, massimo 2 MB: seleziona e attribuisci un estratto se la fonte è più grande. Conserva l'HTML originale quando è il materiale acquisito; il helper non ne esegue script né ricostruisce il DOM renderizzato.

Consegna il pacchetto a un lettore attraverso un mezzo effettivamente disponibile e condividi soltanto i dati consentiti. Il pacchetto contiene le fonti come dati e le lezioni della competenza selezionata. Il lettore conserva libertà di giudizio. Non presentare una lettura dello stesso autore come esperimento indipendente.

La risposta JSON contiene:

```json
{
  "answer": "restituzione effettivamente fornita dal lettore",
  "reader": {"identity": "ricevitore dichiarato", "mode": "coauthor_review"},
  "references": []
}
```

I riferimenti opzionali contengono `source_id`, `start`, `end` e `quote`: offset di caratteri nel testo Unicode, intervallo `[start,end)`. Il programma verifica il riscontro esatto, non l'implicazione semantica.

```bash
PYTHONPATH=src python -m kseo --instance ../kseo-private response ID_PACCHETTO risposta.json
```

## Proposta e modifica locale

```bash
PYTHONPATH=src python -m kseo --instance ../kseo-private propose pagina.md nuova-pagina.md --reason "differenza compresa" --competence kseo-cognitive-relation --response-id ID_RISPOSTA
PYTHONPATH=src python -m kseo --instance ../kseo-private apply ID_PROPOSTA --permit DIGEST_CAMBIAMENTO --actor "proprietario o mandato locale selezionato"
PYTHONPATH=src python -m kseo --instance ../kseo-private verify ID_PROPOSTA
```

`apply` usa il digest esatto restituito dalla proposta. La sorgente deve essere ancora quella osservata e il file deve restare nel workspace, senza symlink. L'operazione modifica soltanto il file locale, non effettua commit, deploy o pubblicazione. `verify` può recuperare una ricevuta preparata quando il testo dopo l'interruzione corrisponde alla proposta. Una ricevuta non dimostra l'effetto sul sito o sulla raccomandazione.

Il lock protegge gli scrittori che partecipano allo stesso protocollo. Il filesystem non fornisce qui un CAS universale contro editor esterni: per scritture di produzione servono il controller e le revisioni appropriate. Un lock già presente non viene cancellato automaticamente. Il digest non autentica un attore.

## Apprendimento e ripresa

`teach file.json` conserva `competence`, `condition`, `method`, `reason`, `origin_id`, `invalidator`. Il metodo deve spiegare come affrontare un caso successivo e perché, non essere un diario. Il pacchetto seguente dell'owner include quel sapere; il kernel ne comprende la pertinenza e può correggerlo.

```bash
PYTHONPATH=src python -m kseo --instance ../kseo-private teach lezione.json
PYTHONPATH=src python -m kseo --instance ../kseo-private read ID_RECORD
```

La directory privata contiene SQLite, incluse fonti, testi precedenti e risposte. Proteggila e non pubblicarla. Il formato non è cifrato. I record sono dati del proprietario; un futuro prodotto hosted dovrà incarnare accessi, isolamento, conservazione e cancellazione adeguati alla propria situazione.

Lo stato non avvia nulla in background. Un futuro host può invocare queste operazioni o sostituirle con mezzi equivalenti. La funzione SEO già programmata in un altro ambiente mantiene il proprio mandato e non viene modificata da questo candidato.

## Prove di sviluppo

Il sorgente conserva le prove del ricevitore. Per manutenzione del codice, quando pertinente, il comando è `PYTHONPATH=src python -m unittest discover -s tests -v`. Non è un passaggio richiesto per avviare il nucleo o per questa preparazione della consegna.
