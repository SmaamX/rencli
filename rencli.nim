import std/[sequtils, strutils, terminal, os, times]

#terminal.eraseScreen()
var cust = @["1", "\x1B[30;1m", "\x1B[40;1m", "2", "\x1B[31;1m", "\x1B[41;1m"]
var fp = 200
var backlog = ""
var bol = false
var mand = true

proc refs(dela: int = 1) =
  sleep(dela)
  if not mand:
   echo "\033[2K\r"
  else:
   try:
     terminal.eraseScreen()
   except:
     discard

proc addLists(list1, list2: seq[string]): seq[string] =
  var intlist1: seq[int] = @[]
  var intlist2: seq[int] = @[]
  for i in list1:
    intlist1.add(parseInt(i))
  for i in list2:
    intlist2.add(parseInt(i))
  var outlist: seq[int] = zip(intlist1, intlist2).mapIt(it[0] + it[1])
  var outlist_str: seq[string] = @[]
  for i in outlist:
    outlist_str.add(intToStr(i))
  outlist_str

proc color_char(char: string, shadow: int = 0): string =
  var vj: string  
  case shadow  
  of 0: vj = "█"  
  of 1: vj = "▓"  
  of 2: vj = "▒"  
  of 3: vj = "░"  
  else:  
   echo "\x1B[31mBSConf: ", shadow
   quit()
  if char == "-2":
    return  "\x1B[0m\n"
  elif char == "-1":
    refs(fp); return "\x1B[0m\r"
  elif char in cust:
    backlog = cust[cust.find(char)+2]
    return "\x1B[0m" & (if shadow == 0: cust[cust.find(char)+2] else: "") & cust[cust.find(char)+1] & vj & "\x1B[0m"
  else:
    if backlog != "":
      return "\x1B[0m" & "\x1B[1m" & backlog & cust[cust.find(char)+2] & char & "\x1B[0m"
    else:
      return "\x1B[0m" & "\x1B[1m" & "\x1B[7m" & cust[cust.find(char)+2] & char & "\x1B[0m"

proc colz(chars: auto, shadow: int = 0, mand: bool = false, lfix: bool = false): string =
  var check_list: seq[string]
  if lfix:  
   for i in chars:  
    if i != "0":
     check_list.add(i)  
    else:  
      check_list = check_list[0 ..< check_list.high]  
      check_list.add(i)  
   try:  
    return check_list.mapIt(color_char(it, shadow)).join()  
   except IOError:
    echo "\x1B[31mNanType"  
    quit()  
  else:  
   try:  
    return chars.mapIt(color_char(it, shadow)).join()  
   except IOError:
    echo "\x1B[31mNanType"  
    quit()  

proc ren_colz(local: seq[seq[auto]], refs: bool = false, shadow: int = 0): string =
  var data_temp_2 = ""  
  for r in local:  
   for i in r:  
    data_temp_2.add(color_char(i, shadow))  
   data_temp_2.add("\n")  
  if refs:  
   data_temp_2.add(color_char("-2"))
   return data_temp_2

proc echx(import_l: seq[seq[auto]], refs = true, sha = 0) =
  echo ren_colz(import_l, refs = refs, shadow = sha)

proc lmove(import_l: var seq[string], mmod: int, targ: string = "0"): seq[string] =
  if mmod == 0:
    if targ == "0":
      let eend = import_l[0]
      import_l.delete(0)
      import_l.add(eend)
    else:
      if import_l[0] == targ:
        return import_l
      else:
        let eend = import_l[0]
        import_l.delete(0)
        import_l.add(eend)
  elif mmod == 180:
    if targ == "0":
      let eend = import_l[len(import_l)-1]
      import_l.delete(len(import_l)-1)
      import_l.insert(eend,0)
    else:
      if import_l[len(import_l)-1] == targ:
        return import_l
      else:
        let eend = import_l[len(import_l)-1]
        import_l.delete(len(import_l)-1)
        import_l.insert(eend,0)
  import_l

proc actouch(import_l: seq[string], import_l2: seq[string], lmove: int, main_targ: string, sec_targ: string): bool =
  if import_l.find(main_targ)+lmove == import_l2.find(sec_targ):
    return true
  else:
    return false

proc actouch(import_l: seq[seq[string]], import_l2: seq[seq[string]], lmove: int, main_targ: string, sec_targ: string): bool =
  for i in import_l:
    if main_targ in i:

      if i.find(main_targ) == import_l2[import_l.find(i)+lmove].find(sec_targ):
        return true
      else:
        return false

proc lmove(import_l: var seq[seq[string]], mmod: int, targ: string = "0"): seq[seq[string]] =
  if mmod == 0:
    for i in import_l:
      if targ in i:
        var import_ll = import_l[import_l.find(i)]
        if targ == "0":
          let eend = import_ll[0]
          import_ll.delete(0)
          import_ll.add(eend)
        else:
          if targ in import_ll[0]:
            return import_l
          else:
            let eend = import_ll[0]
            import_ll.delete(0)
            import_ll.add(eend)
        let eend = import_l.find(i)
        import_l.delete(import_l.find(i))
        import_l.insert(import_ll, eend)
        return import_l
  if mmod == 180:
    for i in import_l:
      if targ in i:
        var import_ll = import_l[import_l.find(i)]
        if targ == "0":
          let eend = import_ll[len(import_ll)-1]
          import_ll.delete(len(import_ll)-1)
          import_ll.insert(eend,0)
        else:
          if targ in import_ll[len(import_l)-1]:
            return import_l
          else:
            let eend = import_ll[len(import_ll)-1]
            import_ll.delete(len(import_ll)-1)
            import_ll.insert(eend,0)
        let eend = import_l.find(i)
        import_l.delete(import_l.find(i))
        import_l.insert(import_ll, eend)
        return import_l
  if mmod == 270:
    if targ == "0":
      let eend = import_l[len(import_l)-1]
      import_l.delete(len(import_l)-1)
      import_l.insert(eend,0)
    else:
      if targ in import_l[len(import_l)-1]:
        return import_l
      else:
        let eend = import_l[len(import_l)-1]
        import_l.delete(len(import_l)-1)
        import_l.insert(eend,0)
  if mmod == 90:
    if targ == "0":
      let eend = import_l[0]
      import_l.delete(0)
      import_l.add(eend)
    else:
      if targ in import_l[0]:
        return import_l
      else:
        let eend = import_l[0]
        import_l.delete(0)
        import_l.add(eend)
  import_l

