print("This program is going to analyse every instruction of your program"
      " and return ranges of values each variable of your program may contain")

ins_num = int(input("How many instructions does your program has: "))
init = 1
while init <= ins_num:
      print(f'Type the number {init} instruction: ')
      init = init + 1