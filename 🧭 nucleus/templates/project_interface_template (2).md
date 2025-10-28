# 🌐 Project Interface (Template)
> Ura zyrtare midis **ChatGPT** dhe **databazës së projektit** (repo, docs, artefakte).  
> Ky dokument përdoret nga AI për orientim të shpejtë dhe punë të saktë.

---

## 1) Informacion i Përgjithshëm
- **Emri:** [Emri i projektit]
- **Repo (kanonik):** [https://...]
- **Docs Index:** [projects/<Emri>/docs/INDEX.md]
- **Owner / Custodian:** [emri ose handle]
- **Version:** v1.0.0
- **Status:** Active | On Hold | Archived

---

## 2) Qëllimi & Vizioni
- **Pse ekziston projekti?** [1–3 rreshta]
- **Rezultati i synuar (KPIs / Outcomes):** [p.sh. rritje X, ulje Y, SLA Z]
- **Kufijtë (Out of Scope):** [çfarë nuk përfshihet]

---

## 3) Struktura & Burimet Kanonike
- **Kodi burimor:** [`src/` ose link]  
- **Dokumentacioni:** [`docs/` ose link]  
- **Të dhënat / Inputs:** [skedarë, tabela, API]  
- **Artefaktet:** [releases, raporte, demo links]  
- **INDEX Kanonik i projektit:** `projects/<Emri>/docs/INDEX.md`

> Rregull: Puno **vetëm** me burime kanonike të listuara këtu ose në `LINKS.md`.

---

## 4) Rregullat e Komunikimit me AI
1) Referoju ** këtij dokumenti** dhe **INDEX-it** për çdo vendim.  
2) **Cito burimin** (skedar/permalink) kur propozon ose konfirmon.  
3) **Mos dil jashtë fushës** pa u kërkuar qartë.  
4) Pas çdo hapi me peshë, **përditëso `system/status.json`** dhe (nëse krijohen dokumente) **shto hyrje** në `system/links.json`.

---

## 5) Flukset kryesore (INIT → MAP → BUILD → SYNC → REFLECT → EVOLVE)
- **INIT:** korniza, objektivat, stakeholders, rreziqet e njohura.  
- **MAP:** harta e burimeve, API/varësitë, backlog minimal.  
- **BUILD:** zhvillim, eksperimente, draft dokumente/skripte.  
- **SYNC:** përditësime, validime, permalinks, CI checks.  
- **REFLECT:** mësime, metrika, çfarë përmirësohet.  
- **EVOLVE:** zgjerime, optimizime, automatikë.

---

## 6) Hyrje/ dalje (I/O) & besueshmëria
- **Inputs:** [burimet primare + formatet]  
- **Processing:** [si trajtohen]  
- **Outputs:** [raporte, modele, dokumente, API]  
- **Cilësia:** [checks, validime, testime]  
- **Rreziqe:** [top 3] — **Mitigim:** [masat]

---

## 7) Varësi & Mjedisi
- **Libraries / Services:** [versione, linke]  
- **Mjedisi ekzekutues:** [Python/Node/…; runtime; secrets]  
- **Konfigurime / `.env` (pa sekrete):** [kyçe të lejuara]

---

## 8) Udhëzime Operacionale
- **Si ekzekutohet lokalisht:** [komanda]  
- **CI / Workflows:** [emra workflows + qëllimi]  
- **Ritmi i sinkronizimit:** [kur përditësohet status/links]

---

## 9) Heartbeat (lokal për projektin)
- **Përditësuar:** –  
- **Status:** Active | On Hold | Archived  
- **Owner:** –

---

## 10) Changelog (shkurt)
- [YYYY-MM-DD] — [ndryshimi] — [autori]

