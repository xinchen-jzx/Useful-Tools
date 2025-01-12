from openai import OpenAI

key = "sk-951NHwqt4kLE1vcXEd1261A0C5744c53A85fB872A0502a7a"
base_url = "https://aihubmix.com/v1"
client = OpenAI(api_key=key, base_url=base_url)

class Chat:
    def __init__(self, conversation_list=[]) -> None:
        self.conversation_list = []  # 初始化对话列表

    def ask(self, prompt):
        self.conversation_list.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(model="o1-mini", 
                                                  messages=self.conversation_list)
        answer = response.choices[0].message.content
        self.conversation_list.append({"role": "assistant", "content": answer})
        
        return answer

def main():
    talk = Chat()

    with open("./prompt.txt", "r") as f:
        prompt = f.read()
    print(f"PROMPT: {prompt}")

    while True:
        try:
            answer = talk.ask(prompt)
            print("====================================")
            print(answer)
            print("====================================")
            break
        except:
            print("server has bugs")

if __name__ == "__main__":
    main()
