import os
from sys import exit
import socket
import time
from urllib.parse import urlparse
from urllib.parse import urljoin
import random
import subprocess
import webbrowser

def sil():
    try:
        name = os.name
        if name == "nt":
            os.system("cls")

        elif name == "posix":
            os.system("clear")
            
        else:
            print("[-] İşletim sistemi desteklenmiyor!")
            input("Devam etmek için enter'a basın...")
            exit(1)
    
    except Exception as e:
        print(f"[-] Hata: {e}")
        input("Devam etmek için enter'a basın...")

def check_connection():
    print("[!] Bağlantı testi için '8.8.8.8' bağlantısı kurulmaya çalışılıyor...")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        print("[+] Test başarılı.")
        return True
    except OSError:
        print("[!] Bağlantı testi başarısız oldu, bazı özellikler kullanılamayabilir!")
        input("Devam etmek için enter'a basın...")
        return False

def check_libraries():
    try:
        print("\nKütüphaneler denetleniyor...\n")
        import requests
        from colorama import Fore, Back, Style, init
        from bs4 import BeautifulSoup
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from selenium.webdriver.edge.service import Service as EdgeService
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from selenium.webdriver.edge.options import Options as EdgeOptions
        from webdriver_manager.firefox import GeckoDriverManager
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

    except ImportError:
        oto_indirilsin_mi = input("\n[?] Eksik kütüphaneler bulundu, bunları otomatik olarak indirmek ister misiniz (y/n): ").lower().strip()
        if oto_indirilsin_mi.startswith("y"):
            setup()
            try:
                import requests
                from colorama import Fore, Back, Style, init
                from bs4 import BeautifulSoup
                from selenium import webdriver
                from selenium.webdriver.chrome.service import Service
                from selenium.webdriver.common.by import By
                from webdriver_manager.chrome import ChromeDriverManager
                from selenium.webdriver.chrome.options import Options
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions as EC
                from selenium.webdriver.chrome.service import Service as ChromeService
                from selenium.webdriver.firefox.service import Service as FirefoxService
                from selenium.webdriver.edge.service import Service as EdgeService
                from selenium.webdriver.chrome.options import Options as ChromeOptions
                from selenium.webdriver.firefox.options import Options as FirefoxOptions
                from selenium.webdriver.edge.options import Options as EdgeOptions
                from webdriver_manager.firefox import GeckoDriverManager
                from webdriver_manager.microsoft import EdgeChromiumDriverManager
                
            except ImportError as e:
                print(f"[ERROR] Eksik modül: {e.name}. Lütfen şunu kullanarak kurun: 'pip install {e.name}'")
                exit(1)
        
        else:
            input("[!] Çıkmak için enter'a basın...")
            exit(1)

def setup():
    try:
        print("[!] Kuruluma başlanıyor...")
        time.sleep(1)
        os.system("pip install requests colorama beautifulsoup4 selenium webdriver-manager")
        sil()
        print("[+] Kurulum başarılı. Lütfen programı yeniden başlatın.")
        input("Devam etmek için enter'a basın...")
        exit(1)

    except Exception as e:
        print(f"[!] Hata: {e}")
        input("Devam etmek için enter'a basın...")
        exit(1)

sil()
check_connection()
check_libraries()

import requests
from colorama import Fore, Back, Style, init
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

init(autoreset=True)

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=50)
session.mount('http://', adapter)
session.mount('https://', adapter)

