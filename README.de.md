[English](README.md) · **Deutsch**

# AgentSkillForge

![AgentSkillForge-Banner](assets/github-banner.jpg)

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![Runtime evals](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml)
[![CodeQL](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Wiederverwendbare Agent Skills, die KI-Coding-Assistenten zu sorgfältigen Änderungen und verständlichen Ergebnissen anleiten.

[Skills entdecken](#skill-katalog) · [Mit Zed oder Codex installieren](#schnellstart) · [All-in-one-Vorlage nutzen](#all-in-one-anweisungen-für-projekte) · [Mitwirken](CONTRIBUTING.md)

> [!NOTE]
> Statische Repository-Prüfungen laufen für jeden Pull Request. Deterministische Runtime-Contract-Checks prüfen den Eval-Runner, während authentifizierte Codex-Smoke-Tests und interaktive Zed-Prüfungen optionale Release-Belege sind. Die [Kompatibilitäts- und Wartungsrichtlinie](docs/compatibility.md) beschreibt die Support-Matrix und ihre klaren Grenzen.

## Was ist AgentSkillForge?

AgentSkillForge ist eine Sammlung kleiner, wiederverwendbarer Agent Skills für KI-Coding-Assistenten. Jeder Skill beschreibt einen Aufgabentyp, die zu sammelnden Belege, nötige Entscheidungen und die Form des Ergebnisses.

Agent Skills sind einfache Markdown-Verzeichnisse mit einer zentralen `SKILL.md`. Sie sind damit nicht an einen bestimmten Client gebunden. Dieses Repository bietet dokumentierte Installer für Zed und Codex; andere Clients benötigen ihren eigenen dokumentierten Mechanismus zum Laden kompatibler Skill-Verzeichnisse.

## Warum verwenden?

- **Gezielte Anleitung:** Wähle einen Skill für die konkrete Aufgabe statt eines allgemeinen Workflows.
- **Belege vor Annahmen:** Skills unterscheiden Beobachtungen, Schlussfolgerungen und nicht ausgeführte Prüfungen.
- **Portable Agent Skills:** Kopiere ein vollständiges Skill-Verzeichnis in einen kompatiblen Client – ohne Python-Laufzeit für die Skill-Dokumente.
- **Geprüfte Distribution:** Die Repository-Automatisierung prüft Struktur, Links, Tests, statische Eval-Fälle und Paketinhalt.

## All-in-one-Anweisungen für Projekte

Kein Bock auf viele verschiedene Skills und komplizierte Installationen? Dann nutze [`templates/AGENTS-AIO.md`](templates/AGENTS-AIO.md) als kompakte All-in-one-Lösung.

Lege die Datei im Stammverzeichnis deines Projekts als `AGENTS.md` ab. Sie enthält allgemeine Anweisungen für Produktbezug, Barrierefreiheit, Sicherheit, Verifikation und Review-Prioritäten – ohne einen bestimmten Agent-Client vorauszusetzen.

```sh
cp templates/AGENTS-AIO.md /pfad/zu/deinem-projekt/AGENTS.md
```

Projektspezifische Regeln gehören in die kopierte Vorlage, nicht in die verteilten Skills.

## Skill-Katalog

Wähle den Skill, der wirklich zur Aufgabe passt – nicht nur zu einem einzelnen Wort im Prompt. Beginne mit der Kategorie, die die Arbeit beschreibt, und wähle dann den engsten Skill, dessen Aktivierungsgrenze zur Situation passt.

> **Quellstruktur und Installation:** Die Kategorien dienen nur der Navigation in diesem Repository. Installer und das flache ZIP-Bundle legen jeden Skill direkt unter `<ziel>/<skill-name>/` ab.

### Kernablauf

Diese Skills decken die repositoryweiten Abläufe ab, die andere Arbeit häufig vorbereiten, ermöglichen, umsetzen, sichern oder fortsetzen.

| Skill | Verwenden, wenn | Anderen Skill verwenden, wenn |
|---|---|---|
| [`repository-onboarding`](skills/core/repository-onboarding/) | Ein unbekanntes, übernommenes oder veraltetes Repository vor umfangreicher Arbeit eine evidenzbasierte technische Arbeitskarte benötigt. | Produktzweck unklar ist (`project-discovery`) oder ein Fehler untersucht werden muss (`failure-investigation`). |
| [`repository-knowledge-curation`](skills/core/repository-knowledge-curation/) | Eine verifizierte wiederverwendbare Repository-Erkenntnis genau einen kanonischen Ablageort benötigt. | Die Erkenntnis unbestätigt, vorübergehend oder eine offene Entscheidung ist. |
| [`safe-code-change`](skills/core/safe-code-change/) | Eine begrenzte Änderung einen bekannten Verhaltensvertrag und eine sichere Änderungsgrenze hat. | Die Ursache unbekannt ist (`failure-investigation`) oder ein Rollout gemischte Versionen koordinieren muss (`compatibility-migration`). |
| [`session-handoff`](skills/core/session-handoff/) | Unfertige konkrete Arbeit anhand verifizierter lokaler Zustände fortgesetzt werden muss. | Dauerhafte Feature-Koordination erforderlich ist (`feature-lifecycle`). |

### Planung und Koordination

Diese Skills definieren Produktabsicht, beobachtbares Verhalten, technische Richtung oder die dauerhafte Koordination einer mehrstufigen Auslieferung, bevor die Implementierung fortschreitet.

| Skill | Verwenden, wenn | Beispiel |
|---|---|---|
| [`project-discovery`](skills/planning/project-discovery/) | Ein neues oder übernommenes Produkt keine verlässlichen Nutzer, Ziele, Grenzen oder erste Release-Grenze besitzt. | „Definiere das kleinste nützliche erste Release.“ |
| [`feature-specification`](skills/planning/feature-specification/) | Eine genehmigte größere Capability Regeln, Zustände, Berechtigungen und Akzeptanzkriterien benötigt. | „Spezifiziere Retry- und Ablehnungsverhalten für den Dateiimport.“ |
| [`solution-framing`](skills/planning/solution-framing/) | Eine folgenreiche technische oder Delivery-Richtung noch offen ist. | „Welcher Migrationsansatz ist am sichersten?“ |
| [`compatibility-migration`](skills/planning/compatibility-migration/) | Eine festgelegte Migration alte und neue Konsumenten, Verträge oder Daten sicher koexistieren lassen muss. | „Plane eine kompatible API-Migration über mehrere Releases.“ |
| [`feature-lifecycle`](skills/planning/feature-lifecycle/) | Ein größeres Feature über Sitzungen oder Agenten hinweg einen kompakten revisionsgebundenen Datensatz benötigt. | „Gleiche dieses Feature-Ledger ab und nenne die nächste sichere Aktion.“ |

### Qualität, Untersuchung und Review

Diese Skills untersuchen Evidenz, bewerten Risiken oder prüfen konkrete Änderungen. Sie schaffen Fakten und Grenzen; sie ersetzen keinen verstandenen Implementierungsschritt.

| Skill | Verwenden, wenn | Wichtige Abgrenzung |
|---|---|---|
| [`failure-investigation`](skills/quality/failure-investigation/) | Ein Fehler in Test, Build, Laufzeit, Integration oder Daten außerhalb der Performance-Domäne eine unbekannte Ursache hat. | Erst diagnostizieren, danach mit `safe-code-change` implementieren. |
| [`performance-investigation`](skills/quality/performance-investigation/) | Ein gemessenes Latenz-, Durchsatz-, Speicher- oder Ressourcenproblem Baseline und Experimente benötigt. | Bei „Mach es schneller“ ohne Signal zuerst Messung schaffen. |
| [`security-boundary-analysis`](skills/quality/security-boundary-analysis/) | Ein explizites Threat Model oder eine Vertrauensgrenzenanalyse gefordert ist. | Ein Routine-Review eines Diffs gehört zu `fact-based-code-review`. |
| [`fact-based-code-review`](skills/quality/fact-based-code-review/) | Ein konkreter Diff oder Satz geänderter Dateien eine faktenbasierte Bewertung für die Integration benötigt. | Eine ausdrücklich tiefe Hochrisiko-Prüfung gehört zu `adversarial-deep-review`. |
| [`adversarial-deep-review`](skills/quality/adversarial-deep-review/) | Eine konkrete Hochrisikoänderung ausdrücklich auf Ausfall, Missbrauch, Recovery, Concurrency oder Betrieb herausgefordert werden soll. | Er liefert Risikoevidenz; die normale Integrationsentscheidung trifft `fact-based-code-review`. |

### Spezialisierte Engineering-Arbeit

Diese Skills besitzen einen fokussierten technischen Bereich und eigene Verhaltensschutzmechanismen.

| Skill | Verwenden, wenn | Wichtige Abgrenzung |
|---|---|---|
| [`product-interface-engineering`](skills/specialized/product-interface-engineering/) | Eine Seite, ein Formular, ein Flow, Accessibility-Verhalten, responsives Layout oder sichtbarer UI-Zustand verändert wird. | Backend-Arbeit und verhaltensbewahrende Refactorings liegen außerhalb des Scopes. |
| [`vue-sfc-decomposition`](skills/specialized/vue-sfc-decomposition/) | Eine Vue- oder Nuxt-SFC eine nachgewiesene Verantwortungs-, Wartbarkeits- oder Testbarkeitsgrenze besitzt. | Änderungen am UI-Verhalten gehören zu `product-interface-engineering`. |

Lies vor der Verwendung die `SKILL.md` eines Skills. Bewahre ein vollständiges Skill-Verzeichnis einschließlich vorhandener `references/` und `assets/` auf, weil der Skill darauf verweisen kann.

## Schnellstart

Installiere Git und Python 3.11 oder neuer, bevor du einen Installer verwendest. Die Wrapper für Zed und Codex installieren alle Skills in das gemeinsame Verzeichnis `~/.agents/skills`.

<details>
<summary>macOS, Linux oder WSL</summary>

```sh
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
python3 scripts/install_zed_skills.py  # oder: scripts/install_codex_skills.py
```

</details>

<details>
<summary>Windows PowerShell</summary>

```powershell
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
py scripts\install_zed_skills.py  # oder: scripts\install_codex_skills.py
```

</details>

Starte nach der Installation eine neue Agentensitzung. Der Installer bricht ab, statt ein vorhandenes Skill-Verzeichnis zu ersetzen.

## Installation

### Portabler Kern

Kopiere oder referenziere das gewünschte kategorisierte Quellverzeichnis mit dem dokumentierten Mechanismus deines Clients. AgentSkillForge beansprucht weder einen universellen Installationspfad noch eine allgemeine Konvention zur automatischen Erkennung.

### Flaches ZIP-Bundle

Erzeuge aus einem Quell-Checkout ein manuell installierbares Bundle:

```sh
python3 scripts/build_skill_bundle.py
```

Dadurch entsteht `dist/agent-skill-forge-skills.zip`. Entpacke dessen Inhalt direkt in das Skill-Verzeichnis deines Clients, beispielsweise `~/.agents/skills`; jedes Verzeichnis auf oberster Ebene ist ein vollständiger Skill. Kopiere die kategorisierten Quellverzeichnisse `core/`, `planning/`, `quality/` oder `specialized/` nicht in dieses Ziel.

### Zed und Codex

Verwende den Client-Wrapper, um nur einen Skill zu installieren, wenn du nicht den gesamten Katalog benötigst:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
python3 scripts/install_codex_skills.py --skill performance-investigation
```

Beide Wrapper verwenden denselben Installer und standardmäßig `~/.agents/skills`. Wiederhole `--skill`, um mehrere Skills zu installieren. Verwende `--target`, um in ein anderes Client- oder Repository-Skill-Verzeichnis zu installieren.

> [!CAUTION]
> `--force` löscht jedes ausgewählte Zielverzeichnis und erstellt es neu. Prüfe lokale Änderungen vorher; der Installer führt Dateien nicht zusammen.

Die vollständigen Installationsanleitungen für [Zed](docs/clients/zed.md) und [Codex](docs/clients/codex.md) beschreiben ausgewählte Skills, eigene Zielpfade, Updates, Überprüfung und Deinstallation.

## Skills kombinieren

Häufige Reihenfolgen sind:

- Unbekanntes Repository: `repository-onboarding` erstellt vor umfangreicher Arbeit eine technische Arbeitskarte; `repository-knowledge-curation` übernimmt verifizierte wiederverwendbare Fakten, wenn sie einen kanonischen dauerhaften Ablageort benötigen.
- Neues Produkt: `project-discovery` legt Produktgrenze und Capability-Map fest; anschließend definiert `feature-specification` eine Capability vor technischer Planung oder Implementierung.
- Mehrsitzungs-Feature: `feature-specification` besitzt den Verhaltensvertrag; `solution-framing` klärt folgenreiche technische Entscheidungen, `feature-lifecycle` führt den dauerhaften revisionsgebundenen Datensatz, `safe-code-change` implementiert jede begrenzte Arbeitseinheit und `session-handoff` übernimmt nur tatsächlich unterbrochene konkrete Arbeit.

- Unbekannter technischer Fehler außerhalb der Performance-Domäne: `failure-investigation` belegt Ursache und sichere Änderungsgrenze, danach implementiert `safe-code-change` den Fix und `fact-based-code-review` prüft ihn.
- Gemessenes Latenz-, Durchsatz-, Speicher- oder Ressourcenproblem: Verwende `performance-investigation`, nicht `failure-investigation`; übergib eine verstandene Änderung an `safe-code-change` und prüfe sie anschließend mit `fact-based-code-review`.
- Mehrstufige Migration: `solution-framing` wählt die Richtung nur, wenn sie noch offen ist, `compatibility-migration` definiert die autoritativen Koexistenz- und Stilllegungszustände, `feature-lifecycle` darf Feature-Evidenz daraus verlinken und `safe-code-change` implementiert jeden lokalen Schritt.
- Explizites Threat Model: `security-boundary-analysis` definiert Vertrauensübergänge, Missbrauchspfade und Kontrollpflichten. Danach übernimmt `solution-framing` Architekturentscheidungen, `product-interface-engineering` sichtbare Berechtigungs- oder Recovery-Interaktionen oder `compatibility-migration` die gestufte Koexistenz; die Outputs bleiben getrennt.
- Hochrisikoänderung: Nutze `adversarial-deep-review` nur für eine explizite tiefe Prüfung einer konkreten Änderung und übergib ihre Evidenz anschließend an `fact-based-code-review` für die alleinige Merge-Entscheidung. Ein getracktes Feature darf die Evidenz in `feature-lifecycle` verlinken, ohne Review-Verantwortung zu übernehmen.

Dein KI-Client entscheidet, wann er einen installierten Skill lädt. Beschreibungen sind Routing-Hinweise und keine Garantie für das Verhalten eines Hosts. Statische und Runtime-Contract-Checks liefern nur begrenzte Belege; aus einer Installation allein folgt weder universelle Portabilität noch zuverlässige automatische Aktivierung. Siehe die [Kompatibilitätsmatrix](docs/compatibility.md).

## Optionale Repository-Anweisungen

[`templates/AGENTS.md`](templates/AGENTS.md) ist eine bewusst meinungsstarke Routing-Vorlage für diesen Katalog mit einer kompakten Write-Then-Verify-Regel. Kopiere sie nur in ein Ziel-Repository, wenn deutsche Antworten und `codebase-memory-mcp` gewünscht sind; passe diese Anforderungen andernfalls vorher an oder entferne sie.


## Kompatibilität

| Bereich | Unterstützt oder erforderlich |
|---|---|
| Agent-Skill-Format | Markdown-Verzeichnisse mit `SKILL.md` und relativen lokalen Referenzen |
| Agent-Clients | Unterstützt: Codex CLI und Zed, abhängig von der dokumentierten Evidenzstufe; andere kompatible Clients sind nicht verifiziert |
| Dokumentierte Integration | Zed mit aktivierten Agent Skills; Codex CLI und Codex-IDE-Erweiterung; siehe [Kompatibilitätsrichtlinie](docs/compatibility.md) |
| Python | 3.11 oder neuer für Zed-/Codex-Installer, Paketierung und Repository-Prüfungen |
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
python scripts/run_runtime_evals.py --client fixture --fixture-response "Behavior contract. Verification plan. Baseline evidence and hypothesis experiment. Finding and verification gap. Trust boundary and abuse path threat. Observed revision in the canonical record and next safe action."
python scripts/check_distribution.py
```

Diese Befehle prüfen Skill-Metadaten und -Struktur, lokale Markdown-Links, Verhalten von Installer und Paketierung, statische Deklarationen für Eval- und Runtime-Contracts, deterministische Contract-Ausführung und den Inhalt des verteilten Wheels.

> [!NOTE]
> Der `fixture`-Client prüft den Runtime-Eval-Mechanismus ohne ein Agentenmodell auszuführen. Ein authentifizierter Codex-Modelllauf ist ein ausdrücklicher Release-Check und kein Pull-Request-Gate. Aufruf, Ergebnisartefakt, Client-/Modellversion, Datenschutzfolgen und Grenzen stehen in der [Kompatibilitätsrichtlinie](docs/compatibility.md). Prüfe externe HTTP-Links ausdrücklich mit `python scripts/check_links.py --external`.

<details>
<summary>Projektstruktur</summary>

```text
.
├── skills/                     # Portable Agent Skills
├── evals/                      # Statische Fälle, Runtime-Contracts, Client-Matrix und Tests
├── scripts/                    # Validierung, Runtime-Eval, Paketierung und Installer
├── docs/                       # Client-Anleitungen und Kompatibilitätsrichtlinie
├── templates/                  # Optionale Vorlagen für Repository-Anweisungen
│   ├── AGENTS.md               # Deutsches Skill-Routing und Verifikation
│   └── AGENTS-AIO.md           # Allgemeine All-in-one-Qualitätsregeln
├── .github/workflows/          # Automatisierungs-Workflows
├── CONTRIBUTING.md             # Regeln zum Mitwirken und Clean-Room-Prozess
├── pyproject.toml              # Python-Werkzeuge und Paketmetadaten
├── README.md                   # Englische Dokumentation
├── README.de.md                # Deutsche Dokumentation
└── LICENSE                     # Apache License 2.0
```

Das Python-Wheel ist eine Datendistribution, keine Anwendung und kein importierbares SDK. Es legt README, Agent Skills, Referenzen, Client-Anleitungen und Installer unter `share/agent-skill-forge/` ab.

</details>

## Mitwirken

Beiträge sind willkommen. Lies vor dem Erstellen eines Pull Requests [CONTRIBUTING.md](CONTRIBUTING.md). Neues oder geändertes Skill-Verhalten muss portable Metadaten und gültige lokale Referenzen bewahren, dem Clean-Room-Prozess folgen und die relevanten Evals sowie Prüfungen des Ausgabevertrags aktualisieren.

## Sicherheit und Support

Behandle Skills von Drittanbietern als nicht vertrauenswürdige Anweisungen. Prüfe vor der Installation Inhalt, Herkunft, Links und Abhängigkeiten. Gewähre nicht allein deshalb Zugriff auf Tools, Zugangsdaten oder das Dateisystem, weil ein Skill-Dokument ihn verlangt.

Melde mögliche Sicherheitslücken über GitHubs private Sicherheitsmeldung. Veröffentliche keine sensiblen Details in einem öffentlichen Issue. Verwende [GitHub Issues](https://github.com/RobinGru/AgentSkillForge/issues) für öffentliche Fehlermeldungen und Fragen.

## Lizenz und Hinweise

AgentSkillForge wird unter der [Apache License 2.0](LICENSE) veröffentlicht. Prüfe vor der Weiterverteilung [NOTICE](NOTICE) und [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
