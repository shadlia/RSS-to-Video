from llama_index.llms.gemini import Gemini

PROMPT = """
            you're job is to extract the text related to the article title and list the URLs of the images that were in the text related to the article title.
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
        response = self.llm.complete(prompt=PROMPT + html_content)
        print(response)
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(str(response))
        return response
