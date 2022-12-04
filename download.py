from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

print("Title: ", yt.title)

print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('C:\Coding\Projects\python\Youtube Downloader\downloads')