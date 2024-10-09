import re
class Phone_Number_extractor():
    def __init__(self):
        self.phone_numbers = []
        
    def extract(self, entries):
        #this is my regex pattern
        pattern = r'07\d{9}'
    

        # Search for the pattern in the diary content
        for item in entries:
            match = re.search(pattern, item.content)
            if match:
                self.phone_numbers.append(match.group(0))
                
        return self.phone_numbers