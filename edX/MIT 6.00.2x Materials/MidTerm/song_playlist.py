# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:52:28 2021

@author: ray-h
"""

# Return song list

# def song_playlist(songs, max_size):
#     """
#     songs: list of tuples, ('song_name', song_len, song_size)
#     max_size: float, maximum size of total songs that you can fit

#     Start with the song first in the 'songs' list, then pick the next 
#     song to be the one with the lowest file size not already picked, repeat

#     Returns: a list of a subset of songs fitting in 'max_size' in the order 
#              in which they were chosen.
#     """
    
    # playlist = []
    
    # # Key is index, value is ratio
    # ratiosDict = {}
    
    # songsCpy = songs.copy()
    
    # currSize = 0
    
    # if songsCpy[0][2] <= max_size:
    #     playlist.append(songs[0][0])
    #     currSize += songs[0][2]
    #     songsCpy.pop(0)
    
    # else:
    #     return playlist
    
    # for song in range(len(songsCpy)):
    #     ratiosDict[song] = songsCpy[song][1] / songsCpy[song][2]
    
    # while currSize <= max_size:
        
    #     currMaxRatio = 0
    #     for ratio in ratiosDict:
    #         if ratiosDict[ratio] >= currMaxRatio:
    #             index = ratio
    #             currMaxRatio = ratiosDict[ratio]
        
    #     # print(currMax)
    #     # ratiosDict.pop(index)
        
    #     if currSize + songsCpy[index][2] < max_size:
            
    #         ratiosDict.pop(index)
            
    #         currSize += songsCpy[index][2]
    #         playlist.append(songsCpy[index][0])
            
        
    #     else:
    #         break
            
    # return playlist
    
    
    
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
              in which they were chosen.
    """
    
    songsCpy = songs.copy()
    
    playlist = []
    
    currSize = 0
    
    # Check if first song fits
    if songsCpy[0][2] <= max_size:
        playlist.append(songsCpy[0][0])
        currSize += songsCpy[0][2]
        songsCpy.pop(0)
    
    else:
        return playlist
    
    while True:    
        
        # print("SongsCpy " + str(songsCpy))
        
        if songsCpy == []:
            break
        
        # print(songsCpy)
        # Setting minimum to first song's size
        currMin = songsCpy[0][2]
        
        index = 0
        
        for song in range(len(songsCpy)):
            if songsCpy[song][2] <= currMin:
                currMin = songsCpy[song][2]
                index = song
                # print(songsCpy[song])
            
        
        if currSize + songsCpy[index][2] <= max_size:
            currSize += songsCpy[index][2]
            playlist.append(songsCpy[index][0])
            songsCpy.pop(index)
            continue
        
        else:
            break
            
    return playlist
    

# max_size = 12.2
# songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

# print(song_playlist(songs, max_size))

# print(song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 20))

# print(song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 5.4))

# print(song_playlist([('z', 0.1, 0.1), ('a', 4.4, 4.0), ('b', 2.7, 1.2), ('cc', 3.5, 7.7), ('ddd', 5.1, 6.9)], 5.4))

# print(song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 12.3))