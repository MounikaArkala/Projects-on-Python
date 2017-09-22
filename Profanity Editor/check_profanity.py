import urllib
def read_text():
    quotes=open("C:\Users\manishreddy\Desktop\udacity\lesson 11\Use classes- Profanity Editor Videos\profanity_sample_test.txt")
    contents=quotes.read()
    print(contents)
    check_profanity(contents)
    quotes.close()
def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    print(output)
    connection.close()
read_text()
