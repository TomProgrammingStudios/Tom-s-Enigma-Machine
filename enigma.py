from tkinter import *
from __rotors import *
import time
import threading
from playsound import playsound

output_string = ""
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ------------------------------------ Launcher section --------------------------------------------------

main = Tk()
main.geometry("1050x750")
main.title("Tom's Enigma Machine")
main.iconbitmap("Assets/icon.ico")
main.resizable(False, False)

background = PhotoImage(file="Assets/background.png").subsample(3, 3)
bck = Label(main, image=background).place(x=0, y=0)

VERSION = "1.0.1.2"
DATE = "17/12/2022"
DEV = "Tom's Customs"
EMAIL = "tommaso07brignoli@gmail.com"

num_table = number_table()

topframe = Frame(main, bg="#97795f", relief="sunken", borderwidth=8)
topframe.pack(pady=15)
rotors_frame = Frame(topframe, bg="#97795f", relief="raised", borderwidth=5)
rotors_frame.grid(row=0, column=0)
letters_frame = Frame(topframe, bg="#97795f", relief="raised", borderwidth=5)
letters_frame.grid(row=0, column=1, padx=30)

plugboard_settings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

letter_status = [[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15],[0,15]]#
color_occupancy = [0,0,0,0,0,0,0,0,0,0,0,0,0]


Rotor1_frame = Frame(rotors_frame, bg="#97795f")
Rotor2_frame = Frame(rotors_frame, bg="#97795f")
Rotor3_frame = Frame(rotors_frame, bg="#97795f")

rotor_1_position = 1
rotor_2_position = 1
rotor_3_position = 1

rotor1_type = 1
rotor2_type = 1
rotor3_type = 1

buffer_config = 0

soundvar = IntVar()
activevar = IntVar()

interrupt_encryption = False

# ------------------------------------ Texture variables section -----------------------------------------

img_a_off = PhotoImage(file="Assets/LampBoard/a_off.png").subsample(7, 7)
img_b_off = PhotoImage(file="Assets/LampBoard/b_off.png").subsample(7, 7)
img_c_off = PhotoImage(file="Assets/LampBoard/c_off.png").subsample(7, 7)
img_d_off = PhotoImage(file="Assets/LampBoard/d_off.png").subsample(7, 7)
img_e_off = PhotoImage(file="Assets/LampBoard/e_off.png").subsample(7, 7)
img_f_off = PhotoImage(file="Assets/LampBoard/f_off.png").subsample(7, 7)
img_g_off = PhotoImage(file="Assets/LampBoard/g_off.png").subsample(7, 7)
img_h_off = PhotoImage(file="Assets/LampBoard/h_off.png").subsample(7, 7)
img_i_off = PhotoImage(file="Assets/LampBoard/i_off.png").subsample(7, 7)
img_j_off = PhotoImage(file="Assets/LampBoard/j_off.png").subsample(7, 7)
img_k_off = PhotoImage(file="Assets/LampBoard/k_off.png").subsample(7, 7)
img_l_off = PhotoImage(file="Assets/LampBoard/l_off.png").subsample(7, 7)
img_m_off = PhotoImage(file="Assets/LampBoard/m_off.png").subsample(7, 7)
img_n_off = PhotoImage(file="Assets/LampBoard/n_off.png").subsample(7, 7)
img_o_off = PhotoImage(file="Assets/LampBoard/o_off.png").subsample(7, 7)
img_p_off = PhotoImage(file="Assets/LampBoard/p_off.png").subsample(7, 7)
img_q_off = PhotoImage(file="Assets/LampBoard/q_off.png").subsample(7, 7)
img_r_off = PhotoImage(file="Assets/LampBoard/r_off.png").subsample(7, 7)
img_s_off = PhotoImage(file="Assets/LampBoard/s_off.png").subsample(7, 7)
img_t_off = PhotoImage(file="Assets/LampBoard/t_off.png").subsample(7, 7)
img_u_off = PhotoImage(file="Assets/LampBoard/u_off.png").subsample(7, 7)
img_v_off = PhotoImage(file="Assets/LampBoard/v_off.png").subsample(7, 7)
img_w_off = PhotoImage(file="Assets/LampBoard/w_off.png").subsample(7, 7)
img_x_off = PhotoImage(file="Assets/LampBoard/x_off.png").subsample(7, 7)
img_y_off = PhotoImage(file="Assets/LampBoard/y_off.png").subsample(7, 7)
img_z_off = PhotoImage(file="Assets/LampBoard/z_off.png").subsample(7, 7)

LetterOffImages = [img_a_off, img_b_off, img_c_off, img_d_off, img_e_off, img_f_off, img_g_off, img_h_off, img_i_off, img_j_off, img_k_off, img_l_off, img_m_off, img_n_off, img_o_off, img_p_off, img_q_off, img_r_off, img_s_off, img_t_off, img_u_off, img_v_off, img_w_off, img_x_off, img_y_off, img_z_off]

