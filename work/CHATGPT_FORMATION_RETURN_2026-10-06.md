# ChatGPT formation return — K-SEO

Date: 2026-10-06
Source base: K-SEO main at f3dde786e3f099683a42c22a9ec696d9c4092a9a
Status: product/knowledge formation candidate; no runtime, installation or site effect is claimed.

## Resultant

K-SEO should not be formed as a collection of GEO tricks or as a rank tracker with an AI label.

Product relation:

> K-SEO is a continuing AI manager for a website's discoverability, intelligibility and usability across human search and agentic systems. It learns the site and the business, obtains evidence from the sources actually available, chooses useful interventions, carries authorized changes through the real publication path, verifies what became live, observes later consequences and improves its method.

Simple product language:

> K-SEO knows your site and keeps improving how people and AI systems can find it, understand it and use it.

This keeps ordinary SEO as a foundation while admitting AI search, citations, agent browsing and later agentic transactions without pretending they are one metric or one provider.

## What the second formation pass changed

### AI SEO is not one separate technical layer

Google's current guidance says ordinary SEO remains relevant to AI Overviews and AI Mode and that its AI search does not require a special schema or LLMS.txt file. The product should therefore avoid an independent GEO checklist and instead model, for every provider, what makes a resource accessible, how it is discovered or retrieved, what controls the owner has, what evidence is exposed and what remains unobservable.

### Measurement is provider-specific

Google Search Console now exposes a generative-AI performance report and a separate inclusion control. Bing Webmaster Tools exposes AI Performance and later added Intents, Topics, Citation Share and Compare. These measures are not equivalent.

K-SEO should preserve an evidence vector rather than collapse everything into one proprietary visibility score whose denominator and coverage are unknown.

### Visibility and agent usability are related but distinct

Current guidance for agent-friendly sites emphasizes semantic HTML, accessibility structures, stable interactive controls and explicit action affordances. Emerging protocols such as UCP extend this into machine-readable commerce capabilities. This suggests a wider path:

~~~text
found -> understood -> cited or linked -> visited -> usable by an agent -> action completed -> business result
~~~

A site may perform well at one relation and poorly at another. K-SEO should diagnose the actual break.

### Provider controls must retain their scope

OpenAI, Anthropic and Perplexity distinguish automatic search crawlers, training crawlers and/or user-initiated fetchers in different ways. Google has separate controls for its own generative search surfaces. K-SEO should therefore model exact provider policy rather than expose one semantically false global allow-AI-bots switch.

### GEO evidence remains conditional

Recent research supports engine, query, language and retrieval differences. A 2026 critical survey treats discoverability, retrieval, citation, absorption and downstream behavior as distinct stages and finds no reviewed tactic with stable longitudinal cross-platform causal proof. K-SEO should experiment and learn without promoting one correlation into a universal rule.

## Six observable relations

### 1. Accessible

Can relevant systems reach the resource? HTTP/rendering, robots and page directives, snippets, provider inclusion controls, WAF/crawler compatibility, sitemaps/IndexNow and JavaScript barriers belong here.

### 2. Discoverable

Can search systems find and index the right resources? Index state, canonicalization, redirects, orphaned pages, internal links, sitemap state, crawl errors and change discovery belong here.

### 3. Understandable

Does the public site express the business, entities, offers, claims and relationships coherently? Page purpose, organization/product/service identity, headings, evidence, structured data consistent with visible content, multilingual consistency and first-hand expertise belong here.

Structured data is one useful representation, not a magic AI-ranking layer.

### 4. Referenced

Where does the site actually appear in qualified evidence? Ordinary search impressions and queries, Google generative-AI impressions, Bing AI citations/intents/topics/citation share, attributed experiments and referral URLs should retain provider, time and environment.

### 5. Usable

Can humans and agents act successfully? Page experience, semantic HTML/accessibility, forms, stable controls, task completion and future protocols such as WebMCP or UCP when materially relevant belong here.

### 6. Valuable

Does discovery or use produce the result the owner values? Qualified sessions, leads, sales, subscriptions, downloads, applications or another site-specific result belong here.

K-SEO must be able to report that visibility changed while business value did not, or vice versa.

## Evidence contract

Every observation should preserve enough information to prevent false comparison:

~~~text
source/provider
acquisition method
time or period
page/entity/query/task scope
unit
coverage and known limits
raw value or evidence
interpretation
confidence/status
~~~

