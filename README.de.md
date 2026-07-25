[English](README.md) · **Deutsch**

# AgentSkillForge

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![CodeQL](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Wiederverwendbare Agent Skills, die KI-Coding-Assistenten zu sorgfältigen Änderungen und verständlichen Ergebnissen anleiten.

[Skills entdecken](#skill-katalog) · [Mit Zed installieren](#schnellstart) · [Mitwirken](CONTRIBUTING.md)

> [!WARNING]
Repository-Prüfungen decken Struktur, lokale Links, Paketierung, statische Aktivierungsfälle und die Skill-Validierung mit der GitHub CLI ab. Sie führen keine Agentenmodelle aus und belegen keine Kompatibilität mit jedem Client. Eine formale Wartungsrichtlinie oder ein Release-Rhythmus sind nicht dokumentiert.

## Was ist AgentSkillForge?

AgentSkillForge ist eine Sammlung kleiner, wiederverwendbarer Agent Skills für KI-Coding-Assistenten. Jeder Skill beschreibt einen Aufgabentyp, die zu sammelnden Belege, nötige Entscheidungen und die Form des Ergebnisses.

Agent Skills sind einfache Markdown-Verzeichnisse mit einer zentralen `SKILL.md`. Sie sind damit nicht an einen bestimmten Client gebunden. Dieses Repository dokumentiert die Installation für Zed; andere Clients benötigen ihren eigenen dokumentierten Mechanismus zum Laden kompatibler Skill-Verzeichnisse.

## Warum verwenden?

- **Gezielte Anleitung:** Wähle einen Skill für die konkrete Aufgabe statt eines allgemeinen Workflows.
- **Belege vor Annahmen:** Skills unterscheiden Beobachtungen, Schlussfolgerungen und nicht ausgeführte Prüfungen.
- **Portable Agent Skills:** Kopiere ein vollständiges Skill-Verzeichnis in einen kompatiblen Client – ohne Python-Laufzeit für die Skill-Dokumente.
- **Geprüfte Distribution:** Die Repository-Automatisierung prüft Struktur, Links, Tests, statische Eval-Fälle und Paketinhalt.

## Skill-Katalog

Wähle den Skill, der wirklich zur Aufgabe passt – nicht nur zu einem einzelnen Wort im Prompt.

| Skill | Wann verwenden? | Beispiel |
|---|---|---|
| [`skills/solution-framing/`](skills/solution-framing/) | Die Richtung ist unklar oder eine Entscheidung enthält wichtige Abwägungen. | „Welcher Migrationsansatz ist am sichersten?“ |
| [`skills/safe-code-change/`](skills/safe-code-change/) | Du brauchst eine kleine, verstandene Änderung oder Fehlerbehebung. | „Behebe diesen reproduzierbaren Validierungsfehler.“ |
| [`skills/fact-based-code-review/`](skills/fact-based-code-review/) | Eine Änderung ist bereit zur Prüfung und braucht einen faktenbasierten Code-Review. | „Prüfe diesen Pull Request vor dem Merge.“ |
| [`skills/product-interface-engineering/`](skills/product-interface-engineering/) | Eine Seite, ein Formular, eine Interaktion, Accessibility oder responsives Verhalten braucht Arbeit. | „Mache dieses Checkout-Formular mobil nutzbar.“ |
| [`skills/performance-investigation/`](skills/performance-investigation/) | Du untersuchst ein gemessenes Latenz-, Durchsatz- oder Speicherproblem. | „Warum ist dieser Endpunkt langsamer geworden?“ |
| [`skills/vue-sfc-decomposition/`](skills/vue-sfc-decomposition/) | Eine Vue- oder Nuxt-Komponente soll ohne Verhaltensänderung aufgeteilt werden. | „Teile diese große Vue-SFC in wartbare Teile auf.“ |
| [`skills/failure-investigation/`](skills/failure-investigation/) | Ein technischer Fehler außerhalb der Performance-Domäne hat eine unbekannte Ursache oder sichere Änderungsgrenze. | „Ermittle vor einem Fix, warum diese Integration fehlschlägt.“ |
| [`skills/security-boundary-analysis/`](skills/security-boundary-analysis/) | Eine explizite Security- oder Threat-Modeling-Aufgabe benötigt Vertrauensübergänge, Missbrauchspfade, Kontrollen und Restunsicherheit. | „Erstelle ein Threat Model für diese Webhook-Grenze.“ |
| [`skills/compatibility-migration/`](skills/compatibility-migration/) | Eine festgelegte Richtung erfordert sichere Koexistenz von altem und neuem Verhalten über mehrere Schritte oder Konsumenten. | „Plane eine kompatible API-Migration über mehrere Releases.“ |

Lies vor der Verwendung die `SKILL.md` eines Skills. Bewahre das vollständige Verzeichnis einschließlich vorhandener `references/` und `assets/` auf, weil der Skill darauf verweisen kann.

## Schnellstart

Installiere Git und Python 3.11 oder neuer, bevor du den Zed-Installer verwendest. Er installiert alle Skills in Zeds gemeinsames Verzeichnis `~/.agents/skills`.

<details>
<summary>macOS, Linux oder WSL</summary>

```sh
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
python3 scripts/install_zed_skills.py
```

</details>

<details>
<summary>Windows PowerShell</summary>

```powershell
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
py scripts\install_zed_skills.py
```

</details>

Starte nach der Installation eine neue Agentensitzung. Der Installer bricht ab, statt ein vorhandenes Skill-Verzeichnis zu ersetzen.

## Installation

### Portabler Kern

Kopiere oder referenziere das gewünschte Verzeichnis `skills/<name>/` mit dem dokumentierten Mechanismus deines Clients. AgentSkillForge beansprucht weder einen universellen Installationspfad noch eine allgemeine Konvention zur automatischen Erkennung.

### Zed

Installiere nur einen Skill, wenn du nicht den gesamten Katalog benötigst:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
```

Wiederhole `--skill`, um mehrere Skills zu installieren. Verwende `--target`, wenn Zed ein anderes Skill-Verzeichnis verwendet.

> [!CAUTION]
> `--force` löscht jedes ausgewählte Zielverzeichnis und erstellt es neu. Prüfe lokale Änderungen vorher; der Installer führt Dateien nicht zusammen.

Die [vollständige Zed-Installationsanleitung](docs/clients/zed.md) beschreibt ausgewählte Skills, eigene Zielpfade, Updates, Überprüfung und Deinstallation.

## Skills kombinieren

Häufige Reihenfolgen sind:

- Unbekannter technischer Fehler außerhalb der Performance-Domäne: `failure-investigation` belegt Ursache und sichere Änderungsgrenze, danach implementiert `safe-code-change` den Fix und `fact-based-code-review` prüft ihn.
- Gemessenes Latenz-, Durchsatz-, Speicher- oder Ressourcenproblem: Verwende `performance-investigation`, nicht `failure-investigation`; übergib eine verstandene Änderung an `safe-code-change` und prüfe sie anschließend mit `fact-based-code-review`.
- Mehrstufige Migration: `solution-framing` wählt die Richtung nur, wenn sie noch offen ist, `compatibility-migration` definiert sichere Koexistenz- und Stilllegungszustände und `safe-code-change` implementiert jeden lokalen Schritt.
- Explizites Threat Model: `security-boundary-analysis` definiert Vertrauensübergänge, Missbrauchspfade und Kontrollpflichten. Danach übernimmt `solution-framing` Architekturentscheidungen, `product-interface-engineering` sichtbare Berechtigungs- oder Recovery-Interaktionen oder `compatibility-migration` die gestufte Koexistenz; die Outputs bleiben getrennt.

Dein KI-Client entscheidet, wann er einen installierten Skill lädt. Beschreibungen sind Routing-Hinweise und keine Garantie für das Verhalten eines Hosts. Die Repository-Evals sind statisch; aus der Installation allein folgt weder Runtime-Portabilität noch zuverlässige Aktivierung.

## Kompatibilität

| Bereich | Unterstützt oder erforderlich |
|---|---|
| Agent-Skill-Format | Markdown-Verzeichnisse mit `SKILL.md` und relativen lokalen Referenzen |
| Agent-Clients | Clients, die kompatible Skill-Verzeichnisse laden können; die genaue Unterstützung hängt von der Client-Konfiguration ab |
| Dokumentierte Integration | Zed mit aktivierten Agent Skills |
| Python | 3.11 oder neuer für Zed-Installer, Paketierung und Repository-Prüfungen |
| Paket-Runtime | Kein importierbares Python-Modul; das Wheel verteilt Agent Skills und Hilfsdateien als Daten |

Die Skill-Dokumente selbst benötigen kein Python. Python wird vom Installer und den Repository-Werkzeugen verwendet.

## Qualität und Entwicklung

Der **Validate**-Workflow führt die folgenden Repository-Prüfungen aus. **CodeQL** analysiert die Python-Werkzeuge auf unterstützte Sicherheitsprobleme.

```sh
python -m pip install -e ".[dev]"
python scripts/validate_repository.py
python scripts/check_links.py
pytest
python scripts/run_evals.py
python scripts/check_distribution.py
```

Diese Befehle prüfen Skill-Metadaten und -Struktur, lokale Markdown-Links, Verhalten von Installer und Paketierung, statische Abdeckung des Eval-Manifests und den Inhalt des verteilten Wheels.

> [!NOTE]
> `python scripts/run_evals.py` prüft statische Falldeklarationen. Der Befehl führt keinen Agenten aus und belegt keine Runtime-Portabilität. Prüfe externe HTTP-Links ausdrücklich mit `python scripts/check_links.py --external`.

<details>
<summary>Projektstruktur</summary>

```text
.
├── skills/                     # Portable Agent Skills
├── evals/                      # Statische Fälle und Repository-Tests
├── scripts/                    # Validierung, Paketierung und Zed-Installer
├── docs/clients/zed.md         # Zed-Integrationsanleitung
├── .github/workflows/          # Automatisierungs-Workflows
├── CONTRIBUTING.md             # Regeln zum Mitwirken und Clean-Room-Prozess
├── pyproject.toml              # Python-Werkzeuge und Paketmetadaten
├── README.md                   # Englische Dokumentation
├── README.de.md                # Deutsche Dokumentation
└── LICENSE                     # Apache License 2.0
```

Das Python-Wheel ist eine Datendistribution, keine Anwendung und kein importierbares SDK. Es legt README, Agent Skills, Referenzen, Zed-Anleitung und Installer unter `share/agent-skill-forge/` ab.

</details>

## Mitwirken

Beiträge sind willkommen. Lies vor dem Erstellen eines Pull Requests [CONTRIBUTING.md](CONTRIBUTING.md). Neues oder geändertes Skill-Verhalten muss portable Metadaten und gültige lokale Referenzen bewahren, dem Clean-Room-Prozess folgen und die relevanten Evals sowie Prüfungen des Ausgabevertrags aktualisieren.

## Sicherheit und Support

Behandle Skills von Drittanbietern als nicht vertrauenswürdige Anweisungen. Prüfe vor der Installation Inhalt, Herkunft, Links und Abhängigkeiten. Gewähre nicht allein deshalb Zugriff auf Tools, Zugangsdaten oder das Dateisystem, weil ein Skill-Dokument ihn verlangt.

Melde mögliche Sicherheitslücken über GitHubs private Sicherheitsmeldung. Veröffentliche keine sensiblen Details in einem öffentlichen Issue. Verwende [GitHub Issues](https://github.com/RobinGru/AgentSkillForge/issues) für öffentliche Fehlermeldungen und Fragen.

## Lizenz und Hinweise

AgentSkillForge wird unter der [Apache License 2.0](LICENSE) veröffentlicht. Prüfe vor der Weiterverteilung [NOTICE](NOTICE) und [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
