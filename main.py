from src.Utils import banner, save_array_as_file
from src.Collector import Collector

websites = [
    'https://damanecash.ma',
    'https://www.creditdumaroc.ma',
    'https://www.umniabank.ma',
    'https://www.cihbank.ma',
    'https://attijarinet.attijariwafa.com',
    'https://www.bmci.ma',
    'https://bpnet.gbp.ma',
    'https://www.wafasalaf.ma',
    'https://www.cashplus.ma',
    'https://www.sgmaroc.com',
    'https://www.albaridbank.ma',
    'https://www.creditagricole.ma',
]

def main():
    for website in websites:
        website_domain = website.split('://')[1]
        print("Started processing : " + website + " - " + website_domain)
        collector = Collector()
        collector.set_website(website_domain)
        collector.handle()
        pages = collector.get_suggested_pages()
        save_array_as_file('datasets/finance/' + website_domain, pages)


if __name__ == "__main__":
    banner()
    main()