# ⚙️ MindSync — Constitution (Operative)

> Manuali operativ i MindSync: ligjet, rregullat dhe protokollet ekzekutive.
> Ky dokument është derivuar nga **MindSync_SUPREME_STRUCTURE.md** dhe fokusohet vetëm në zbatim.

---

## 1) Qëllimi
Të garantojë **koherencë, gjurmueshmëri dhe sinkronizim** në të gjitha projektet MindSync, në bashkëpunim të vazhdueshëm me ChatGPT.

---

## 2) Ligjet Operative

**L1. Koherenca** — Çdo njësi informacioni (file, issue, dataset) duhet të ketë qëllim të qartë dhe referencë te projekti/INDEX.  
**L2. Reflektimi** — Çdo veprim ka shënim reflektimi (why/impact). Pas çdo cikli kryhet `REFLECT`.  
**L3. Njësia** — Asnjë dokument nuk është i izoluar: lidhet te INDEX si burim kanonik.  
**L4. Sinkronizimi** — Gjithmonë ekziston **një** burim “live”; të tjerët janë mirror me datë/version.  
**L5. Transparenca** — Çdo vendim, ndryshim dhe artefakt duhet të jetë i gjurmueshëm (autor, datë, link, version).

---

## 3) Politika e Linkeve

- **Permalink** (i pandryshueshëm) për citime kritike:  
  `.../blob/<commit-sha>/path/file.ext`
- **Live link** (branch, p.sh. `main`) kur kërkohet freski:  
  `.../blob/main/path/file.ext`
- **Drive/Notion**: përdor *view-only* dhe shëno **owners** / të drejtat.
- Çdo burim “kanonik” ka **1 link primar** te `INDEX.md`. Mirrors shënohen qartë.

---

## 4) Versionimi & Changelog

- **SemVer** për dokumente kritike: `MAJOR.MINOR.PATCH` (p.sh. `v1.2.0`).  
- Çdo dokument kanonik ruan **tabelë ndryshimesh** (Changelog) me: Data, Autor, Ndryshimet, Referencat.  
- Release të rëndësishme etiketo: **Git tag** + link në `INDEX.md`.

---

## 5) Struktura minimale e një projekti

```
<Project>/
├─ docs/
│  ├─ INDEX.md          # burimi kanonik i projektit
│  ├─ architecture.md   # (ops.) dizajn & vendime
│  └─ changelog.md      # histori ndryshimesh
├─ tasks/
│  ├─ backlog.md
│  └─ today.md
├─ src/                 # kod burimor
└─ data/                # dataset-e (ose linke te jashtme)
```

- `docs/INDEX.md` duhet të ketë: Qëllimin, Harten Kanonike, Regjistrin e linkeve, Protokollin e sinkronizimit dhe Heartbeat.

---

## 6) Cikli Operativ (RUNBOOK)

1. **INIT** — krijo projekt nga template; plotëso `docs/INDEX.md`.  
2. **MAP** — identifiko komponentë, burime, varësi; përditëso Harten Kanonike.  
3. **BUILD** — shto/ndrysho kodin & dokumentet; cito ticket/issue.  
4. **SYNC** — përditëso linke kanonike; vendos permalinks për citime.  
5. **REFLECT** — shkruaj mësimet/kostot/impact në `docs/changelog.md`.  
6. **EVOLVE** — propagim i përmirësimeve në template globale (`nucleus/templates/`).

> Asnjë PR nuk bashkohet pa kaluar **SYNC checklist**-in.

---

## 7) SYNC Checklist

- [ ] INDEX i përditësuar (links kanonike të sakta)
- [ ] Changelog me datë/autor/impact
- [ ] Permalinks për reference kritike
- [ ] Status/Owner të përditësuar
- [ ] Hequr linke të vdekura / mirrors pa etiketa

---

## 8) Role & Përgjegjësi

- **Custodian** (kujdestar projekti): mban `INDEX.md`, miraton strukturë & linke.  
- **Contributors**: zbatojnë ciclin, shkruajnë changelog, respektojnë ligjet operative.  
- **AI Operator (ChatGPT)**: punon vetëm me burime kanonike, cito linke, kërkon shtesa në INDEX kur nevojiten.

---

## 9) Emërtim & Konventa

- Folders: `snake-case` ose `kebab-case`.  
- Dokumente: `lowercase-with-dashes.md` (p.sh. `project_interface.md`).  
- Komente commit: `type(scope): summary` (p.sh. `docs(index): add canonical map`).  
- Tickets/Issues: prefiks projektit (p.sh. `GPT-GO-23`).

---

## 10) Miratim & Qeverisje

- Ndryshimet në **Constitution** kërkojnë:  
  1) PR me justifikim, 2) miratim nga Custodian global, 3) version të ri `vX.Y.Z`.  
- Çdo projekt mban **Governance Note** te `docs/INDEX.md` (si merren vendimet).

---

## 11) Incident & Deviation Policy

- Nëse konstatohet devijim nga kanoni:  
  - hap **Issue: Deviation**, vendos plan korrigjimi, përditëso `INDEX.md`.  
- Në incident kritik: ngrij mirrors, kodifiko “state of truth”, krijo **postmortem** në `docs/incident-<date>.md`.

---

## 12) Shtesa: Operim me Burime të Jashtme

- **Notion/Drive**: centralizo linke te `INDEX.md`; ruaj audit log (kush/kur).  
- **Dashboards/Telemetry**: refero si kanonik vetëm nëse riprodhueshme (query version + data).  
- **API connectors**: dokumento versionet, çelësat dhe kufijtë e përdorimit.

---

## 13) Glossary

- **Kanonik** — burimi primar i së vërtetës.  
- **Mirror** — kopje e sinkronizuar, jo burim vendimor.  
- **Permalink** — link me commit/tag të pandryshueshëm.  
- **Live** — link drejt branch-it aktiv për freski.  
- **Heartbeat** — status i fundit i projektit (datë, owner, ndryshime).

---

## 14) Referenca

- Kushtetuta Supreme: `../MindSync_SUPREME_STRUCTURE.md`
- Template interfejsi projekti: `../Templates/project_interface_template.md`
- Template indeks global: `../Templates/INDEX_template.md`

---

**Status:** v1.0 — i miratuar si bazë operative.  
**Owner:** [Vendos emrin]  
**Data:** [YYYY-MM-DD]

