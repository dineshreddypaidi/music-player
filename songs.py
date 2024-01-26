import os
import fnmatch

class Songs:
    def FindSong(pattern,path):
        songpath = []                
        for root, dirs, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                if fnmatch.fnmatch(name, pattern) and os.path.getsize(file_path) > 1024 * 1024:
                    songpath.append(file_path)
        return songpath
   
    def SongName(pattern,path):
        namees = []                
        for root, dirs, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                if fnmatch.fnmatch(name, pattern) and os.path.getsize(file_path) > 1024 * 1024:
                    namees.append(name)
        return namees
           
    songpath = FindSong("*.mp3","/")
    songname = SongName("*.mp3","/")


if __name__ == "__main__" :
       Songs()