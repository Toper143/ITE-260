# anagram.py
# A command-line anagram game written in Python

# Created by Group 9
# Harold Andrei Atillo, Teokan Duran Demircan, Christopher Richard Lua, Jhazmine Clyze Troyo

# Last updated: October 19, 2023, 7:52:52 PM

# References

# https://simpleaudio.readthedocs.io/en/latest/capabilities.html
# https://asciimatics.readthedocs.io/en/stable/io.html#drawing-shapes
# https://github.com/pwaller/pyfiglet
# https://textkool.com/en/test-ascii-art-generator?text=TAXES



# list of English words
# Sourced from
# https://raw.githubusercontent.com/kkrypt0nn/wordlists/main/wordlists/languages/english.txt
# https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
# https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt
# https://drive.google.com/file/d/1oGDf1wjWp5RF_X9C7HoedhIWMh5uJs8s/view

# try:

import simpleaudio as sa
import time

from random import randint, sample, choice
from asciimatics.screen import Screen
from asciimatics.event import MouseEvent, KeyboardEvent
from asciimatics.widgets import *
from colorama import Style, Fore

from menus import *
from words_demo_simple import anagram_generator_diff, shuffle

wave_obj = sa.WaveObject.from_wave_file("./music/anagram_music_v0.1.2.wav") 

final = False
is_playing = False
play_cache = []

color_count = 0

debug = False
no_emoji = False
real_anagram_word = False
flicker = True

high_scores = {
    "easy": [],
    "medium": [],
    "hard": []
}

def play_click():
    click_wav = sa.WaveObject.from_wave_file("./music/blang.wav")
    play_clicker = click_wav.play()
    play_clicker.wait_done()

def play_intro():
    global is_playing, play_cache
    play_obj = wave_obj.play()
    play_cache = [play_obj, time.time(), 6.857]
    is_playing = True

def stop_playing():
    global is_playing, play_cache
    if is_playing == True:
        play_cache[0].stop()
        is_playing = False


