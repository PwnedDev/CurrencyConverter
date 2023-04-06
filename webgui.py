#!/usr/bin/env python3
import cherrypy
from main import CurrencyConverter
class CurrencyConverterGUI(object):
  @cherrypy.expose
  def index(self):
    return """<html>
          <head>
            <style type='text/css'>
              body {
                text-align: center;
              }

              form { box-sizing: border-box; padding: 10px; margin:20px 0; border:2px solid #eee; box-shadow:0 0 15px 4px rgba(0,0,0,0.06); border-radius:10px; width:100%; height: 100%; display: inline-block;}
              input, textarea {
              font-family:inherit;
              font-size: inherit;
              padding: 10px;
              margin:10px;
              }
              button {

              appearance:none;
              -webkit-appearance:none;

              /* usual styles */
              padding:10px;
              border:none;
              background-color:#3F51B5;
              color:#fff;
              font-weight:600;
              border-radius:5px;
              width:100%;

              }
                  </style>
          </head>
          <body>
            <form method="get" action="send_parameters">
              <input type="text" value="EUR" name="from_cur" />
              <input type="text" value="USD" name="to_cur" / >
              <input type="text" value="100" name="amount" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""
  @cherrypy.expose
  def send_parameters(self, from_cur, to_cur, amount):
    converter = CurrencyConverter()
    converted = converter.convert(from_cur, to_cur, int(amount))
    return str(converted)
if __name__ == '__main__':
  cherrypy.quickstart(CurrencyConverterGUI())
