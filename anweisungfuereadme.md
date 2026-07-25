# KI-Anweisung zur Erstellung von `README.md` und `README.de.md`

## Zweck dieser Datei

Diese Datei ist eine verbindliche Arbeitsanweisung für eine KI, die für dieses Repository zwei hochwertige GitHub-README-Dateien erstellen oder vollständig überarbeiten soll:

- `README.md` – englische Hauptversion
- `README.de.md` – vollständige deutsche Übersetzung

Die README-Dateien sollen dem modernen Stand von GitHub-Repositories im Juni 2026 entsprechen. Sie müssen technisch korrekt, klar strukturiert, professionell formuliert, vertrauenswürdig, gut lesbar und für neue Nutzer schnell verständlich sein.

Es dürfen ausschließlich Englisch und Deutsch verwendet werden. Weitere Sprachversionen, Sprachordner oder Übersetzungsdateien sind nicht vorgesehen.

---

# 1. Rolle der KI

Du arbeitest gleichzeitig als:

- technischer Redakteur
- Open-Source-Maintainer
- Software-Dokumentationsspezialist
- GitHub-Repository-Reviewer
- UX-Autor für Entwicklerprodukte
- technischer Marketing-Redakteur

Deine Aufgabe ist nicht, eine generische README mit Platzhaltern zu erzeugen. Du musst zuerst das Repository analysieren und anschließend zwei projektspezifische README-Dateien erstellen.

Die README soll wie eine professionelle technische Produkt-Landingpage funktionieren. Sie soll neue Besucher schnell überzeugen, ohne werblich übertrieben oder unseriös zu wirken.

---

# 2. Verbindliche Sprachregeln

## 2.1 Hauptsprache

`README.md` wird vollständig auf Englisch geschrieben.

Englisch ist die Hauptsprache des Repositorys und die Standardsprache der GitHub-Landingpage.

## 2.2 Deutsche Übersetzung

`README.de.md` wird vollständig auf Deutsch geschrieben.

Die deutsche Version muss inhaltlich vollständig mit der englischen Version übereinstimmen.

## 2.3 Sprachumschalter

Beide Dateien müssen ganz oben einen Sprachumschalter enthalten.

In `README.md`:

```md
**English** · [Deutsch](README.de.md)
```

In `README.de.md`:

```md
[English](README.md) · **Deutsch**
```

Keine Flaggen als alleinige Sprachkennzeichnung verwenden.

## 2.4 Nicht übersetzen

Folgende Inhalte dürfen in der deutschen Datei normalerweise nicht übersetzt oder verändert werden:

- Dateinamen
- Verzeichnisnamen
- Befehle
- CLI-Optionen
- Umgebungsvariablen
- API-Endpunkte
- Funktionsnamen
- Klassennamen
- Paketnamen
- Importpfade
- Produktnamen
- Markennamen
- Lizenznamen
- Versionsnummern
- URLs
- Codebeispiele
- technische Schlüsselwörter, wenn eine Übersetzung unüblich oder missverständlich wäre

Beispiel:

```md
Set the `DATABASE_URL` environment variable.
```

Deutsch:

```md
Setze die Umgebungsvariable `DATABASE_URL`.
```

Nicht:

```md
Setze die Umgebungsvariable `DATENBANK_URL`.
```

---

# 3. Repository zuerst vollständig analysieren

Bevor du Text schreibst, untersuche alle relevanten Dateien und Verzeichnisse des Repositorys.

Prüfe insbesondere:

- vorhandene `README`-Dateien
- Quellcode
- Paket- und Projektdateien
- Build-Konfiguration
- Abhängigkeiten
- Skripte
- CLI-Befehle
- API-Routen
- Docker-Dateien
- Compose-Dateien
- Konfigurationsdateien
- `.env.example`
- Tests
- Beispiele
- Dokumentation
- Lizenz
- Changelog
- Contribution Guidelines
- Security Policy
- GitHub Actions
- Release-Konfiguration
- unterstützte Plattformen
- unterstützte Runtime-Versionen
- Projektstatus
- Screenshots und Medien
- Repository-Struktur
- bekannte Einschränkungen

Typische Dateien, die geprüft werden sollen:

```text
package.json
pnpm-lock.yaml
package-lock.json
yarn.lock
pyproject.toml
requirements.txt
Cargo.toml
go.mod
pom.xml
build.gradle
Dockerfile
docker-compose.yml
compose.yml
.env.example
Makefile
LICENSE
CHANGELOG.md
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
.github/
docs/
examples/
src/
tests/
```

Nutze ausschließlich Informationen, die durch das Repository, vorhandene Dokumentation oder eindeutig erkennbare Projektdateien belegt sind.

---

# 4. Keine erfundenen Angaben

Du darfst keine technischen oder organisatorischen Angaben erfinden.

Insbesondere nicht erfinden:

- Leistungswerte
- Benchmarks
- Nutzerzahlen
- Downloadzahlen
- Kunden
- Unternehmen
- Referenzen
- unterstützte Plattformen
- unterstützte Versionen
- API-Funktionen
- Installationsschritte
- Systemanforderungen
- Sicherheitsmerkmale
- Roadmap-Termine
- Wartungsstatus
- Lizenz
- Supportkanäle
- URLs
- Kontaktadressen
- Badges
- Paketnamen
- Docker-Images
- Demo-Links
- Dokumentationsseiten
- Projektstatus wie „production-ready“

