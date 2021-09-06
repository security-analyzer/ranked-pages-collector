from src.Utils import config, save_array_as_file
from src.Collector import Collector

websites = [
    'https://www.uca.ma',
    'https://fstbm.ac.ma',
    'https://um6p.ma',
    'https://www.uir.ac.ma',
    'https://www.ueuromed.org',
    'https://upm.ac.ma',
    'https://www.emsi.ma',
    'https://emi.ac.ma',
    'https://www.groupeiscae.ma',
    'https://www.encgcasa.ma',
    'https://universiapolis.ma',
    'https://www.ofppt.ma',
]

def main():
    collector = Collector()
    
    for website in websites:
        website_domain = website.split('://')[1]
        print("Started processing : " + website)
        collector.set_website(website_domain)
        collector.handle()
        pages = collector.get_suggested_pages()
        save_array_as_file('datasets/education/' + website_domain, pages)