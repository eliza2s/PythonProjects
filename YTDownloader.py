from pytube import YouTube

try:
    link = input("Enter the YouTube URL: ")
    video = YouTube(link)
    print("Title :", video.title)
    print("Views :", video.views)
    yd = video.streams.get_highest_resolution()
    yd.download()
    print("Download is completed")


except Exception as error:
    print("An error occurred:", str(error))