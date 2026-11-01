SOLAR CLOCK  -  full-screen Django clock
========================================

SETUP (Windows PowerShell / VS Code terminal)
  1. mkdir solar
  2. cd solar
  3. py -m venv .venv
  4. .venv\Scripts\activate
  5. Extract solar.zip INTO this folder (manage.py must sit directly in "solar")
  6. pip install -r requirements.txt
  7. python manage.py runserver
  8. Open http://127.0.0.1:8000

macOS / Linux: use  python3 -m venv .venv  and  source .venv/bin/activate

CONTROLS
  Click or F    Full screen (Esc exits)
  T / Right     Next theme      Left   Previous theme
  Space         12 / 24 hour
  S             Seconds on / off

Themes: Solar, Neon Drive, Matrix, Aurora, Cosmos, Minimal.
Your choices are remembered by the browser.
Stop the server with Ctrl + C.