Wenn eine wichtige Information nicht ermittelt werden kann, verwende keine ausgedachte Aussage.

Stattdessen:

1. lasse den betreffenden Abschnitt weg, wenn er nicht zwingend notwendig ist;
2. kennzeichne eine offene Stelle eindeutig;
3. oder verwende einen klar sichtbaren Platzhalter.

Zulässiges Beispiel:

```md
<!-- TODO: Add the official documentation URL. -->
```

Unzulässiges Beispiel:

```md
Documentation is available at https://docs.example.com.
```

wenn diese URL nicht existiert oder nicht belegt ist.

---

# 5. Ziel der README

Jede README muss neue Besucher möglichst schnell zu folgenden Antworten führen:

1. Was ist dieses Projekt?
2. Welches Problem löst es?
3. Für wen ist es gedacht?
4. Was sind die wichtigsten Vorteile?
5. Wie installiere ich es?
6. Wie starte ich es?
7. Wie verwende ich es?
8. Welche Voraussetzungen gibt es?
9. Wie konfiguriere ich es?
10. Wo finde ich weitere Dokumentation?
11. Wie melde ich Fehler?
12. Wie kann ich beitragen?
13. Wie melde ich Sicherheitsprobleme?
14. Unter welcher Lizenz steht das Projekt?
15. Wird das Projekt aktiv gepflegt?

Die wichtigsten Antworten müssen möglichst weit oben stehen.

---

# 6. Grundprinzip für den Aufbau

Die README soll nicht einfach alle verfügbaren Informationen sammeln.

Sie soll eine klare Informationshierarchie besitzen:

1. verstehen
2. Vertrauen gewinnen
3. schnell starten
4. Funktionen kennenlernen
5. Details nachschlagen
6. Unterstützung erhalten
7. mitwirken

Die README ist ein Einstiegspunkt und kein vollständiges Handbuch.

Ausführliche technische Inhalte gehören bei Bedarf in das Verzeichnis `docs/`.

---

# 7. Empfohlene Hauptstruktur

Verwende die folgenden Abschnitte in dieser Reihenfolge, sofern sie für das Projekt sinnvoll und belegbar sind.

Nicht jeder Abschnitt ist für jedes Repository verpflichtend. Entferne irrelevante Abschnitte vollständig, anstatt leere Überschriften zu erzeugen.

```text
1. Sprachumschalter
2. Projektname
3. Logo oder Projektgrafik
4. Ein-Satz-Nutzenversprechen
5. Wichtige Links
6. Badges
7. Screenshot, Demo oder minimales Codebeispiel
8. Projektüberblick
9. Highlights
10. Projektstatus oder Warnhinweis
11. Quick Start
12. Voraussetzungen
13. Installation
14. Verwendung
15. Konfiguration
16. Dokumentation
17. Architektur oder Funktionsweise
18. Projektstruktur
19. Kompatibilität
20. Roadmap
21. Mitwirken
22. Sicherheit
23. Support
24. Lizenz
25. Danksagungen
26. Zitation
```

---

# 8. Kopfbereich der README

Der Kopfbereich ist der wichtigste Teil der README.

Er muss innerhalb weniger Sekunden verständlich machen:

- wie das Projekt heißt
- was es ist
- wem es hilft
- welchen konkreten Nutzen es bietet
- wie man starten oder mehr erfahren kann

## 8.1 Projektname

Verwende genau eine Hauptüberschrift mit `#`.

Beispiel:

```md
# Project Name
```

Keine zweite `#`-Überschrift verwenden.

## 8.2 Logo

Ein vorhandenes offizielles Logo darf verwendet werden.

Beispiel:

```md
<div align="center">
  <img
    src="docs/assets/logo.svg"
    alt="Project Name logo"
    width="160"
  />
</div>
```

Regeln:

- nur vorhandene Bilddateien verwenden
- aussagekräftigen `alt`-Text schreiben
- keine übergroßen Bilder
- möglichst SVG oder optimiertes WebP/PNG verwenden
- keine erfundenen Bildpfade
- keine externen Bilder ohne erkennbaren Grund einbinden

## 8.3 Nutzenversprechen

Direkt unter dem Projektnamen steht ein kurzer, konkreter Satz.

Empfohlene Formel:

```text
[Project name] is a [product category] for [target audience] that helps [specific result].
```

Optional:

```text
[Project name] is a [product category] for [target audience] that helps [specific result] without [common problem].
```

Das Nutzenversprechen muss konkret sein.

Schlecht:

```text
A modern and powerful application.
```

Besser:

```text
A self-hosted deployment dashboard for small development teams.
```

## 8.4 Wichtige Links

Nur tatsächlich vorhandene und relevante Links aufnehmen.

Mögliche Links:

- Documentation
- Demo
- Releases
- Changelog
- Report Bug
- Request Feature
- Discussions

Beispiel:

```md
[Documentation](...) ·
[Demo](...) ·
[Report Bug](...) ·
[Request Feature](...)
```

Keine toten, erfundenen oder vorläufigen Links einbauen.

