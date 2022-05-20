#German sound_files / sound_files mit deutschen Audios
# import random
import board, time, pygame, digitalio
#import tkinter.filedialog as filedialog

from adafruit_debouncer import Debouncer


# First button set up Button Next
button1 = digitalio.DigitalInOut(board.D5) # port D5 du grove
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP
button_input1 = Debouncer(button1) # Push the button

#Second button set up Button Previous
button2 = digitalio.DigitalInOut(board.D18) # port D18
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP
button_input2 = Debouncer(button2)

#Third button set up Button Pause
button3 = digitalio.DigitalInOut(board.D16) # port D16
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP
button_input3 = Debouncer(button3)


#files setup GERMAN AUDIOS
path = "/home/pi/audiostxt/eng/"

sound_files = ['sound0.mp3', 'sound1.mp3','sound7.mp3', 'sound30.mp3']


#pygame setup installation
pygame.mixer.init()
music = pygame.mixer.music
speaker_volume = 0.5 # Le volume
music.set_volume(speaker_volume)

sound_number = 0 
total_sounds = 41 
clock = pygame.time.Clock() 
music_playing = True

played_at = None
#Loop
inactive_ticks = 0


#Condition pour lancer un sound dès le démarrage !!!
i = 0 
premier = True
deuxieme = True



SONG_FINISHED = pygame.USEREVENT + 1
# When a song is finished, pygame will add the
# SONG_FINISHED event to the event queue.
pygame.mixer.music.set_endevent(SONG_FINISHED)
# Load and play the first song.

#if music.get_busy() == False:
 

music.load(path + "sound7.mp3".format(sound_number))
pygame.mixer.music.play(-1)
      
while True:   

    button_input1.update() == True
    button_input2.update() == True
    button_input3.update() == True    
    if button_input1.fell: # Button next D5         
            sound_number +=1
            print("NextBtn: sound{}.mp3".format(sound_number))
            music.load(path + "sound{}.mp3".format(sound_number))
            pygame.mixer.music.play(-1)

            if sound_number >= total_sounds:
                   sound_number =0  
            

    if button_input2.fell: #Button Previous D18
            sound_number -=1
            print("PrevBtn: sound{}.mp3".format(sound_number))
            music.load(path + "sound{}.mp3".format(sound_number))
            pygame.mixer.music.play(-1)    
        
            if sound_number >= total_sounds:
                  sound_number = 0      

               
    if button_input3.fell: #Button Pause D16 
            if music_playing:
                print("PAUSE_btn3: sound{}.mp3".format(sound_number))
                pygame.mixer.music.pause()
                music_playing = False
            else:
                print("UNPAUSE_btn3: sound{}.mp3".format(sound_number))
                pygame.mixer.music.unpause()
                music_playing = True


