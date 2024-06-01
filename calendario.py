from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    return service

def add_event_to_calendar(summary, start_datetime, end_datetime):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Your Timezone',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Your Timezone',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Evento aggiunto:', event.get('htmlLink'))

def main():
    summary = input("Inserisci il titolo dell'evento: ")
    start_datetime = input("Inserisci data e ora di inizio (YYYY-MM-DDTHH:MM:SS): ")
    end_datetime = input("Inserisci data e ora di fine (YYYY-MM-DDTHH:MM:SS): ")
    add_event_to_calendar(summary, start_datetime, end_datetime)

if __name__ == "__main__":
    main()