Existing K-SEO invariants remain core: missing is not zero; impression, click, session, citation, prompt response and conversion are distinct units; K-SEO diagnostic traffic should be recognizable; a user-agent string does not prove identity; one inspected URL does not represent the whole site; correlation may choose the next investigation without proving cause.

### No universal AI visibility score in v1

A later interface may summarize evidence for humans, but provider-native observations and coverage remain inspectable.

## Public product and private site instance

### Public K-SEO

May contain domain methods, schemas/contracts, adapters, deterministic tools, tests, public provider references, reusable competences, setup/runtime code and migration/update logic.

### Private site instance

Contains or points to site inventory, business goals, connected accounts, secrets, Search Console/analytics/Webmaster state, CMS or repository bindings, site-specific learned context, effect policies, intervention history, receipts, private conversions/revenue and scheduled operational state.

Private site state must not leak into the public product as examples, tests or learned rules unless deliberately de-identified and approved.

## Initial configuration

### Pass 1 — automatic public discovery

Given a domain, inspect robots.txt, sitemaps, representative URLs, response state, redirects, canonicals, index directives, titles/descriptions/headings, internal links, structured data, languages/hreflang, rendering/JavaScript dependence, semantic/accessibility signals, performance evidence where useful and known crawler policy.

The result is a qualified site model and coverage map, not a claim that the business is fully understood.

### Pass 2 — infer the environment

Detect or ask only when necessary: repository-backed vs CMS-managed publication, available analytics/search sources, languages, main offer/action, local/e-commerce relevance, logs and the owner's actual outcome.

### Pass 3 — connect optional evidence sources

Initial candidates: Google Search Console, GA4 or another analytics owner, Bing Webmaster Tools, source repository/CMS, server/CDN logs, Merchant/local sources when relevant. Lack of one source reduces evidence coverage; it does not automatically block K-SEO.

### Pass 4 — resolve effect authority

Keep independent authorities such as observe only, propose changes, write source without publishing, publish bounded site changes, submit supported discovery/index notifications, change provider controls and perform external/public effects.

These are authorities, not maturity levels.

## Capability architecture

Provider capability and semantic product knowledge stay separate. A capability adapter should expose at least:

~~~text
capability
controller/provider
read/write/effect class
authentication state
scope
recovery/readback path
availability
~~~

Initial capability families: public web inspection; Google Search; Bing/Microsoft Search; AI crawler/access policy; analytics/business outcomes; source/CMS intervention.

Important current boundary: official Google documentation establishes the generative-AI report and inclusion control in Search Console, but the current Search Console API documentation does not establish a dedicated generative-AI API surface. Likewise, Bing's generic Webmaster API documentation does not establish that all new AI Performance fields are exposed programmatically. K-SEO must keep API evidence, UI/browser evidence and manual evidence distinct until exercised.

## Runtime and scheduling

K-SEO needs a cycle invokable by different hosts. A candidate command surface is:

~~~text
kseo init <site>
kseo inspect
kseo cycle
kseo apply <intervention>
kseo verify <intervention>
kseo status
~~~

The exact CLI is not product identity. The same cycle may later be called manually, by cron/systemd, CI, a desktop receiver, VPS or hosted service. Do not build an internal scheduler when the receiving host already supplies one.

Scheduled runs should remain quiet when no material difference exists.

## Candidate reference implementation

A small open reference runner is the most useful next engineering form because it can exercise the causal cycle without deciding the final commercial host.

Candidate, subject to implementation review:

- Python 3.12+ package/application;
- SQLite for local evidence, state and receipts;
- secrets outside the repository via environment/OS/provider store;
- HTTP crawler plus optional browser adapter;
- typed provider adapters;
- JSON/YAML configuration/schema;
- deterministic audit helpers where possible;
- domain competence layer for interpretation/intervention;
- host-invokable cycle rather than a mandatory daemon.

Python is proposed for implementation leverage, not as K-SEO identity.

## First vertical slice

The first build should prove one complete useful movement, not maximize audit checks.

1. Initialize one owner-controlled site.
2. Build the public site model.
3. Connect at least one owner-native search data source if available.
4. Connect one real source/publishing path or operate in propose-only mode.
5. Record effect authority and recovery.
6. Select one materially supported issue/opportunity; no useful change is a valid result.
7. Form the smallest intervention.
8. Carry it through the actual authorized source/CMS path.
9. Read back the live site state.
10. Observe later consequences only through measures that can answer the hypothesis.
11. Return reusable learning to the competence that must behave differently next time.

