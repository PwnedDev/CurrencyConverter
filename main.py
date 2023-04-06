#!/usr/bin/env python3
import requests
import sys
url = "https://api.exchangerate.host/latest"

class CurrencyConverter():
  def __init__(self):
    self.url = url
    self.data = requests.get(url).json()
    self.currencies = self.data['rates']

  def convert(self, from_c, to_c, amount):
    self.newamount = amount
    
    if from_c != "EUR":
      self.newamount = amount / self.currencies[from_c]

    self.newamount = self.newamount * self.currencies[to_c]
    return round(self.newamount, 4)

if __name__ == '__main__':
  converter = CurrencyConverter()
  if(len(sys.argv)<3):
    print("USAGE: <From_C> <To_C> <amount>")
  else:
    print(converter.convert(sys.argv[1], sys.argv[2], int(sys.argv[3])))

      
