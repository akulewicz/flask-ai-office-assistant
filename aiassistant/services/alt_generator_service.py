from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AltGeneratorService:
    def __init__(self, model="gpt-4o-mini", max_tokens=500):
        self.client = OpenAI()
        self.model = model
        self.max_tokens = max_tokens
        
    def generate_alt(self, image_url):
        try:
            alt = self._send_to_openai(image_url)
            return alt
        except:
            return 'Przepraszamy, ale wystąpił błąd w generowaniu tekstu alternatywnego.'
        
    def _send_to_openai(self, image_url):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Jesteś specjalstą do spraw dostępności stron internetowych dla osób ze szczególnymi potrzebami. Stwórz tekst alternatywny dla obrazka z podanego linku. Tekst powinien mieć maksymalnie 220 znaków. Nie dodawaj napisu 'tekst alternatywny', zwróć sam tekst, który można przekopiować i wkleić na stronę WWW."},
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                    },
                    },
                ],
                }
            ],
            max_tokens=self.max_tokens,
        )

        return response.choices[0].message.content
                