img_a_on = PhotoImage(file="Assets/LampBoard/a_on.png").subsample(7, 7)
img_b_on = PhotoImage(file="Assets/LampBoard/b_on.png").subsample(7, 7)
img_c_on = PhotoImage(file="Assets/LampBoard/c_on.png").subsample(7, 7)
img_d_on = PhotoImage(file="Assets/LampBoard/d_on.png").subsample(7, 7)
img_e_on = PhotoImage(file="Assets/LampBoard/e_on.png").subsample(7, 7)
img_f_on = PhotoImage(file="Assets/LampBoard/f_on.png").subsample(7, 7)
img_g_on = PhotoImage(file="Assets/LampBoard/g_on.png").subsample(7, 7)
img_h_on = PhotoImage(file="Assets/LampBoard/h_on.png").subsample(7, 7)
img_i_on = PhotoImage(file="Assets/LampBoard/i_on.png").subsample(7, 7)
img_j_on = PhotoImage(file="Assets/LampBoard/j_on.png").subsample(7, 7)
img_k_on = PhotoImage(file="Assets/LampBoard/k_on.png").subsample(7, 7)
img_l_on = PhotoImage(file="Assets/LampBoard/l_on.png").subsample(7, 7)
img_m_on = PhotoImage(file="Assets/LampBoard/m_on.png").subsample(7, 7)
img_n_on = PhotoImage(file="Assets/LampBoard/n_on.png").subsample(7, 7)
img_o_on = PhotoImage(file="Assets/LampBoard/o_on.png").subsample(7, 7)
img_p_on = PhotoImage(file="Assets/LampBoard/p_on.png").subsample(7, 7)
img_q_on = PhotoImage(file="Assets/LampBoard/q_on.png").subsample(7, 7)
img_r_on = PhotoImage(file="Assets/LampBoard/r_on.png").subsample(7, 7)
img_s_on = PhotoImage(file="Assets/LampBoard/s_on.png").subsample(7, 7)
img_t_on = PhotoImage(file="Assets/LampBoard/t_on.png").subsample(7, 7)
img_u_on = PhotoImage(file="Assets/LampBoard/u_on.png").subsample(7, 7)
img_v_on = PhotoImage(file="Assets/LampBoard/v_on.png").subsample(7, 7)
img_w_on = PhotoImage(file="Assets/LampBoard/w_on.png").subsample(7, 7)
img_x_on = PhotoImage(file="Assets/LampBoard/x_on.png").subsample(7, 7)
img_y_on = PhotoImage(file="Assets/LampBoard/y_on.png").subsample(7, 7)
img_z_on = PhotoImage(file="Assets/LampBoard/z_on.png").subsample(7, 7)

LetterOnImages = [img_a_on, img_b_on, img_c_on, img_d_on, img_e_on, img_f_on, img_g_on, img_h_on, img_i_on, img_j_on, img_k_on, img_l_on, img_m_on, img_n_on, img_o_on, img_p_on, img_q_on, img_r_on, img_s_on, img_t_on, img_u_on, img_v_on, img_w_on, img_x_on, img_y_on, img_z_on]

img_01 = PhotoImage(file="Assets/Rotors/rotor_1.png").subsample(7, 7)
img_02 = PhotoImage(file="Assets/Rotors/rotor_2.png").subsample(7, 7)
img_03 = PhotoImage(file="Assets/Rotors/rotor_3.png").subsample(7, 7)
img_04 = PhotoImage(file="Assets/Rotors/rotor_4.png").subsample(7, 7)
img_05 = PhotoImage(file="Assets/Rotors/rotor_5.png").subsample(7, 7)
img_06 = PhotoImage(file="Assets/Rotors/rotor_6.png").subsample(7, 7)
img_07 = PhotoImage(file="Assets/Rotors/rotor_7.png").subsample(7, 7)
img_08 = PhotoImage(file="Assets/Rotors/rotor_8.png").subsample(7, 7)
img_09 = PhotoImage(file="Assets/Rotors/rotor_9.png").subsample(7, 7)
img_10 = PhotoImage(file="Assets/Rotors/rotor_10.png").subsample(7, 7)
img_11 = PhotoImage(file="Assets/Rotors/rotor_11.png").subsample(7, 7)
img_12 = PhotoImage(file="Assets/Rotors/rotor_12.png").subsample(7, 7)
img_13 = PhotoImage(file="Assets/Rotors/rotor_13.png").subsample(7, 7)
img_14 = PhotoImage(file="Assets/Rotors/rotor_14.png").subsample(7, 7)
img_15 = PhotoImage(file="Assets/Rotors/rotor_15.png").subsample(7, 7)
img_16 = PhotoImage(file="Assets/Rotors/rotor_16.png").subsample(7, 7)
img_17 = PhotoImage(file="Assets/Rotors/rotor_17.png").subsample(7, 7)
img_18 = PhotoImage(file="Assets/Rotors/rotor_18.png").subsample(7, 7)
img_19 = PhotoImage(file="Assets/Rotors/rotor_19.png").subsample(7, 7)
img_20 = PhotoImage(file="Assets/Rotors/rotor_20.png").subsample(7, 7)
img_21 = PhotoImage(file="Assets/Rotors/rotor_21.png").subsample(7, 7)
img_22 = PhotoImage(file="Assets/Rotors/rotor_22.png").subsample(7, 7)
img_23 = PhotoImage(file="Assets/Rotors/rotor_23.png").subsample(7, 7)
img_24 = PhotoImage(file="Assets/Rotors/rotor_24.png").subsample(7, 7)
img_25 = PhotoImage(file="Assets/Rotors/rotor_25.png").subsample(7, 7)
img_26 = PhotoImage(file="Assets/Rotors/rotor_26.png").subsample(7, 7)

RotorImages = [img_01, img_02, img_03, img_04, img_05, img_06, img_07, img_08, img_09, img_10, img_11, img_12, img_13, img_14, img_15, img_16, img_17, img_18, img_19, img_20, img_21, img_22, img_23, img_24, img_25, img_26]

