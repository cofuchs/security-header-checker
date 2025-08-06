import requests

required_headers = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url):
    try:
        response = requests.get(url)
        print(f"\n🔍 Scanning: {url}\n")
        headers = response.headers

        for header in required_headers:
            if header in headers:
                print(f"✅ {header}: vorhanden")
            else:
                print(f"❌ {header}: fehlt")

    except requests.exceptions.RequestException as e:
        print("Fehler beim Abrufen der Seite:", e)

if __name__ == "__main__":
    url = input("Gib eine URL ein (mit https://): ")
    check_headers(url)