Immediate live verification proves the intended site state exists. It does not prove SEO or AI-visibility improvement.

## Collaboration with sibling kernels

K-SEO remains independently useful. Other owners participate only when they change the movement.

### Editoriali

K-SEO owns the site/search problem and evidence. Editoriali owns reusable writing method. Do not send a generic rewrite-for-SEO request; send the page purpose, receiver, ambiguity/evidence, site truth, constraints and intended result.

### Social Kernel

K-SEO owns site discoverability. Social Kernel owns the changing public field and relationships. Use it when public conversations, third-party representations, off-site sources or public consequences materially change the site/search movement. Do not manufacture mentions merely to influence AI systems.

### Business Manager

K-SEO may detect many technically valid opportunities. Business Manager can change which matters economically when priority depends on offer, conversion path, customer relation, resources or product strategy. Business priority does not alter underlying search evidence.

### Portable collaboration envelope

Request: purpose; site/object; minimum context; qualified sources/evidence; current hypothesis; expected useful return; allowed effect class.

Return: owner; contribution/result; sources/reasons; evidence status; proposed or occurred effects; unresolved differences; reusable learning.

## Competence functions to make reachable

Do not create all of these as files before real use. The first vertical slice should reveal their proper continuing bodies.

1. Site understanding.
2. Search access and inclusion.
3. Evidence and measurement.
4. Content/entity intelligibility.
5. Agent usability.
6. Intervention and effect.
7. Consequence and learning.
8. Capability composition.

## Product/business horizon

The public reference product can coexist later with setup/integration, managed operation, hosting, business-specific connectors, review/consulting, agency/partner deployment or enterprise/private instances.

Do not set pricing or force a service form before the first complete site exercise supplies delivery evidence.

## Proposed next engineering movement

Objective for GPT-Pro/Codex:

> Implement the smallest K-SEO reference slice that can initialize a real site, preserve evidence semantics, identify one supported intervention, carry it through an authorized source path, verify the live result and leave a durable readback/learning state.

Suggested outputs:

1. public package/project structure;
2. site-instance schema separated from secrets;
3. observation/evidence schema;
4. capability-adapter interface;
5. public web inspector;
6. at least one search-data adapter;
7. one source/CMS write adapter or propose-only fallback;
8. effect receipt and recovery relation;
9. one cycle command;
10. tests for missing data, provenance, partial coverage and readback;
11. one controlled real-site exercise after the owner selects site and authority.

Do not build the dashboard first. Represent capability after the causal cycle works.

## Qualified sources added by this pass

Provider/official sources:

- Google generative-AI search optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google Search Console generative-AI performance report: https://support.google.com/webmasters/answer/16984139
- Google Search Console generative-AI inclusion control: https://support.google.com/webmasters/answer/16908024
- Search Console API: https://developers.google.com/webmaster-tools/v1/api_reference_index
- Google robots/snippet controls: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- Google structured-data policies: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Agent-friendly websites: https://web.dev/articles/ai-agent-site-ux
- GA4 Data API: https://developers.google.com/analytics/devguides/reporting/data/v1
- OpenAI crawler roles: https://developers.openai.com/api/docs/bots
- OpenAI publishers/developers FAQ: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- Bing AI Performance: https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/
- Bing AI visibility — Intents, Topics, Citation Share, Compare: https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/
- Bing Webmaster API: https://learn.microsoft.com/en-us/bingwebmaster/
- IndexNow: https://www.indexnow.org/documentation
- Anthropic crawler controls: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity crawler controls: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Universal Commerce Protocol: https://ucp.dev/

Research sources are retained as research rather than provider contracts:

- Chen et al., Generative Engine Optimization: How to Dominate AI Search, arXiv:2509.08919 (2025).
- Martinez, Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023-2026), arXiv:2607.14035 (2026).
- Marketing Science, ChatGPT Referrals to E-Commerce Websites: How Do LLMs Compare Against Traditional Channels?, DOI 10.1287/mksc.2025.0489 (2026).

## Open determinations

- K-SEO license;
- first controlled site;
- initial execution host;
- first authenticated search-data source;
- first actual write/publish controller;
- implementation language after engineering review;
- scheduler/host relation;
- product packaging and price;
- future UI/hosted surface.

The first exercised site should resolve several of these more truthfully than further abstract planning.