def demo(screen):
    global a, is_playing, play_cache, final, no_emoji

    def centre_printer(text, y = 0, centre = True, flicker_text = False, colour = COLOUR_YELLOW):
        global color_count
        lines = text.split("\n")
        for line in range(len(lines)):
            if centre == True:
                screen.centre(lines[line], y + line + 1, colour=colour, attr = (color_count % 3) if flicker_text == True else Screen.A_NORMAL)
            else:
                screen.print_at(lines[line], 0, y + line + 1, colour=Screen.COLOUR_DEFAULT, attr = Screen.A_NORMAL)
            color_count += randint(1,3)

    def menu(text, menu = "splash_screen", play_loop =  False, centre = False, flicker_text = False, colour = 3):
        global play_cache, is_playing, play_intro, play_click, stop_playing, final, real_anagram_word, flicker, no_emoji

        while True:
            if play_loop:
                if is_playing == False and final == False:
                    play_intro()

                if time.time() >= play_cache[1] + play_cache[2]:
                    stop_playing()
            elif final == False:
                play_click()
                final = True
            
            centre_printer(text, centre = centre, flicker_text = flicker_text, colour = colour)
            
            event = screen.get_event()
            if event is not None:
                if isinstance(event, MouseEvent):
                    if menu == "main_menu":
                        if 15 <= event.y <= 20 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 2 # start game
                        elif 22 <= event.y <= 27 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 3 # options
                        elif 29 <= event.y <= 34 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 4 # high scores
                        elif 36 <= event.y <= 41 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 5 # about menu
                        elif 43 <= event.y <= 48 and event.buttons == MouseEvent.LEFT_CLICK:
                            return 0 # exit
                    elif menu == "about_menu" and event.buttons == MouseEvent.LEFT_CLICK:
                        screen.clear()
                        return 1
                    elif menu == "options_menu" and event.buttons == MouseEvent.LEFT_CLICK:
                        if 9 <= event.y <= 14 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 2 # mute
                        elif 16 <= event.y <= 21 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 3 # real anagram
                        elif 23 <= event.y <= 28 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 4 # flicker
                        elif 30 <= event.y <= 35 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 5
                        elif 37 <= event.y <= 42 and event.buttons == MouseEvent.LEFT_CLICK:
                            screen.clear()
                            return 6
                    elif menu == "options_menu":
                        options_tooltip = ""

                        if 9 <= event.y <= 14:
                            options_tooltip = "\nToggles audio mute" + (" (on)" if final else " (off)")
                        if 16 <= event.y <= 21:
                            options_tooltip = "\nWhen enabled, uses actual anagrams instead of using scrambling the anagrams' letters" + (" (enabled)" if real_anagram_word else " (disabled)")
                        if 23 <= event.y <= 28:
                            options_tooltip = "\nToggles the flicker effect" + (" (on)" if flicker else " (off)")
                        if 30 <= event.y <= 35:
                            options_tooltip = "\nToggles ASCII fallback for emojis - use as fallback if icons don't display properly" + (" (on)" if no_emoji else " (off)")
                        
                        screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT, x = 0, w = screen.width, y=45, h = 46)
                        centre_printer(options_tooltip, y=45, centre = centre, flicker_text = flicker, colour = colour)
                        # screen.refresh()
                    elif menu == "difficulty_menu" and event.buttons == MouseEvent.LEFT_CLICK:
                        if 9 <= event.y <= 14:
                            screen.clear()
                            return 2
                        elif 16 <= event.y <= 21:
                            screen.clear()
                            return 3
                        elif 23 <= event.y <= 28:
                            screen.clear()
                            return 4
                        elif 30 <= event.y <= 35:
                            screen.clear()
                            return 5
                    elif menu == "difficulty_menu":
                        difficulty_tooltip = ""

                        if 9 <= event.y <= 14:
                            difficulty_tooltip = "\nEasy (60 seconds, 5 extra attempts, replenishes 1 attempt per correct answer, 4-6 letters per word, hint available)"
                        if 16 <= event.y <= 21:
                            difficulty_tooltip = "\nMedium (30 seconds, 3 extra attempts, replenishes 1 attempt per correct answer, 5-8 letters per word, hint available)"
                        if 23 <= event.y <= 28:
                            difficulty_tooltip = "\nHard (10 seconds, 1 extra attempt, adds 2 seconds per correct answer, 5 or more letters per word)"
                        
                        screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT, x = 0, w = screen.width, y=40, h = 41)
                        centre_printer(difficulty_tooltip, y=40, centre = centre, flicker_text = flicker, colour = colour)
                    elif menu == "loss_menu" and event.buttons == MouseEvent.LEFT_CLICK:
                        screen.clear()
                        return 1
                    if debug == True:
                        screen.centre(str(event), 50)
                        screen.refresh()
                elif isinstance(event, KeyboardEvent):
                    key = event.key_code

                    if key in [Screen.KEY_UP, Screen.KEY_DOWN, Screen.KEY_LEFT, Screen.KEY_RIGHT]:
                        pass
                    elif key <= 0 or key >= 0x100000 or chr(key).lower() == "q":
                        screen.clear()
                        return 0
                    elif chr(key).lower() == " ":
                        screen.clear() 
                        stop_playing()
                        # final = True
                        return 1
                    elif chr(key).lower() == "m":
                        stop_playing()
                        final = (True if final == False else False)
                    elif menu == "main_menu":
                        if chr(key).lower() == "1":
                            screen.clear()
                            return 2 # start game
                        elif chr(key).lower() == "2":
                            screen.clear()
                            return 3 # options
                        elif chr(key).lower() == "3":
                            screen.clear()
                            return 4 # high scores
                        elif chr(key).lower() == "4":
                            screen.clear()
                            return 5 # about menu
                        elif chr(key).lower() == "5":
                            return 0 # exit
                    elif menu == "options_menu":
                        if chr(key).lower() == "1":
                            screen.clear()
                            return 2 # mute
                        elif chr(key).lower() == "2":
                            screen.clear()
                            return 3 # real anagram
                        elif chr(key).lower() == "3":
                            screen.clear()
                            return 4 # flicker
                        elif chr(key).lower() == "4":
                            screen.clear()
                            return 5 # no-emoji
                        elif chr(key).lower() == "5":
                            screen.clear()
                            return 6
                    elif menu == "difficulty_menu":
                        if chr(key).lower() == "1":
                            screen.clear()
                            return 2
                        elif chr(key).lower() == "2":
                            screen.clear()
                            return 3
                        elif chr(key).lower() == "3":
                            screen.clear()
                            return 4
                        elif chr(key).lower() == "4":
                            screen.clear()
                            return 5

            screen.refresh()

    def splash_screen_display():
        splash_code = menu(splash_screen, play_loop = True, centre = True, flicker_text = True)
        if splash_code == 1:
            main_menu_display()

    def main_menu_display():
        global flicker
        menu_code = menu(main_menu, menu="main_menu", play_loop = True, centre = True, flicker_text = flicker)
        if menu_code == 0 or main_menu == 6:
            return 0
        elif menu_code == 1:
            main_menu_display()
        elif menu_code == 2:
            difficulty_menu_display()
        elif menu_code == 3:
            options_menu_display()
        elif menu_code == 4:
            game_over_display(display=True)
        elif menu_code == 5:
            about_menu_display()

    def options_menu_display():
        global final, real_anagram_word, flicker, no_emoji
        menu_code = menu(options_menu, menu="options_menu", play_loop = True, centre = True, flicker_text = flicker)
        if menu_code == 0:
            return 1
        elif menu_code == 1:
            main_menu_display()
        elif menu_code == 2:
            stop_playing()
            final = (True if final == False else False)
            options_menu_display()
        elif menu_code == 3:
            real_anagram_word = not real_anagram_word
            options_menu_display()
        elif menu_code == 4:
            flicker = not flicker
            options_menu_display()
        elif menu_code == 5:
            no_emoji = not no_emoji
            options_menu_display()
        elif menu_code == 6:
            main_menu_display()

    def difficulty_menu_display():
        global flicker
        menu_code = menu(difficulty_menu, menu="difficulty_menu", play_loop = True, centre = True, flicker_text = flicker)
        if menu_code == 0:
            return 1
        elif menu_code == 1:
            main_menu_display()
        elif menu_code == 2:
            main_game_display(difficulty = "easy")
        elif menu_code == 3:
            main_game_display(difficulty = "medium")
        elif menu_code == 4:
            main_game_display(difficulty = "hard")
        elif menu_code == 5:
            main_menu_display()

    def main_game_display(difficulty = "easy"):
        global flicker, no_emoji

        play_loop = True
        return_value = 0

        time_limits = {
            "easy": 60,
            "medium": 30,
            "hard": 10
        }

        attempts = {
            "easy": 5,
            "medium": 3,
            "hard": 1
        }

        now = time.time() + time_limits[difficulty]

        entered_characters = []


        answer = anagram_generator_diff(difficulty)
        pre_scrambled_word = choice(answer[1])
        scrambled_word = pre_scrambled_word if real_anagram_word else shuffle(pre_scrambled_word)

        score = 0
        current_streak = 0
        max_streak = 0
        attempts_left = attempts[difficulty]

        global play_cache, is_playing, play_intro, play_click, stop_playing, final

        def location_printer(text, x = 0, y = 0, align="left", flicker_text = False, colour = COLOUR_YELLOW, attr = Screen.A_NORMAL):
            global color_count
            lines = text.split("\n")
            for line in range(len(lines)):
                if align == "right":
                    x = screen.width - len(lines[line])
                elif align == "center":
                    x = (screen.width - len(lines[line])) // 2
                screen.print_at(lines[line], x, y + line, colour=colour, attr = (color_count % 3) if flicker_text == True else attr)
                color_count += randint(1,3)
        
        while True:
            if play_loop:
                if is_playing == False and final == False:
                    play_intro()

                if time.time() >= play_cache[1] + play_cache[2]:
                    stop_playing()
            elif final == False:
                play_click()
                final = True

            screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT, x = int(screen.width / 2 - 25), w = int(screen.width / 2 + 25), y=0, h = 8)

            location_printer(game_buttons["main_menu"], 0, 0, align="right", flicker_text = flicker)
            if difficulty in ["easy", "medium"]: location_printer(game_buttons["hint_button"], 0, screen.height-3, flicker_text = flicker)
            location_printer((("💛" if not no_emoji else "O") * attempts_left) + (("🖤"  if not no_emoji else "X") * (attempts[difficulty] - attempts_left)), 0, 1, flicker_text = True)
            # location_printer(("♥" * attempts_left) + ("☠" * (attempts[difficulty] - attempts_left)), 0, 1, flicker_text = True)
            location_printer(figlet_printer(scrambled_word.upper(), font="blocks", width=150), 0, 15, align="center", colour = COLOUR_YELLOW, flicker_text = flicker, attr = A_BOLD)
            location_printer(figlet_printer(str(int(now - time.time())), font="ogre"), 0, 0, align="center", colour = COLOUR_YELLOW, flicker_text = False, attr = A_BOLD)
            location_printer((f"x{current_streak}" if current_streak >= 2 else "") + "\n" + figlet_printer(str(score), font="ogre"), 0, screen.height-6, align="right", flicker_text = flicker)

            def loss_condition():
                screen.clear()

                over_now = time.time()
                while time.time() - over_now < 5:
                    location_printer(loss_menu, 0, 5, align="center", flicker_text = flicker, colour = COLOUR_RED)
                    location_printer(insults[min(range(len(insults)), key=lambda i: abs(insults[i][0] - score))][1], 0, 15, align="center", flicker_text = flicker, colour = COLOUR_RED)
                    location_printer(f"Score: {score}{' Max streak: x' + str(max_streak) if max_streak >= 2 else ''}", 0, 16, align="center", flicker_text = flicker, colour = COLOUR_YELLOW, attr=A_BOLD)
                    location_printer(figlet_printer(f"Answer", font="ansi_regular", width=150), 0, 18, align="center", flicker_text = False, colour = COLOUR_YELLOW, attr = A_BOLD)
                    location_printer(figlet_printer("\n".join(answer[1]), font="standard", width=150), 0, 24, align="center", flicker_text = False, colour = COLOUR_YELLOW)
                    location_printer("Please wait and remain still for a few seconds...", 0, 50, align="center", flicker_text = flicker, colour = COLOUR_YELLOW)
                    screen.refresh()
                
                screen.clear()
                stop_playing()

                return [2, score, difficulty]

            location_printer(figlet_printer("".join(entered_characters).upper(), font="bubble", width=150), 0, 40, align="center", colour = COLOUR_YELLOW, flicker_text = flicker, attr = A_BOLD)

            if time.time() - now > 0:
                return_value = loss_condition()
                break
            
            event = screen.get_event()
            if event is not None:
                if isinstance(event, MouseEvent):
                    if 0 <= event.y <= 3 and (screen.width - 16) <= event.x <= screen.width and event.buttons == MouseEvent.LEFT_CLICK:
                        screen.clear()
                        stop_playing()
                        return_value = 1
                        break
                    if (screen.height - 4) <= event.y <= screen.height and 0 <= event.x <= 12 and event.buttons == MouseEvent.LEFT_CLICK and difficulty in ["easy", "medium"]:
                        screen.clear()
                        scrambled_word = shuffle(pre_scrambled_word)
                    if debug == True:
                        screen.centre(str(event) + " " + str(screen.width) + " " + str(screen.height), 50)
                        screen.refresh()
                elif isinstance(event, KeyboardEvent):
                    key = event.key_code

                    if key in [Screen.KEY_UP, Screen.KEY_DOWN, Screen.KEY_LEFT, Screen.KEY_RIGHT]:
                        pass
                    elif key  == -300:  # chr(key) == Screen.KEY_BS:
                        if len(entered_characters) > 0:
                            entered_characters.pop()
                            screen.refresh()
                            screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT, x = 0, w = screen.width, y=33, h = 48)
                    elif key == 13: # enter
                        if "".join(entered_characters).upper() in [word.upper() for word in answer[1]] and (not real_anagram_word or "".join(entered_characters).upper() != pre_scrambled_word.upper()):
                            # screen.centre("Correct", 48)
                            location_printer("Correct", 0, 48, align="center", flicker_text = flicker)

                            score += 1
                            current_streak += 1
                            max_streak = max(max_streak, current_streak)
                            entered_characters = []

                            now = time.time() + time_limits[difficulty]

                            if difficulty != "hard":
                                attempts_left = min(attempts_left + 1, attempts[difficulty])
                            else:
                                now += 2

                            answer = anagram_generator_diff(difficulty)
                            pre_scrambled_word = choice(answer[1])
                            scrambled_word = pre_scrambled_word if real_anagram_word else shuffle(pre_scrambled_word)

                            screen.refresh()
                            screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT)
                        else:
                            if attempts_left > 0:
                                attempts_left -= 1
                                current_streak = 0
                                if debug:
                                    location_printer(f"Incorrect {answer} {entered_characters}", 0, 48, align="center", flicker_text = flicker)
                                else:
                                    location_printer("Incorrect", 0, 48, align="center", flicker_text = flicker)
                            else:
                                return_value = loss_condition()
                                break

                            screen.refresh()
                            if debug:
                                time.sleep(1)
                        screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT, x = 0, w = screen.width, y=33, h = 48)
                    elif key <= 0 or key >= 0x100000: # q #  
                        screen.clear()
                        return_value = 0
                        break
                    elif chr(key).lower() == " ":
                        pass
                    elif chr(key).upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        entered_characters += chr(key).upper()
                        screen.clear_buffer(COLOUR_YELLOW, A_BOLD, Screen.COLOUR_DEFAULT, x = 0, w = screen.width, y=40, h = 44)
            screen.refresh()


        if return_value == 0:
            return 1
        elif return_value == 1:
            main_menu_display()
        elif type(return_value) == list:
            if return_value[0] == 2:
                game_over_display(score = return_value[1], difficulty = return_value[2])

    def game_over_display(score = 0, difficulty = "easy", display = False):
        global flicker, no_emoji
        if display == False:
            high_scores[difficulty].append(score)
            high_scores[difficulty].sort(reverse=True)
            if len(high_scores[difficulty]) > 10 and (score >= high_scores[difficulty][-1]):
                high_scores[difficulty].pop()
                high_scores[difficulty].sort(reverse=True)

        menu_code = menu(fire + f"{figlet.figlet_format('Easy Medium  Hard', font='speed', width=300)}\n" + "\n".join([f" {str(high_scores['easy'][i]) if len(high_scores['easy']) > i else ' ':5s}{' '*39}{str(high_scores['medium'][i]) if len(high_scores['medium']) > i else ' ':7s}{' '*39}{str(high_scores['hard'][i]) if len(high_scores['hard']) > i else ' ':4s}" for i in range(10)]) + "\nClick anywhere to go back", menu="loss_menu", play_loop = True, centre = True, flicker_text = flicker)
        if menu_code == 0:
            return 1
        elif menu_code == 1:
            main_menu_display()

    def about_menu_display():
        global flicker
        menu_code = menu(about_menu, menu="about_menu", play_loop = True, centre = True, flicker_text = flicker)
        if menu_code == 0:
            return 1
        elif menu_code == 1:
            main_menu_display()

    splash_screen_display()

Screen.wrapper(demo)

# except:
#     print("An error has occurred. Exiting...")