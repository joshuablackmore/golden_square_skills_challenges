def make_snippet(str):
    my_lis = str.split(" ")
    if len(my_lis) > 5:
        return " ".join(my_lis) + f"..."
    else:
        return str
    
    
print(make_snippet('here is my test string all'))