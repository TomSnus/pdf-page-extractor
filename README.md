# PDF Seitenextraktor

Eine Anwendung mit grafischer Benutzeroberfläche zum Extrahieren bestimmter Seiten aus PDF-Dateien und Zusammenfassen in einer ZIP-Datei.

## Funktionen

- Benutzerfreundliche grafische Oberfläche
- Extrahieren bestimmter Seiten aus mehreren PDF-Dateien
- Zusammenfassen der extrahierten Seiten in einer ZIP-Datei
- Integrierte Hilfe-Funktion
- Standardauswahl der Seiten (2,3)
- Protokollierung für Fehlerbehebung

## Voraussetzungen

### Für Benutzer
- Windows: Einfach die EXE-Datei herunterladen und ausführen
- Keine Python-Installation erforderlich

### Für Entwickler
- Python 3.x
- Erforderliche Pakete:
  ```bash
  pip install PyPDF2 pyinstaller
  ```

## Installation

### Benutzer
1. Laden Sie die aktuelle `PDF Seitenextraktor.exe` aus dem Release-Bereich herunter
2. Doppelklicken Sie auf die Datei, um die Anwendung zu starten

### Entwickler
1. Repository klonen:
   ```bash
   git clone 
   cd pdf-page-extractor
   ```

2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install PyPDF2 pyinstaller
   ```

## Verwendung

1. Starten Sie die Anwendung
2. Wählen Sie das PDF-Verzeichnis über den "Durchsuchen"-Button
3. Geben Sie die zu extrahierenden Seitenzahlen ein (Standard: 2,3)
4. Wählen Sie den Speicherort für die ZIP-Datei
5. Klicken Sie auf "Extraktion starten"

## Executable erstellen

### Windows
```bash
pyinstaller pdf_extractor.spec
```
Die ausführbare Datei wird im `dist`-Verzeichnis erstellt.

## Fehlerbehebung

- Überprüfen Sie die `pdf_extractor.log` Datei für detaillierte Fehlerinformationen
- Häufige Probleme:
  - Stellen Sie sicher, dass die PDF-Dateien nicht in anderen Programmen geöffnet sind
  - Überprüfen Sie, ob die angegebenen Seitenzahlen in den PDF-Dateien existieren
  - Überprüfen Sie die Schreibrechte für den Ausgabeordner

## Programmstruktur
 ```
 pdf-page-extractor/
├── pdf_extractor.py # Hauptanwendungsdatei
├── pdf_extractor.spec # PyInstaller-Spezifikation
├── pdf_extractor.ico # Anwendungssymbol
├── README.md # Diese Datei
└── pdf_extractor.log # Protokolldatei (wird beim Ausführen erstellt)
   ```


## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe LICENSE-Datei für Details.

## Unterstützung

Bei Problemen:
1. Konsultieren Sie das integrierte Hilfehandbuch (Hilfe-Button in der Anwendung)
2. Überprüfen Sie die Protokolldatei
3. Erstellen Sie ein Issue auf GitHub

## Änderungsprotokoll

### Version 1.0.0
- Erstveröffentlichung mit grafischer Benutzeroberfläche
- Hilfehandbuch hinzugefügt
- Protokollierungsfunktion hinzugefügt
- Standardseitenauswahl (2,3)
- Windows-Executable-Unterstützung

## Funktionsweise

Der PDF Seitenextraktor ermöglicht es Ihnen, bestimmte Seiten aus mehreren PDF-Dateien zu extrahieren:

1. **PDF-Verzeichnis auswählen**: 
   - Wählen Sie den Ordner, der Ihre PDF-Dateien enthält
   - Alle PDF-Dateien in diesem Ordner werden verarbeitet

2. **Seiten auswählen**: 
   - Geben Sie die gewünschten Seitenzahlen ein
   - Verwenden Sie Kommas zur Trennung (z.B. "2,3")
   - Die Seitennummerierung beginnt bei 1

3. **Ausgabe-ZIP**: 
   - Wählen Sie, wo die ZIP-Datei gespeichert werden soll
   - Die extrahierten Seiten werden automatisch in der ZIP-Datei zusammengefasst

4. **Verarbeitung**: 
   - Klicken Sie auf "Extraktion starten"
   - Der Fortschritt wird in der Protokolldatei dokumentiert
   - Nach erfolgreicher Verarbeitung erscheint eine Bestätigungsmeldung

## Technische Details

- Entwickelt in Python mit tkinter für die Benutzeroberfläche
- Verwendet PyPDF2 für die PDF-Verarbeitung
- Protokollierung mit dem Python-logging-Modul
- Standalone-Executable mit PyInstaller erstellt

## Systemanforderungen

- Windows 7 oder höher
- Mindestens 100 MB freier Speicherplatz
- Mindestens 2 GB RAM