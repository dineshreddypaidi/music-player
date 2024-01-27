import os
import fnmatch

class Songs:
    def FindSong(patterns,paths):
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
        return songpath,namees
        
    songextensions = ["*.mp3","*.m4a"]
    searchpaths = ["C:/Users","D:/","E:/"]
    
    songpath, songname  = FindSong(songextensions,searchpaths)

if __name__ == "__main__" :
       Songs()    