---

# 9. Badges

Badges sind nur zulässig, wenn sie einen echten Informationswert besitzen und korrekt funktionieren.

Geeignete Badges:

- Build-Status
- CI-Status
- Teststatus
- Release-Version
- Paketversion
- Lizenz
- Code Coverage
- unterstützte Runtime-Version
- Container-Image
- Dokumentationsstatus

Verwende in der Regel höchstens drei bis sechs wichtige Badges im sichtbaren Kopfbereich.

Vermeide:

- Besucherzähler
- dekorative Technologie-Badges
- „Made with love“
- „Awesome“
- übermäßig viele Social-Media-Badges
- Badges ohne funktionierenden Link
- Badges zu nicht vorhandenen Workflows
- Badges mit erfundenen Paketnamen
- Badges für interne oder irrelevante Dienste

Jeder Status-Badge soll möglichst auf die zugehörige Detailseite verlinken.

---

# 10. Screenshot, Demo oder Codebeispiel

Wähle die Darstellungsform passend zum Projekttyp.

## Für sichtbare Anwendungen

Bei Webanwendungen, Desktop-Apps, Terminal-UIs oder Visualisierungen ist ein aktueller Screenshot sinnvoll.

```md
![Dashboard showing deployment status](docs/assets/dashboard.webp)
```

## Für Bibliotheken und SDKs

Bei Bibliotheken ist ein kurzes, funktionierendes Codebeispiel meist besser.

```ts
import { createClient } from "@example/sdk";

const client = createClient();
const result = await client.run();
```

## Für CLI-Tools

Zeige einen typischen Befehl und bei Bedarf eine kurze Beispielausgabe.

```bash
projectctl deploy my-project
```

## Regeln

- nur aktuelle Medien verwenden
- keine veralteten Oberflächen zeigen
- Code muss zur aktuellen API passen
- Beispielbefehle müssen tatsächlich funktionieren
- Animationen und GIFs nur sparsam verwenden
- keine riesigen Medien einbinden
- Alt-Texte müssen den Bildinhalt beschreiben

---

# 11. Abschnitt „About“ oder „Über das Projekt“

Dieser Abschnitt soll in zwei bis vier kurzen Absätzen erklären:

- Was ist das Projekt?
- Für wen ist es gedacht?
- Welches Problem löst es?
- Wie löst es dieses Problem?
- Was unterscheidet es von naheliegenden Alternativen?

Englische Überschrift:

```md
## About
```

Deutsche Überschrift:

```md
## Über das Projekt
```

Vermeide lange Entstehungsgeschichten am Anfang.

Die Geschichte des Projekts darf nur aufgenommen werden, wenn sie für Verständnis, Vertrauen oder Nutzung relevant ist.

---

# 12. Highlights

Fasse die wichtigsten Vorteile in drei bis sechs Punkten zusammen.

Empfohlenes Format:

```md
## Highlights

- **Fast setup:** Start locally with one documented command.
- **Self-hosted:** Keep project data within your own infrastructure.
- **Extensible:** Add integrations through a documented interface.
- **Observable:** Use built-in health checks and structured logs.
```

Jeder Punkt besteht aus:

1. einer kurzen hervorgehobenen Eigenschaft;
2. einer konkreten Erklärung oder einem belegbaren Nutzen.

Nicht verwenden:

```md
- Fast
- Modern
- Secure
- Easy
```

Solche Einzelwörter sind zu ungenau.

---

# 13. Marketingwörter und Werbesprache

Die README darf überzeugend formuliert sein. Sie darf jedoch nicht wie unbelegte Werbung wirken.

## 13.1 Zulässige Begriffe

Diese Begriffe dürfen verwendet werden, wenn sie durch das Repository oder eine konkrete Erklärung gestützt werden:

- fast
- lightweight
- efficient
- reliable
- stable
- developer-friendly
- type-safe
- extensible
- modular
- self-hosted
- privacy-first
- local-first
- secure by default
- accessible
- configurable
- cross-platform
- reproducible
- scalable
- low-latency
- resource-efficient
- production-ready

## 13.2 Belegpflicht

Marketingbegriffe müssen konkretisiert werden.

Schlecht:

```text
Blazing-fast performance.
```

Besser:

```text
Processes large files through a streaming pipeline without loading the complete file into memory.
```

Schlecht:

```text
Easy to use.
```

Besser:

```text
Install the package and create the first client with three lines of code.
```

Schlecht:

```text
Secure.
```

Besser:

```text
Secrets remain on the local system and are not sent to an external service.
```

## 13.3 Problematische Begriffe

Vermeide unbelegte oder übertriebene Wörter wie:

- revolutionary
- groundbreaking
- ultimate
- unmatched
- unparalleled
- magical
- game-changing
- world-class
- best-in-class
- next-generation
- cutting-edge
- insanely fast
- effortless
- flawless
- bulletproof
- 100% secure
- enterprise-grade

Solche Begriffe sind nur dann zulässig, wenn unmittelbar eine nachvollziehbare und überprüfbare Begründung folgt. In den meisten Fällen ist eine sachliche Alternative vorzuziehen.

## 13.4 Bessere Formulierungen

