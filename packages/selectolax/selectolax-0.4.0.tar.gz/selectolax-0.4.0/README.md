![selectolax logo](docs/logo.png)

---

[![PyPI version](https://img.shields.io/pypi/v/selectolax.svg)](https://pypi.python.org/pypi/selectolax)

A fast HTML5 parser with CSS selectors using [Modest](https://github.com/lexborisov/Modest/) and [Lexbor](https://github.com/lexbor/lexbor) engines.

## Installation

From PyPI using pip:

```bash
pip install selectolax
```

If installation fails due to compilation errors, you may need to install [Cython](https://github.com/cython/cython):

```bash
pip install selectolax[cython]
```

This usually happens when you try to install an outdated version of selectolax on a newer version of Python.

Development version from GitHub:

```bash
git clone --recursive  https://github.com/rushter/selectolax
cd selectolax
pip install -r requirements_dev.txt
python setup.py install
```

How to compile selectolax while developing:

```bash
make clean
make dev
```

## Basic examples

Here are some basic examples to get you started with selectolax:

Parsing HTML and extracting text:

```python
In [1]: from selectolax.lexbor import LexborHTMLParser
   ...:
   ...: html = """
   ...: <h1 id="title" data-updated="20201101">Hi there</h1>
   ...: <div class="post">Lorem Ipsum is simply dummy text of the printing and typesetting industry. </div>
   ...: <div class="post">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
   ...: """
   ...: tree = LexborHTMLParser(html)

In [2]: tree.css_first('h1#title').text()
Out[2]: 'Hi there'

In [3]: tree.css_first('h1#title').attributes
Out[3]: {'id': 'title', 'data-updated': '20201101'}

In [4]: [node.text() for node in tree.css('.post')]
Out[4]:
['Lorem Ipsum is simply dummy text of the printing and typesetting industry. ',
 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.']
```

### Using advanced CSS selectors

```python
In [1]: html = "<div><p id=p1><p id=p2><p id=p3><a>link</a><p id=p4><p id=p5>text<p id=p6></div>"
   ...: selector = "div > :nth-child(2n+1):not(:has(a))"

In [2]: for node in LexborHTMLParser(html).css(selector):
   ...:     print(node.attributes, node.text(), node.tag)
   ...:     print(node.parent.tag)
   ...:     print(node.html)
   ...:
{'id': 'p1'}  p
div
<p id="p1"></p>
{'id': 'p5'} text p
div
<p id="p5">text</p>
```

#### Using `lexbor-contains` CSS pseudo-class to match text

```python
from selectolax.lexbor import LexborHTMLParser
html = "<div><p>hello </p><p id='main'>lexbor is AwesOme</p></div>"
parser = LexborHTMLParser(html)
# Case-insensitive search
results = parser.css('p:lexbor-contains("awesome" i)')
# Case-sensitive search
results = parser.css('p:lexbor-contains("AwesOme")')
assert len(results) == 1
assert results[0].text() == "lexbor is AwesOme"
```

* [Detailed overview](https://github.com/rushter/selectolax/blob/master/examples/walkthrough.ipynb)

### Available backends

Selectolax supports two backends: `Modest` and `Lexbor`. By default, all examples use the Modest backend.
Most of the features between backends are almost identical, but there are still some differences.

As of 2024, the preferred backend is `Lexbor`. The `Modest` backend is still available for compatibility reasons
and the underlying C library that selectolax uses is not maintained anymore.

To use `lexbor`, just import the parser and use it in the similar way to the `HTMLParser`.

```python
In [1]: from selectolax.lexbor import LexborHTMLParser

In [2]: html = """
   ...: <title>Hi there</title>
   ...: <div id="updated">2021-08-15</div>
   ...: """

In [3]: parser = LexborHTMLParser(html)
In [4]: parser.root.css_first("#updated").text()
Out[4]: '2021-08-15'
```

## Simple Benchmark

* Extract title, links, scripts and a meta tag from main pages of top 754 domains. See `examples/benchmark.py` for more information.

| Package                       | Time      |
|-------------------------------|-----------|
| Beautiful Soup (html.parser)  | 61.02 sec.|
| lxml / Beautiful Soup (lxml)  | 9.09 sec. |
| html5_parser                  | 16.10 sec.|
| selectolax (Modest)           | 2.94 sec. |
| selectolax (Lexbor)           | 2.39 sec. |

## Links

* [selectolax API reference and examples](https://selectolax.readthedocs.io/en/latest/index.html)
* [Video introduction to web scraping using selectolax](https://youtu.be/HpRsfpPuUzE)
* [How to Scrape 7k Products with Python using selectolax and httpx](https://www.youtube.com/watch?v=XpGvq755J2U)
* [Modest introduction](https://lexborisov.github.io/Modest/)
* [Modest benchmark](https://lexborisov.github.io/benchmark-html-parsers/)
* [Python benchmark](https://rushter.com/blog/python-fast-html-parser/)
* [Another Python benchmark](https://www.peterbe.com/plog/selectolax-or-pyquery)
* [Universal interface to lxml and selectolax](https://github.com/lorien/domselect)

## License

* Modest engine — [LGPL2.1](https://github.com/lexborisov/Modest/blob/master/LICENSE)
* lexbor engine — [Apache-2.0 license](https://github.com/lexbor/lexbor?tab=Apache-2.0-1-ov-file#readme)
* selectolax - [MIT](https://github.com/rushter/selectolax/blob/master/LICENSE)