img_type_1 = PhotoImage(file="Assets/General/type1.png").subsample(5, 5)
img_type_2 = PhotoImage(file="Assets/General/type2.png").subsample(5, 5)
img_type_3 = PhotoImage(file="Assets/General/type3.png").subsample(5, 5)
img_type_4 = PhotoImage(file="Assets/General/type4.png").subsample(5, 5)
img_type_5 = PhotoImage(file="Assets/General/type5.png").subsample(5, 5)

RotorTypeImages = [img_type_1, img_type_2, img_type_3, img_type_4, img_type_5]

img_increase = PhotoImage(file="Assets/General/increase.png").subsample(5, 5)
img_decrease = PhotoImage(file="Assets/General/decrease.png").subsample(5, 5)

submit_image = PhotoImage(file="Assets/General/submit_button.png").subsample(5, 5)

#------------------------------------- Functions section -------------------------------------------------

def plugboard_window_handler() -> None:
    global plugboard_settings, buffer_config

    Plugboard_window = Tk()
    Plugboard_window.geometry("750x450")
    Plugboard_window.title("Plugboard")
    Plugboard_window.iconbitmap("Assets/icon.ico")

    plugboard_letter_list = []
    colors = ["green", "light_blue", "lime", "orange", "purple", "pink", "red", "white", "yellow", "dark_green", "dark_blue", "blue", "aqua"]

    def loadPrevious():
        global letter_status

        plugboard_letters = [p_a, p_b, p_c, p_d, p_e, p_f, p_g, p_h, p_i, p_j, p_k, p_l, p_m, p_n, p_o, p_p, p_q, p_r, p_s, p_t, p_u, p_v, p_w, p_x, p_y, p_z]

        for index, item in enumerate(letter_status):
            if item[0] != 0:
                _img_ = PhotoImage(file=f"Assets/PlugBoard/{char_list[item[0]]}_{colors[item[1]]}.png", master=Plugboard_window).subsample(8, 8)
                plugboard_letters[item[0]].config(image=_img_)
                plugboard_letters[item[0]].image=_img_
                _img_ = PhotoImage(file=f"Assets/PlugBoard/{char_list[index]}_{colors[item[1]]}.png", master=Plugboard_window).subsample(8, 8)
                plugboard_letters[index].config(image=_img_)
                plugboard_letters[index].image=_img_
                
    def commitChanges():
        global letter_status, plugboard_settings

        plugboard_settings = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        for item in letter_status:
            if item[0] != 0:
                plugboard_settings[item[0]] = letter_status[item[0]][0] + 1 
                plugboard_settings[letter_status[item[0]][0]] = item[0] + 1
        Plugboard_window.destroy()

    def change_letter(letter_id : int) -> None:
        global buffer_config ,letter_status, color_occupancy
        plugboard_letters = [p_a, p_b, p_c, p_d, p_e, p_f, p_g, p_h, p_i, p_j, p_k, p_l, p_m, p_n, p_o, p_p, p_q, p_r, p_s, p_t, p_u, p_v, p_w, p_x, p_y, p_z]

        print(letter_status[letter_id])
        if letter_status[letter_id] == [0, 15]:
            for color in colors:
                print("True")
                if color_occupancy[colors.index(color)] == 2:
                    continue

                _img_ = PhotoImage(file=f"Assets/PlugBoard/{char_list[letter_id]}_{color}.png", master=Plugboard_window).subsample(8, 8)
                plugboard_letters[letter_id].config(image=_img_)
                plugboard_letters[letter_id].image=_img_

                if color_occupancy[colors.index(color)] == 0:                   # Prima lettera in selezione
                    color_occupancy[colors.index(color)] = 1
                    buffer_config = letter_id
                    break
                elif color_occupancy[colors.index(color)] == 1:                 # Seconda lettera in selezione
                    color_occupancy[colors.index(color)] = 2
                    plugboard_settings[buffer_config] = letter_id
                    plugboard_settings[letter_id] = buffer_config
                    letter_status[letter_id][0] = buffer_config
                    letter_status[letter_id][1] = colors.index(color)
                    letter_status[buffer_config][0] = letter_id
                    letter_status[buffer_config][1] = colors.index(color)
                    break
        else:
            index = letter_status[letter_id][0]
            color_occupancy[letter_status[letter_id][1]] = 0
            letter_status[index] = [0, 15]
            letter_status[letter_id] = [0, 15]
            _img_ = PhotoImage(file=f"Assets/PlugBoard/{char_list[letter_id]}_off.png", master=Plugboard_window).subsample(8, 8)
            plugboard_letters[letter_id].config(image=_img_)
            plugboard_letters[letter_id].image=_img_
            _img_ = PhotoImage(file=f"Assets/PlugBoard/{char_list[index]}_off.png", master=Plugboard_window).subsample(8, 8)
            plugboard_letters[index].config(image=_img_)
            plugboard_letters[index].image=_img_
    
        print(letter_status)
        print(color_occupancy)
        print(buffer_config)         


    for letter in char_list:
        _img_ = PhotoImage(file=f"Assets/PlugBoard/{letter}_off.png", master=Plugboard_window).subsample(8, 8)
        plugboard_letter_list.append(_img_)

    main_frame = Frame(Plugboard_window, bg="#97795f", relief="sunken", borderwidth=5)
    main_frame.pack()
    upper_frame = Frame(main_frame, bg="#97795f")
    upper_frame.pack()
    middle_frame = Frame(main_frame, bg="#97795f")
    middle_frame.pack()
    lower_frame = Frame(main_frame, bg="#97795f")
    lower_frame.pack()

    p_q = Button(upper_frame, image=plugboard_letter_list[16], bd=3, command= lambda : change_letter(16))
    p_q.image=plugboard_letter_list[16]
    p_q.grid(row=0, column=0, padx=5, pady=10)
    p_w = Button(upper_frame, image=plugboard_letter_list[22], bd=3, command= lambda : change_letter(22))
    p_w.image=plugboard_letter_list[22]
    p_w.grid(row=0, column=1, padx=5, pady=10)
    p_e = Button(upper_frame, image=plugboard_letter_list[4], bd=3, command= lambda : change_letter(4))
    p_e.image=plugboard_letter_list[4]
    p_e.grid(row=0, column=2, padx=5, pady=10)
    p_r = Button(upper_frame, image=plugboard_letter_list[17], bd=3, command= lambda : change_letter(17))
    p_r.image=plugboard_letter_list[17]
    p_r.grid(row=0, column=3, padx=5, pady=10)
    p_t = Button(upper_frame, image=plugboard_letter_list[19], bd=3, command= lambda : change_letter(19))
    p_t.image=plugboard_letter_list[19]
    p_t.grid(row=0, column=4, padx=5, pady=10)
    p_z = Button(upper_frame, image=plugboard_letter_list[25], bd=3, command= lambda : change_letter(25))
    p_z.image=plugboard_letter_list[25]
    p_z.grid(row=0, column=5, padx=5, pady=10)
    p_u = Button(upper_frame, image=plugboard_letter_list[20], bd=3, command= lambda : change_letter(20))
    p_u.image=plugboard_letter_list[20]
    p_u.grid(row=0, column=6, padx=5, pady=10)
    p_i = Button(upper_frame, image=plugboard_letter_list[8], bd=3, command= lambda : change_letter(8))
    p_i.image=plugboard_letter_list[8]
    p_i.grid(row=0, column=7, padx=5, pady=10)
    p_o = Button(upper_frame, image=plugboard_letter_list[14], bd=3, command= lambda : change_letter(14))
    p_o.image=plugboard_letter_list[14]
    p_o.grid(row=0, column=8, padx=5, pady=10)
    p_p = Button(upper_frame, image=plugboard_letter_list[15], bd=3, command= lambda : change_letter(15))
    p_p.image=plugboard_letter_list[15]
    p_p.grid(row=0, column=9, padx=5, pady=10)

    p_a = Button(middle_frame, image=plugboard_letter_list[0], bd=3, command= lambda : change_letter(0))
    p_a.image=plugboard_letter_list[0]
    p_a.grid(row=0, column=0, padx=5, pady=10)
    p_s = Button(middle_frame, image=plugboard_letter_list[18], bd=3, command= lambda : change_letter(18))
    p_s.image=plugboard_letter_list[18]
    p_s.grid(row=0, column=1, padx=5, pady=10)
    p_d = Button(middle_frame, image=plugboard_letter_list[3], bd=3, command= lambda : change_letter(3))
    p_d.image=plugboard_letter_list[3]
    p_d.grid(row=0, column=2, padx=5, pady=10)
    p_f = Button(middle_frame, image=plugboard_letter_list[5], bd=3, command= lambda : change_letter(5))
    p_f.image=plugboard_letter_list[5]
    p_f.grid(row=0, column=3, padx=5, pady=10)
    p_g = Button(middle_frame, image=plugboard_letter_list[6], bd=3, command= lambda : change_letter(6))
    p_g.image=plugboard_letter_list[6]
    p_g.grid(row=0, column=4, padx=5, pady=10)
    p_h = Button(middle_frame, image=plugboard_letter_list[7], bd=3, command= lambda : change_letter(7))
    p_h.image=plugboard_letter_list[7]
    p_h.grid(row=0, column=5, padx=5, pady=10)
    p_j = Button(middle_frame, image=plugboard_letter_list[9], bd=3, command= lambda : change_letter(9))
    p_j.image=plugboard_letter_list[9]
    p_j.grid(row=0, column=6, padx=5, pady=10)
    p_k = Button(middle_frame, image=plugboard_letter_list[10], bd=3, command= lambda : change_letter(10))
    p_k.image=plugboard_letter_list[10]
    p_k.grid(row=0, column=7, padx=5, pady=10)
    p_l = Button(middle_frame, image=plugboard_letter_list[11], bd=3, command= lambda : change_letter(11))
    p_l.image=plugboard_letter_list[11]
    p_l.grid(row=0, column=8, padx=5, pady=10)
    
    p_y = Button(lower_frame, image=plugboard_letter_list[24], bd=3, command= lambda : change_letter(24))
    p_y.image=plugboard_letter_list[24]
    p_y.grid(row=0, column=0, padx=5, pady=10)
    p_x = Button(lower_frame, image=plugboard_letter_list[23], bd=3, command= lambda : change_letter(23))
    p_x.image=plugboard_letter_list[23]
    p_x.grid(row=0, column=1, padx=5, pady=10)
    p_c = Button(lower_frame, image=plugboard_letter_list[2], bd=3, command= lambda : change_letter(2))
    p_c.image=plugboard_letter_list[2]
    p_c.grid(row=0, column=2, padx=5, pady=10)
    p_v = Button(lower_frame, image=plugboard_letter_list[21], bd=3, command= lambda : change_letter(21))
    p_v.image=plugboard_letter_list[21]
    p_v.grid(row=0, column=3, padx=5, pady=10)
    p_b = Button(lower_frame, image=plugboard_letter_list[1], bd=3, command= lambda : change_letter(1))
    p_b.image=plugboard_letter_list[1]
    p_b.grid(row=0, column=4, padx=5, pady=10)
    p_n = Button(lower_frame, image=plugboard_letter_list[13], bd=3, command= lambda : change_letter(13))
    p_n.image=plugboard_letter_list[13]
    p_n.grid(row=0, column=5, padx=5, pady=10)
    p_m = Button(lower_frame, image=plugboard_letter_list[12], bd=3, command= lambda : change_letter(12))
    p_m.image=plugboard_letter_list[12]
    p_m.grid(row=0, column=6, padx=5, pady=10)

    saveButton = Button(main_frame, text="Save", font="calibri 17 bold", fg="green", width=5, command=commitChanges)
    saveButton.pack()

    loadPrevious()