| Schwach oder übertrieben | Besser und konkreter |
|---|---|
| Revolutionary architecture | Event-driven architecture with independently deployable workers |
| Enterprise-grade security | OIDC authentication, encrypted secrets and audit logging |
| Blazing fast | Completes the documented benchmark in a measured time |
| Effortless setup | Starts with one Docker Compose command |
| Highly scalable | Supports horizontal worker scaling |
| Zero configuration | Works with sensible defaults; configuration is optional |
| Production-ready | Used in production and covered by integration tests |
| Lightweight | Runs as a single binary without external runtime dependencies |

Verwende solche Aussagen nur, wenn sie tatsächlich stimmen.

---

# 14. Projektstatus und Warnhinweise

Wenn das Projekt experimentell, Alpha, Beta, archiviert, nicht aktiv gepflegt oder vor Version 1.0 ist, muss dies weit oben sichtbar sein.

Beispiel:

```md
> [!WARNING]
> This project is currently in beta. Configuration formats may change before version 1.0.
```

Deutsch:

```md
> [!WARNING]
> Dieses Projekt befindet sich derzeit in der Beta-Phase. Konfigurationsformate können sich vor Version 1.0 noch ändern.
```

Mögliche Hinweise:

```md
> [!NOTE]
```

```md
> [!TIP]
```

```md
> [!IMPORTANT]
```

```md
> [!WARNING]
```

```md
> [!CAUTION]
```

Hinweise sparsam einsetzen.

---

# 15. Quick Start

Der Quick Start ist einer der wichtigsten Abschnitte.

Er zeigt den kürzesten vollständigen Weg von einer neuen Umgebung zu einem funktionierenden Ergebnis.

Englische Überschrift:

```md
## Quick Start
```

Deutsche Überschrift:

```md
## Schnellstart
```

Der Quick Start soll:

- kopierbar sein
- vollständig sein
- getestet sein
- möglichst wenige Schritte enthalten
- notwendige Voraussetzungen nennen
- keine unerklärten Platzhalter enthalten
- das erwartete Ergebnis nennen
- keine optionalen Details enthalten
- zur aktuellen Projektversion passen

Beispiel für eine Anwendung:

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
cp .env.example .env
docker compose up -d
```

Danach:

```md
Open `http://localhost:3000`.
```

Deutsch:

```md
Öffne anschließend `http://localhost:3000`.
```

Beispiel für eine Bibliothek:

```bash
npm install @example/package
```

```ts
import { createClient } from "@example/package";

const client = createClient();
const result = await client.run();
```

Keinen Quick Start erzeugen, der nur theoretisch plausibel klingt. Prüfe die Befehle anhand des Repositorys.

---

# 16. Voraussetzungen

Nenne nur tatsächlich erforderliche Voraussetzungen.

Englisch:

```md
## Requirements
```

Deutsch:

```md
## Voraussetzungen
```

Mögliche Inhalte:

- Runtime-Version
- Betriebssystem
- Datenbank
- Docker-Version
- Paketmanager
- Compiler
- externe Dienste
- Hardwareanforderungen
- Berechtigungen

Beispiel:

```md
- Node.js 22 or newer
- PostgreSQL 17
- Docker 27 or newer for container-based installation
```

Optionale Abhängigkeiten separat kennzeichnen.

```md
### Optional
```

Keine Versionsnummern raten.

---

# 17. Installation

Dokumentiere nur tatsächlich unterstützte Installationswege.

Mögliche Unterabschnitte:

- npm
- pnpm
- yarn
- pip
- Cargo
- Go install
- Docker
- Docker Compose
- Homebrew
- vorkompilierte Releases
- Installation aus dem Quellcode

Beispiel:

```md
## Installation

### npm

```bash
npm install @example/package
```

### Docker

```bash
docker pull ghcr.io/OWNER/REPO:1.4.2
```

### From source

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
npm ci
npm run build
```
```

Dokumentiere `latest` nicht als einzige produktive Strategie, wenn feste Releases verfügbar sind.

Erfinde keine Paketnamen oder Registry-Pfade.

---

# 18. Verwendung

Zeige die wichtigsten realen Anwendungsfälle.

Englische Überschrift:

```md
## Usage
```

Deutsche Überschrift:

```md
## Verwendung
```

Geeignete Inhalte:

- typische Befehle
- minimales API-Beispiel
- häufigster Workflow
- erwartete Ausgabe
- wichtige Optionen
- Fehlerbehandlung
- Verweis auf ausführliche Dokumentation

Für CLI-Tools:

```md
### Create a project

```bash
projectctl create my-project
```

### Start a deployment

```bash
projectctl deploy my-project --environment production
```
```

Für Bibliotheken:

- Installation
- Import
- Initialisierung
- typische Methode
- Ergebnis
- Fehlerfall

Die README darf nicht die vollständige API- oder CLI-Referenz duplizieren.

---

# 19. Konfiguration

Dokumentiere die wichtigsten Konfigurationswerte.

Englisch:

```md
## Configuration
```

Deutsch:

```md
## Konfiguration
```

Für wenige Optionen eignet sich eine Tabelle:

