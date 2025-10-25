def tienShip(a, b):
    c = 0
    if ( a <= 0 ):
     return "Đầu vào không hợp lệ"
    if ( a > 10):
      return "Quá quãng đường quy định"
    if ( b == "no"):
       if (a > 0 and a < 5):
        c = 4000*a
       else:
         c = 20000
    elif ( b == "normal"):
      if ( a > 0 and a < 5):
        c = 4000*a -5000
        if ( c <= 0):
          return 0
      else:
        c = 20000 - 5000
    elif ( b == "freeship"):
      c = 0
    else:
      return "Đầu vào không hợp lệ"
    return c
    

    