def info_window_handler() -> None:
    Info_window = Tk()
    Info_window.geometry("550x400")
    Info_window.title("Info")
    Info_window.iconbitmap("Assets/icon.ico")

    Info_title = Label(Info_window, text="Info", font="calibri 20 bold")
    Info_title.pack()
    things_frame = Frame(Info_window)
    things_frame.pack()
    Version_text_1 = Label(things_frame, text="Version", font="calibri 15 bold")
    Version_text_1.grid(row=0, column=0, padx=50, pady=20)
    Version_text_2 = Label(things_frame, text=VERSION, font="calibri 12")
    Version_text_2.grid(row=0, column=1, padx=50, pady=20)
    Version_date_text_1 = Label(things_frame, text="V. date", font="calibri 15 bold")
    Version_date_text_1.grid(row=1, column=0, padx=50, pady=20)
    Version_date_text_2 = Label(things_frame, text=DATE, font="calibri 12")
    Version_date_text_2.grid(row=1, column=1, padx=50, pady=20)
    Developer_text_1 = Label(things_frame, text="Developer", font="calibri 15 bold")
    Developer_text_1.grid(row=2, column=0, padx=50, pady=20)
    Developer_text_2 = Label(things_frame, text=DEV, font="calibri 12")
    Developer_text_2.grid(row=2, column=1, padx=50, pady=20)
    Website_text_1 = Label(things_frame, text="Email", font="calibri 15 bold")
    Website_text_1.grid(row=3, column=0, padx=50, pady=20)
    Website_text_2 = Label(things_frame, text=EMAIL, font="calibri 12")
    Website_text_2.grid(row=3, column=1, padx=50, pady=20)

