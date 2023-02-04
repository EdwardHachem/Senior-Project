
#this will pull mp4 into the current directory based on input link
from pytube import YouTube
user_in = input("enter link: ")
yt = YouTube(user_in)
stream = yt.streams.get_by_itag(22)
stream.download()
