from g4f.client import Client
from warnings import filterwarnings

filterwarnings(action="ignore", category=RuntimeWarning)
client = Client()


print('привет я Кевин, чат-бот от ютубера @Ааамммиииррр, чем я могу тебе помочь?\n')

while True:
    request = input("Пользователь: ")

    system_instruction = "Тебя зовут Кевин, твоя задача отвечать на вопросы саркастично"
    full_request = system_instruction + request

    response = client.chat.completions.create([{"role": "system", "content": full_request}],
                                              model="gpt-4o")
    print(response.choices[0].message.content)