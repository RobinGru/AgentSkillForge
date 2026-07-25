[English](README.md) · **Deutsch**

# AgentSkillForge

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/RobinGru/AgentSkillForge/badge)](https://scorecard.dev/viewer/?uri=github.com/RobinGru/AgentSkillForge)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Klare, wiederverwendbare Anleitungen, die KI-Coding-Assistenten helfen, sorgfältig zu arbeiten und ihre Ergebnisse verständlich zu erklären.

[Zed-Installation](docs/clients/zed.md) · [Skill-Pakete](skills/) · [Mitwirken](CONTRIBUTING.md)

> [!WARNING]
> AgentSkillForge befindet sich derzeit in der Beta-Phase. Die Paketversion ist `0.2.0b1`, und alle sechs Skill-Dokumente verwenden Version `0.2.0-beta.1`. Repository-Prüfungen decken Struktur, lokale Links, Paketierung und statische Aktivierungsfälle ab; sie führen keine Agentenmodelle aus und belegen keine Kompatibilität mit jedem Client. Eine formale Wartungsrichtlinie oder ein Release-Rhythmus ist nicht dokumentiert.

## Über das Projekt

AgentSkillForge ist eine Sammlung kleiner Anleitungspakete für KI-Coding-Assistenten. Du kannst dir einen Skill wie eine Checkliste vorstellen: Er sagt dem Assistenten, welche Art Aufgabe vorliegt, was er zuerst prüfen soll und wie er das Ergebnis erklärt.

Ein Skill hilft zum Beispiel bei einer schwierigen Entscheidung, ein anderer bei einer kleinen Fehlerbehebung, ein weiterer beim Prüfen einer fertigen Änderung. Die Pakete bestehen aus einfachen Markdown-Dateien und sind deshalb nicht an ein bestimmtes KI-Tool gebunden. Für Zed gibt es einen dokumentierten Installer. Andere Tools benötigen ihren eigenen Weg, Skill-Ordner zu laden.

## Highlights

- **Klare Anleitung:** Jeder Skill sagt, wofür er gedacht ist und wann er nicht passt.
- **Ehrliche Ergebnisse:** Skills fordern den Assistenten auf, Fakten, Vermutungen und nicht ausgeführte Prüfungen zu trennen.
- **Gut kombinierbar:** Du kannst Skills verbinden, wenn eine Aufgabe mehrere Schritte braucht, etwa planen, Code ändern und prüfen.
- **Einfach übertragbar:** Ein Skill ist ein Ordner mit Markdown-Dateien, den du in ein kompatibles KI-Tool kopieren kannst.
- **Vorher geprüft:** Das Repository enthält automatische Prüfungen für Dateien, Links, Tests und Paketinhalt.
- **Eigenständige Inhalte:** Mitwirkende schreiben neue Skills ausgehend vom Problem, statt einen anderen Skill zu kopieren.

## Schnellstart

Installiere Git und Python 3.11 oder neuer, bevor du den Zed-Installer verwendest. Unter macOS, Linux oder WSL:

```sh
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
python3 scripts/install_zed_skills.py
```

Unter Windows PowerShell:

```powershell
git clone https://github.com/RobinGru/AgentSkillForge.git AgentSkillForge
cd AgentSkillForge
py scripts\install_zed_skills.py
```

Der Installer kopiert alle Skills in Zeds gemeinsames Verzeichnis `~/.agents/skills` und zeigt die installierten Pfade an. Starte danach eine neue Agentensitzung. Wenn ein Ordner bereits existiert, bricht der Installer ab, statt ihn zu ersetzen.

Die [vollständige Zed-Installationsanleitung](docs/clients/zed.md) beschreibt ausgewählte Skills, eigene Zielpfade, Updates, Überprüfung und Deinstallation.

## Skill-Katalog

- [`skills/solution-framing/`](skills/solution-framing/) — Hilft dem Assistenten, eine sichere Richtung zu wählen, wenn eine Aufgabe unklar ist oder wichtige Abwägungen enthält.
- [`skills/safe-code-change/`](skills/safe-code-change/) — Hilft ihm, eine kleine, verstandene Codeänderung vorzunehmen und zu prüfen, ob sie funktioniert.
- [`skills/evidence-led-code-review/`](skills/evidence-led-code-review/) — Hilft ihm, eine vorgeschlagene Codeänderung zu prüfen und Probleme klar zu erklären.
- [`skills/product-interface-engineering/`](skills/product-interface-engineering/) — Hilft ihm, verwendete Seiten, Formulare, Accessibility und responsives Verhalten zu verbessern.
- [`skills/performance-investigation/`](skills/performance-investigation/) — Hilft ihm, ein gemessenes Geschwindigkeits- oder Speicherproblem zu untersuchen, bevor er Code ändert.
- [`skills/vue-sfc-decomposition/`](skills/vue-sfc-decomposition/) — Hilft ihm, eine schwierige Vue- oder Nuxt-Komponente aufzuteilen, ohne ihr Verhalten zu ändern.

Lies vor der Verwendung die `SKILL.md` des Pakets. Bewahre das vollständige Verzeichnis einschließlich vorhandener `references/` und `assets/` auf, weil der Workflow auf diese Dateien verweisen kann.

## Installation

### Portabler Kern

Kopiere oder referenziere das gewünschte Verzeichnis `skills/<name>/` mit dem dokumentierten Mechanismus deines Agent-Clients. Das Repository beansprucht weder einen universellen Installationspfad noch eine allgemeine Konvention zur automatischen Erkennung.

### Zed

Der enthaltene Installer unterstützt Windows-, macOS-, Linux- und WSL-Pfade über Pythons Dateisystem-APIs. Installiere einen Skill mit:

```sh
python3 scripts/install_zed_skills.py --skill performance-investigation
```

Installiere mehrere Skills, indem du `--skill` wiederholst. Verwende `--target`, wenn Zed für ein anderes Verzeichnis konfiguriert ist.

> [!CAUTION]
> `--force` löscht jedes ausgewählte Zielverzeichnis und erstellt es neu. Prüfe lokale Änderungen vor der Verwendung; der Vorgang führt Dateien nicht zusammen.

## Verwendung

Wähle den Skill, der wirklich zur Aufgabe passt. Wähle ihn nicht nur, weil ein Wort im Prompt ähnlich klingt.

Eine häufige Reihenfolge ist:

1. Verwende `solution-framing`, wenn eine wichtige Entscheidung noch unklar ist.
2. Verwende `performance-investigation`, wenn du ein echtes Geschwindigkeits- oder Speicherproblem untersuchen möchtest.
3. Verwende `safe-code-change` für eine gezielte Fehlerbehebung.
4. Verwende `evidence-led-code-review`, um die fertige Änderung zu prüfen.

Dein KI-Tool entscheidet, wann es einen installierten Skill lädt. Jeder Skill erklärt außerdem, welche Art Antwort der Assistent geben soll.

## Voraussetzungen und Kompatibilität

| Bereich | Unterstützt oder erforderlich |
|---|---|
| Git | Für den dokumentierten, auf Klonen basierenden Schnellstart erforderlich |
| Skill-Format | Markdown-Pakete mit `SKILL.md` und relativen lokalen Referenzen |
| Agent-Clients | Clients, die kompatible Skill-Verzeichnisse laden können; die genaue Unterstützung hängt von der Client-Konfiguration ab |
| Dokumentierte Integration | Zed mit aktivierten Agent Skills |
| Python | 3.11 oder neuer für Zed-Installer, Paketierung und Repository-Prüfungen |
| CI-Umgebung | Python 3.12 auf `ubuntu-latest` |
| Paket-Runtime | Kein importierbares Python-Modul; das Wheel verteilt Skill- und Hilfsdateien als Daten |

Die Skill-Dokumente selbst benötigen keine Python-Runtime. Python wird vom Installer und den Repository-Werkzeugen verwendet.

## Validierung und Entwicklung

Installiere die Entwicklungsabhängigkeiten und führe die Prüfungen des Repository-Workflows aus:

```sh
python -m pip install -e ".[dev]"
python scripts/validate_repository.py
python scripts/check_links.py
pytest
python scripts/run_evals.py
python scripts/check_distribution.py
```

Diese Befehle decken Folgendes ab:

- Skill-Namen, Frontmatter, Verzeichnisstruktur, relative Referenzen und README-Inventar;
- lokale Markdown-Ziele und Anker;
- Tests für Validator, Installer, Paketierung und Skill-Verträge;
- statische Abdeckung des Eval-Manifests für positive, negative, Konflikt-, Ausgabe- und adversariale Fälle;
- Wheel-Inhalte für jedes verteilte Skill-Dokument und jede Zed-Hilfsdatei.

`python scripts/run_evals.py` validiert nur statische Falldeklarationen. Der Befehl führt keinen Agenten aus und belegt keine Runtime-Portabilität. Externe HTTP-Links werden nur geprüft, wenn `python scripts/check_links.py --external` ausdrücklich ausgeführt wird.

## Projektstruktur

```text
.
├── skills/                     # Portable skill packages
├── evals/                      # Static cases and repository tests
├── scripts/                    # Validation, packaging, and Zed installer tools
├── docs/clients/zed.md         # Zed integration guide
├── .github/workflows/          # Repository validation workflow
├── CONTRIBUTING.md             # Contribution and clean-room rules
├── pyproject.toml              # Python tooling and data-package metadata
├── README.md                   # English documentation
├── README.de.md                # German documentation
└── LICENSE                     # Apache License 2.0
```

Das Python-Wheel ist eine Datendistribution, keine Anwendung und kein importierbares SDK. Es legt README, Skill-Pakete, Referenzen, Zed-Anleitung und Installer unter `share/agent-skill-forge/` ab.

## Dokumentation

- [Zed-Installation](docs/clients/zed.md)
- [Beitragsleitfaden](CONTRIBUTING.md)
- [Skill-Pakete](skills/)
- [Statische Eval-Fälle](evals/manifest.yaml)
- [Hinweise zu Drittinhalten](THIRD_PARTY_NOTICES.md)

## Mitwirken

Beiträge sind willkommen. Lies vor dem Erstellen eines Pull Requests [CONTRIBUTING.md](CONTRIBUTING.md). Neues oder geändertes Skill-Verhalten muss portable Metadaten beibehalten, gültige lokale Referenzen erhalten, dem Clean-Room-Prozess folgen und die relevanten Evals sowie Prüfungen des Ausgabevertrags aktualisieren.

## Sicherheit

Behandle alle Skills von Drittanbietern als nicht vertrauenswürdige Anweisungen. Prüfe vor der Installation Inhalt, Herkunft, Links und Abhängigkeiten. Gewähre nicht allein deshalb Zugriff auf Tools, Zugangsdaten oder das Dateisystem, weil ein Skill-Dokument ihn verlangt.

Dieses Repository stellt keine `SECURITY.md` bereit. Melde mögliche Sicherheitslücken über die private Sicherheitsmeldung von GitHub; veröffentliche keine sensiblen Details in einem öffentlichen Issue.

## Support

Verwende GitHub Issues für öffentliche Fehlermeldungen und Fragen. Füge keine sensiblen Sicherheitsdetails zu einem Issue hinzu; nutze stattdessen die private Sicherheitsmeldung.

## Lizenz und Hinweise

AgentSkillForge wird unter der [Apache License 2.0](LICENSE) veröffentlicht. Prüfe vor der Weiterverteilung [NOTICE](NOTICE) und [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
