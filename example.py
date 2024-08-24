from rencli import prinx, cuscol, color_char
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

def matrcli():
    cuscol(lis=['2','\u001b[37m','1','\u001b[30;1m','0','\u001b[34m'])
    local_player = [[1, 2, 0], [0, 0, 1], [1, 2, 0]]
    data_temp_2 = ""
    for r in range(len(local_player)):
        for i in local_player[r]:
            data_temp_2 += color_char(str(i),shadow=0)
        color_char("ę")
        data_temp_2 += "\n"
    print(data_temp_2)

welcome()
matrcli()