from requests import get
from bs4 import BeautifulSoup
import slack

# source URL to scrape data from
url = 'https://www.mohfw.gov.in/'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser') # to parse page
all_span=[]
for span in html_soup.find_all("span"):     # to hold the key values
    all_span.append(span.text)
active = all_span[1]
cured = all_span[2]
death = all_span[3]

# transit data over to Slack
client = slack.WebClient(token=os.environ['SLACK_API_TOKEN']) # authenticate
response = client.chat_postMessage(
    channel='#covid-19-update',
    text="COVID-19 India Report\n\nActive cases: " + active + "\nCured/discharged cases: " + cured + "\nDeath Cases: " + death)
assert response["ok"]
