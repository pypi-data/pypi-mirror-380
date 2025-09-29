# Freaky Funky Fonts Middleware (Django)

For when you feel the funk that freaks you fonts

## What it this?

Freaky Funky Fonts Middleware is essentially a Django “font chaos” middleware package with configurable behaviour.

It intercespts the html of Djangos reponses

## Usage

- Install the package
- Apply the middleare in your Django project settings as middleare
- (Optional but recommended) Configure in your `freakyfunkyfonts.toml` (or `.ini` for versions before python 3.11)


### Installing

```bash

```

### Applying

In the project settings

```py
MIDDLEWARE = [
    # ...
    "freakyfunkyfonts.middleware.FunkyFontMiddleware",
]
```

### Configs

Example: 

```toml
[fonts]
# List of fonts to cycle through
pool = [
  "Times New Roman",
  "Georgia",
  "Merriweather",
  "Lora"
]

[inject]
# Extra tags to inject into <head> (Like a link tag to google fonts)
# More than one tag can be applied, just append to the list
# Make sure that the fonts in the pool are convered
tags = [
  '<link href="https://fonts.googleapis.com/css2?family=Merriweather&family=Lora&display=swap" rel="stylesheet">'
]

[behaviour]
# HTML tags to skip completely
skip_tags = ["script", "style", "noscript", "title"]
```

## Dev

### Installing

```bash
pip install -e .
```