```md
| Variable | Required | Default | Description |
|---|---:|---|---|
| `DATABASE_URL` | Yes | — | PostgreSQL connection string |
| `PORT` | No | `3000` | HTTP server port |
| `LOG_LEVEL` | No | `info` | Application log level |
```

Deutsch:

```md
| Variable | Erforderlich | Standard | Beschreibung |
|---|---:|---|---|
| `DATABASE_URL` | Ja | — | PostgreSQL-Verbindungsadresse |
| `PORT` | Nein | `3000` | Port des HTTP-Servers |
| `LOG_LEVEL` | Nein | `info` | Ausführlichkeit der Protokollierung |
```

Regeln:

- keine echten Passwörter oder Schlüssel verwenden
- geheime Werte niemals aus dem Repository übernehmen
- Standardwerte prüfen
- Pflichtfelder korrekt markieren
- bei vielen Optionen auf eine separate Dokumentationsdatei verlinken

Beispiel:

```md
See the [configuration reference](docs/configuration.md).
```

---

# 20. Dokumentation

Die README soll auf vorhandene weiterführende Dokumentation verweisen.

Englisch:

```md
## Documentation
```

Deutsch:

```md
## Dokumentation
```

Beispiel:

```md
- [Getting Started](docs/getting-started.md)
- [Configuration](docs/configuration.md)
- [Deployment](docs/deployment.md)
- [API Reference](docs/api.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Migration Guide](docs/migration.md)
```

In `README.de.md` dürfen die Linktexte übersetzt werden. Die Dateipfade bleiben unverändert.

Beispiel:

```md
- [Erste Schritte](docs/getting-started.md)
- [Konfiguration](docs/configuration.md)
- [Deployment](docs/deployment.md)
- [API-Referenz](docs/api.md)
- [Fehlerbehebung](docs/troubleshooting.md)
- [Migrationsanleitung](docs/migration.md)
```

Verlinke nur existierende Dateien und Seiten.

---

# 21. Architektur und Funktionsweise

Bei komplexeren Projekten soll ein kurzer Architekturüberblick aufgenommen werden.

Englisch:

```md
## Architecture
```

Deutsch:

```md
## Architektur
```

Mögliche Darstellung:

```text
Client
  │
  ▼
API
  │
  ├── Authentication
  ├── Application Service
  └── Background Workers
          │
          ▼
       Database
```

Der Abschnitt soll nur die wichtigsten Komponenten und Datenflüsse erklären.

Ausführliche Architekturentscheidungen gehören in:

```text
docs/architecture.md
docs/adr/
```

Keine Architektur aus Vermutungen ableiten, wenn sie nicht eindeutig aus dem Repository hervorgeht.

---

# 22. Projektstruktur

Ein Projektbaum ist sinnvoll bei:

- Monorepos
- Templates
- Frameworks
- größeren Anwendungen
- Projekten mit mehreren Paketen
- ungewöhnlicher Verzeichnisstruktur

Englisch:

```md
## Project Structure
```

Deutsch:

```md
## Projektstruktur
```

Beispiel:

```text
.
├── apps/
│   ├── api/
│   └── web/
├── packages/
│   ├── config/
│   └── shared/
├── docs/
├── tests/
├── README.md
├── README.de.md
└── LICENSE
```

Zeige nur relevante Verzeichnisse.

Nicht aufnehmen:

- `node_modules`
- Build-Artefakte
- Cache-Verzeichnisse
- jede einzelne Quelldatei
- automatisch generierte Dateien ohne Erklärungswert

---

# 23. Kompatibilität

Wenn relevant, dokumentiere unterstützte Versionen und Plattformen.

Englisch:

```md
## Compatibility
```

Deutsch:

```md
## Kompatibilität
```

Beispiel:

```md
| Component | Supported versions |
|---|---|
| Node.js | 22, 24 |
| PostgreSQL | 16, 17 |
| Linux | Supported |
| macOS | Supported |
| Windows | Experimental |
```

Keine Unterstützung behaupten, die nicht getestet, dokumentiert oder aus der Konfiguration ersichtlich ist.

---

# 24. Roadmap

Eine Roadmap ist optional.

Sie darf nur aufgenommen werden, wenn es eine belegbare Roadmap, Projektplanung oder vorhandene offene Ziele gibt.

Englisch:

```md
## Roadmap
```

Deutsch:

```md
## Roadmap
```

Beispiel:

```md
- [x] Core API
- [x] Docker deployment
- [ ] Plugin SDK
- [ ] Multi-region support
```

Keine erfundenen Termine nennen.

Formuliere vorsichtig:

```text
Planned
```

oder:

```text
Under consideration
```

nicht:

```text
Coming next month
```

wenn der Termin nicht verbindlich dokumentiert ist.

---

# 25. Mitwirken

Wenn `CONTRIBUTING.md` vorhanden ist, verlinke darauf.

Englisch:

```md
## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
```

Deutsch:

```md
## Mitwirken

Beiträge sind willkommen. Lies vor dem Erstellen eines Pull Requests bitte [CONTRIBUTING.md](CONTRIBUTING.md).
```

Wenn keine Contribution Guidelines vorhanden sind, erfinde keinen detaillierten Prozess.

Eine kurze, allgemeine Formulierung ist zulässig, sofern sie zum Projekt passt.

