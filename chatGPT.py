import openai

class chatGPT: 
    def __init__(self, api_key, rolle):
        openai.api_key = api_key
        self.dialog = [{"role":"system", "content":rolle}]

    def fragen(self, frage):
        self.dialog.append({"role":"user", "content":frage})
        ergebnis = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=self.dialog)
        antwort = ergebnis["choices"][0].message.content
        self.dialog.append({"role":"assistant", "content":antwort})
        return antwort
    
if __name__ == '__main__':
    with open('api.key') as api_key:
        api_key = api_key.read()
        chatbot = chatGPT(api_key, "Sei ein Hacker.")

        while (frage := input('\n>'))!='X':
            antwort = chatbot.fragen(frage) 
            print(antwort)