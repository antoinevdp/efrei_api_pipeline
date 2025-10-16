import requests
import json

RANDOMMER_API_KEY = 'b4a95ecc867f4c6496b36e35bb43e654'

def fetch_random_user():
    res = requests.get('https://randomuser.me/api/?nat=fr')
    data = res.json()['results'][0]
    return {
        'name': f'{data["name"]["first"]} {data["name"]["last"]}',
        'email': data['email'],
        'gender': data['gender'],
        'location': f'{data["location"]["city"]}, {data["location"]["country"]}',
        'picture': data['picture']['large']
    }

def fetch_randommer_phone():
    res = requests.get('https://randommer.io/api/Phone/Generate?CountryCode=FR&Quantity=1', headers={'X-Api-Key': RANDOMMER_API_KEY})
    return res.json()[0]

def fetch_randommer_iban():
    res = requests.get('https://randommer.io/api/Finance/Iban/FR', headers={'X-Api-Key': RANDOMMER_API_KEY})
    return res.json()

def fetch_credit_card():
    res = requests.get('https://randommer.io/api/Card', headers={'X-Api-Key': RANDOMMER_API_KEY})
    card = res.json()
    return {
        'card_number': card['cardNumber'],
        'card_type': card['type'],
        'expiration_date': card['date'],
        'cvv': card['cvv']
    }

def fetch_randommer_name():
    res = requests.get('https://randommer.io/api/Name?nameType=firstname&quantity=1', headers={'X-Api-Key': RANDOMMER_API_KEY})
    return res.json()[0]

def fetch_random_pet():
    res = requests.get('https://random-animal-api.vercel.app/api/random-animal')
    return res.json()['city']

def fetch_quote():
    res = requests.get('https://zenquotes.io/api/random')
    data = res.json()[0]
    return {
        'content': data['q'],
        'author': data['a']
    }

def fetch_joke():
    res = requests.get('https://v2.jokeapi.dev/joke/Programming?type=single')
    data = res.json()
    return {
        'type': data['category'],
        'content': data['joke']
    }

def create_full_profile():
    try:
        user = fetch_random_user()
        phone = fetch_randommer_phone()
        iban = fetch_randommer_iban()
        credit_card = fetch_credit_card()
        name = fetch_randommer_name()
        pet = fetch_random_pet()
        quote = fetch_quote()
        joke = fetch_joke()

        profile = {
            'user': user,
            'phone_number': phone,
            'iban': iban,
            'credit_card': credit_card,
            'name': name,
            'pet': pet,
            'quote': quote,
            'joke': joke
        }

        print(json.dumps(profile, indent=2))
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    create_full_profile()