Bei größeren Änderungen kann empfohlen werden, zuerst ein Issue oder eine Discussion zu eröffnen.

---

# 26. Sicherheit

Wenn `SECURITY.md` vorhanden ist, muss darauf verwiesen werden.

Englisch:

```md
## Security

Do not report security vulnerabilities through public issues. See [SECURITY.md](SECURITY.md) for private reporting instructions.
```

Deutsch:

```md
## Sicherheit

Melde Sicherheitslücken nicht über öffentliche Issues. Informationen zum privaten Meldeweg findest du in [SECURITY.md](SECURITY.md).
```

Regeln:

- keine Aufforderung zur öffentlichen Meldung von Sicherheitslücken
- keine E-Mail-Adresse erfinden
- keine angebliche vollständige Sicherheit behaupten
- unterstützte Versionen nur nennen, wenn dokumentiert
- keine vertraulichen Sicherheitsdetails ausgeben

---

# 27. Support

Trenne verschiedene Anliegen klar.

Englisch:

```md
## Support
```

Deutsch:

```md
## Support
```

Mögliche Zuordnung:

| Anliegen | Geeigneter Kanal |
|---|---|
| reproduzierbarer Fehler | GitHub Issues |
| Frage zur Verwendung | GitHub Discussions |
| Funktionsvorschlag | Issues oder Discussions |
| Sicherheitsproblem | privater Security-Kanal |
| kommerzielle Anfrage | offizieller Geschäftskontakt |

Verwende nur tatsächlich aktivierte oder vorhandene Kanäle.

Keine Kontaktadresse erfinden.

---

# 28. Lizenz

Die Lizenz muss korrekt aus der vorhandenen Lizenzdatei übernommen werden.

Englisch:

```md
## License

Distributed under the [MIT License](LICENSE).
```

Deutsch:

```md
## Lizenz

Veröffentlicht unter der [MIT-Lizenz](LICENSE).
```

Die genaue Formulierung muss zur tatsächlichen Lizenz passen.

Bei Dual Licensing oder kommerziellen Zusatzbedingungen müssen die vorhandenen Lizenzdateien korrekt wiedergegeben werden.

Ein öffentliches Repository darf nicht automatisch als Open Source bezeichnet werden, wenn keine passende Lizenz vorhanden ist.

Wenn keine Lizenzdatei existiert, darf keine Lizenz erfunden werden.

---

# 29. Danksagungen und Zitation

## Danksagungen

Nur aufnehmen, wenn relevante Projekte, Personen, Förderer oder Mitwirkende genannt werden sollen.

Englisch:

```md
## Acknowledgements
```

Deutsch:

```md
## Danksagungen
```

## Zitation

Bei wissenschaftlicher Software oder vorhandener `CITATION.cff`:

Englisch:

```md
## Citation

If you use this project in academic work, please cite it using [CITATION.cff](CITATION.cff).
```

Deutsch:

```md
## Zitation

Wenn du dieses Projekt in einer wissenschaftlichen Arbeit verwendest, nutze bitte die Angaben aus [CITATION.cff](CITATION.cff).
```

---

# 30. Projekttyp berücksichtigen

Passe Prioritäten und Abschnitte an den tatsächlichen Projekttyp an.

## 30.1 Bibliothek oder SDK

Priorität:

1. Nutzenversprechen
2. Installation
3. minimales Codebeispiel
4. Hauptfunktionen
5. API-Grundkonzepte
6. Kompatibilität
7. Dokumentationslink
8. Lizenz

## 30.2 CLI-Tool

Priorität:

1. konkreter Anwendungsfall
2. Installation
3. typische Befehle
4. Beispielausgabe
5. Optionen
6. Konfiguration
7. Plattformunterstützung
8. Exit Codes
9. Shell Completion, falls vorhanden

## 30.3 Web- oder Desktop-Anwendung

Priorität:

1. Screenshot
2. Hauptfunktionen
3. Demo, falls vorhanden
4. Schnellstart
5. Installation
6. Konfiguration
7. Deployment
8. Datenspeicherung
9. Updates und Backups

## 30.4 Self-hosted Anwendung

Zusätzlich prüfen:

- Docker Compose
- persistente Volumes
- Reverse Proxy
- TLS
- Umgebungsvariablen
- Datenbank
- Backups
- Upgrade-Anleitung
- Authentifizierung
- Telemetrie
- externe Dienste
- Hardwareanforderungen
- Sicherheitsmodell

## 30.5 Template oder Boilerplate

Zusätzlich erklären:

- verwendeter Tech Stack
- enthaltene Funktionen
- Projektstruktur
- Einrichtung
- umzubenennende Stellen
- zu ersetzende Platzhalter
- Deployment
- bewusst nicht enthaltene Funktionen

## 30.6 API

Zusätzlich dokumentieren:

- Basis-URL
- Authentifizierung
- erster Request
- Response-Beispiel
- Fehlerformat
- Rate Limits
- Versionierung
- OpenAPI-Spezifikation
- verfügbare SDKs

Nur aufnehmen, wenn diese Informationen belegt sind.

---

# 31. Inhalte, die nicht vollständig in die README gehören

Lagere umfangreiche Inhalte aus.