def rotor_increase(rotor_number) -> None:
    global rotor_1_position, rotor_2_position, rotor_3_position
    def rotor_increase__() -> int:
        global rotor_1_position, rotor_2_position, rotor_3_position

        if rotor_number == 1:
            rotor_1_position = rotor_1_position + 1
            return rotor_1_position
        elif rotor_number == 2:
            rotor_2_position = rotor_2_position + 1
            return rotor_2_position
        elif rotor_number == 3:
            rotor_3_position = rotor_3_position + 1
            return rotor_3_position

    rotor_1_objects = [Rotor1_increase, Rotor1_current, Rotor1_decrease]
    rotor_2_objects = [Rotor2_increase, Rotor2_current, Rotor2_decrease]
    rotor_3_objects = [Rotor3_increase, Rotor3_current, Rotor3_decrease]

    rotor_objects_list = [rotor_1_objects, rotor_2_objects, rotor_3_objects]
    rotor_positions_list = [rotor_1_position, rotor_2_position, rotor_3_position]

    rotor_objects = rotor_objects_list[rotor_number - 1]
    rotor_position = rotor_positions_list[rotor_number - 1]

    current_label = rotor_objects[1]

    if rotor_position == 26:
        if rotor_number == 1:
            rotor_1_position = 1
        elif rotor_number == 2:
            rotor_2_position = 1
        elif rotor_number == 3:
            rotor_3_position = 1
        current_label.config(image=img_01)
    else:
        new_position = rotor_increase__()

        current_label.config(image=RotorImages[new_position - 1])

def rotor_decrease(rotor_number) -> None:
    global rotor_1_position, rotor_2_position, rotor_3_position

    def rotor_decrease__() -> int:
        global rotor_1_position, rotor_2_position, rotor_3_position

        if rotor_number == 1:
            rotor_1_position = rotor_1_position - 1
            return rotor_1_position
        elif rotor_number == 2:
            rotor_2_position = rotor_2_position - 1
            return rotor_2_position
        elif rotor_number == 3:
            rotor_3_position = rotor_3_position - 1
            return rotor_3_position

    rotor_1_objects = [Rotor1_increase, Rotor1_current, Rotor1_decrease]
    rotor_2_objects = [Rotor2_increase, Rotor2_current, Rotor2_decrease]
    rotor_3_objects = [Rotor3_increase, Rotor3_current, Rotor3_decrease]

    rotor_objects_list = [rotor_1_objects, rotor_2_objects, rotor_3_objects]
    rotor_positions_list = [rotor_1_position, rotor_2_position, rotor_3_position]

    rotor_objects = rotor_objects_list[rotor_number - 1]
    rotor_position = rotor_positions_list[rotor_number - 1]


    current_label = rotor_objects[1]

    if rotor_position == 1:
        if rotor_number == 1:
            rotor_1_position = 26
        elif rotor_number == 2:
            rotor_2_position = 26
        elif rotor_number == 3:
            rotor_3_position = 26
        current_label.config(image=img_26)
    else:
        new_position = rotor_decrease__()

        current_label.config(image=RotorImages[new_position - 1])

