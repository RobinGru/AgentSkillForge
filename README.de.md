[English](README.md) · **Deutsch**

# AgentSkillForge

![AgentSkillForge-Banner](assets/github-banner.jpg)

[![Validate](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/validate.yml)
[![Runtime evals](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/runtime-evals.yml)
[![CodeQL](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/RobinGru/AgentSkillForge/actions/workflows/codeql.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)

Wiederverwendbare Agent Skills, die KI-Coding-Assistenten zu sorgfältigen Änderungen und verständlichen Ergebnissen anleiten.

[Skills entdecken](#skill-katalog) · [Mit Zed oder Codex installieren](#schnellstart) · [Mitwirken](CONTRIBUTING.md)

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

## Skill-Katalog

Wähle den Skill, der wirklich zur Aufgabe passt – nicht nur zu einem einzelnen Wort im Prompt. Der Katalog folgt einem typischen Arbeitsablauf; verwende die spezialisierten Investigations-Skills, bevor du eine ansonsten verstandene Änderung vornimmst.

| Skill | Wann verwenden? | Beispiel |
|---|---|---|
| [`skills/project-discovery/`](skills/project-discovery/) | Ein neues oder unklares Produkt benötigt Nutzer, Ziele, Grenzen und eine erste Capability-Map. | „Definiere das kleinste nützliche erste Release.“ |
| [`skills/feature-specification/`](skills/feature-specification/) | Eine größere Capability benötigt beobachtbare Regeln, Zustände, Berechtigungen und Akzeptanzkriterien. | „Spezifiziere Retry- und Ablehnungsverhalten für den Dateiimport.“ |
| [`skills/feature-lifecycle/`](skills/feature-lifecycle/) | Ein größeres Feature benötigt eine dauerhafte, revisionsgebundene Koordination über Sitzungen, Agenten oder Arbeitseinheiten hinweg. | „Gleiche dieses Feature-Ledger ab und nenne die nächste sichere Aktion.“ |
| [`skills/solution-framing/`](skills/solution-framing/) | Die Richtung ist unklar oder eine Entscheidung enthält wichtige Abwägungen. | „Welcher Migrationsansatz ist am sichersten?“ |
| [`skills/compatibility-migration/`](skills/compatibility-migration/) | Eine festgelegte Richtung erfordert sichere Koexistenz von altem und neuem Verhalten über mehrere Schritte oder Konsumenten. | „Plane eine kompatible API-Migration über mehrere Releases.“ |
| [`skills/failure-investigation/`](skills/failure-investigation/) | Ein technischer Fehler außerhalb der Performance-Domäne hat eine unbekannte Ursache oder sichere Änderungsgrenze. | „Ermittle vor einem Fix, warum diese Integration fehlschlägt.“ |
| [`skills/performance-investigation/`](skills/performance-investigation/) | Du untersuchst ein gemessenes Latenz-, Durchsatz- oder Speicherproblem. | „Warum ist dieser Endpunkt langsamer geworden?“ |
| [`skills/security-boundary-analysis/`](skills/security-boundary-analysis/) | Eine explizite Security- oder Threat-Modeling-Aufgabe benötigt Vertrauensübergänge, Missbrauchspfade, Kontrollen und Restunsicherheit. | „Erstelle ein Threat Model für diese Webhook-Grenze.“ |
| [`skills/safe-code-change/`](skills/safe-code-change/) | Du brauchst eine kleine, verstandene Änderung oder Fehlerbehebung. | „Behebe diesen reproduzierbaren Validierungsfehler.“ |
| [`skills/product-interface-engineering/`](skills/product-interface-engineering/) | Eine Seite, ein Formular, eine Interaktion, Accessibility oder responsives Verhalten braucht Arbeit. | „Mache dieses Checkout-Formular mobil nutzbar.“ |
| [`skills/vue-sfc-decomposition/`](skills/vue-sfc-decomposition/) | Eine Vue- oder Nuxt-Komponente soll ohne Verhaltensänderung aufgeteilt werden. | „Teile diese große Vue-SFC in wartbare Teile auf.“ |
| [`skills/fact-based-code-review/`](skills/fact-based-code-review/) | Eine Änderung ist bereit zur Prüfung und braucht einen faktenbasierten Code-Review. | „Prüfe diesen Pull Request vor dem Merge.“ |
| [`skills/adversarial-deep-review/`](skills/adversarial-deep-review/) | Eine ausdrücklich gewünschte tiefe Prüfung einer konkreten Hochrisiko-Änderung braucht evidenzbasierte Stressszenarien. | „Prüfe diesen Payment-Retry-Diff adversarial.“ |
| [`skills/session-handoff/`](skills/session-handoff/) | Unfertige Repository-Arbeit muss von einer anderen Sitzung oder Person anhand verifizierter Zustände fortgesetzt werden. | „Halte Worktree und die eine sichere nächste Aktion fest.“ |

Lies vor der Verwendung die `SKILL.md` eines Skills. Bewahre das vollständige Verzeichnis einschließlich vorhandener `references/` und `assets/` auf, weil der Skill darauf verweisen kann.

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

Kopiere oder referenziere das gewünschte Verzeichnis `skills/<name>/` mit dem dokumentierten Mechanismus deines Clients. AgentSkillForge beansprucht weder einen universellen Installationspfad noch eine allgemeine Konvention zur automatischen Erkennung.

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

- Neues Produkt: `project-discovery` legt Produktgrenze und Capability-Map fest; anschließend definiert `feature-specification` eine Capability vor technischer Planung oder Implementierung.
- Mehrsitzungs-Feature: `feature-specification` besitzt den Verhaltensvertrag; `solution-framing` klärt folgenreiche technische Entscheidungen, `feature-lifecycle` führt den dauerhaften revisionsgebundenen Datensatz, `safe-code-change` implementiert jede begrenzte Arbeitseinheit und `session-handoff` übernimmt nur tatsächlich unterbrochene konkrete Arbeit.

- Unbekannter technischer Fehler außerhalb der Performance-Domäne: `failure-investigation` belegt Ursache und sichere Änderungsgrenze, danach implementiert `safe-code-change` den Fix und `fact-based-code-review` prüft ihn.
- Gemessenes Latenz-, Durchsatz-, Speicher- oder Ressourcenproblem: Verwende `performance-investigation`, nicht `failure-investigation`; übergib eine verstandene Änderung an `safe-code-change` und prüfe sie anschließend mit `fact-based-code-review`.
- Mehrstufige Migration: `solution-framing` wählt die Richtung nur, wenn sie noch offen ist, `compatibility-migration` definiert sichere Koexistenz- und Stilllegungszustände und `safe-code-change` implementiert jeden lokalen Schritt.
- Explizites Threat Model: `security-boundary-analysis` definiert Vertrauensübergänge, Missbrauchspfade und Kontrollpflichten. Danach übernimmt `solution-framing` Architekturentscheidungen, `product-interface-engineering` sichtbare Berechtigungs- oder Recovery-Interaktionen oder `compatibility-migration` die gestufte Koexistenz; die Outputs bleiben getrennt.
- Hochrisiko-Änderung: Verwende `adversarial-deep-review` nur für eine ausdrücklich gewünschte tiefe Prüfung einer konkreten Änderung und übergib die Evidenz anschließend an `fact-based-code-review` für die Merge-Entscheidung.

Dein KI-Client entscheidet, wann er einen installierten Skill lädt. Beschreibungen sind Routing-Hinweise und keine Garantie für das Verhalten eines Hosts. Statische und Runtime-Contract-Checks liefern nur begrenzte Belege; aus einer Installation allein folgt weder universelle Portabilität noch zuverlässige automatische Aktivierung. Siehe die [Kompatibilitätsmatrix](docs/compatibility.md).

## Optionale Repository-Anweisungen

[`templates/AGENTS.md`](templates/AGENTS.md) ist eine bewusst meinungsstarke Vorlage für die Repository-Wurzel. Sie übernimmt das Routing zwischen den Skills und definiert eine kompakte Write-Then-Verify-Regel. Kopiere sie nur in ein Ziel-Repository, wenn deutsche Antworten und `codebase-memory-mcp` gewünscht sind; passe diese Anforderungen andernfalls vorher an oder entferne sie. Projektspezifische Regeln gehören in die kopierte Datei, nicht in die verteilten Skills.

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
python scripts/run_runtime_evals.py --client fixture --fixture-response "Behavior contract. Verification plan. Baseline evidence and hypothesis experiment. Finding and verification gap. Trust boundary and abuse path threat. Revision-bound evidence and next safe action."
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
├── templates/AGENTS.md         # Optionale Repository-Anweisungen
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
