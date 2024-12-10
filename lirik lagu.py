import time
import sys


def print_lirik(lirik, delay=0.1):
    for char in lirik:
        sys.stdout.write(char)
        sys.stdout.flush()                      # Mengeluarkan output tanpa baris baru
        time.sleep(delay)                       # Jeda antar huruf
    print()                                         # Setelah selesai, tampilkan baris baru

# Lirik lagu
lyrics = [
    "I could walk you by, and I'll tell without a thought   ",
    "You'd be mine   ",
    "Would you mind if I took your hand tonight   ",
    "Know you're all that I want - this life   ",
    ".........................\n",
]


for line in lyrics:
    print_lirik(line, delay=0.1)  
    time.sleep(0.65) 


lyrics = [
    "I'll imagine we fell in love",
    "I'll nap under moonlight skies with you",
    "I think I'll picture us, you with the waves",
    "The ocean's colors on your face",
]


for line in lyrics:
    print_lirik(line, delay=0.08) 
    time.sleep(0.65)  


lyrics = [
    "I'll leave my heart with your air",
    "So let me fly with you",
]


for line in lyrics:
    print_lirik(line, delay=0.09)  
    time.sleep(0.9)  

lyrics = [
    "Will you be forever with me?",
    " :) "
]

# Menampilkan lirik satu per satu, per huruf
for line in lyrics:
    print_lirik(line, delay=0.15)# Ganti delay sesuai kebutuhan
    time.sleep(0.9)# Jeda antara lirik satu dengan lirik berikutnya
