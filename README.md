# Jobanzeige-Analyse-mit-KI

Ein Python-Tool, das mit Hilfe von OpenAI's GPT-3.5 analysiert, wie gut ein Lebenslauf zu einer Stellenausschreibung passt.

## 📋 Beschreibung

Dieses Projekt nutzt künstliche Intelligenz, um automatisch zu bewerten, wie gut ein Lebenslauf zu einer bestimmten Jobanzeige passt. Das Tool liest sowohl die Stellenausschreibung als auch den Lebenslauf aus Textdateien ein und gibt eine Bewertung von 1 bis 10 aus.

## 🚀 Features

- **🤖 KI-basierte Analyse**: Nutzt OpenAI's GPT-3.5-turbo für intelligente Textanalyse
- **📁 Einfache Bedienung**: Jobanzeige und Lebenslauf werden aus separaten Textdateien gelesen
- **📊 Numerische Bewertung**: Gibt eine klare Bewertung von 1-10 aus
- **🇩🇪 Deutsche Sprache**: Vollständig auf Deutsch optimiert
- **🔒 Sicherheit**: API-Schlüssel werden sicher über Umgebungsvariablen verwaltet
- **⚡ Einfache Installation**: Automatische Abhängigkeitsverwaltung mit requirements.txt

## 📁 Projektstruktur

```
Jobanzeige-Analyse-mit-KI/
├── main.py              # Hauptprogramm
├── job_posting.txt      # Stellenausschreibung (zu bearbeiten)
├── resume.txt           # Lebenslauf (zu bearbeiten)
├── .env                 # Umgebungsvariablen (nicht in Git, lokal erstellen)
├── .env.example         # Vorlage für Umgebungsvariablen
├── requirements.txt     # Python-Abhängigkeiten
├── .gitignore          # Git-Ignore-Datei für Sicherheit
└── README.md           # Diese Datei
```

## 🛠️ Installation

### Voraussetzungen
- Python 3.10 oder höher
- OpenAI API-Schlüssel

### Schritt-für-Schritt Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/Theodor-Mrozik/Jobanzeige-Analyse-mit-KI.git
   cd Jobanzeige-Analyse-mit-KI
   ```

2. **Virtuelle Umgebung erstellen (empfohlen)**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen einrichten**
   ```bash
   # Kopiere die Beispiel-Datei
   cp .env.example .env
   
   # Windows
   copy .env.example .env
   ```
   
   Dann öffne die `.env`-Datei und trage deinen OpenAI API-Schlüssel ein:
   ```
   OPENAI_API_KEY=dein_echter_api_schlüssel_hier
   ```

5. **OpenAI API-Schlüssel besorgen**
   - Gehe zu [platform.openai.com](https://platform.openai.com/)
   - Erstelle einen Account und füge eine Zahlungsmethode hinzu
   - Generiere einen neuen API-Schlüssel
   - Trage ihn in die `.env`-Datei ein

## 📝 Verwendung

1. **Stellenausschreibung hinzufügen**
   - Öffne `job_posting.txt`
   - Füge den vollständigen Text der Stellenausschreibung ein

2. **Lebenslauf hinzufügen**
   - Öffne `resume.txt` 
   - Füge den vollständigen Lebenslauf ein

3. **Analyse starten**
   ```bash
   python main.py
   ```

4. **Ergebnis**
   Das Programm gibt eine Zahl zwischen 1 und 10 aus, die angibt, wie gut der Lebenslauf zur Stellenausschreibung passt.

## ⚙️ Konfiguration

### Sicherheitshinweise

🔒 **API-Schlüssel Sicherheit**: 
- Der API-Schlüssel wird über Umgebungsvariablen geladen
- Die `.env`-Datei wird nicht in Git übertragen (durch `.gitignore` geschützt)
- Verwende die `.env.example` als Vorlage für die Einrichtung

### Umgebungsvariablen

Das Programm lädt automatisch Umgebungsvariablen aus der `.env`-Datei:

```bash
# .env Datei Beispiel:
OPENAI_API_KEY=sk-proj-dein_api_schlüssel_hier
```

### Alternative: System-Umgebungsvariablen

Du kannst auch System-Umgebungsvariablen verwenden:

```bash
# Windows
set OPENAI_API_KEY=dein-api-schlüssel

# macOS/Linux
export OPENAI_API_KEY=dein-api-schlüssel
```

## 💡 Beispiel

**job_posting.txt:**
```
Software Developer Position
Wir suchen einen erfahrenen Softwareentwickler mit Python-Kenntnissen...
```

**resume.txt:**
```
Max Mustermann
Software Engineer
5 Jahre Erfahrung in Python-Entwicklung...
```

**Output:**
```
8
```

## 🔧 Anpassungen

Du kannst den Prompt in `main.py` anpassen, um:
- Detailliertere Bewertungen zu erhalten
- Spezifische Kriterien zu bewerten
- Feedback statt nur Zahlen zu bekommen

Beispiel für detaillierteres Feedback:
```python
prompt = f"""
Vergleiche den Lebenslauf mit der Jobanzeige und gib eine detaillierte Analyse:
- Bewertung (1-10)
- Stärken des Kandidaten
- Verbesserungsmöglichkeiten
- Fazit

Jobanzeige: {job_text}
Lebenslauf: {ll_text}
"""
```

## 🚨 Wichtige Hinweise

- **🔒 Sicherheit**: API-Schlüssel werden sicher über Umgebungsvariablen verwaltet
- **💰 Kosten**: Jede Anfrage kostet Geld über die OpenAI API
- **🔐 Datenschutz**: Sensible Daten werden nicht in Git gespeichert (siehe `.gitignore`)
- **🎯 Genauigkeit**: Die KI-Bewertung ist ein Hilfsmittel, ersetzt aber nicht die menschliche Bewertung
- **📁 Dateien**: Die `.env`-Datei muss lokal erstellt werden und wird nicht mit Git synchronisiert

## 🐛 Fehlerbehebung

### Häufige Fehler:

- **`ModuleNotFoundError: No module named 'openai'`**
  ```bash
  pip install -r requirements.txt
  ```

- **`ValueError: OPENAI_API_KEY environment variable not set`**
  - Erstelle eine `.env`-Datei basierend auf `.env.example`
  - Trage deinen API-Schlüssel in die `.env`-Datei ein
  - Stelle sicher, dass `python-dotenv` installiert ist

- **`RateLimitError: You exceeded your current quota`**
  - Prüfe dein OpenAI-Guthaben
  - Füge eine Zahlungsmethode hinzu

- **`AuthenticationError: Incorrect API key`**
  - Überprüfe deinen API-Schlüssel in der `.env`-Datei
  - Generiere einen neuen API-Schlüssel auf der OpenAI-Plattform

- **`FileNotFoundError`**
  - Stelle sicher, dass `job_posting.txt` und `resume.txt` im gleichen Verzeichnis sind

## 🤝 Beitragen

1. Fork das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/amazing-feature`)
3. Committe deine Änderungen (`git commit -m 'Add some amazing feature'`)
4. Push zum Branch (`git push origin feature/amazing-feature`)
5. Öffne eine Pull Request

## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe `LICENSE` Datei für Details.

## 👤 Autor

**Theodor Mrozik**
- GitHub: [@Theodor-Mrozik](https://github.com/Theodor-Mrozik)

