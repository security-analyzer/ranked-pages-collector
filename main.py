
from src.Collector import Collector

collector = Collector()
collector.set_website('www.hespress.com')
collector.handle()
pages = collector.get_suggested_pages()

print(pages)