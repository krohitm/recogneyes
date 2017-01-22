import pprint

from googleapiclient.discovery import build


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyB1hIpNK7rEtHcjNQfwFXHrLdlWB4aW6g4")

  res = service.cse().list(
      q='lectures',
      cx='009623384591570899968:pgdat6gk7ee',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()