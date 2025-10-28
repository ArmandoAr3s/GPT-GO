# 📚 Global INDEX — GPT‑GO

> **SSOT (Single Source of Truth)** për bisedat me ChatGPT dhe navigimin në të gjithë “databazën” e projektit.  
> Ky dokument lidh burimet **brenda repo‑s** me burimet **live të jashtme** dhe përcakton rregullat e sinkronizimit.

---

## 🧭 1) Orientim i shpejtë
- **Link kryesor i databazës (jashtë):** –  
- **Repo i këtij indeks‑i (brenda):** https://github.com/ArmandoAr3s/GPT-GO/tree/main/docs/INDEX.md  
- **Kontakt / Kujdestar i indeksit:** [Vendos emrin]  
- **Politikë:** Nëse një burim **nuk është i listuar këtu**, konsiderohet **jo‑kanonik** derisa të shtohet.

---

## 🧩 2) Regjistër projektesh (live)
| Projekt | Qëllimi i shkurtër | Repo | Docs | Data | Status | Owner |
|---|---|---|---|---|---|---|
| **GPT‑GO** | Shabllon nisjeje & orientim pune me GPT | https://github.com/ArmandoAr3s/GPT-GO | https://github.com/ArmandoAr3s/GPT-GO/tree/main/docs | – | Active | [@vendos] |

> **Udhëzim:** Përdor linke **permaling** kur nevojitet riprodhueshmëri; përdor linke **branch** (p.sh. `main`) kur kërkohet freski. Shiko seksionin “🔗 Politika e linkeve”.

---

## 🗺️ 3) Harta e rrugëve kanonike
- **Kodi burimor (kanonik):** https://github.com/ArmandoAr3s/GPT-GO/tree/main/src  
- **Dokumentacion teknik (kanonik):** https://github.com/ArmandoAr3s/GPT-GO/tree/main/docs  
- **Detyrat / planifikimi:** https://github.com/ArmandoAr3s/GPT-GO/tree/main/tasks  
- **Artefakte (builds/raporte):** –

> **Rregull:** Çdo burim kanonik duhet të ketë **një** link primar këtu. Duplikimet shënoji si “mirror”.

---

## 🤝 4) Rregullat e komunikimit me ChatGPT
1. **Bazoju gjithmonë** te ky **INDEX**. Nëse një burim mungon, shtoje këtu para përdorimit.  
2. Në përgjigje, **cito seksionin + linkun** (p.sh. “Harta e rrugëve kanonike › Dokumentacion”).  
3. **Mos dil jashtë fushës** së indekstit pa kërkesë të qartë.  
4. Prefero **permaling** për citime të pandryshueshme; **branch links** për kërkesa “live”.  
5. Kur një material azhurnohet, **përditëso INDEX‑in** sipas “🔄 Protokolli i përditësimit”.

---

## 🔗 5) Politika e linkeve (Permalink vs Live)
- **Permalink (i pandryshueshëm):** `.../blob/<sha>/path/file.ext` për **riprodhueshmëri**.  
- **Live (i përditësueshëm):** `.../blob/main/...` për **freski**.  
- **Drive/Notion:** përdor linke **view‑only** dhe shëno të drejtat.  
- **Emërtim:** `kanonik`, `mirror`, `draft`. Vetëm `kanonik` përdoret për vendime.

---

## 🧪 6) Kontrollet e sinkronizimit (checklist)
- [ ] Projekti shtuar në **Regjistër**  
- [ ] Rrugë **kanonike** të përcaktuara  
- [ ] **Permalinks** për citime kritike  
- [ ] Fushat **Status** dhe **Owner** të përditësuara  
- [ ] Hequr linke të vdekura/jo‑kanonike

> **Standard:** Asnjë PR/ndryshim nuk pranohet pa kaluar këtë checklist.

---

## 🔄 7) Protokolli i përditësimit
1. Shto/ndrysho projektin në “Regjistër”.  
2. Azhurno “Harta e rrugëve kanonike” me **linkun primar**.  
3. Vendos **permaling** për artefakte të cituara.  
4. Përditëso **Status**, **Owner** dhe **🫀 Heartbeat**.  
5. Shto një rresht në **📜 Changelog**.

---

## 🫀 8) Heartbeat (gjendja e fundit)
- **Përditësimi i fundit i indeksit:** [vendos datën]  
- **Ndryshime kryesore:** –  
- **Rreziqe/Varësi:** –

---

## 📜 9) Changelog
| Version | Data | Ndryshimet | Autor |
|---|---|---|---|
| v1.0 | [vendos datën] | Krijuar `docs/INDEX.md` për GPT‑GO | [emri] |

---

## 🧩 10) Mini‑template për projekt/nen‑projekt të ri
**{Emri i nën‑projektit}**  
- **Qëllimi:** …  
- **Repo/Folder:** …  
- **Docs:** …  
- **Data:** …  
- **Artefakte:** …  
- **Owner:** …  
- **Status:** Active / On Hold / Archived  
- **Permalinks thelbësore:**  
  - Release notes: …  
  - Spec kryesor: …  
  - Dataset i versionuar: …

---

## ❓ 11) FAQ shpejt
- **Çfarë ndodh nëse një link ndryshon?** → Përditëso këtu; ruaj permaling të vjetër për histori.  
- **Si i trajtojmë mirrors?** → Shënoji qartë; vendos `kanonik` te rruga primare.  
- **A mund të përdoren burime jo të listuara?** → Jo, derisa të shtohen këtu.

---

## 📎 12) Shtesa (opsionale)
- Badge‑e statusi (build, docs, coverage)  
- Link dashboards/telemetri  
- Rregulla emërtimi (repos, branches, tags, skedarë)

---

> **Udhëzim për biseda:** “Bazoju te **docs/INDEX.md**: https://github.com/ArmandoAr3s/GPT-GO/tree/main/docs/INDEX.md — cito seksionet përkatëse në çdo kërkesë.”
