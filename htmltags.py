import re

"""
  Class:
    HTMLTAGS(data, dictionary)
  Function:
    loadTags()
    replaceTags()
  Variable:
    html_data

  See example in the Readme file...
"""

class HTMLTAGS:
    def __init__(self, html_data, html_replace):
        self.html_data = html_data
        self.html_replace = html_replace

    def loadTags(self):
        for html_key in self.html_replace:
            html_val = self.html_replace[html_key]
            html_search = re.search("\.{1,2}\/.*\.\w{2,}", html_val)
            if html_search:
                html_val = open(html_val, "r").read()
            self.html_replace[html_key] = html_val

    def replaceTags(self):
        for html_key in self.html_replace:
            self.html_data = re.sub(
                re.escape(f"/* {html_key} */"),
                self.html_replace[html_key],
                self.html_data,
            )
            self.html_data = re.sub(
                re.escape(f"<!-- {html_key} -->"),
                self.html_replace[html_key],
                self.html_data,
            )