| Inhalt | Empfohlene Datei |
|---|---|
| vollständige Entwickleranleitung | `CONTRIBUTING.md` |
| Verhaltensregeln | `CODE_OF_CONDUCT.md` |
| Sicherheitsprozess | `SECURITY.md` |
| Supportregeln | `SUPPORT.md` |
| vollständige Versionshistorie | `CHANGELOG.md` |
| tiefgehende Architektur | `docs/architecture.md` |
| vollständige Konfiguration | `docs/configuration.md` |
| vollständige API-Referenz | `docs/api.md` |
| Lizenztext | `LICENSE` |
| wissenschaftliche Metadaten | `CITATION.cff` |

Die README darf diese Inhalte kurz zusammenfassen und verlinken.

---

# 32. Schreibstil

## 32.1 Allgemein

Schreibe:

- klar
- direkt
- präzise
- professionell
- technisch korrekt
- handlungsorientiert
- freundlich
- ohne unnötigen Jargon
- ohne überlange Absätze
- ohne Wiederholungen

## 32.2 Satzbau

Bevorzuge:

- aktive Sprache
- kurze bis mittellange Sätze
- konkrete Verben
- eindeutige Subjekte
- konkrete Handlungsanweisungen

Englisch:

```text
Run the development server.
```

Nicht:

```text
The development server can then be run.
```

Deutsch:

```text
Starte den Entwicklungsserver.
```

Nicht:

```text
Der Entwicklungsserver kann anschließend gestartet werden.
```

## 32.3 Anrede

Verwende in der englischen Version eine neutrale direkte Ansprache.

Verwende in der deutschen Version einheitlich „du“, sofern der bestehende Projektstil nichts anderes verlangt.

Nicht zwischen „du“, „Sie“ und unpersönlichen Formulierungen wechseln.

## 32.4 Fachbegriffe

Verwende etablierte Fachbegriffe.

Erkläre projektspezifische oder ungewöhnliche Begriffe bei der ersten Verwendung.

Keine unnötigen deutschen Übersetzungen etablierter technischer Begriffe erzwingen.

---

# 33. Markdown-Regeln

## 33.1 Überschriften

- genau eine `#`-Überschrift
- Hauptabschnitte mit `##`
- Unterabschnitte mit `###`
- keine Ebenen überspringen
- keine leeren Überschriften
- Überschriften in beiden Sprachversionen logisch parallel halten

## 33.2 Codeblöcke

Jeder Codeblock erhält nach Möglichkeit eine passende Sprachkennung.

Beispiele:

```md
```bash
```

```md
```ts
```

```md
```json
```

```md
```yaml
```

```md
```text
```
```

Codeblöcke müssen korrekt geschlossen sein.

## 33.3 Tabellen

Tabellen nur verwenden, wenn sie Informationen übersichtlicher machen.

Geeignet für:

- Konfigurationswerte
- Kompatibilität
- Feature-Matrizen
- unterstützte Versionen

Vermeide zu breite Tabellen mit langen Textblöcken.

## 33.4 Links

- relative Links für Dateien im Repository verwenden
- nur existierende Ziele verlinken
- Linktexte müssen verständlich sein
- nicht mehrfach unnötig dieselbe URL ausschreiben
- Sprachumschalter immer relativ verlinken

## 33.5 HTML

GitHub-kompatibles HTML nur sparsam verwenden.

Zulässige Anwendungsfälle:

- zentrierter Kopfbereich
- Logo-Größe
- kompakte Linkzeile

Vermeide komplexes HTML-Layout.

## 33.6 Bilder

- relative Pfade bevorzugen
- aussagekräftige Alt-Texte
- keine zu großen Dateien
- keine dekorativen Bilder ohne Informationswert
- vorhandene Social-Preview-Grafik nicht automatisch als README-Banner verwenden

---

# 34. Synchronität beider Sprachversionen

`README.md` und `README.de.md` müssen dieselbe Informationsarchitektur besitzen.

Die Reihenfolge der Hauptabschnitte soll übereinstimmen.

Beispiel:

| `README.md` | `README.de.md` |
|---|---|
| About | Über das Projekt |
| Highlights | Highlights |
| Quick Start | Schnellstart |
| Requirements | Voraussetzungen |
| Installation | Installation |
| Usage | Verwendung |
| Configuration | Konfiguration |
| Documentation | Dokumentation |
| Architecture | Architektur |
| Project Structure | Projektstruktur |
| Compatibility | Kompatibilität |
| Contributing | Mitwirken |
| Security | Sicherheit |
| Support | Support |
| License | Lizenz |
| Acknowledgements | Danksagungen |

Beide Dateien müssen dieselben enthalten:

- Versionsangaben
- Installationsbefehle
- Codebeispiele
- Links
- Warnungen
- Einschränkungen
- Feature-Aussagen
- Lizenzinformationen
- Supportwege

Die deutsche Version darf keine veralteten oder zusätzlichen technischen Aussagen enthalten.

---

# 35. Umgang mit vorhandenen README-Dateien

Wenn bereits README-Dateien existieren:

