# RenCLI
## Dynamic render (RCLI)
A simple module for image and animation outputs in CLI
+ color_char() - Takes a list of color codes and returns escape codes to print the colors
+ colz() - Calls color_char() to convert a string to colored text
+ chn() - check type x= input, typ=type(int,str,bool,list...)
+ neli() - returns a newline character
+ refs() - clears the console screen
+ random_noise() - Generates random colors
+ prinx() - sys.stdout.write(colz(image))
+ prinx2() - 2d outset
+ cuscol() - custom color, text color, etc.
  (cuscol(lis=['A','\033[93m',...]))

## Static render
+ image2rencli('test.png',250, show=False) - return image in CLI
+ imgx() - image2rencli but direct print
+ renweb() - import image from web (renweb('http://google.com/test.jpg',100,save='Test',dr=True))

## List manager (dynamic render)
+ d_list(list1,list2) - combine two list directly
+ move_2list(listin, ind, mod, spee=0, speel=1, emp=0, lback = [], final_rend=False) - move one object from list for example 1 in [[0,0,1],[0,0,0]]
