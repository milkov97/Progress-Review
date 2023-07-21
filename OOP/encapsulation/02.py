class Video:
    def __init__(self):
        self._views = 0

    @property
    def views(self):
        return self._views

    def play(self):
        self._views += 1
        return self.views
    

video_one = Video()
video_two = Video()
video_one.play()
video_two.play()
video_two.play()
print(video_one.views)
print(video_two.views)