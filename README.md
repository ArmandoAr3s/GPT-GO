# MindSync Template — Përdorimi i Shpejtë

- Në ChatGPT **ngarko BOOT.md** në fillim të bisedës (ose dërgo linkun kanonik).  
- Sistemi lexon **system/status.json** (heartbeat) dhe **system/links.json** (regjistër).  
- Harta e të gjithë databazës gjenerohet automatikisht te **LINKS.md** (nga `system/linkgen.py`).  
- Për projekt të ri: krijo `projects/<Emri>/docs/INDEX.md` nga template dhe shto hyrje në `system/links.json`.

> Faza e punës: `INIT → MAP → BUILD → SYNC → REFLECT → EVOLVE`.
