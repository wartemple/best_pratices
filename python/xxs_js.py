
from lxml.html.clean import Cleaner
from lxml import html
text = '<img style="cienter: auto; display: block; margin-left: auto; margin-right: auto;" src="x" onerror="alert(1)">'
clean = Cleaner(safe_attrs=html.defs.safe_attrs | set(['style']))
print(clean.clean_html(text))
