# from pytube import Playlist

# def download_playlist(playlist_url):
#     playlist = Playlist(playlist_url)
#     for video in playlist.videos:
#         stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#         stream.download()



# playlist_url = 'https://youtu.be/NB8OceGZGjA?si=3-CJYNp6zm_8jALm'
# download_playlist(playlist_url)



# second script




# from pytube import Playlist, YouTube

# def download_video(video_url):
#     video = YouTube(video_url)
#     stream = video.streams.filter(progressive=True).get_highest_resolution()
#     stream.download()

# def download_playlist(playlist_url):
#     playlist = Playlist(playlist_url)
#     for video in playlist.videos:
#         download_video(video.watch_url)

# def download_content(url):
#     if 'playlist' in url:
#         download_playlist(url)
#     else:
#         download_video(url)

# url = 'https://youtu.be/NB8OceGZGjA?si=3-CJYNp6zm_8jALm'  # Replace with the URL of the video or playlist you want to download
# download_content(url)








# third script








from pytube import Playlist

# URL of the YouTube playlist
playlist_url = "https://youtube.com/playlist?list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&si=zUYbceHR_kYVvVE3"

# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate over each video in the playlist
for video in playlist.videos:
    # Get streams with 4K resolution if available, else get the highest resolution stream
    stream = video.streams.filter(res="1080p", progressive=True).first() or video.streams.get_highest_resolution()
    
    # Download the video
    print(f"Downloading: {video.title}")
    stream.download()
    
print("Download completed!")
