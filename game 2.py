import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Identitas
NAMA = "Nafis Ainul Lathif"

# Variabel
skor = 0
nyawa = 3
waktu = 10
A, B = set(), set()
level = "Easy"

def buat_himpunan():
    if level == "Easy":
        return set(random.sample(range(1, 10), 3))
    elif level == "Medium":
        return set(random.sample(range(1, 20), 4))
    else:
        return set(random.sample(range(1, 30), 5))

def soal_baru():
    global A, B, waktu
    A = buat_himpunan()
    B = buat_himpunan()
    
    label_A.configure(text=f"A = {A}")
    label_B.configure(text=f"B = {B}")
    
    entry_union.delete(0, "end")
    entry_inter.delete(0, "end")
    
    waktu = 10
    update_timer()

def update_timer():
    global waktu, nyawa
    if waktu > 0:
        label_timer.configure(text=f"⏱️ {waktu}")
        waktu -= 1
        root.after(1000, update_timer)
    else:
        nyawa -= 1
        label_nyawa.configure(text=f"❤️ {nyawa}")
        label_hasil.configure(text="⏰ Waktu habis!")
        
        if nyawa == 0:
            game_over()
        else:
            soal_baru()

def cek_jawaban():
    global skor, nyawa
    
    try:
        u = set(map(int, entry_union.get().split()))
        i = set(map(int, entry_inter.get().split()))
        
        benar_u = A | B
        benar_i = A & B
        
        if u == benar_u and i == benar_i:
            skor += 20
            label_hasil.configure(text="🔥 BENAR SEMUA!")
        else:
            nyawa -= 1
            label_hasil.configure(text=f"❌ Salah!\nUnion:{benar_u}\nInter:{benar_i}")
        
        label_skor.configure(text=f"🏆 {skor}")
        label_nyawa.configure(text=f"❤️ {nyawa}")
        
        if nyawa == 0:
            game_over()
        else:
            soal_baru()
    
    except:
        label_hasil.configure(text="⚠ Input salah!")

def game_over():
    frame_game.pack_forget()
    frame_over.pack(pady=50)
    label_final.configure(text=f"Game Over!\nSkor Akhir: {skor}")

def mulai_game(lvl):
    global level, skor, nyawa
    level = lvl
    skor = 0
    nyawa = 3
    
    frame_menu.pack_forget()
    frame_game.pack(pady=20)
    
    label_skor.configure(text="🏆 0")
    label_nyawa.configure(text="❤️ 3")
    
    soal_baru()

# UI
root = ctk.CTk()
root.geometry("420x520")
root.title("Game Himpunan PRO")

# MENU
frame_menu = ctk.CTkFrame(root)
frame_menu.pack(pady=40)

ctk.CTkLabel(frame_menu, text="🎮 GAME HIMPUNAN", font=("Arial", 20)).pack(pady=5)
ctk.CTkLabel(frame_menu, text=f"Oleh: {NAMA}", font=("Arial", 12)).pack(pady=5)

ctk.CTkButton(frame_menu, text="Easy", command=lambda: mulai_game("Easy")).pack(pady=5)
ctk.CTkButton(frame_menu, text="Medium", command=lambda: mulai_game("Medium")).pack(pady=5)
ctk.CTkButton(frame_menu, text="Hard", command=lambda: mulai_game("Hard")).pack(pady=5)

# GAME
frame_game = ctk.CTkFrame(root)

label_skor = ctk.CTkLabel(frame_game, text="🏆 0")
label_skor.pack()

label_nyawa = ctk.CTkLabel(frame_game, text="❤️ 3")
label_nyawa.pack()

label_timer = ctk.CTkLabel(frame_game, text="⏱️ 10")
label_timer.pack()

label_A = ctk.CTkLabel(frame_game, text="")
label_A.pack()

label_B = ctk.CTkLabel(frame_game, text="")
label_B.pack()

entry_union = ctk.CTkEntry(frame_game, placeholder_text="Masukkan Union")
entry_union.pack(pady=5)

entry_inter = ctk.CTkEntry(frame_game, placeholder_text="Masukkan Intersection")
entry_inter.pack(pady=5)

ctk.CTkButton(frame_game, text="Submit", command=cek_jawaban).pack(pady=10)

label_hasil = ctk.CTkLabel(frame_game, text="")
label_hasil.pack()

# GAME OVER
frame_over = ctk.CTkFrame(root)

label_final = ctk.CTkLabel(frame_over, text="", font=("Arial", 18))
label_final.pack(pady=10)

ctk.CTkButton(frame_over, text="Main Lagi", command=lambda: mulai_game(level)).pack(pady=5)
ctk.CTkButton(frame_over, text="Keluar", command=root.quit).pack(pady=5)

root.mainloop()