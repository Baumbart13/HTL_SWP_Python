from pytube import YouTube

#where to save
SAVE_PATH = "C:\\Users\\Baumbart13\\Desktop\\Christin" #to_do

#link of the video to be downloaded
link=["https://youtu.be/vXFXP6YfN3k",
	  "https://youtu.be/TCDt-c-uzyE"
	  ]
yt: YouTube = None

for i in link:
	try:

		# object creation using YouTube
		# which was imported in the beginning
		yt = YouTube(i)
	except:

		#to handle exception
		print("Connection Error")

		#filters out all the files with "mp4" extension
	mp3files = yt.streams.filter(type="audio", subtype="mp3", only_audio=True)

	# get the video with the extension and
	# resolution passed in the get() function
	ys = yt.streams.get_audio_only(subtype="mp3")
	try:
		# downloading the video
		ys.download(output_path=SAVE_PATH)
	except:
		print("Some Error!")
print('Task Completed!')
