from llama_index.llms.gemini import Gemini
import time

PROMPT = """
            from the html below,
            you're job is to extract the article text related to the title with the URLs of the images that were in the article text related to title.
            each url should be with the related text that was near the image in the article text.
            HTML Content:
            {html_content}
        """
class Agent:
    def __init__(self, api_key):
        self.llm = Gemini(
            model_name="models/gemini-1.5-flash",
            api_key=api_key,
        )
        
    def extract_content(self, html_content):
        start = time.time()
        response = self.llm.complete(prompt=PROMPT + html_content)
        end = time.time()
        print("Time taken: ", int(end-start),"sec \n" ,"Response generated!!","\n-------------------------\n")
        print(response)
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(str(response))
        return response
