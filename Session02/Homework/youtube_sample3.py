from youtube_dl import YoutubeDL

options = {
"format" : "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=NYdxOpDCiKY"])
