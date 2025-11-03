# BuddyCall Prototype

Dieses Repository enthält einen Flowise-Chatflow, der den BuddyCall-Chatbot mit den spezifizierten Verhaltensrichtlinien bereitstellt.

## Inhalte
- `BuddyCall_Prototype Chatflow.json`: Export des Flowise-Chatflows mit Azure-OpenAI-Anbindung, Moderation und Speicher.
- `README.md`: Kurzanleitung zur Nutzung.

## Verwendung
1. Flowise öffnen und unter **Chatflows** die Option **Import** wählen.
2. Die Datei `BuddyCall_Prototype Chatflow.json` hochladen.
3. In den Azure-OpenAI-Knoten die eigenen Azure-Zugangsdaten sowie das gewünschte Modell auswählen.
4. Optional die Speicher- und Moderationsparameter anpassen.
5. Den Chatflow deployen und testen.

Der Chatflow enthält den vollständigen BuddyCall-Systemprompt mit allen Vorgaben zu Tonalität, Ausgabeformat und Sicherheitsregeln.