def banner():
    print(Style.BRIGHT + Fore.LIGHTRED_EX + """
 .S S.    .S_SSSs     .S_sSSs              .S    sSSs_sSSs     .S_SSSs      sSSs  
.SS SS.  .SS~SSSSS   .SS~YS%%b            .SS   d%%SP~YS%%b   .SS~SSSSS    d%%SP  
S%S S%S  S%S   SSSS  S%S   `S%b           S%S  d%S'     `S%b  S%S   SSSS  d%S'    
S%S S%S  S%S    S%S  S%S    S%S           S%S  S%S       S%S  S%S    S%S  S%|     
S%S S%S  S%S SSSS%S  S%S    S&S           S&S  S&S       S&S  S%S SSSS%P  S&S     
 SS SS   S&S  SSS%S  S&S    S&S           S&S  S&S       S&S  S&S  SSSY   Y&Ss    
  S S    S&S    S&S  S&S    S&S           S&S  S&S       S&S  S&S    S&S  `S&&S   
  SSS    S&S    S&S  S&S    S&S           S&S  S&S       S&S  S&S    S&S    `S*S  
  S*S    S*S    S&S  S*S    S*S           d*S  S*b       d*S  S*S    S&S     l*S  
  S*S    S*S    S*S  S*S    S*S          .S*S  S*S.     .S*S  S*S    S*S    .S*P  
  S*S    S*S    S*S  S*S    S*S        sdSSS    SSSbs_sdSSS   S*S SSSSP   sSS*S   
  S*S    SSS    S*S  S*S    SSS        YSSY      YSSP~YSSY    S*S  SSY    YSS'    
  SP            SP   SP                                       SP                  
  Y             Y    Y                                        Y                   
                                                                                  
                            [github.com/Yan-Jobs]            
""")
    print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTRED_EX + "Bu kodu yönetici olarak çalıştırmanız tavsiye edilir!\n")

def url_domain_cevir(url):
    parsedurl = urlparse(url)
    domain = parsedurl.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain

def random_headers():
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]
    random_user_agent = random.choice(user_agents)
    headers = {
    "User-Agent": random_user_agent,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}
    return headers

def tarayici_sec():
    tarayici = None

    try:
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[+] Chrome başlatılıyor...")
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')
        tarayici = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        return tarayici
    
    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[-] Chrome başlatılamadı: {e}")


    try:
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[+] Firefox başlatılıyor...")
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        tarayici = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        return tarayici
    
    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[-] Firefox başlatılamadı: {e}")


    try:
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"[+] Edge başlatılıyor...")
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        tarayici = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
        return tarayici
    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[-] Edge başlatılamadı: {e}")


    print(Style.BRIGHT + Fore.LIGHTRED_EX + "[-] Hiçbir tarayıcı başlatılamadı! Chrome, Firefox veya Edge'nin sisteminizde kurulu olduğundan emin olun!\n")
    time.sleep(5)
    return None

def download_file(url, save_path):
    try:
        response = requests.get(url, timeout=20, headers=random_headers())
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"[+] Dosya başarıyla kaydedildi: {save_path}")
        else:
            print(Style.DIM + Fore.LIGHTRED_EX + f"[-] Dosya indirilemedi: {response.status_code}")
    except Exception as e:
        print(Style.DIM + Fore.LIGHTRED_EX + f"[-] Hata: {type(e).__name__} - {e}")


