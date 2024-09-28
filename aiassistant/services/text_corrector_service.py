from openai import OpenAI

class TextCorrectorService:
    def __init__(self):
        self.client = OpenAI()
        
    def correct_text(self, text, simplify=False):
        prompt = self._generate_prompt(text, simplify)
        corrected_text = self._send_to_openai(prompt)
        return corrected_text
        
    def _generate_prompt(self, text, simplify):
        prompt = f"Popraw w poniższym tekście błędy ortograficzne, stylistyczne i interpunkcyjne."
        if simplify:
            prompt += "Uprość tekst tak, żeby był bardziej zrozumiały"
        prompt += f"Oto tekst: {text}"
        return prompt
    
    def _send_to_openai(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "Jesteś profesjonalnym korektorem tekstu. Twoim zadaniem jest poprawienie tekstu wpisanego przez użytkownika. Nie dodawaj nowych słów. Zrób odstępy pomiędzy akapitami."
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": prompt
                    }
                ]
                },
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "text"
            }
        )
        
        return response.choices[0].message.content

   
    
        