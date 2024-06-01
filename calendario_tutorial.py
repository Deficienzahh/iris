import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
def get_access_token():
    # Carica le credenziali dal file JSON
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        'gcalendar_api_access.json', scopes=['https://www.googleapis.com/auth/calendar'])

    # Avvia il processo di autorizzazione
    credentials = flow.run_console()

    # Restituisce il token di accesso
    return credentials.token

# Esempio di utilizzo:
access_token = get_access_token()
print("Token di accesso:", access_token)