def rotor_type_increase(rotor_number) -> None:
    global rotor1_type, rotor2_type, rotor3_type

    if rotor_number == 1:
        if rotor1_type == 5:
            rotor1_type = 1
        else:
            rotor1_type = rotor1_type + 1
        Rotor1_type.config(image=RotorTypeImages[rotor1_type - 1])
    elif rotor_number == 2:
        if rotor2_type == 5:
            rotor2_type = 1
        else:
            rotor2_type = rotor2_type + 1
        Rotor2_type.config(image=RotorTypeImages[rotor2_type - 1])
    elif rotor_number == 3:
        if rotor3_type == 5:
            rotor3_type = 1
        else:
            rotor3_type = rotor3_type + 1
        Rotor3_type.config(image=RotorTypeImages[rotor3_type - 1])
    else:
        raise Warning(f"Cannot increase rotor type for rotor {rotor_number}")

def change_ui_status(how : str) -> None:
    Rotor1_scale.config(state=how)
    Rotor2_scale.config(state=how)
    Rotor3_scale.config(state=how)
    active_check.config(state=how)
    
    for x in range(3):
        rotor_1_objects = [Rotor1_increase, Rotor1_current, Rotor1_decrease]
        rotor_2_objects = [Rotor2_increase, Rotor2_current, Rotor2_decrease]
        rotor_3_objects = [Rotor3_increase, Rotor3_current, Rotor3_decrease]
        rotor_type_objects = [Rotor1_type, Rotor2_type, Rotor3_type]

        rotor_objects_list = [rotor_1_objects, rotor_2_objects, rotor_3_objects]

        rotor_objects = rotor_objects_list[x]
        type_object = rotor_type_objects[x]
        
        add_button = rotor_objects[0]
        rem_button = rotor_objects[2]

        add_button.config(state=how)
        rem_button.config(state=how)
        type_object.config(state=how)

def play_sound() -> None:
    playsound("Assets/click.wav")

def message_encryption(automatic_trigger = False, returnoverride = False, characteroverride = "") -> None or int:

    def light_aux(y):
        letters_list[y].config(image=LetterOnImages[y])
        time.sleep(0.3)
        letters_list[y].config(image=LetterOffImages[y])

    global interrupt_encryption

    if not returnoverride:
        output_box.delete(1.0, END)
    error_label.config(text="A software recreation of the famous german machine!", fg="black", bg="#97795f")

    if (rotor1_type == rotor2_type) or (rotor2_type == rotor3_type) or (rotor3_type == rotor1_type):
        error_label.config(text="You cannot use the same rotor type while processing.", fg="red", bg="white")
        return False, ""
    
    if not returnoverride:
        to_encode = input_box.get(1.0, "end-1c")
    else:
        to_encode = characteroverride

    raw_characters = []
    refined_characters = []
    
    for char in to_encode:
        try:
            raw_characters.append(num_table.cypher_number(char.lower()))
        except:
            if char == " ":
                raw_characters.append(char)
            else:
                error_label.config(text="The enigma machine can only encrypt lowercase letters.", fg="red", bg="white")
                return False, ""
    
    change_ui_status("disabled")
    
    Rotor_1 = rotor(rotor1_type)
    Rotor_2 = rotor(rotor2_type)
    Rotor_3 = rotor(rotor3_type)
    Reflector = reflector() 
    
    for char in raw_characters:

        space = False

        if interrupt_encryption:
            interrupt_encryption = False
            change_ui_status("normal")
            return False, ""
        
        if char == " ":
            if not returnoverride:
                previous_output = output_box.get(1.0, "end-1c")
                output_box.delete(1.0, END)
                output_box.insert(1.0, f"{previous_output} ")
            else:
                space = True
            continue

        if plugboard_settings[char - 1] != 0:
            char = plugboard_settings[char - 1]

        print(plugboard_settings)
        char = Rotor_3.encrypt(char, rotor_3_position)
        char = Rotor_2.encrypt(char, rotor_2_position)
        char = Rotor_1.encrypt(char, rotor_1_position)
        char = Reflector.reflect(char)
        char = Rotor_1.reverse_encrypt(char, rotor_1_position)
        char = Rotor_2.reverse_encrypt(char, rotor_2_position)
        char = Rotor_3.reverse_encrypt(char, rotor_3_position)

        if plugboard_settings[char - 1] != 0:
            char = plugboard_settings[char - 1]

        refined_characters.append(char)

        if rotor_3_position == Rotor3_scale.get():
            if rotor_2_position == Rotor2_scale.get():
                rotor_increase(1)
                rotor_increase(2)
                rotor_increase(3)
            else:
                rotor_increase(2)
                rotor_increase(3)
        else:
            rotor_increase(3)

        decyphered = num_table.decypher_number(char)
        letters_list[char - 1].config(image=LetterOnImages[char-1])

        if not returnoverride:
            previous_output = output_box.get(1.0, "end-1c")
            output_box.delete(1.0, END)
            output_box.insert(1.0, f"{previous_output}{decyphered}")
        if soundvar.get() == 1:
            soundThread = threading.Thread(target=play_sound)
            soundThread.start()

        if not automatic_trigger:
            time.sleep(1/speed_scale.get())
            letters_list[char - 1].config(image=LetterOffImages[char-1])
        else:
            light_thread = threading.Thread(target= lambda : light_aux(char-1))
            light_thread.start()
        
    change_ui_status("normal")
    if space:
        return True, " "
    else:
        return True, decyphered

def work_stopper() -> None:
    global interrupt_encryption
    interrupt_encryption  =  not interrupt_encryption

def thread_buffer() -> None:
    EncThread = threading.Thread(target=message_encryption)
    EncThread.start()

