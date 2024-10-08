
class Diary_Entry():
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def count_content(self):
        return len(self.content.split(" "))