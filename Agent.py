from llama_index.llms.gemini import Gemini

PROMPT = """
            "As an expert in analyzing articles for speech synthesis, your task is to extract and structure the text of the article. REMOVE ALL  the HTML BALISES like href or <a> or anything start with < , i want it to be only Text to read like News and make sure each picture is related to the context of its paraphraph"
            "Please split the text into paragraphs and identify the picture from the site that is most related to each paragraph. "
            "Make sure each paragraph is readable and understandable when its read as a speech in news "
            "The response should be formatted as follows:\n\n"
            "[Paragraph 1: <Text of paragraph 1> : Picture related to it: <URL of picture 1> , "
            "Paragraph 2: <Text of paragraph 2> : Picture related to it: <URL of picture 2>, ...]\n\n"
            "Keep the text in its original French language.\n\n"
            f"HTML Content:\n{html_content}"
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