def constant_encryption() -> None:
    global rotor_3_position, rotor_2_position, rotor_1_position
    previous_text = ""
    waszero = True
    while True:
        if activevar.get() == 1:
            if waszero:
                output_box.delete(1.0, END)
                input_box.delete(1.0, END)
                waszero = False
            current_text = input_box.get(1.0, "end-1c")
            if current_text != previous_text and len(current_text) > len(previous_text):
                previous_output = output_box.get(1.0, "end-1c")
                result, character = message_encryption(automatic_trigger=True, returnoverride=True, characteroverride=current_text[-1])
                if not result:
                    time.sleep(3)
                else:
                    previous_text = current_text
                    output_box.delete(1.0, END)
                    output_box.insert(1.0, f"{previous_output}{character}")
            elif current_text != previous_text:
                previous_text = ""
                previous_output = ""
                current_text = ""
                output_box.delete(1.0, END)
                input_box.delete(1.0, END)
        else:
            waszero = True
        time.sleep(0.07)               

def constant_thread_buffer() -> None:
    thread = threading.Thread(target=constant_encryption)
    thread.daemon = True
    thread.start()

constant_thread_buffer()

menubar = Menu(main)
plugboard_menu = Menu(menubar, tearoff=0)
plugboard_menu.add_command(label="Open", command=plugboard_window_handler)
info_menu = Menu(menubar, tearoff=0)
info_menu.add_command(label="Open", command=info_window_handler)
menubar.add_cascade(label="Plugboard", menu=plugboard_menu)
menubar.add_cascade(label="Info", menu=info_menu)
main.config(menu=menubar)

top_letter_frame = Frame(letters_frame, bg="#97795f")
top_letter_frame.pack()
middle_letter_frame = Frame(letters_frame, bg="#97795f")
middle_letter_frame.pack()
bottom_letter_frame = Frame(letters_frame, bg="#97795f")
bottom_letter_frame.pack()

letter_q = Label(top_letter_frame, image=img_q_off, bg="#97795f")
letter_q.grid(row=0, column=0)
letter_w = Label(top_letter_frame, image=img_w_off, bg="#97795f")
letter_w.grid(row=0, column=1)
letter_e = Label(top_letter_frame, image=img_e_off, bg="#97795f")
letter_e.grid(row=0, column=2)
letter_r = Label(top_letter_frame, image=img_r_off, bg="#97795f")
letter_r.grid(row=0, column=3)
letter_t = Label(top_letter_frame, image=img_t_off, bg="#97795f")
letter_t.grid(row=0, column=4)
letter_z = Label(top_letter_frame, image=img_z_off, bg="#97795f")
letter_z.grid(row=0, column=5)
letter_u = Label(top_letter_frame, image=img_u_off, bg="#97795f")
letter_u.grid(row=0, column=6)
letter_i = Label(top_letter_frame, image=img_i_off, bg="#97795f")
letter_i.grid(row=0, column=7)
letter_o = Label(top_letter_frame, image=img_o_off, bg="#97795f")
letter_o.grid(row=0, column=8)
letter_p = Label(top_letter_frame, image=img_p_off, bg="#97795f")
letter_p.grid(row=0, column=9)

letter_a = Label(middle_letter_frame, image=img_a_off, bg="#97795f")
letter_a.grid(row=0, column=0)
letter_s = Label(middle_letter_frame, image=img_s_off, bg="#97795f")
letter_s.grid(row=0, column=1)
letter_d = Label(middle_letter_frame, image=img_d_off, bg="#97795f")
letter_d.grid(row=0, column=2)
letter_f = Label(middle_letter_frame, image=img_f_off, bg="#97795f")
letter_f.grid(row=0, column=3)
letter_g = Label(middle_letter_frame, image=img_g_off, bg="#97795f")
letter_g.grid(row=0, column=4)
letter_h = Label(middle_letter_frame, image=img_h_off, bg="#97795f")
letter_h.grid(row=0, column=5)
letter_j = Label(middle_letter_frame, image=img_j_off, bg="#97795f")
letter_j.grid(row=0, column=6)
letter_k = Label(middle_letter_frame, image=img_k_off, bg="#97795f")
letter_k.grid(row=0, column=7)
letter_l = Label(middle_letter_frame, image=img_l_off, bg="#97795f")
letter_l.grid(row=0, column=8)

letter_y = Label(bottom_letter_frame, image=img_y_off, bg="#97795f")
letter_y.grid(row=0, column=0)
letter_x = Label(bottom_letter_frame, image=img_x_off, bg="#97795f")
letter_x.grid(row=0, column=1)
letter_c = Label(bottom_letter_frame, image=img_c_off, bg="#97795f")
letter_c.grid(row=0, column=2)
letter_v = Label(bottom_letter_frame, image=img_v_off, bg="#97795f")
letter_v.grid(row=0, column=3)
letter_b = Label(bottom_letter_frame, image=img_b_off, bg="#97795f")
letter_b.grid(row=0, column=4)
letter_n = Label(bottom_letter_frame, image=img_n_off, bg="#97795f")
letter_n.grid(row=0, column=5)
letter_m = Label(bottom_letter_frame, image=img_m_off, bg="#97795f")
letter_m.grid(row=0, column=6)

letters_list = [letter_a, letter_b, letter_c, letter_d, letter_e, letter_f, letter_g, letter_h, letter_i, letter_j, letter_k, letter_l, letter_m, letter_n, letter_o, letter_p, letter_q, letter_r, letter_s, letter_t, letter_u, letter_v, letter_w, letter_x, letter_y, letter_z]

