# Fonti e basi iniziali

Ricognizione del 6 ottobre 2026. Questo primo giro è selettivo: le fonti possono cambiare e non descrivono tutti i sistemi di ricerca o tutti gli agenti. Un requisito di un fornitore conserva il proprio ambito.

## Ricerca e accesso ai siti

Google conferma che i principi SEO restano applicabili ad AI Overviews e AI Mode: non richiedono ottimizzazioni speciali, file AI o uno schema aggiuntivo. L'idoneità passa da indicizzazione e possibilità di mostrare uno snippet. Le risposte possono coinvolgere più ricerche collegate. Il traffico delle funzioni AI confluisce nel rapporto Web di Search Console. Queste indicazioni riguardano Google, senza garantire inclusione o fornire una misura separata di ogni risposta AI. [Google Search Central — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features).

OpenAI distingue OAI-SearchBot per la ricerca, GPTBot per contenuti potenzialmente usati nell'addestramento e ChatGPT-User per azioni avviate dagli utenti. I controlli hanno scopi distinti; le richieste avviate dall'utente possono avere un comportamento diverso rispetto ai crawler automatici. La fonte pubblica anche intervalli IP. K-SEO dovrà comprendere l'effetto concreto di una politica di accesso invece di applicare un'unica categoria generica a tutti i client AI. [OpenAI — Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots).

Nel febbraio 2026 Bing ha annunciato in anteprima pubblica AI Performance per osservare citazioni nelle esperienze AI supportate. Citazioni, pagine citate e query di recupero hanno coperture e unità proprie: non equivalgono a posizione, importanza o autorità di una pagina. Le query mostrate costituiscono un campione. È una possibile fonte da verificare nell'account e nell'interfaccia realmente disponibili. [Bing — Introducing AI Performance in Bing Webmaster Tools](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/).

Da queste fonti ricaviamo una prima relazione di progetto: conservare la base SEO, comprendere i diversi modi in cui i sistemi accedono al sito e misurare ciò che ogni fonte permette realmente di osservare. È una sintesi di formazione, da approfondire attraverso ulteriori fonti e casi.

## Kernel pubblici da cui conoscere il saper fare

Le identità seguenti sono snapshot sorgente letti il 6 ottobre. Non sono dichiarazioni di installazione o prove di autonomia K-SEO. Gli aggiornamenti successivi possono rendere pertinente una nuova lettura.

