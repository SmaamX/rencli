from rencli import prinx, cuscol, color_char, ren_colz, prinx2, move_2list, d_list, check_r, check_l, check_d, check_u
import keyboard

def welcome():
  cuscol(fp2=2000)
  prinx(((("Ą"*10)+"ŀ")*4)+"ę")
  welcome = "welcome"
  prinx((((("Ą"*(10-len(welcome)-2%len(welcome)))+welcome+("Ą"*(10-len(welcome)-2%len(welcome))))+"ŀ")*4)+"ę",lfix=False) #str in center
  prinx(((("Ą"*10)+"ŀ")*4)+"ę")
  cuscol(fp2=500)
  def anim_1(a_obj,b_obj,sha=0):
    e = 10;v = 0
    for i in range(11):
      prinx(((((a_obj*e)+(b_obj*v))+"ŀ")*4)+"ę")
      e -= 1;v += 1
  anim_1("Ą","¦")
  anim_1("¦","¶",sha=1)
  anim_1("¶","¸",sha=2)

def matr_move():
  cuscol(lis=['4', '\u001b[33;1m', '3', '\u001b[33;1m', '2','\u001b[37m','1','\u001b[30;1m','0','\u001b[34m'], fp2=500)
  test_list = [[0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 1, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0]]
  item_list = [[0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,3, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0]]
  test_list_back = [[0, 0, 2, 0, 0, 0, 0 ,0, 0], [0, 0, 2, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 2, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0]]
  prinx2(d_list((d_list(test_list, test_list_back)), item_list), refs=True)
  item = 3
  wall = 2
  rate = 1
  def move1():
    if check_r(test_list, test_list_back, rate, wall, False):
      if check_r(test_list, item_list, rate, item, True):
        prinx2(d_list(d_list(move_2list(test_list, rate, 1), test_list_back),item_list))
        print("You w0n");exit()
      else:
        prinx2(d_list(d_list(move_2list(test_list, rate, 1), test_list_back),item_list))
  def move2():
    if check_u(test_list, test_list_back, rate, wall, False):
      if check_u(test_list, item_list, rate, item, True):
        prinx2(d_list(d_list(move_2list(test_list, rate, 2), test_list_back),item_list))
        print("You w0n");exit()
      else:
        prinx2(d_list(d_list(move_2list(test_list, rate, 2), test_list_back),item_list))
  def move4():
    if check_d(test_list, test_list_back, rate, wall, False):
      if check_d(test_list, item_list, rate, item, True):
        prinx2(d_list(d_list(move_2list(test_list, rate, 4), test_list_back),item_list))
        print("You w0n");exit()
      else:
        prinx2(d_list(d_list(move_2list(test_list, rate, 4), test_list_back),item_list))
  def move3():
    if check_l(test_list, test_list_back, rate, wall, False):
      if check_l(test_list, item_list, rate, item, True):
        prinx2(d_list(d_list(move_2list(test_list, rate, 3), test_list_back),item_list))
        print("You w0n");exit()
      else:
        prinx2(d_list(d_list(move_2list(test_list, rate, 3), test_list_back),item_list))
  keyboard.add_hotkey("w",move2)
  keyboard.add_hotkey("d",move1)
  keyboard.add_hotkey("a",move3)
  keyboard.add_hotkey("s",move4)
  keyboard.wait()

matr_move()