Rotor1_frame.grid(row=0, column=0, padx=25)
Rotor1_decrease = Button(Rotor1_frame, image=img_decrease, command = lambda : rotor_decrease(1), borderwidth=5)
Rotor1_decrease.grid(row=0, column=0, pady=10)
Rotor1_current = Label(Rotor1_frame, image=img_01)
Rotor1_current.grid(row=1, column=0)
Rotor1_increase = Button(Rotor1_frame, image=img_increase, command = lambda : rotor_increase(1), borderwidth=5)
Rotor1_increase.grid(row=2, column=0, pady=10)

Rotor2_frame.grid(row=0, column=1, padx=25)
Rotor2_decrease = Button(Rotor2_frame, image=img_decrease, command = lambda : rotor_decrease(2), borderwidth=5)
Rotor2_decrease.grid(row=0, column=0, pady=10)
Rotor2_current = Label(Rotor2_frame, image=img_01)
Rotor2_current.grid(row=1, column=0)
Rotor2_increase = Button(Rotor2_frame, image=img_increase, command = lambda : rotor_increase(2), borderwidth=5)
Rotor2_increase.grid(row=2, column=0, pady=10)

Rotor3_frame.grid(row=0, column=2, padx=25)
Rotor3_decrease = Button(Rotor3_frame, image=img_decrease, command = lambda : rotor_decrease(3), borderwidth=5)
Rotor3_decrease.grid(row=0, column=0, pady=10)
Rotor3_current = Label(Rotor3_frame, image=img_01)
Rotor3_current.grid(row=1, column=0)
Rotor3_increase = Button(Rotor3_frame, image=img_increase, command = lambda : rotor_increase(3), borderwidth=5)
Rotor3_increase.grid(row=2, column=0, pady=10)

Rotor1_type = Button(Rotor1_frame, image=RotorTypeImages[0], command = lambda : rotor_type_increase(1), borderwidth=5)
Rotor1_type.grid(row=4, column=0, pady=20)
Rotor2_type = Button(Rotor2_frame, image=RotorTypeImages[0], command = lambda : rotor_type_increase(2), borderwidth=5)
Rotor2_type.grid(row=4, column=0, pady=20)
Rotor3_type = Button(Rotor3_frame, image=RotorTypeImages[0], command = lambda : rotor_type_increase(3), borderwidth=5)
Rotor3_type.grid(row=4, column=0, pady=20)

Rotor1_scale = Scale(Rotor1_frame, from_ = 1, to = 26, bg="#97795f")
Rotor1_scale.grid(row=0, column=1, rowspan=4)
Rotor1_scale.set(38)
Rotor2_scale = Scale(Rotor2_frame, from_ = 1, to = 26, bg="#97795f")
Rotor2_scale.grid(row=0, column=1, rowspan=4)
Rotor2_scale.set(38)
Rotor3_scale = Scale(Rotor3_frame, from_ = 1, to = 26, bg="#97795f")
Rotor3_scale.grid(row=0, column=1, rowspan=4)
Rotor3_scale.set(38)
bottom_frame = Frame(main, bg="#97795f", relief="raised", borderwidth=5)
bottom_frame.pack()

b_l_frame = Frame(bottom_frame, bg="#97795f")
b_l_frame.grid(row=0, column=0, padx=20)
b_c_frame = Frame(bottom_frame, bg="#97795f")
b_c_frame.grid(row=0, column=1, padx=20)
b_r_frame = Frame(bottom_frame, bg="#97795f")
b_r_frame.grid(row=0, column=2, padx=20)

input_label = Label(b_l_frame, text="Input Text", font="comic_sans 15 bold", bg="#97795f")
input_label.grid(row=0, column=0, pady=15)
input_box = Text(b_l_frame, height=7, width=30, font="calibri 12", bd=5)
input_box.grid(row=1, column=0) 

input_label = Label(b_c_frame, text="Working speed ch/s", font="comic_sans 15 bold", bg="#97795f")
input_label.grid(row=0, column=0)
speed_scale = Scale(b_c_frame, from_ = 1, to = 10, orient=HORIZONTAL, bg="#97795f")
speed_scale.grid(row=1, column=0)
key_frame = Frame(b_c_frame, bg="#97795f")
key_frame.grid(row=2, column=0, pady=10)
encode_button = Button(key_frame, image=submit_image, command=thread_buffer, borderwidth=8)
encode_button.grid(row=0, column=0, padx=30)
encode_button = Button(key_frame, text="Stop Encryption", font="calibri 10 bold", fg="white", bg="red", height=1, width=15, command=work_stopper)
encode_button.grid(row=1, column=0, pady=10)
checks_frame = Frame(key_frame, relief="raised", borderwidth=5, bg="#97795f")
checks_frame.grid(row=2, column=0)
audio_check = Checkbutton(checks_frame, text="Sound", variable=soundvar, onvalue=1, offvalue=0, bg="#97795f")
audio_check.grid(row=0, column=0, pady=2)
active_check = Checkbutton(checks_frame, text="Real Time Encryption", variable=activevar, onvalue=1, offvalue=0, bg="#97795f")
active_check.grid(row=0, column=1, pady=2)

output_label = Label(b_r_frame, text="Output Text", font="comic_sans 15 bold", bg="#97795f")
output_label.grid(row=0, column=0, pady=15)
output_box = Text(b_r_frame, height=7, width=30, font="calibri 12", bd=5)
output_box.grid(row=1, column=0)
error_label = Label(main, text="A software recreation of the famous german machine!", font="comic_sans 15 bold", fg="black", bg="#97795f")
error_label.pack(pady=5)

mainloop()