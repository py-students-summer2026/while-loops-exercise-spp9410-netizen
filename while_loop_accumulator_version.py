def get_starting_number():
    
    while True:
       response = input("How many bottles of beer on the wall? ")

       if response.isdigit() and int(response) >= 1:
        return int(response)
       

def sing(start):
   i = start
   while i >= 1:
      if i == 1:
         i_phase = "1 bottle"
      else:
         i_phase = str(i) + " bottles"
      

      remaining = i - 1
      if remaining == 0:
         remaining_p = 'no more bottles'
      elif remaining == 1:
         remaining_p = "1 bottle"
      else:
         remaining_p = str(remaining) + " bottles"
      
      if i == 1:
         action = "Take it down, pass it around"
      else:
         action = "Take one down, pass it around"
    
      print(f"{i_phase} of beer on the wall, {i_phase} of beer.")
      if remaining == 0:
         print(f"{action}, {remaining_p} of beer on the wall!")
      else:
         print(f"{action}, {remaining_p} of beer on the wall.")
      
      print()
      i = i - 1


   
   