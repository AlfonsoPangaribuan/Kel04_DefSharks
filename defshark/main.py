import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width = 800
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Defying Shark')

# Variabel untuk mengontrol status suara (on/off)
sound_on = True

# Load gambar tombol sound on/off
sound_button_image = pygame.image.load('images/sound_on.png')  # Gambar tombol sound on
sound_button_image = pygame.transform.scale(sound_button_image, (30, 30))  # Mengubah ukuran gambar
sound_button_rect = sound_button_image.get_rect(topright=(width - 10, 10))  # Letakkan di pojok kanan atas

# Load musik latar belakang
pygame.mixer.music.load('sounds/background.mp3')
# Load efek suara perenang
swimmer_sound = pygame.mixer.Sound('sounds/swim.mp3')
#coin suara
coin_sound = pygame.mixer.Sound('sounds/coin.mp3')
#start suara
start_sound = pygame.mixer.Sound('sounds/start.mp3')
# Load efek suara game over
game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')

# Load gambar latar belakang menu utama
main_menu_background = pygame.image.load('images/background.png').convert()  # Menangani profil warna
main_menu_background = pygame.transform.scale(main_menu_background, screen_size)

# Load gambar tombol Start
start_button_image = pygame.image.load('images/start.png')
start_button_image = pygame.transform.scale(start_button_image, (200, 100))  # Mengubah ukuran gambar tombol
start_button_rect = start_button_image.get_rect(center=(width // 2, height // 2 - 75))

# Load gambar tombol About
about_button_image = pygame.image.load('images/about.png')
about_button_image = pygame.transform.scale(about_button_image, (200, 100))  # Mengubah ukuran gambar tombol
about_button_rect = about_button_image.get_rect(center=(width // 2, height // 2 + 75))

# Load gambar tombol Shop
shop_button_image = pygame.image.load('images/shop.png')
shop_button_image = pygame.transform.scale(shop_button_image, (200, 100))  # Mengubah ukuran gambar tombol
shop_button_rect = shop_button_image.get_rect(center=(width // 2, height // 2 + 225))

# Load gambar background air laut
background_image1 = pygame.image.load('images/bg1.png').convert()  # Menangani profil warna
background_image2 = pygame.image.load('images/bg2.png').convert()  # Menangani profil warna
background_rect1 = background_image1.get_rect()
background_rect2 = background_image2.get_rect()
background_rect2.y = -height  # Mulai dari luar layar atas

# Kecepatan gerakan latar belakang
background_speed = 1

# Load gambar perenang
swimmer_image = pygame.image.load('images/perenang.png')
swimmer_size = (swimmer_image.get_width() // 5, swimmer_image.get_height() // 5)  # Ukuran perenang yang baru
swimmer_image = pygame.transform.scale(swimmer_image, swimmer_size)  # Menyesuaikan ukuran perenang
swimmer_image = pygame.transform.rotate(swimmer_image, 270)  # Memutar gambar perenang 180 derajat

# Inisialisasi posisi awal perenang di luar layar
swimmer_rect = swimmer_image.get_rect()
swimmer_rect.centerx = width // 2
swimmer_rect.bottom = height  # Mulai dari luar layar bawah

# Kecepatan gerak perenang
swimmer_speed = 5

# Load gambar animasi hiu
shark_images = [pygame.image.load('images/hiu1.png'),
                pygame.image.load('images/hiu2.png'),
                pygame.image.load('images/hiu3.png')]
shark_size = (shark_images[0].get_width() // 2, shark_images[0].get_height() // 2)  # Ukuran hiu yang baru
for i in range(len(shark_images)):
    shark_images[i] = pygame.transform.scale(shark_images[i], shark_size)  # Menyesuaikan ukuran hiu

# Kecepatan gerak hiu
shark_speed = 2

# Load gambar koin
coin_image = pygame.image.load('images/koin.png')
coin_size = (coin_image.get_width() // 4, coin_image.get_height() // 4)  # Ukuran koin yang baru
coin_image = pygame.transform.scale(coin_image, coin_size)  # Menyesuaikan ukuran koin

# Inisialisasi posisi awal koin di luar layar
coin_rect = coin_image.get_rect()
coin_rect.centerx = random.randint(0, width)  # Random posisi horizontal di layar
coin_rect.top = -coin_rect.height  # Mulai dari luar layar atas

# Kecepatan gerak koin
coin_speed = 2

# Skor awal
score = 0
total_score = 0  # Menambahkan total skor

# Inisialisasi nyawa
heart_image = pygame.image.load('images/heart.png')
heart_size = (30, 30)
heart_image = pygame.transform.scale(heart_image, heart_size)
hearts = [heart_image.copy() for _ in range(3)]  # Membuat tiga nyawa

# Load gambar halaman desc
desc_page = pygame.image.load('images/desc.png')
desc_page_rect = desc_page.get_rect(center=(width // 2, height // 2))
back_button_image = pygame.image.load('images/back.png')
back_button_rect = back_button_image.get_rect(topleft=(10, 10))

# Variabel untuk mengontrol apakah menu utama harus ditampilkan
menu_active = True
about_active = False

# Variabel untuk mengontrol nyawa pemain
player_health = 3

# Variabel untuk mengatur interval kemunculan item hati
heart_spawn_timer = 0

#load potion
# Load gambar ramuan
potion_image = pygame.image.load('images/ramuan.png')
potion_size = (potion_image.get_width() // 12, potion_image.get_height() // 12)  # Ukuran ramuan yang baru
potion_image = pygame.transform.scale(potion_image, potion_size)  # Menyesuaikan ukuran ramuan
potion_rect = potion_image.get_rect()  # Mendapatkan rect dari gambar ramuan

# Variabel untuk mengatur kemunculan hiu
shark_spawn_timer = 0
sharks = []
potions = [] 

# Variabel untuk mengatur level
level = 1
level_text = None

# Variabel untuk mengatur kontrol bergerak terus menerus saat tombol panah ditekan lama
continuous_move_up = False
continuous_move_down = False
continuous_move_left = False
continuous_move_right = False

#variabel potion
potion_count = 0
potion_spawn_timer = 0
potion_skill_active = False  # Inisialisasi variabel potion_skill_active
potion_speed = 2  # Kecepatan gerak ramuan

# Loop utama game
running = True
game_over = False
# Load musik latar belakang
pygame.mixer.music.load('sounds/background.mp3')
# Mulai memainkan musik latar belakang (looping)
pygame.mixer.music.play(-1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if about_button_rect.collidepoint(event.pos):
                about_active = True  # Aktifkan halaman about saat tombol about diklik
            elif start_button_rect.collidepoint(event.pos):
                start_sound.play()
                menu_active = False
            elif shop_button_rect.collidepoint(event.pos):
                # Lakukan aksi yang sesuai, seperti membuka layar belanja
                pass  # Tambahkan kode aksi yang sesuai di sini
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Menangkap tombol Escape
                if about_active:
                    about_active = False  # Menutup halaman about jika tombol Escape ditekan
                else:
                    menu_active = True  # Set menu_active menjadi True
            elif event.key == pygame.K_SPACE:  # Tambahkan penanganan tombol spasi
                if not about_active:  # Jika about tidak aktif, aktifkan
                    about_active = True
                else:  # Jika about aktif, nonaktifkan
                    about_active = False
            elif event.key == pygame.K_UP:  # Bergerak ke atas
                swimmer_rect.y -= swimmer_speed
                swimmer_rect.y = max(swimmer_rect.y, 0)  # Membatasi pergerakan ke atas
                continuous_move_up = True  # Set continuous_move_up menjadi True saat tombol panah atas ditekan
            elif event.key == pygame.K_DOWN:  # Bergerak ke bawah
                swimmer_rect.y += swimmer_speed
                swimmer_rect.y = min(swimmer_rect.y, height - swimmer_rect.height)  # Membatasi pergerakan ke bawah
                continuous_move_down = True  # Set continuous_move_down menjadi True saat tombol panah bawah ditekan
            elif event.key == pygame.K_LEFT:  # Bergerak ke kiri
                swimmer_rect.x -= swimmer_speed
                swimmer_rect.x = max(swimmer_rect.x, 0)  # Membatasi pergerakan ke kiri
                continuous_move_left = True  # Set continuous_move_left menjadi True saat tombol panah kiri ditekan
            elif event.key == pygame.K_RIGHT:  # Bergerak ke kanan
                swimmer_rect.x += swimmer_speed
                swimmer_rect.x = min(swimmer_rect.x, width - swimmer_rect.width)  # Membatasi pergerakan ke kanan
                continuous_move_right = True  # Set continuous_move_right menjadi True saat tombol panah kanan ditekan
            elif event.key == pygame.K_p:  # Mengaktifkan skill ramuan
                if potion_count > 0:
                    print("Skill diaktifkan")
                    potion_count -= 1
                    potion_skill_active = True
                    potion_skill_timer = 0
                    swimmer_speed *= 2  # Meningkatkan kecepatan perenang
                else:
                    print("Tidak ada skill")
        elif event.type == pygame.KEYUP:
            # Set continuous_move_* menjadi False saat tombol panah dilepas
            if event.key == pygame.K_UP:
                continuous_move_up = False
            elif event.key == pygame.K_DOWN:
                continuous_move_down = False
            elif event.key == pygame.K_LEFT:
                continuous_move_left = False
            elif event.key == pygame.K_RIGHT:
                continuous_move_right = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                menu_active = False
            elif shop_button_rect.collidepoint(event.pos):
                # Lakukan aksi yang sesuai, seperti membuka layar belanja
                pass  # Tambahkan kode aksi yang sesuai di sini
            elif about_button_rect.collidepoint(event.pos):
                about_active = True
            elif back_button_rect.collidepoint(event.pos) and about_active:
                about_active = False
            elif sound_button_rect.collidepoint(event.pos):  # Ketika tombol sound on/off diklik
                sound_on = not sound_on  # Ubah status suara (on menjadi off, off menjadi on)
                if sound_on:
                    pygame.mixer.unpause()  # Hidupkan suara
                    sound_button_image = pygame.image.load('images/sound_on.png')  # Gunakan gambar sound on
                else:
                    pygame.mixer.pause()  # Matikan suara
                    sound_button_image = pygame.image.load('images/sound_off.png')  # Gunakan gambar sound off
                sound_button_image = pygame.transform.scale(sound_button_image, (30, 30))  # Ukuran tombol

    # Tampilkan menu utama jika aktif
    if menu_active:
        screen.blit(main_menu_background, (0, 0))
        screen.blit(sound_button_image, sound_button_rect)
        screen.blit(start_button_image, start_button_rect)  # Tampilkan tombol Start di atas background
        screen.blit(about_button_image, about_button_rect)  # Tampilkan tombol About di atas background
        screen.blit(shop_button_image, shop_button_rect)  # Tampilkan tombol Shop di atas background
        # Tampilkan total skor di bawah tombol Shop
        font = pygame.font.Font(None, 24)
        total_score_text = font.render(f'Total Skor: {total_score}', True, (255, 255, 255))
        total_score_rect = total_score_text.get_rect(topright=(width - 10, 10))
        screen.blit(total_score_text, total_score_rect)
    elif about_active:
        screen.blit(desc_page, desc_page_rect)
        screen.blit(back_button_image, back_button_rect)
    else:
        screen.blit(sound_button_image, sound_button_rect)
        # Logika game over
        if player_health <= 0:
            game_over = True
            level = 1
            potion_count = 0
            potion_skill_active = False
            game_over_sound.play()

        if game_over:
            # Tampilkan pesan game over
            font = pygame.font.Font(None, 36)
            game_over_text = font.render('Game Over. Tekan Enter untuk memulai kembali.', True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))
            esc_text = font.render('Tekan "Esc" untuk kembali ke menu utama.', True, (255, 255, 255))
            esc_rect = esc_text.get_rect(center=(width // 2, height // 2 + 50))
            screen.blit(game_over_text, game_over_rect)
            screen.blit(esc_text, esc_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # Reset game jika pemain menekan Enter
                swimmer_rect.centerx = width // 2
                swimmer_rect.bottom = height
                sharks = []
                coin_rect.centerx = random.randint(0, width)
                coin_rect.top = -coin_rect.height
                game_over = False
                score = 0
                player_health = 3
                hearts = [heart_image.copy() for _ in range(3)]  # Reset hearts to 3
            elif keys[pygame.K_ESCAPE]:
                menu_active = True  # Return to main menu

        else:
            # Update permainan seperti sebelumnya
            background_rect1.y += background_speed
            background_rect2.y += background_speed
            if background_rect1.y >= height:
                background_rect1.y = -height
            if background_rect2.y >= height:
                background_rect2.y = -height
            screen.blit(background_image1, background_rect1)
            screen.blit(background_image2, background_rect2)

            # Update posisi dan gambar koin
            coin_rect.y += coin_speed
            if coin_rect.top >= height:
                coin_rect.top = -coin_rect.height
                coin_rect.centerx = random.randint(0, width)
            screen.blit(coin_image, coin_rect)

            # Logika ambil koin
            if swimmer_rect.colliderect(coin_rect):
                score += 1
                total_score += 1  # Menambah total skor
                coin_rect.top = -coin_rect.height
                coin_rect.centerx = random.randint(0, width)
                coin_sound.play()

            # Update posisi dan gambar hiu
            for shark_rect in sharks:
                shark_rect.y += shark_speed
                if shark_rect.top >= height:
                    shark_rect.top = -shark_rect.height
                    side = random.choice(["left", "center", "right"])
                    if side == "left":
                        shark_rect.centerx = random.randint(0, width // 3)
                    elif side == "center":
                        shark_rect.centerx = random.randint(width // 3, 2 * width // 3)
                    else:
                        shark_rect.centerx = random.randint(2 * width // 3, width)
                    # Tambahkan level setiap kali hiu muncul
                    level += 1
                    print("Level:", level)
                # Menggambar animasi hiu
                current_shark_image = shark_images[level % len(shark_images)]  # Menggunakan sisa pembagian untuk mengakses gambar yang benar
                screen.blit(current_shark_image, shark_rect)
                # Cek tabrakan dengan pemain
                if swimmer_rect.colliderect(shark_rect):
                    player_health -= 1
                    hearts.pop()  # Kurangi satu nyawa
                    sharks.remove(shark_rect)

            # Tampilkan nyawa
            heart_x = 10
            for heart in hearts:
                screen.blit(heart, (heart_x, 10))
                heart_x += heart_size[0] + 5

            # Tampilkan skor
            font = pygame.font.Font(None, 24)
            score_text = font.render(f'Skor: {score}', True, (255, 255, 255))
            screen.blit(score_text, (10, 50))

            # Tampilkan jumlah ramuan
            potion_text = font.render(f'Jumlah Ramuan (P): {potion_count}', True, (255, 255, 255))
            screen.blit(potion_text, (10, 80))

            # Tampilkan level
            level_text = font.render(f'Level {level}', True, (255, 255, 255))
            screen.blit(level_text, (width - 100, 10))

            # Update posisi dan gambar perenang
            if continuous_move_up:
                swimmer_rect.y -= swimmer_speed
                swimmer_rect.y = max(swimmer_rect.y, 0)  # Membatasi pergerakan ke atas
            if continuous_move_down:
                swimmer_rect.y += swimmer_speed
                swimmer_rect.y = min(swimmer_rect.y, height - swimmer_rect.height)  # Membatasi pergerakan ke bawah
            if continuous_move_left:
                swimmer_rect.x -= swimmer_speed
                swimmer_rect.x = max(swimmer_rect.x, 0)  # Membatasi pergerakan ke kiri
            if continuous_move_right:
                swimmer_rect.x += swimmer_speed
                swimmer_rect.x = min(swimmer_rect.x, width - swimmer_rect.width)  # Membatasi pergerakan ke kanan
            screen.blit(swimmer_image, swimmer_rect)

            # Cek kemunculan item hati setiap 10 detik
            heart_spawn_timer += 1
            if heart_spawn_timer >= 600:  # 10 detik (60 frame/detik * 10 detik)
                # Reset timer
                heart_spawn_timer = 0
                # Munculkan item hati
                if player_health < 3:  # Hanya jika nyawa pemain kurang dari 3
                    heart_rect = heart_image.get_rect()
                    heart_rect.centerx = random.randint(0, width)
                    heart_rect.top = -heart_rect.height
                    screen.blit(heart_image, heart_rect)
                    # Cek ambil item hati
                    if swimmer_rect.colliderect(heart_rect):
                        player_health += 1
                        # Jika nyawa melebihi 3, batasi ke 3
                        player_health = min(player_health, 3)

            # Update timer untuk kemunculan hiu
            shark_spawn_timer += 1
            if shark_spawn_timer >= 120:  # 2 detik (60 frame/detik * 2 detik)
                # Reset timer
                shark_spawn_timer = 0
                # Munculkan hiu baru
                side = random.choice(["left", "center", "right"])
                if side == "left":
                    shark_centerx = random.randint(0, width // 3)
                elif side == "center":
                    shark_centerx = random.randint(width // 3, 2 * width // 3)
                else:
                    shark_centerx = random.randint(2 * width // 3, width)
                new_shark_rect = shark_images[0].get_rect(center=(shark_centerx, -shark_images[0].get_height()))  # Create new rect for the new shark
                sharks.append(new_shark_rect)

            # Update timer untuk kemunculan ramuan
            potion_spawn_timer += 1
            if potion_spawn_timer >= 900:  # 15 detik (60 frame/detik * 15 detik)
                # Reset timer
                potion_spawn_timer = 0
                # Munculkan ramuan baru
                potion_rect = potion_image.get_rect()
                side = random.choice(["left", "center", "right"])
                if side == "left":
                    potion_rect.centerx = random.randint(0, width // 3)
                elif side == "center":
                    potion_rect.centerx = random.randint(width // 3, 2 * width // 3)
                else:
                    potion_rect.centerx = random.randint(2 * width // 3, width)
                potion_rect.top = -potion_rect.height  # Mulai dari luar layar atas
                potions.append(potion_rect)

            # Gambar dan perbarui posisi ramuan
            for potion_rect in potions:
                potion_rect.y += potion_speed
                screen.blit(potion_image, potion_rect)
                # Cek tabrakan dengan pemain
                if swimmer_rect.colliderect(potion_rect):
                    potion_count += 1
                    potions.remove(potion_rect)
                    coin_sound.play()

            # Logika aktivasi skill ramuan
            if potion_skill_active:
                potion_skill_timer += 1
                if potion_skill_timer >= 300:  # 5 detik (60 frame/detik * 5 detik)
                    potion_skill_active = False
                    swimmer_speed //= 2  # Mengembalikan kecepatan perenang ke settingan awal
                    print("Skill ramuan berhasil diaktifkan")

    # Update layar
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Keluar dari game
pygame.quit()
sys.exit()