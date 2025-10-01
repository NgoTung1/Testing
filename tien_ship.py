def tienShip(a, b):
    if ( a <= 0 ):
     return "Đầu vào không hợp lệ"
    if ( a > 10):
      return "Quá quãng đường quy định"
    if ( b == "no"):
       if (a > 0 and a < 5):
        return 4000*a
       if ( a >= 5 and a <= 10 ):
         return 20000
    if ( b == "normal"):
      if ( a > 0 and a < 5):
        c = 4000*a -5000
        if ( c <= 0):
          return 0
        return c
      if ( a >= 5 and a <= 10):
        return 20000 - 5000
    if ( b == "freeship"):
      return 0
    

    