| Base pubblica | Relazione utile da studiare | Fonte osservata |
| --- | --- | --- |
| kernel_chat | Continuità controllata dall'utente, fonti, competenze che apprendono, rientro e adattamento ai mezzi reali del destinatario | [README a `82a5bd7`](https://github.com/GrazianoGuiducci/kernel_chat/blob/82a5bd78f5ecb667e6392e1dd149be2c34c4ec3c/README.md) |
| Social Kernel | Contesto persistente, adozione nel sistema dell'utente, composizione del lavoro e capacità effettive dell'ambiente | [BOOT a `dc7ee3d`](https://github.com/GrazianoGuiducci/social-kernel/blob/dc7ee3d2ef6bac888836d4389d3ceb2a2777d42e/BOOT.md), [KERNEL](https://github.com/GrazianoGuiducci/social-kernel/blob/dc7ee3d2ef6bac888836d4389d3ceb2a2777d42e/KERNEL.md) |
| MAIOS Project Kernel | Formazione e combinazione di competenze, apprendimento che modifica il metodo, conoscenza e prosecuzione tra agenti | [README a `af333b1`](https://github.com/GrazianoGuiducci/maios-project-kernel/blob/af333b106a34601c03a5c4854eb0e45f89af44f3/README.md) |

I metodi pertinenti vanno raggiunti nei loro corpi quando il lavoro li rende utili. K-SEO ne trasferirà le funzioni nella propria situazione e nel linguaggio del prodotto. Il riuso materiale conserverà provenienza, compatibilità e obblighi delle licenze: Apache-2.0 per kernel_chat e Social Kernel, MIT per MAIOS Project Kernel, secondo i metadati GitHub verificati in questa ricognizione. La licenza K-SEO è ancora da scegliere.

Editoriali e Business Manager sono relazioni di collaborazione indicate dall'operatore. I rispettivi repository non sono pubblici alla data della ricognizione: non si presume che un destinatario possa leggerli o usarli. Il sapere necessario potrà arrivare attraverso un contributo autorizzato o una futura superficie pubblica. Non sono dipendenze obbligatorie per l'avvio di K-SEO.

## Conoscenza già maturata nel lavoro SEO

Codex ha riportato nell'[intento](PRODUCT_INTENT.md#conoscenza-e-capacit%C3%A0-da-rendere-operative) una sintesi funzionale dell'esperienza interna su analisi del traffico, richieste diagnostiche riconoscibili, ispezioni di indicizzazione, intenzioni di ricerca, collegamenti e continuità degli interventi. Sono metodi generalizzati, senza trasferimento di dati privati, credenziali o stato dei siti. K-SEO dovrà costruire e provare la propria incarnazione.

## Ricerca successiva

Il primo giro lascia aperti altri fornitori, protocolli e strumenti per agenti, studi empirici, casi di adozione, integrazioni con siti e CMS, misure dei risultati, costi e modalità di distribuzione. Occorre distinguere documentazione, affermazioni commerciali, risultati sperimentali e ipotesi. Una conoscenza utile deve cambiare il sapere o il metodo che la userà, oltre ad aggiungere un riferimento.

## Secondo giro ChatGPT — 6 ottobre 2026

Il contributo completo è in [work/CHATGPT_FORMATION_RETURN_2026-10-06.md](../work/CHATGPT_FORMATION_RETURN_2026-10-06.md). Questo giro amplia il primo senza sostituirne le fonti.

Relazioni che cambiano il prodotto:

- Google tratta AEO/GEO come prosecuzione della SEO per le proprie funzioni AI e dichiara di non usare `llms.txt` come requisito della Ricerca AI; distingue inoltre report prestazioni AI e controllo di inclusione in Search Console.
- Bing espone misure AI proprie — citazioni, intenti, topic, citation share e confronti — che non sono equivalenti alle metriche Google.
- OpenAI, Anthropic e Perplexity distinguono ruoli diversi per crawler di ricerca, training e richieste avviate dall'utente; K-SEO deve conservare il perimetro del singolo provider.
- L'usabilità agentica rende pertinenti HTML semantico, accessibilità e controlli azionabili; protocolli transazionali come UCP restano un orizzonte situato, non un requisito universale.
- La letteratura GEO recente va trattata come ricerca sperimentale: engine, lingua, query e retrieval cambiano i risultati; non è una base sufficiente per una metrica causale universale.

Nuove fonti primarie/provider:

- [Google — Generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Search Console — Generative AI performance](https://support.google.com/webmasters/answer/16984139)
- [Google Search Console — Generative AI inclusion control](https://support.google.com/webmasters/answer/16908024)
- [Google Search Console API](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Google — Robots meta and snippet controls](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [web.dev — Agent-friendly websites](https://web.dev/articles/ai-agent-site-ux)
- [OpenAI — Crawlers](https://developers.openai.com/api/docs/bots)
- [OpenAI — Publishers and developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [Bing — AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)
- [Bing — AI Visibility Insights](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/)
- [Bing Webmaster API](https://learn.microsoft.com/en-us/bingwebmaster/)
- [IndexNow](https://www.indexnow.org/documentation)
- [Anthropic — crawler controls](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [Perplexity — crawler controls](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Universal Commerce Protocol](https://ucp.dev/)

Fonti di ricerca da mantenere distinte dalla documentazione provider:

- Chen et al., *Generative Engine Optimization: How to Dominate AI Search*, arXiv:2509.08919 (2025).
- Martinez, *Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026)*, arXiv:2607.14035 (2026).
- *Marketing Science*, *ChatGPT Referrals to E-Commerce Websites: How Do LLMs Compare Against Traditional Channels?*, DOI 10.1287/mksc.2025.0489 (2026).

Confine operativo importante: le superfici UI documentate per i nuovi report AI non dimostrano automaticamente parità con le API pubbliche. Fino a esercizio reale, K-SEO deve distinguere dati API, osservazione browser/UI, export e input manuale.

## Direzione LLM-first: stato della prova — 6 ottobre 2026

L'operatore seleziona come orizzonte di prodotto una scoperta online sempre più mediata da LLM e agenti. **Le fonti correnti supportano la direzione, non la formulazione assoluta “a breve ci saranno solo LLM”.** K-SEO conserva questa differenza perché la previsione temporale non deve diventare un falso requisito tecnico.

Evidenze correnti che rendono la direzione già operativa:

- Google dichiara che le preferenze degli utenti si stanno spostando rapidamente verso esperienze di AI generativa per trovare informazioni e collega la SEO corrente alle proprie esperienze AI.
- Bing parla esplicitamente di visibilità nell'“AI web” e misura citazioni, intenti, topic e citation share nelle risposte AI.
- ChatGPT Search ricerca sul web e restituisce risposte con fonti/citazioni; OpenAI fornisce ai publisher controlli di discovery tramite OAI-SearchBot e referral attribuibili.
- OpenAI e web.dev documentano già interazione agentica con i siti attraverso struttura semantica/accessibilità e controlli interattivi riconoscibili.

Da queste fonti K-SEO può assumere già oggi che **l'LLM è un destinatario intermedio reale**, senza assumere che sia l'unico canale. Questo giustifica una progettazione LLM-first mantenendo compatibilità e valore umano.

Fonti pertinenti:

- [Google — Generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Bing — AI Visibility Insights](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/)
- [OpenAI — ChatGPT Search](https://help.openai.com/en/articles/9237897-chatgpt-search)
- [OpenAI — Publishers and developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [web.dev — Agent-friendly websites](https://web.dev/articles/ai-agent-site-ux)
