from Extractor import HTMLExtractor
from Agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    url = "https://www.purepeople.com/article/en-plein-divorce-avec-luana-paul-belmondo-partage-un-beau-moment-avec-leur-fils-victor-et-l-immortalise-en-photo_a526200/1"

    html_extractor = HTMLExtractor()
    print("-------------------extracting HTML------------------...")
    html_content = html_extractor.get_html(url)
    print("---------------END EXTRACTING HTML-----------------------")
    agent = Agent(api_key=api_key)
    agent.extract_content(html_content=html_content)


if __name__ == "__main__":
    main()
