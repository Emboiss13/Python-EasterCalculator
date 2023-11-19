#!/usr/bin/python3
import cgi #, cgitb
import datetime
form = cgi.FieldStorage()

# This defines how we want to right the date (order)

def format_numerically(date):
    return date.strftime("%d/%m/%Y")

# This is how we define the extra mark verboselly character

def get_extramark(date):
    if date.day == 1 or date.day == 21 or date.day == 31:
        return "st"
    if date.day == 2 or date.day == 22:
        return "nd"
    if date.day == 3 or date.day == 23:
        return "rd"
    return "th"

# We will now define what happens when we select the radial button for the other options

def format_verbosely(date):
    extramark = get_extramark(date)
    return date.strftime(f"%d<sup>{extramark}</sup> %B %Y")

def format_both(date):
    f_sub = format_numerically(date)
    f_verb = format_verbosely(date)
    return f"{f_sub}<br>{f_verb}"

def format_option(date,choice_str):
    if choice_str == "numerically":
        return format_numerically(date)
    if choice_str == "verbosely":
        return format_verbosely(date)
    if choice_str == "both":
        return format_both(date)
    raise Exception("Invalid choice string")

# Here we define the easter function

def Easter(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    return datetime.date(year=y, month=n, day=p)

def html_error_page(error_str):
    return f"""<!DOCTYPE html>
<html lang="en">
        <head>
                <meta charset="utf-8">
                <title>Results Page</title>
                <link rel="stylesheet" href="../easter-styles.css" />
        </head>
        <body>
                <div id="error-box">
                        <p>{error_str}</p>
                        <p>Click <a href="../easter.html">here</a> to return to the form</p>
                </div>
        </body>
</html>
"""

# Special message for user
username = form.getvalue('username')
year_str = form.getvalue('year')
year = int(year_str)
desired_format = form.getvalue("format")
easter_date = Easter(year)
txt = format_option(easter_date, desired_format)

print(f"""Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Calculate easter dates</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../website.style.css"
  </head>
  <body>
    <header>
      <div class="bannercalculator">
          <div class="navbar">
            <img src="../logo.png" class="logo">
            <ul>
              <li><a href="../index.html">Home</a></li>
              <li><a href="../python.html">Python</a></li>
              <li><a href="../discusion.html">Discussion</a></li>
              <li><a href="../news.html">News</a></li>
              <li><a href="../eastercalculator.html">Calculator</a></li>
              <li><a href="../references.html">Reference</a></li>
            </ul>
          </div>

          <div class="eastercalculator-image">
            <a href="https://www.primarygames.com/holidays/easter/games/bunnyjumpcarrots/">
              <img src="../easterimage1.png" class="easterimage1">
            </a>
          </div>


          <div class="textbox-form">

            <h1 class="Title">The calculation was succesful:</h1>
            <br></br>
            <h2>Dear {username} ... In the year {year}, Easter Sunday will fall on:</h2>
            <blockquote>{txt}</blockquote>
            <br></br>
            </div>
            </form>
          </div>
        </div>
      </header>
  </body>
</html>""")