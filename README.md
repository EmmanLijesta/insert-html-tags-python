# Insert-HTML-Tags-In-Python
Inserts multiple HTML tags into an HTML file in Python.

# Example in Python
```
import htmltags

HTML_PATH = "../documents/test.html"
HTML_DATA = open(HTML_PATH, "r").read()

# Tag : Path to CSS/JS/HTML or code
HTML_REPLACE = {
    "styles:1": """
        body: {
            background-color: #000000;
        }
    """,
    "scripts:1": "../static/js/test.js",
    "heading:1": "The Title of the Page",
    "paragraph:1": """
        The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
        The quick brown fox jumps over the lazy dog.
    """,
    "heading:2": "<a href='#some-id'>Go to Label</a>",
    "paragraph:2": "The quick brown fox jumps over the lazy dog.",
    "body:1": "../views/tagtest.html",
}

my_tags = HTMLTAGS(HTML_DATA, HTML_REPLACE)
my_tags.loadTags()
my_tags.replaceTags()
print(my_tags.html_data)
```
## Sample test.html
Take note of the comment tags and format in the HTML file. They will be replaced.
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><!-- heading:1 --></title>
  <style>
    /* styles:1 */
  </style>
  <script>
    /* scripts:1 */
  </script>
</head>
<body>
  <h1><!-- heading:1 --></h1>
  <p><!-- paragraph:1 --></p>
  <h2><!-- heading:2 --></h2>
  <p><!-- paragraph:2 --></p>
  <!-- body:1 -->
</body>
</html>
```
## Output
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The Title of the Page</title>
  <style>
        body: {
            background-color: #000000;
        }
  </style>
  <script>
    console.log("Javascript Inserted")
  </script>
</head>
<body>
  <h1>The Title of the Page</h1>
  <p>
        The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
        The quick brown fox jumps over the lazy dog.
    </p>
  <h2><a href='#some-id'>Go to Label</a></h2>
  <p>The quick brown fox jumps over the lazy dog.</p>
  <h2>This is a Heading</h2>
<p>The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.
  The quick brown fox jumps over the lazy dog.</p>
<p>The <b>quick</b> brown fox jumps over the lazy dog.</p>
</body>
</html>
```
## Technologies Used
- Python
- Regular Expressions
- HTML/CSS/JS
