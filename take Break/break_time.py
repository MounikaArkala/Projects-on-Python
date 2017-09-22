import webbrowser
import time
total_breaks=3
break_count=0
#ctime displays current time
print("This program started on"+time.ctime())

while(break_count<total_breaks):
#parameter value for sleep() will be insecs
      time.sleep(10)
      break_count=break_count+1
      webbrowser.open("http://www.youtube.com/watch? v=dQw4w9WgXcQ")
