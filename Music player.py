
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlist = []
        self.current_song = 0

    def add_song(self, song_path):
        if song_path.endswith('.mp3'):
            self.playlist.append(song_path)
        else:
            print("Invalid file format. Only MP3 files are supported.")

    def remove_song(self, index):
        if 0 <= index < len(self.playlist):
            del self.playlist[index]
        else:
            print("Invalid song index.")

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            print(f"Now playing: {self.playlist[self.current_song]}")
        else:
            print("Playlist is empty.")

    def next_song(self):
        if self.current_song < len(self.playlist) - 1:
            self.current_song += 1
            self.play()
        else:
            print("End of playlist.")

    def prev_song(self):
        if self.current_song > 0:
            self.current_song -= 1
            self.play()
        else:
            print("This is the first song in the playlist.")

    def display_playlist(self):
        if self.playlist:
            print("Playlist:")
            for i, song in enumerate(self.playlist):
                print(f"{i + 1}. {song}")
        else:
            print("Playlist is empty.")

    def run(self):
        while True:
            print("\nMusic Player Menu:")
            print("1. Add Song to Playlist")
            print("2. Remove Song from Playlist")
            print("3. Play")
            print("4. Next Song")
            print("5. Previous Song")
            print("6. Display Playlist")
            print("7. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                song_path = input("Enter the path to the MP3 file: ")
                self.add_song(song_path)
            elif choice == '2':
                index = int(input("Enter the index of the song to remove: "))
                self.remove_song(index - 1)
            elif choice == '3':
                self.play()
            elif choice == '4':
                self.next_song()
            elif choice == '5':
                self.prev_song()
            elif choice == '6':
                self.display_playlist()
            elif choice == '7':
                pygame.mixer.music.stop()
                pygame.quit()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
