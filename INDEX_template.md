# 📚 Global INDEX — Databaza e Projekteve (Template)

> **Qëllimi:** Ky dokument është **pika e vetme e së vërtetës (SSOT)** për bisedat me ChatGPT dhe për navigimin në të gjithë “databazën” (GitHub / Drive / Notion / etj.).  
> Përdoreni si **indeks kryesor** që lidh burimet e brendshme të repo‑s me burimet “live” të jashtme. Çdo kërkesë, verifikim, ose ndryshim duhet të referojë linke nga ky dokument.

---

## 🧭 1) Orientim i shpejtë
- **Link kryesor i databazës (jashtë):** [Vendos linkun kryesor të “hub”-it live p.sh. Google Drive / Notion]  
- **Repo/Folder i këtij indeks-i (brenda):** [Vendos path-in në GitHub p.sh. `/docs/INDEX.md`]  
- **Kontakt / Kujdestar i indeksit:** [Emri, email ose handle]  
- **Politikë:** Nëse një burim **nuk është i listuar këtu**, konsiderohet **jo‑kanonik** derisa të shtohet.

---

## 🧩 2) Regjistër projektesh (live)
> Mbaj të gjithë projektet e lidhura këtu. Përdor linke **permalink** kur kërkohet stabilitet; linke **branch** kur kërkohet freski (shih seksionin “🔗 Politika e linkeve”).

| Projekt | Qëllimi i shkurtër | Repo | Docs | Data | Status | Owner |
|---|---|---|---|---|---|---|
| _shembull: GPT‑GO_ | Shabllon nisjeje & orientim | https://github.com/... | https://github.com/.../docs | drive://... | Active | @emri |

**Shënim:** Nëse një kolonë s’zbatohet (p.sh. “Data”), vendos `–` në vend që ta lësh bosh.

---

## 🗺️ 3) Harta e rrugëve kanonike
- **Kodi burimor (kanonik):** [link]  
- **Dokumentacion teknik (kanonik):** [link]  
- **Të dhënat / dataset (kanonik):** [link]  
- **Backlog & plane**: [link]  
- **Artefakte (builds, raporte):** [link]

> **Rregull:** Çdo burim kanonik duhet të ketë **një** link primar këtu. Duplikimet të shënohen si “pasqyra/mirror”.

---

## 🤝 4) Rregullat e komunikimit me ChatGPT
1. **Bazoju gjithmonë** te ky **INDEX**. Nëse një burim mungon, kërko të shtohet këtu para përdorimit.  
2. Kur përgjigjesh, **cito seksionin + linkun** (p.sh. “Harta e rrugëve kanonike › Dokumentacion”).  
3. **Mos dil jashtë fushës** së indekstit/rrugëve kanonike pa kërkesë të qartë.  
4. Prefero **permaling** për cita të pandryshueshme; **branch links** për kërkesa “live”.  
5. Kur një material azhurnohet, **përditëso këtë INDEX** sipas “🔄 Protokolli i përditësimit”.

---

## 🔗 5) Politika e linkeve (Permalink vs Live)
- **Permalink (i pandryshueshëm):** Përdor link me **commit SHA/tag** p.sh. `.../blob/<sha>/path/file.ext` kur kërkohet **riprodhueshmëri**.  
- **Live (i përditësueshëm):** Përdor link **branch** p.sh. `.../blob/main/...` kur kërkohet **freski**.  
- **Drive/Notion:** përdor linke **view‑only** dhe shëno të drejtat.  
- **Emërtim:** `kanonik`, `mirror`, `draft`. Vetëm `kanonik` përdoret për vendime.

---

## 🧪 6) Kontrollet e sinkronizimit (checklist)
- [ ] A është shtuar projekti i ri në **Regjistër**?  
- [ ] A kanë burimet **link primar (kanonik)**?  
- [ ] A ekziston **permaling** për citime kritike?  
- [ ] A është përditësuar **Status** + **Owner**?  
- [ ] A është hequr ndonjë link i vdekur/jo kanonik?

> **Standard:** Asnjë PR/ndryshim s’pranohet pa kaluar këtë checklist.

---

## 🔄 7) Protokolli i përditësimit
1. **Shto/ndrysho** projektin në “Regjistër”.  
2. **Azhurno “Harta e rrugëve kanonike”** me linkun primar (një e vetme).  
3. Vendos **permaling** për artefakte të cituara.  
4. Përditëso **Status**, **Owner** dhe data te “🫀 Heartbeat”.  
5. Shto një rresht në “📜 Changelog”.

---

## 🫀 8) Heartbeat (gjendja e fundit)
- **Përditësimi i fundit i indeksit:** YYYY‑MM‑DD
- **Ndryshime kryesore:** [1‑2 pika]
- **Rreziqe/Varësi:** [shkurt]

---

## 📜 9) Changelog
| Version | Data | Ndryshimet | Autor |
|---|---|---|---|
| v1.0 | YYYY‑MM‑DD | Krijuar `INDEX` global (template) | [emri] |

---

## 🧩 10) Mini‑template për një projekt të ri
> Kopjo këtë bllok te “Regjistër projektesh” kur shton projekt të ri.

**{Emri i projektit}**  
- **Qëllimi:** …  
- **Repo:** …  
- **Docs:** …  
- **Data:** …  
- **Artefakte:** …  
- **Owner:** …  
- **Status:** Active / On Hold / Archived  
- **Permalinks thelbësore:**  
  - Release notes: …  
  - Spec kryesor: …  
  - Dataset versionuar: …

---

## ❓ 11) FAQ shpejt
- **Çfarë ndodh nëse një link ndryshon?** → Përditëso këtu; mbaj permaling te versioni i vjetër për histori.  
- **Si i trajtojmë mirrors?** → Shënoji qartë; vendos `kanonik` te rruga primare.  
- **A mund të përdoren burime jo të listuara?** → Jo, derisa të shtohen këtu.

---

## 📎 12) Shtesa (opsionale)
- **Badge‑e statusi:** (p.sh. build, docs, coverage)  
- **Matje/telemetri:** link te dashboards  
- **Rregullat e emërtimit:** për repos, branches, tags, skedarë

---

> **Udhëzim përdorimi (për bisedat):** Në fillim të çdo bisede, thuaj:  
> “Bazoju te **INDEX**: [link‑u i këtij file‑i]. Kërkesat dhe përgjigjet të citojnë seksione nga ky dokument.”