def web_sayfasi_indir(target_url):
    try:
        domain = url_domain_cevir(target_url)

        os.makedirs(domain, exist_ok=True)
        css_folder = os.path.join(domain, "css")
        js_folder = os.path.join(domain, "js")
        os.makedirs(css_folder, exist_ok=True)
        os.makedirs(js_folder, exist_ok=True)

        tarayici = tarayici_sec()
        if not tarayici:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + "[-] Tarayıcı başlatılamadı!")
            return main()

        try:
            tarayici.get(target_url)
            WebDriverWait(tarayici, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "html")))

            page_source = tarayici.page_source
            tarayici.quit()

            soup = BeautifulSoup(page_source, "html.parser")

        except Exception as e:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[!] Hata: {e}")
            return
        
    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[!] Hata: {e}")
        return

    try:
        response = session.get(target_url, timeout=10, headers=random_headers())
        htmlkodu = response.text
        soup = BeautifulSoup(htmlkodu, "html.parser")
        with open(f"{domain}.html", "w", encoding="utf-8") as file:
            file.write(page_source)
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"[+] Saf html kodu '{domain}.html' olarak kayıt edildi!")

        for link in soup.find_all("link", {"rel": "stylesheet"}):
            css_url = link.get("href")
            if css_url:
                if not css_url.startswith(("http://", "https://")):
                    css_url = urljoin(target_url, css_url)
                try:
                    file_name = os.path.basename(css_url)
                    save_path = os.path.join(css_folder, file_name)
                    download_file(css_url, save_path)
                    link["href"] = f"css/{file_name}"
                except Exception as e:
                    print(Style.DIM + Fore.LIGHTRED_EX + f"[-] CSS indirilemedi: {css_url} - Hata: {e}")

        for script in soup.find_all("script"):
            js_url = script.get("src")
            if js_url:
                if not js_url.startswith(("http://", "https://")):
                    js_url = urljoin(target_url, js_url)
                try:
                    file_name = os.path.basename(js_url)
                    save_path = os.path.join(js_folder, file_name)
                    download_file(js_url, save_path)
                    script["src"] = f"js/{file_name}"
                except Exception as e:
                    print(Style.DIM + Fore.LIGHTRED_EX + f"[-] JS indirilemedi: {js_url} - Hata: {e}")

        html_path = os.path.join(domain, "updated.html")
        with open(html_path, "w", encoding="utf-8") as file:
            file.write(soup.prettify())
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"\n[+] Güncellenmiş HTML dosyası '{html_path}' olarak kaydedildi!")

        local_calistirilsin_mi = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Bu sayfayı 'localhost:8000' üzerinden çalıştırmak istermisiniz (y/n): ").strip().lower()

        if local_calistirilsin_mi == "y":
            try:
                print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[+] Lütfen bekleyiniz...")

                process = subprocess.Popen(["python", "-m", "http.server"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "[+] Http Server başlatıldı. 'Ctrl + C' yaparak sunucuyu kapatabilirsiniz.")
                webbrowser.open_new("http://localhost:8000")

                input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\n[+] Sunucuyu kapatmak için 'enter' tuşuna basınız...\n")

                process.terminate()
                process.wait()
                print(Style.BRIGHT + Fore.LIGHTRED_EX + "[+] Sunucu başarıyla kapatıldı!")
                time.sleep(3)
                return main()

            except Exception as e:
                print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[-] Hata: {e}")

        else:
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[+] Localhost çalıştırma atlandı.")
            input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\n[+] Devam etmek için 'enter' tuşuna basınız...\n")
            return main()

    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"[-] Hata: {e}")

def contact():
    contact_menu = Style.BRIGHT + Fore.LIGHTCYAN_EX + """
    Welcome the world
"""
    print(contact_menu)
    input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[*] Devam etmek için 'enter' tuşuna basınız...\n")
    return main()

def main():
    try:
        sil()
        banner()
        menu = Style.BRIGHT + Fore.LIGHTCYAN_EX + """
        [1] - Web Sayfası İndir
        [2] - Otomatik Kurulum
        [3] - İletişim
        [4] - Çıkış
    """
        print(menu)
        secim = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Lütfen seçiminizi yapınız: ").strip().lower()

        if secim == "1" or secim.startswith("w"):
            sil()
            banner()
            target_url = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "[?] Lütfen URL adresini giriniz: ").strip()
            print("\n")
            if not target_url.startswith(("https://", "http://")):
                target_url = "https://" + target_url
            web_sayfasi_indir(target_url)

        elif secim == "2" or secim.startswith("o"):
            sil()
            banner()
            check_connection()
            check_libraries()
            print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\n[+] Tüm testler başarılı. Ana menüye yönlendiriliyorsunuz...\n")
            time.sleep(3)
            return main()
        
        elif secim == "3" or secim.startswith("i"):
            sil()
            banner()
            contact()

        elif secim == "4" or secim.startswith("q") or secim.startswith("x") or secim.startswith("e"):
            exit(0)

        else:
            return main()
        
    except Exception as e:
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"\n[-] Hata: {e}\n")
        input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "Devam etmek için 'enter' tuşuna basınız...\n")
        return main()

if __name__ == "__main__":
    main()
