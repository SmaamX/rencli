from rencli import prinx, cuscol, color_char, ren_colz, prinx2, move_2list, d_list, check_vi
import keyboard, threading

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
  exit_ = 4
  item = 3
  wall = 2
  rate = 1
  null = 0
  cuscol(lis=[str(exit_+item), '\u001b[32;1m', str(exit_), '\u001b[35;1m', str(item), '\u001b[33;1m', str(wall), '\u001b[37m',str(rate), '\u001b[30;1m', str(null), '\u001b[34m'], fp2=0)
  test_list = [[0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 1, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0]]
  item_list = [[0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,3, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0]]
  exit_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 4, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0]]
  test_list_back = [[0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 2, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 2, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 0, 0, 0, 0, 0 ,0, 0], [0, 0, 2, 0, 0, 0, 0 ,0, 0]]
  prinx2(d_list(d_list(d_list(test_list, test_list_back), item_list), exit_list), refs=True)
  def refre():
    prinx2(d_list(d_list(d_list(test_list, test_list_back), item_list), exit_list), refs=True)
  def move1():
    if check_vi.check_r(test_list, test_list_back, rate, wall, False) and check_vi.check_r(test_list, exit_list, rate, exit_, False):
      if check_vi.check_r(test_list, item_list, rate, item, True):
        if check_vi.check_r(item_list, test_list_back, item, wall, False):
          move_2list(test_list, rate, 1)
          prinx2(d_list(d_list(d_list(move_2list(item_list, item, 1), test_list_back),test_list),exit_list))
          if check_vi.check_r(item_list, exit_list, item, exit_, True, r=0):
            prinx2(d_list(d_list(d_list(item_list, test_list_back),test_list),exit_list))
            print("You w0n");exit()
      else:
        prinx2(d_list(d_list(d_list(move_2list(test_list, rate, 1), test_list_back), item_list), exit_list), refs=True)
  def move2():
    if check_vi.check_u(test_list, test_list_back, rate, wall, False) and check_vi.check_u(test_list, exit_list, rate, exit_, False):
      if check_vi.check_u(test_list, item_list, rate, item, True):
        if check_vi.check_u(item_list, test_list_back, item, wall, False):
          move_2list(test_list, rate, 2)
          prinx2(d_list(d_list(d_list(move_2list(item_list, item, 2), test_list_back),test_list),exit_list))
          if check_vi.check_u(item_list, exit_list, item, exit_, True, r=0):
            prinx2(d_list(d_list(d_list(item_list, test_list_back),test_list),exit_list))
            print("You w0n");exit()
      else:
        prinx2(d_list(d_list(d_list(move_2list(test_list, rate, 2), test_list_back), item_list), exit_list), refs=True)
  def move4():
    if check_vi.check_d(test_list, test_list_back, rate, wall, False) and check_vi.check_d(test_list, exit_list, rate, exit_, False):
      if check_vi.check_d(test_list, item_list, rate, item, True):
        if check_vi.check_d(item_list, test_list_back, item, wall, False):
          move_2list(test_list, rate, 4)
          prinx2(d_list(d_list(d_list(move_2list(item_list, item, 4), test_list_back),test_list),exit_list))
          if check_vi.check_d(item_list, exit_list, item, exit_, True, r=0):
            prinx2(d_list(d_list(d_list(item_list, test_list_back),test_list),exit_list))
            print("You w0n");exit()
      else:
        prinx2(d_list(d_list(d_list(move_2list(test_list, rate, 4), test_list_back), item_list), exit_list), refs=True)
  def move3():
    if check_vi.check_l(test_list, test_list_back, rate, wall, False) and check_vi.check_l(test_list, exit_list, rate, exit_, False):
      if check_vi.check_l(test_list, item_list, rate, item, True):
        if check_vi.check_l(item_list, test_list_back, item, wall, False):
          move_2list(test_list, rate, 3)
          prinx2(d_list(d_list(d_list(move_2list(item_list, item, 3), test_list_back),test_list),exit_list))
          if check_vi.check_l(item_list, exit_list, item, exit_, True, r=0):
            prinx2(d_list(d_list(d_list(item_list, test_list_back),test_list),exit_list))
            print("You w0n");exit()
      else:
        prinx2(d_list(d_list(d_list(move_2list(test_list, rate, 3), test_list_back), item_list), exit_list), refs=True)
  keyboard.add_hotkey("w",move2)
  keyboard.add_hotkey("d",move1)
  keyboard.add_hotkey("a",move3)
  keyboard.add_hotkey("s",move4)
  tref = threading.Thread(target=refre)
  tref.start()
  tref.join()
  keyboard.wait()
matr_move()
