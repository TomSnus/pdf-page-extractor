Hier ist die README-Datei korrekt formatiert als Markdown:

# PDF Seitenextraktor
Dieses Python-Programm ermöglicht das Extrahieren von Seiten aus PDF-Dateien und das Speichern der extrahierten Seiten in einer ZIP-Datei.

## Voraussetzungen
Um das Programm auszuführen, müssen Sie die folgenden Python-Pakete installieren:

```python
PyPDF2
```
Führen Sie den folgenden Befehl aus, um die erforderlichen Pakete zu installieren:

```bash
pip install PyPDF2
```

## Programmablauf
1. Kopieren Sie den oben stehenden Python-Code in eine neue Datei.

2. Setzen Sie die erforderlichen Variablen am Ende des Skripts.
```python
# Input directory containing all PDF files
input_directory = "<pfad>"

# Page numbers to extract (starting from 1)
pages_to_extract = [2, 3]

# Output ZIP file path
output_zip_file = "<pfad>"
```
Setzen Sie `<pfad>` auf den tatsächlichen Pfad zur PDF-Datei und zum Ausgabeverzeichnis. Stellen Sie sicher, dass der `output_zip_file`-Pfad auf eine Datei und nicht auf ein Verzeichnis verweist, z.B. `output_zip_file = "C:\\Users\\benutzer\\Documents\\3TTX\\LBU\\25\\extracted_pages.zip"`.

3. Speichern Sie die Datei mit einer **.py**-Erweiterung, z.B. **pdf_seitenextraktor.py**.

4. Öffnen Sie eine Konsole oder ein Terminalfenster und navigieren Sie zu dem Verzeichnis, in dem Sie die Datei **pdf_seitenextraktor.py** gespeichert haben.

5. Führen Sie den Befehl **python pdf_seitenextraktor.py** aus, um das Programm auszuführen.

Das Programm wird die angegebenen PDF-Dateien im Eingabeverzeichnis verarbeiten und die extrahierten Seiten in einer ZIP-Datei abspeichern.

## Zusätzliche Hinweise
- Stellen Sie sicher, dass die PDF-Dateien im Eingabeverzeichnis vorhanden sind.
- Stellen Sie sicher, dass Sie Schreibzugriff auf den Ordner haben, in dem die ZIP-Datei gespeichert wird.
- Wenn Sie das Programm unter Windows ausführen, stellen Sie sicher, dass Sie die Konsole oder das Terminalfenster als Administrator öffnen, um mögliche Berechtigungsprobleme zu vermeiden.
- Überprüfen Sie, ob der Pfad zur ZIP-Datei korrekt ist und auf eine Datei verweist, nicht auf ein Verzeichnis.
- Python muss auf Ihrem System installiert sein, um dieses Programm auszuführen. Sie können die neueste Version von Python von der offiziellen [Python-Website](https://www.python.org/downloads/) herunterladen und installieren.

## Beispiel
Hier ist ein Beispiel, wie die Variablen gesetzt werden können:

```python
# Input directory containing all PDF files
input_directory = r'C:\Users\benutzer\Documents\3TTX\LBU\25'

# Page numbers to extract (starting from 1)
pages_to_extract = [2, 3]

# Output ZIP file path
output_zip_file = r'C:\Users\benutzer\Documents\3TTX\LBU\25\extracted_pages.zip'
```

## Fehlerbehebung
Falls Sie auf Fehlermeldungen stoßen, überprüfen Sie die folgenden Punkte:
- Überprüfen Sie die Dateiberechtigungen und stellen Sie sicher, dass Sie die notwendigen Lese- und Schreibrechte haben.
- Stellen Sie sicher, dass die Pfade korrekt gesetzt sind und dass die Dateien existieren.
- Stellen Sie sicher, dass keine anderen Programme die PDF-Dateien geöffnet haben, die Sie verarbeiten möchten.


