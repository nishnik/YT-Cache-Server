# YT-Cache-Server

## Instructions to run

* Clone this repository and install the requirements.

* cd into the repo and do `python server.py --host 127.0.0.2 --port 8080` (or any other desired host and port)

* Also run `python3 -m http.server --port 8000`. This would run a server at `0.0.0.0:8000/`

* Place an MP4 file (named MY_VIDEO.mp4 for example) in the same directory. You can access it at `0.0.0.0:8000/MY_VIDEO.mp4`.

* Go to a youtube video and do the following in the console :
	
	player.innerHTML = "<video width='640' height='360' id='my-video' class='video-js' controls preload='auto' width='640' height='264' data-setup='{ 'autoplay': true}'><source src='http://0.0.0.0:8000/MYVIDEO.mp4/MY_VIDEO.mp4' type='video/mp4'></video>";

* This would run the video in place of the youtube video.