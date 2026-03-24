import requests
import dotenv
import os

def main():
    dotenv.load_dotenv()
    url='https://dadata.ru/api/clean/name/'
    key=os.getenv('DADATA_API')
    secret=os.getenv('DADATA_SECRET')
    name=input().strip()
    data=[name]
    headers={
        "Content-Type": "application/json",
        "Authorization": "Token "+key,
        "X-Secret": secret_key
    }
    answer=requests.post(url,headers=headers,json=data)
    if answer.status_code==200:
        if answer.json()[0].get('qc')==0:
            print(f"Родительный падеж: {answer.get('genitive')}")
            print(f"Дательный падеж: {answer.get('dative')}")
            print(f"Творительный падеж: {answer.get('instrumental')}")
        else:
            print("Человек, мне нужна твоя помощь")
    else:
        print("Человек, мне нужна твоя помощь")

if __name__ == '__main__':
    main()