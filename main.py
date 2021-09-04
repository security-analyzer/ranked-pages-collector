from src.ApiProxy import ApiProxy
from src.Collector import Collector


collector = Collector()
collector.set_website('www.richbond.ma')
collector.handle()
pages = collector.get_suggested_pages()

print(pages)

