import requests

def search(query, search_type=None):
    params = {
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'lr': 'lang_en',
        'cr': 'countryIN|countryUS'
    }

    if search_type == 'image':
        params['searchType'] = 'image'

    response = requests.get(url, params=params)
    results = response.json().get('items', [])

    if not results:
        print("No results found.")
        return

    for item in results:
        print(item['link'])
def search_info():
    query = input("Enter your search query for information: ").lower()
    search(query, 'information')

def search_images():
    query = input("Enter your search query for images: ").lower()
    search(query, 'image')

def exit_code():
    print("Thank you For using our Search Engine!.")
    print("Exiting the program.")
    exit()

def display_menu():
    print("Automated Search Engine Using API")
    print("WELCOME")
    print("\nWhat would you like to Search for Today?")
    print("\nMenu:")
    print("1. Search for Information")
    print("2. Search for Images")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            search_info()
        elif choice == '2':
            search_images()
        elif choice == '3':
            exit_code()
        else:
            print("Invalid choice. Please enter an option between 1 and 3.")

if __name__ == "__main__":
    API_KEY = open('API_KEY').read().strip()
    SEARCH_ENGINE_ID = open('SEARCH_ENGINE_ID').read().strip()
    url = 'https://www.googleapis.com/customsearch/v1'

    main()
