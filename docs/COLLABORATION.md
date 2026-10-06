# Collaborare mantenendo il proprio prodotto

K-SEO deve poter produrre un risultato utile da solo. Quando un'altra competenza può cambiare il lavoro, forma una domanda concreta per il suo owner invece di delegare genericamente l'intero problema.

## Relazioni tra prodotti

| Prodotto / owner | Contributo | Che cosa resta a K-SEO |
| --- | --- | --- |
| Editoriali | Espressione, argomentazione, organizzazione del contenuto e forme pubbliche | Fonte, bisogno, evidenze dell'incontro e decisione dell'intervento nel proprio dominio |
| Social Kernel | Campo pubblico, conversazioni, relazioni, presenza e conseguenze sulle piattaforme | Relazione tra le fonti e la comprensione che deve diventare possibile |
| Business Manager | Priorità, offerta, valore, risorse e sostenibilità | Le osservazioni non cambiano per adattarsi alla priorità economica |
| Design | Forma percettiva, medium, gerarchia e interazione | Significato da rendere comprensibile e verità della capacità presentata |

Il supporto di base alla scrittura e alla scelta di un intervento è nel metodo locale. Un prodotto fratello più profondo può cambiare domanda, metodo o risultato. Editoriali e Business Manager pubblici sono in preparazione; non nominare URL pubblici, versioni o installazioni non ancora stabiliti.

## Scambio minimo, utilizzabile anche senza API

La richiesta porta una **relazione di lavoro**, non soltanto un testo da migliorare. Per esempio: “Questa pagina descrive l'offerta X; il lettore ha ricostruito Y nel caso Z. Le fonti permettono A e B. Occorre una presentazione che renda distinguibile C. Restituisci contributo e ragioni; la pubblicazione resta nel mio controller”.

Una rappresentazione JSON iniziale può usare:

```json
{
  "schema": "kseo-collaboration/1",
  "request_id": "local-unique-id",
  "purpose": "risultato utile da formare",
  "object": "fonte / pagina / entità",
  "source_refs": [],
  "context": "solo il contesto condivisibile necessario",
  "requested_contribution": "domanda situata",
  "permitted_effects": [],
  "return_to": "owner che continua"
}
```

Il ritorno deve identificare la richiesta, l'owner, il contributo, le fonti/ragioni, la natura proposta o accaduta degli effetti, le questioni aperte e l'apprendimento. È un contratto semantico/documentale, non un connettore implementato né un'autorizzazione eseguibile.

Concorda la proiezione dei dati privati prima di inviare lo scambio. Un altro prodotto non riceve l'intero database per default. Il ritorno non autorizza il ricevitore a eseguire azioni che la richiesta non comprendeva. Un mandato già applicabile può invece coprire gli effetti esplicitamente delegati.

Prima di usare un collegamento, distingui: prodotto leggibile; compatibilità del contributo; trasporto disponibile; ricevitore autenticato; operazione consentita; risultato osservato. Un file inviabile a mano è già un mezzo utile, senza essere presentato come orchestrazione automatica.

Quando il contributo cambia la comprensione, rileggi l'intervento nel contesto cambiato. Porta a ogni owner soltanto la lezione che deve modificarne il metodo. Mantieni l'indipendenza delle istanze e la possibilità di una futura integrazione diversa.
