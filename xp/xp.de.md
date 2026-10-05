---
author: Christian Apolloni
date: 2026-09-26
lang: de-CH
---

# Extreme Programming (XP)

**Embrace Change**

---

## Über mich & XP

**6 Jahre** (2006–2013) tägliche Arbeit mit XP bei
[Lifeware](https://www.lifeware.ch)

- Damals ~20 Mitarbeitende, darunter Kent Beck, der Erfinder von XP
- Outsourcing für Lebensversicherungen: SaaS, bei Lifeware gehostet, Web-GUI
- 11 Versicherungsgesellschaften
- ~800K aktive Policen
- ~35K Klassen
- ~200K Unit-Tests

---

## Die Referenz

- Kent Beck mit Cynthia Andres, _Extreme Programming Explained: Embrace
  Change_, 2. Auflage (2004)

---

## Historischer Kontext: Software in den 1990ern

- Vorherrschendes Modell: **Wasserfall** und schwergewichtige Prozesse
  - Umfangreiches Design im Voraus, lange Phasen, dicke Dokumente
  - Releases alle 6–24 Monate
- Annahme: _Änderungen sind teuer_, also verhindert man sie
- Realität: Die Anforderungen änderten sich trotzdem ➔ verspätete und
  gescheiterte Projekte
- 1996: Kent Beck, Ron Jeffries & andere im **Chrysler-C3**-Projekt ➔ XP
  entsteht
- 2001: **Agiles Manifest**, Kent Beck ist einer der 17 Unterzeichner

---

## Die Wirkung von XP

Praktiken, die XP erfunden oder zum Mainstream gemacht hat:

- **Test-Driven Development**
- **Continuous Integration** (➔ CI/CD-Pipelines)
- **Pair Programming** (➔ Mob/Ensemble Programming)
- **Refactoring** als tägliche Tätigkeit
- **User Stories**, kurze Iterationen, kleine Releases
- **Gemeinsamer Code-Besitz**, Coding-Standards

Wie konnte eine einzige Methodik uns so vieles bescheren, was wir heute als
grundlegend betrachten?

---

## Die Kernidee

Kent Becks Bild: ein Mischpult mit einem Regler für jede Praktik, die sich
bewährt hat. Was passiert, wenn wir alle Regler auf 10 drehen?

- Ausgangspunkt ist etwas, das weithin als **gut gilt**
- Frage: _Was passiert, wenn wir es kompromisslos, bis ins **Extreme**
  betreiben?_
- Manchmal funktioniert das Ergebnis **überraschend** gut, bis hin zur
  **Transformation**

---

## Beispiel 1: Testen

- Testen ist gut
- **Früher** testen ist besser
- **Vor** der Implementierung testen? Überraschenderweise noch besser

➔ **Test-First Programming / TDD**

_Tests werden zum Design-Werkzeug, nicht nur zur Absicherung._

---

## Beispiel 2: Code-Review

- Code-Review ist gut
- **Häufigere** Code-Reviews sind besser
- **Fortlaufend** reviewen, während der Code geschrieben wird?
  Überraschenderweise noch besser

➔ **Pair Programming**

_Keine Review-Warteschlange, kein „LGTM“ für einen 2000-Zeilen-PR._

---

## Beispiel 3: Integration

- Änderungen zu integrieren ist notwendig – und schmerzhaft
- **Häufiger** integrieren macht jede Integration kleiner und einfacher
- **Kontinuierlich** integrieren? Überraschenderweise wird es fast zur
  Nebensache

➔ **Continuous Integration** ➔ **CI/CD**

_Wenn es wehtut, mach es öfter._

---

## Beispiel 4: Design & Releases

- Gutes Design ist wertvoll ➔ das Design **jeden Tag** verbessern ➔
  **Refactoring / Incremental Design**
- Kundenfeedback ist wertvoll ➔ es **ständig** einholen ➔ **Daily Deployment,
  Real Customer Involvement**

_Jedes Mal dasselbe Muster._

---

## Die Struktur von XP

```text
Werte        ➔  warum wir es tun      (wenige, universell)
  ⬇
Prinzipien   ➔  Brücke / Leitlinien   (domänenspezifisches Denken)
  ⬇
Praktiken    ➔  was wir täglich tun   (konkret, situationsabhängig)
```

- Praktiken ohne Werte sind leere Rituale
- Werte ohne Praktiken sind Wunschdenken
- Prinzipien zeigen, wie man Praktiken an den eigenen Kontext **anpasst**

---

## Werte

- **Kommunikation**: Alle gehören zum Team; persönliche Zusammenarbeit, von den
  Anforderungen bis zum Code
- **Einfachheit**: Tun, was nötig ist und verlangt wird, aber nicht mehr;
  kleine, einfache Schritte machen
- **Feedback**: In jeder Iteration funktionierende Software liefern, früh und
  oft demonstrieren, zuhören und anpassen (auch den Prozess)
- **Mut**: Die Wahrheit über Fortschritt und Schätzungen sagen, sich an
  Änderungen anpassen; niemand arbeitet allein, und Prinzipien leiten durch
  Unsicherheit
- **Respekt**: Alle tragen Wert bei; Entwickler und Kunden respektieren die
  Expertise des anderen; Teams sind für ihre Arbeit verantwortlich

_Nach Don Wells,
[extremeprogramming.org](http://www.extremeprogramming.org/values.html)_

---

## Prinzipien (Auswahl)

- **Humanity**: Software wird von Menschen für Menschen gebaut; ihre Bedürfnisse
  erfüllen
- **Economics**: Jemand bezahlt dafür; ROI schaffen, Geschäftswert liefern
- **Mutual Benefit**: Jede Tätigkeit sollte allen Beteiligten nützen / Win-win
- **Self-Similarity**: Die Struktur einer Lösung auf anderen Ebenen
  wiederverwenden. Passt nicht immer, aber bewährte Strukturen sind ein guter
  Ausgangspunkt
- **Improvement**: „Perfekt“ ist ein Verb, kein Adjektiv
- **Flow**: Kontinuierlich liefern, nicht in grossen Brocken
- **Redundancy**: Kritische Probleme oder Risiken verdienen mehrere
  Schutzmassnahmen
- **Failure**: Wenn unklar ist, welcher Weg der beste ist, einen ausprobieren,
  oder beide. Ist Ausprobieren unverhältnismässig teuer oder gefährlich: im
  Kleinen versuchen / Risiko mindern
- **Baby Steps**: Kleine Schritte sind billig zu machen und rückgängig zu
  machen. Grosse Lücken mit Trittsteinen überbrücken.
- **Accepted Responsibility**: Verantwortung kann nicht zugewiesen, nur
  übernommen werden

---

## Praktiken (primär)

| Team & Umfeld         | Planung         | Programmierung         |
| --------------------- | --------------- | ---------------------- |
| Sit Together          | Stories         | Pair Programming       |
| Whole Team            | Weekly Cycle    | Test-First Programming |
| Informative Workspace | Quarterly Cycle | Incremental Design     |
| Energized Work        | Slack           | Ten-Minute Build       |
|                       |                 | Continuous Integration |

- Ergänzende Praktiken (Corollary Practices): Shared Code, Single Code Base,
  Daily Deployment, Root-Cause Analysis...
- Mit denen beginnen, die den grössten Schmerz adressieren, aber den vollen
  Nutzen erst erwarten, wenn auch die unterstützenden Praktiken etabliert sind

---

## Ein XP-Team in der Praxis

| Rhythmus      | Was passiert                                             | Feedback von |
| ------------- | -------------------------------------------------------- | ------------ |
| Minuten       | Im Pair: fehlschlagender Test ➔ grün machen ➔ refactoren | Tests        |
| Stunden       | Integrieren; der Ten-Minute Build führt alle Tests aus   | CI           |
| Täglich       | Stand-up, Pairs wechseln, Kunden zu Unklarem befragen    | Team, Kunde  |
| Wöchentlich   | Kunde wählt Stories; Demo; Retrospektive                 | Kunde, Team  |
| Quartalsweise | Themen, Planung im Grossen, den Prozess reflektieren     | Business     |

Feedbackschleifen auf jeder Zeitskala: Je kürzer die Schleife, desto billiger
die Korrektur

---

## Synergie: Das Ganze kann mehr sein als die Summe seiner Teile

```text
     Automatisierte Tests
        ⤢           ⤡
Refactoring   ↔   Continuous Integration
```

- **Tests ↔ Refactoring**: Tests machen Refactoring sicher; Refactoring hält den
  Code einfach und gut testbar
- **Tests ↔ CI**: Tests geben der Integration eine Bedeutung über „es
  kompiliert“ hinaus; CI führt sie ständig aus, Fehler fallen innert Minuten auf
- **Refactoring ↔ CI**: Häufige kleine Merges machen weitreichende Refactorings
  machbar; gut strukturierter Code hält Änderungen lokal und Konflikte selten

Eine einzelne Praktik isoliert herauszupicken, bringt oft weniger als erhofft:
Die Synergieeffekte sind erheblich

---

## Mutual Benefit: Kunde und Lieferant auf derselben Seite

Festpreisverträge mit fixem Umfang können Kunde und Lieferant gegeneinander
aufbringen:

- Der Lieferant schützt sich mit erschöpfenden Spezifikationen: lange, teure
  Vorstudien, bevor eine Zeile Code geschrieben wird
- Änderungen nach der Abnahme werden als Change Requests verrechnet: _„Es
  funktioniert wie spezifiziert“_
- Der Kunde bezahlt jede Erkenntnis unterwegs, der Lieferant profitiert davon

XP sucht stattdessen **Win-win**:

- **Negotiated Scope Contract**: Zeit, Kosten und Qualität festlegen; den Umfang
  verhandeln, während man dazulernt
- **Pay-Per-Use**: Der Lieferant verdient, wenn die Software Wert liefert
- Wöchentliche Zyklen: Der Kunde kann Prioritäten ohne Strafe ändern

„Funktioniert wie spezifiziert“ heisst nicht „funktioniert für den Kunden“

---

## Die menschliche Seite: Nachhaltigkeit

Software ist ein Marathon, kein Sprint: XP strebt ein Tempo an, das man über
Jahre halten kann

- **Energized Work**: Müde Entwickler machen schlechte Software; Überstunden
  sind ein Warnsignal, keine Gewohnheit
- **Sicherheitsnetze** halten Fehler klein und Stress gering: Baby Steps, Tests,
  CI
  - Etwas kaputt gemacht? Die Tests sagen es innert Minuten
  - Steckengeblieben? Der Pair-Programming-Partner sitzt gleich daneben
  - Falsche Richtung? Der nächste Wochenzyklus korrigiert sie
- **Mut** wächst aus Sicherheit: Entwickler trauen sich zu ändern, aufzuräumen
  und zu experimentieren – Mut ist nicht Leichtsinn
- **Code bleibt änderbar**: Ständiges Aufräumen hält die Änderungskosten tief,
  statt Schulden anzuhäufen

Burnout und technische Schulden sind derselbe Fehler: Man borgt bei der Zukunft

---

## Baby Steps: Grosse Änderungen aufteilen

Eine grosse Änderung ist beängstigend: langlebiger Branch, schmerzhafter Merge,
riesiges Review, Big-Bang-Release, schwer rückgängig zu machen

- In **kleine Schritte** aufteilen, nach denen das System jeweils funktioniert:
  Tests grün, integriert, deploybar
- Jeder Schritt ist leicht zu reviewen und billig rückgängig zu machen: Risiko
  und Komplexität bleiben **beherrschbar**
- Nicht trivial: Die Schritte zu finden ist eine **Fähigkeit**, und der Weg ist
  oft länger
  - _„Make the change easy (warning: this may be hard), then make the easy
    change“_ (Kent Beck)
  - **Parallel Change**: erweitern ➔ migrieren ➔ zurückbauen
  - **Branch by Abstraction**, **Feature Flags**: Unfertiges integrieren, ohne
    es freizuschalten
  - **Strangler Fig**: Eine neue Komponente übernimmt die Fähigkeiten einer
    alten eine nach der anderen, bis die alte entfernt werden kann

Ist die Lücke zu gross, baut man Trittsteine

---

## Kritik & Grenzen

- **Alles oder nichts**: Die Praktiken hängen voneinander ab, aber die volle
  Einführung braucht Engagement auf allen Ebenen der Organisation
- **Organisatorische Passung**: Kundeneinbindung, Zusammensitzen und
  verhandelter Umfang kollidieren mit verteilten Teams, strikten Hierarchien und
  Outsourcing der Entwicklung, ohne auch die Verantwortung auszulagern
- **Regulierte Umfelder**: Audits und Compliance können Prozesse, Dokumentation
  oder Design im Voraus verlangen, die XP bewusst zu minimieren versucht
- **Pair Programming**: gilt als teuer, kann anstrengend sein, passt nicht in
  jede Situation
- **Evolutionäres Design**: Ohne ständige Refactoring-Disziplin kann die
  Architektur verwildern
- **Gefahr des Dogmatismus**: „Extrem“ kann zur Orthodoxie erstarren, aber XP
  ist im Kern pragmatisch: Die Praktiken dienen den Werten und passen sich dem
  Kontext an
- Sogar das **C3-Projekt** wurde 2000 eingestellt: 1997 ging es live und zahlte
  die Löhne von ~10'000 Angestellten, deckte aber nie alle Lohnabrechnungen ab

XP ist keine Wunderwaffe: Wisse, was du bei einem Kompromiss aufgibst, und warum

---

## XP und Scrum: Geschwister

|             | XP                                  | Scrum                                   |
| ----------- | ----------------------------------- | --------------------------------------- |
| Ursprung    | 1996, Chrysler C3                   | 1993, Easel Corp.; 1995 an der OOPSLA   |
| Fokus       | Wie man **Software baut**           | Wie man **Arbeit organisiert**          |
| Zyklus      | Wöchentlich                         | Sprint, ein Monat oder weniger          |
| Rollen      | Ganzes Team, echte Kundeneinbindung | Product Owner, Scrum Master, Developers |
| Engineering | TDD, Pairing, CI, Refactoring...    | Offen gelassen: „bewusst unvollständig“ |

- Ihre Gründer haben 2001 alle das Agile Manifest unterzeichnet: Beck, Schwaber,
  Sutherland

---

## XP und Scrum: Gegenseitiger Einfluss

Scrum ➔ XP

- **Daily Stand-up**: Copliens Pattern (1993) ➔ Daily Scrum ➔ XP-Kernpraktik
  (1998); XP-Teams übernahmen später Scrums drei Fragen
- 1995: Kent Beck bat Jeff Sutherland um die Scrum-Papers, als er XP
  ausarbeitete; laut Sutherland sollte XP die Engineering-Praktiken übernehmen,
  Scrum das Teammanagement

XP ➔ Scrum

- Das frühe Scrum wurde als Hülle um XP präsentiert: _XP@Scrum_ (Schwaber),
  _XBreed_ (Beedle), das erste Scrum-Buch (2001)
- **User Stories**, **Velocity**, **Planning Poker**: XP-Ideen, heute
  alltägliches Scrum-Vokabular
- Der Kurs **Certified Scrum Developer** lehrt die Engineering-Praktiken von XP:
  TDD, Pairing, Refactoring, CI

---

## Scrum braucht Engineering-Praktiken

- Scrum passt in **traditionelle Grossorganisationen**: Seine Rollen lassen sich
  auf bestehende abbilden, Sprints speisen Planung und Reporting, SAFe/LeSS
  skalieren es, Zertifizierungen machen es lehrbar
- Sprints allein halten den Code nicht gesund: _„after a while progress is slow
  because the code base is a mess“_ (Martin Fowler, 2009)
- Scrum + XP ergänzen sich: Scrum organisiert das **Was** und **Wann**, XP hält
  den Code **änderbar**

Sprints machen nicht agil, wenn sich der Code nicht ändern lässt

---

## XP im Zeitalter der KI

Software wird immer noch von Menschen gebaut... aber zunehmend **mit** KI

- **Test-First**: Tests werden zur Spezifikation und zur Leitplanke für
  generierten Code
- **Ten-Minute Build / CI**: mehr Code, schneller ➔ schnelles automatisiertes
  Feedback zählt noch mehr
- **Einfachheit / YAGNI** (You Aren't Gonna Need It): Code ist jetzt billig zu
  erzeugen, aber immer noch teuer im Unterhalt
- **Baby Steps**: KI verleitet zu riesigen Diffs; kleine, überprüfte Schritte
  behalten die Kontrolle
- **Pair Programming**: KI kann ein unermüdlicher Pair-Partner sein, verteilt
  aber weder Wissen noch Verantwortung im Team
- **Accepted Responsibility**: Die KI schreibt Code, aber die Menschen bleiben
  verantwortlich

---

## Wichtigste Erkenntnisse

- Die „Extreme“ von XP wurden zu den heutigen **Industriestandards**
- Kompromissloses Engagement kann Ergebnisse ermöglichen, die mit Kompromissen
  vielleicht nie erreicht würden
- **Kompromisse** können den Nutzen verbergen:
  - „Wir machen TDD, ausser wenn wir in Eile sind“
  - „Wir integrieren kontinuierlich... alle zwei Monate“
- Die Praktiken verstärken sich gegenseitig: **Halbe Sachen brechen die
  Synergie**

---

![bg right:40%](img/wizards.png)

## Von Zauberern zu guten Gewohnheiten

- _„I'm not a great programmer; I'm just a good programmer with great habits“_,
  Kent Beck
- Eine gute Methodik, gewissenhaft angewandt, macht die „Magie“ wiederholbar:
  Viele Entwickler können zu Zauberern werden

---

## Ihr seid dran: Das „Extrem“-Spiel

Wählt etwas, das euer Team für gut hält, dann:

1. **Warum** ist es gut? Welchen **Werten** oder **Prinzipien** dient es?
2. _Was, wenn wir es ins **Extreme** treiben?_
   - Was würde **kaputtgehen**? Was würde **wehtun**?
   - Was müsste **anders funktionieren**, damit es nicht kaputtgeht? Damit es
     nicht mehr wehtut?
   - Was könnten wir dadurch **gewinnen**?
3. Dient die extreme Version noch **denselben Werten**? Wenn nicht, seid ihr zu
   weit gegangen

Oft zeigt gerade das, was kaputtgeht oder wehtut, was als Nächstes verbessert
werden muss!

---

**Vielen Dank!**

> Fragen? Anmerkungen? Diskussion erwünscht!
