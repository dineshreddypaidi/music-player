import os
import fnmatch
import os

class Songs:
    def FindSong(patterns,paths):
        print("searching for songs in the OS")
        songpath = []  
        namees = []    
        for pattern in patterns:
            for path in paths:
                for root, dirs, files in os.walk(path):
                    for name in files:
                        file_path = os.path.join(root, name)
                        if fnmatch.fnmatch(name, pattern) and os.path.getsize(file_path) > 1024 * 1024:
                            songpath.append(file_path)
                            namees.append(name)
        print("searching completed..")
        return songpath,namees
    
    def is_empty():
        return True if len(Songs.songpath) == 0 else False
    
    songextensions = ["*.mp3",]
    
    osname = os.name
    if osname == 'nt':
        searchpaths = ["C:/Users","D:/","E:/"]     
    if osname == 'posix':
        searchpaths = ["/","/usr"]   
    
    songpath, songname  = FindSong(songextensions,searchpaths)
    
if __name__ == "__main__" :
       Songs()