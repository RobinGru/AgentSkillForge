# Agent Skills

Dieses Repository sammelt spezialisierte **Agent Skills** für KI-Coding-Assistenten wie **Codex**, **Claude Code** oder vergleichbare agentische Entwicklungswerkzeuge.

Die Skills sind als wiederverwendbare Arbeitsanweisungen gedacht. Sie helfen einem KI-Agenten, bei bestimmten Aufgaben strukturierter, konsistenter und mit klaren Qualitätskriterien vorzugehen.

## Was enthält dieses Repository?

Jeder Skill liegt in einem eigenen Ordner und enthält eine `SKILL.md` mit:

- Metadaten wie `name` und `description`
- Einsatzgebiet und Abgrenzung
- Schritt-für-Schritt-Vorgehen
- Qualitäts- und Validierungskriterien
- konkreten Regeln für die Zusammenarbeit mit Nutzerinnen und Nutzern

Aktuell enthaltene Skills:

| Ordner | Skill | Zweck |
| --- | --- | --- |
| `brainstorming/` | `brainstorming` | Unterstützt die strukturierte Klärung, Ausarbeitung und Validierung von Ideen, bevor Code geschrieben wird. Geeignet für neue Features, Architekturentscheidungen, größere Refactorings oder unklare Anforderungen. |
| `frontend-product-designer/` | `frontend-product-designer` | Hilft beim Entwerfen und Umsetzen hochwertiger, zugänglicher und produktionsreifer Frontend-Oberflächen. Der Fokus liegt auf UI-Qualität, Accessibility, Responsiveness, Zuständen und visueller Produktpassung. |
| `vue-refactor-assistant/` | `vue-refactor-assistant` | Unterstützt das schrittweise Refactoring großer Vue-3- oder Nuxt-Komponenten, ohne bestehendes Verhalten zu ändern. Der Fokus liegt auf behutsamer Modularisierung mit Composables, Komponenten, Typen und Utilities. |

## Wofür sind Agent Skills gedacht?

Agent Skills ergänzen allgemeine KI-Assistenten um domänenspezifisches Verhalten. Statt bei jeder Aufgabe dieselben Regeln erneut zu formulieren, kann ein Skill wiederverwendet werden, sobald eine Aufgabe in seinen Bereich fällt.

Typische Vorteile:

- konsistentere Arbeitsweise bei wiederkehrenden Aufgaben
- klarere Entscheidungskriterien für Agenten
- weniger vorschnelle Implementierungen
- bessere Dokumentation von Annahmen, Risiken und Akzeptanzkriterien
- höhere Qualität bei Refactoring-, Design- und Produktentscheidungen

## Nutzung mit Codex oder Claude Code

Je nach Tool können Skills unterschiedlich eingebunden werden. Typische Möglichkeiten sind:

1. Den passenden Skill-Ordner in die Skill-/Agent-Konfiguration des Tools kopieren.
2. Die jeweilige `SKILL.md` als projektspezifische Anweisung referenzieren.
3. Den Inhalt der `SKILL.md` bei Bedarf in einen System-, Developer- oder Projektprompt übernehmen.
4. Skills als interne Vorlagen für wiederkehrende Agent-Aufgaben verwenden.

Wenn ein Tool ein eigenes Skill-Format erwartet, sollte der Inhalt der `SKILL.md` entsprechend angepasst oder gemappt werden.

## Hinweise zur Erweiterung

Neue Skills sollten jeweils in einem eigenen Ordner liegen und mindestens eine `SKILL.md` enthalten.

Empfohlene Struktur:

```txt
neuer-skill-name/
└── SKILL.md
```

Eine gute `SKILL.md` sollte beschreiben:

- wann der Skill verwendet werden soll
- wann er nicht verwendet werden soll
- welches Ziel der Skill verfolgt
- welche Schritte der Agent ausführen soll
- welche Regeln, Grenzen und Qualitätskriterien gelten
- welche Ergebnisse oder Artefakte erwartet werden

## Sprache

Die vorhandenen Skill-Dateien sind überwiegend auf Englisch formuliert, damit sie direkt in englischsprachigen Agent-Umgebungen genutzt werden können. Diese README ist bewusst auf Deutsch gehalten, um den Zweck des Repositories schnell verständlich zu machen.
