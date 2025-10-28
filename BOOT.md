# 🚀 MindSync — BOOT.md (Universal Entry File)

> Qëllimi: Ky dokument është **hyrja universale** që më vendos mua (AI) në rrjedhën e plotë të sistemit MindSync për çdo bisedë.  
> Përdorimi: **Ngarko vetëm këtë skedar në fillim të bisedës** (ose dërgo linkun e tij kanonik). Unë lexoj, sinkronizohem dhe vazhdoj punën aty ku mbetëm.

---

## 1) Identiteti i Sistemit
- **Emri i sistemit:** MindSync
- **Versioni i BOOT:** v1.0
- **Data e fundit e përditësimit:** 2025-10-28
- **Burimi kanonik:** (vendos linkun GitHub të BOOT.md)
- **Kushtetuta Supreme:** ./MindSync_SUPREME_STRUCTURE.md
- **Kushtetuta Operative:** ./nucleus/constitution.md

---

## 2) Si funksionon BOOT.md
- Ky file ka dy pjesë:
  - **Pjesa e fiksuar** (orientimi, rrugët, rregullat) — **nuk ndryshon**.
  - **Pjesa dinamike** (🫀 _Heartbeat_ + 📜 _Log_) — **përditësohet** gjatë punës.
- BOOT lexon **statusin** dhe **regjistrin e linkeve** nga `./system/status.json` dhe `./system/links.json`.
- Çdo bisedë e re → ngarko **BOOT.md** → unë lexoj statusin & linket → **vazhdoj aty ku u ndalëm**.

---

## 3) Rrugët Kanonike (Paths)
- **Nucleus (bërthama):** `./nucleus/`
  - `constitution.md` — ligjet operative
  - `templates/` — bazat e projekteve
- **Cortex:** `./cortex/` *(opsionale)*
  - `INDEX.md` — indeks global
  - `observatory/` — telemetri & reflektim
- **Projects:** `./projects/<ProjectName>/`
  - `docs/INDEX.md` — hyrja kanonike e projektit
- **System (gjendja):** `./system/`
  - `status.json` — heartbeat & faza e fundit
  - `links.json` — regjistër linkesh (auto-registrar)

---

## 4) Rregulla për AI (Operator Protocol)
1. **Puno vetëm me burime kanonike** (linke nga BOOT, status.json, links.json, INDEX-et).
2. **Cito burimin** kur jep përgjigje (skedar/folder/permalink).
3. **Mos dil jashtë fushës** pa u kërkuar qartë.
4. **Pasi kryen një hap**, përditëso _Heartbeat_ dhe shto rresht në _Log_.
5. **Kur gjeneron dokumente të reja**, regjistroji në `links.json` sipas skemës.

---

## 5) SYNC Checklist (para merge/commit)
- [ ] `system/status.json` i përditësuar (phase, active_project, updated_at)
- [ ] `system/links.json` ka hyrje për dokumentet/linket e reja
- [ ] `docs/INDEX.md` i projektit të prekur është në sinkron
- [ ] Changelog u azhurnua (nëse është kritike)
- [ ] Permalinks shtuar për citime kritike

---

## 6) Skemat (gjenden edhe si shembuj më poshtë)

### 6.1) `system/status.json` (schema minimale)
```
{
  "updated_at": "YYYY-MM-DD",
  "phase": "INIT|MAP|BUILD|SYNC|REFLECT|EVOLVE",
  "active_project": "EmriProjektitOse-",
  "version": "v1.0.x",
  "owner": "emri/handle",
  "note": "koment i shkurtër mbi ndryshimin e fundit"
}
```

### 6.2) `system/links.json` (schema minimale)
```
{
  "projects": [{ "name": "Emri", "repo": "https://...", "docs_index": "path ose url", "status": "Active|On Hold|Archived", "owner": "..." }],
  "canon": [{ "name": "Kodi burimor", "path_or_url": "..." }, { "name": "Dokumentacion", "path_or_url": "..." }],
  "artifacts": [{ "name": "Release notes", "permalink": "..." }]
}
```

---

## 7) Pjesa Dinamike — 🫀 Heartbeat
> **Ky seksion modifikohet gjatë punës.**

- **Përditësuar:** (vendoset automatikisht)
- **Faza aktuale:** INIT
- **Projekti aktiv:** –
- **Versioni:** v1.0.0
- **Custodian:** –
- **Shënim i fundit:** –

---

## 8) Pjesa Dinamike — 📜 Log i Zhvillimeve
> Shto këtu rreshta të shkurtër (data, veprimi, impakti).

- 2025-10-28: Krijuar BOOT.md dhe inicializuar sistemin.

---

## 9) Auto‑Registrar i Linkeve (Si funksionon)
- Çdo herë që shtohet një dokument i ri, regjistro **hyrje** në `./system/links.json`:
  - `name` (si do shfaqet), `path_or_url` (rruga lokale ose URL), (opsionale: `type`, `project`, `owner`).
- **Projekti i ri**: shto në `projects[]` me `repo`, `docs_index`, `status`, `owner`.
- Kur unë lexoj BOOT → lexoj `links.json` → **lëvizi në rrjedhën e saktë** pa pyetje.

---

## 10) Strukturë minimale e rekomanduar
```
/ (rrënja)
├─ MindSync_SUPREME_STRUCTURE.md
├─ BOOT.md
├─ nucleus/
│  ├─ constitution.md
│  └─ templates/
│     ├─ INDEX_template.md
│     ├─ project_interface_template.md
│     └─ architecture_template.md
├─ projects/
│  └─ <ProjectName>/
│     ├─ docs/INDEX.md
│     ├─ tasks/{backlog.md,today.md}
│     └─ src/
└─ system/
   ├─ status.json
   └─ links.json
```

---

## 11) Udhëzim i shpejtë përdorimi (për ty)
1. Në bisedë, **ngarko vetëm BOOT.md** (ose dërgo linkun e tij kanonik).
2. Unë lexoj BOOT + `system/*` dhe futem në rrjedhë automatikisht.
3. Punojmë sipas fazave: INIT → MAP → BUILD → SYNC → REFLECT → EVOLVE.
4. Çdo ndryshim i rëndësishëm → përditësohet _Heartbeat_ + _Log_ + `links.json`.
5. Para merge → kalon **SYNC Checklist**.

---

## 12) Nota
- BOOT **nuk ndryshon në logjikë**; vetëm **pjesa dinamike** përditësohet.
- Gjithçka është versionuar në Git (gjurmueshmëri e plotë).
- Nëse krijohet projekt i ri, mjafton një hyrje në `links.json` + një `docs/INDEX.md` sipas template-it.

---