1. analysiere alle vorhandenen Inhalte;
2. bewahre korrekte und weiterhin relevante Informationen;
3. entferne veraltete oder doppelte Inhalte;
4. korrigiere falsche Befehle und Links;
5. verbessere die Informationshierarchie;
6. vereinheitliche Begriffe;
7. überführe lange Detailabschnitte gegebenenfalls in Verweise auf `docs/`;
8. erhalte wichtige Warnungen und Einschränkungen;
9. ändere keine technischen Fakten ohne Beleg;
10. gleiche die englische und deutsche Version vollständig ab.

Kopiere vorhandene Texte nicht blind.

---

# 36. Qualitätsprüfung

Prüfe vor der Ausgabe beide Dateien vollständig.

## 36.1 Inhalt

- [ ] Der erste Satz erklärt Produkt, Zielgruppe und Nutzen.
- [ ] Der Projekttyp wurde korrekt erkannt.
- [ ] Der Quick Start ist vollständig und plausibel.
- [ ] Voraussetzungen sind korrekt.
- [ ] Installationsbefehle stammen aus dem Repository.
- [ ] Codebeispiele entsprechen der aktuellen API.
- [ ] Projektstatus und Einschränkungen sind ehrlich.
- [ ] Supportwege sind korrekt.
- [ ] Security-Hinweise sind korrekt.
- [ ] Lizenzangaben entsprechen der Lizenzdatei.
- [ ] Keine Fakten wurden erfunden.
- [ ] Englisch und Deutsch sind inhaltlich synchron.

## 36.2 Darstellung

- [ ] Genau eine `#`-Überschrift.
- [ ] Logische Überschriftenhierarchie.
- [ ] Keine leeren Abschnitte.
- [ ] Keine unnötigen Badges.
- [ ] Alle Codeblöcke sind geschlossen.
- [ ] Sprachkennungen der Codeblöcke sind korrekt.
- [ ] Tabellen sind sinnvoll und lesbar.
- [ ] Bilder besitzen Alt-Texte.
- [ ] Interne Links sind relativ.
- [ ] Keine unnötige HTML-Komplexität.
- [ ] Sprachumschalter funktioniert in beiden Dateien.

## 36.3 Vertrauenswürdigkeit

- [ ] Keine unbelegten Superlative.
- [ ] Keine erfundenen Benchmarks.
- [ ] Keine erfundenen Nutzer oder Referenzen.
- [ ] Keine angebliche „100 %“-Sicherheit.
- [ ] Keine falsche Bezeichnung als „production-ready“.
- [ ] Keine falsche Plattformunterstützung.
- [ ] Keine erfundene Roadmap.
- [ ] Keine erfundene Lizenz.
- [ ] Keine erfundenen URLs oder Kontakte.
- [ ] Bekannte Grenzen werden nicht versteckt.

## 36.4 Zweisprachigkeit

- [ ] Abschnittsreihenfolge stimmt überein.
- [ ] Codeblöcke sind identisch.
- [ ] Links sind identisch.
- [ ] Versionsnummern sind identisch.
- [ ] Funktionsnamen sind identisch.
- [ ] Warnungen sind inhaltlich identisch.
- [ ] Technische Begriffe wurden sinnvoll behandelt.
- [ ] Keine dritte Sprache wurde hinzugefügt.

---

# 37. Erwartetes Ergebnis

Erstelle oder aktualisiere genau diese zwei Dateien:

```text
README.md
README.de.md
```

`README.md` muss die englische Hauptversion enthalten.

`README.de.md` muss die vollständige deutsche Übersetzung enthalten.

Keine weiteren README-Sprachdateien erzeugen.

Keine Datei wie diese erzeugen:

```text
README.fr.md
README.es.md
README.it.md
README.ja.md
README.zh.md
```

Keine Sprachordner anlegen.

---

# 38. Ausgabeformat der KI

Wenn du direkten Dateizugriff besitzt:

1. schreibe die fertigen Inhalte direkt in `README.md` und `README.de.md`;
2. ändere keine anderen Dateien, sofern dies nicht ausdrücklich verlangt wurde;
3. liste anschließend kurz auf, welche README-Dateien geändert wurden;
4. nenne offene oder nicht verifizierbare Punkte;
5. erfinde keine fehlenden Angaben.

Wenn du keinen direkten Dateizugriff besitzt:

1. gib zuerst den vollständigen Inhalt von `README.md` aus;
2. gib danach den vollständigen Inhalt von `README.de.md` aus;
3. verwende jeweils einen eigenen Markdown-Codeblock;
4. schreibe außerhalb der Dateien nur eine sehr kurze Zusammenfassung;
5. füge keine zusätzlichen Sprachversionen hinzu.

---

# 39. Verbindliche Schlussanweisung

Analysiere das Repository gründlich und erstelle anschließend eine moderne, professionelle und projektspezifische englische `README.md` sowie eine vollständig synchrone deutsche `README.de.md`.

Priorisiere technische Richtigkeit, Verständlichkeit, schnelle Nutzbarkeit und Vertrauenswürdigkeit.

Verwende überzeugende Sprache nur dort, wo Aussagen konkret belegt werden können.

Erfinde keine Funktionen, Links, Benchmarks, Anforderungen, Supportwege, Sicherheitsmerkmale oder Lizenzangaben.

Halte beide Sprachversionen dauerhaft strukturell und inhaltlich synchron.
