from rencli import prinx, cuscol, color_char, ren_colz, prinx2, move_2list

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
  cuscol(lis=['2','\u001b[37m','1','\u001b[30;1m','0','\u001b[34m'], fp2=500)
  test_list = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
  test_list_back = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
  prinx2(d_list(test_list, test_list_back), refs=True)
  for i in range(2):
    prinx2(d_list(move_2list(test_list, 1, 1), test_list_back))
  for i in range(1):
    prinx2(d_list(move_2list(test_list, 1, 2), test_list_back))
  for i in range(2):
    prinx2(d_list(move_2list(test_list, 1, 4), test_list_back))

matr_move()
welcome()
