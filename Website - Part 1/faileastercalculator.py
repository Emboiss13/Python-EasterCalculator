#!/usr/bin/python3
import cgi #, cgitb
import datetime
form = cgi.FieldStorage()

y = form.getvalue('year')
username = form.getvalue('username')
type = form.getvalue('format')

def Easternum(y):
    
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

def Eastermonth(y):
    
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
    return datetime.strptime(y, n, p, "%Y/%b/%w")



# Test values
# y = '2022'
# username = 'Giuly'
# type = 'both'


if type == 'numerically': 
    print('content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('  <head>')
    print('    <meta charset="utf-8">')
    print('    <title>Calculate easter dates</title>')
    print('    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    print('    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">')
    print('    <link rel="stylesheet" href="../website.style.css"')
    print('  </head>')
    print('  <body>')
    print('    <header>')
    print('      <div class="bannercalculator">')
    print('          <div class="navbar">')
    print('            <img src="logo.png" class="logo">')
    print('            <ul>')
    print('              <li><a href="index.html">Home</a></li>')
    print('              <li><a href="python.html">Python</a></li>')
    print('              <li><a href="discusion.html">Discussion</a></li>')
    print('              <li><a href="news.html">News</a></li>')
    print('              <li><a href="eastercalculator.html">Calculator</a></li>')
    print('              <li><a href="references.html">Reference</a></li>')
    print('            </ul>')
    print('          </div>')
    print('          <div class="textbox-form">')
    print(('            <h1 class="Title">'), ('Dear'), (username), ('The calculation was succesful</h1>'))
    print('            <br></br>')
    print('            <p>Easter will fall on: </p>')
    print('            <br></br>')
    print(('            <p>'),(Easternum(int(y))),('</p>'))
    print('          </div>')
    print('        </div>')
    print('      </header>')
    print('  </body>')
    print('</html>')
elif type == 'verbose':
    print('content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('  <head>')
    print('    <meta charset="utf-8">')
    print('    <title>Calculate easter dates</title>')
    print('    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    print('    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">')
    print('    <link rel="stylesheet" href="../website.style.css"')
    print('  </head>')
    print('  <body>')
    print('    <header>')
    print('      <div class="bannercalculator">')
    print('          <div class="navbar">')
    print('            <img src="logo.png" class="logo">')
    print('            <ul>')
    print('              <li><a href="index.html">Home</a></li>')
    print('              <li><a href="python.html">Python</a></li>')
    print('              <li><a href="discusion.html">Discussion</a></li>')
    print('              <li><a href="news.html">News</a></li>')
    print('              <li><a href="eastercalculator.html">Calculator</a></li>')
    print('              <li><a href="references.html">Reference</a></li>')
    print('            </ul>')
    print('          </div>')
    print('          <div class="textbox-form">')
    print(('            <h1 class="Title">'), ('Dear'), (username), ('The calculation was succesful</h1>'))
    print('            <br></br>')
    print('            <p>Easter will fall on: </p>')
    print('            <br></br>')
    print(('            <p>'),(Eastermonth(int(y))),('</p>'))
    print('          </div>')
    print('        </div>')
    print('      </header>')
    print('  </body>')
    print('</html>')    
else:
    print('content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('  <head>')
    print('    <meta charset="utf-8">')
    print('    <title>Calculate easter dates</title>')
    print('    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    print('    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">')
    print('    <link rel="stylesheet" href="../website.style.css"')
    print('  </head>')
    print('  <body>')
    print('    <header>')
    print('      <div class="bannercalculator">')
    print('          <div class="navbar">')
    print('            <img src="logo.png" class="logo">')
    print('            <ul>')
    print('              <li><a href="index.html">Home</a></li>')
    print('              <li><a href="python.html">Python</a></li>')
    print('              <li><a href="discusion.html">Discussion</a></li>')
    print('              <li><a href="news.html">News</a></li>')
    print('              <li><a href="eastercalculator.html">Calculator</a></li>')
    print('              <li><a href="references.html">Reference</a></li>')
    print('            </ul>')
    print('          </div>')
    print('          <div class="textbox-form">')
    print(('            <h1 class="Title">'), ('Dear'), (username), ('The calculation was succesful</h1>'))
    print('            <br></br>')
    print('            <p>Easter will fall on: </p>')
    print('            <br></br>')
    print(('            <p>'),(Eastermonth(int(y))),(Easternum(int(y))),('</p>'))
    print('          </div>')
    print('        </div>')
    print('      </header>')
    print('  </body>')
    print('</html>')

