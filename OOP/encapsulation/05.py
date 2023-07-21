# What will be the output of the following code? Why?
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
video_one.play
print(video_one.views)