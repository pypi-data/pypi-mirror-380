import threading
import os
import pygame
import time
import tempfile
from pydub import AudioSegment

class music_me:
    pygame.mixer.init()
    @staticmethod
    def trilha_sonora_inloop(velocidade, arquivo):
        """Toca uma música em loop infinito com alteração de velocidade."""
        def player():
            try:
                audio = AudioSegment.from_file(arquivo)
                audio = audio._spawn(audio.raw_data, overrides={
                    "frame_rate": int(audio.frame_rate * velocidade)
                }).set_frame_rate(audio.frame_rate)

                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                temp_path = temp_file.name
                temp_file.close()
                audio.export(temp_path, format="wav")

                sound = pygame.mixer.Sound(temp_path)
                sound.play(loops=-1)

                print(f"Tocando {arquivo} em loop (velocidade {velocidade}x)")

                while True:
                    time.sleep(0.1)

            except Exception as e:
                print(f"[music_me erro] {e}")

        threading.Thread(target=player, daemon=True).start()

    @staticmethod
    def elemento_musical(velocidade, arquivo, tempo_a_esperar=0):
        """Toca um elemento musical após um tempo definido."""
        def player():
            try:
                if tempo_a_esperar > 0:
                    time.sleep(tempo_a_esperar)

                audio = AudioSegment.from_file(arquivo)
                audio = audio._spawn(audio.raw_data, overrides={
                    "frame_rate": int(audio.frame_rate * velocidade)
                }).set_frame_rate(audio.frame_rate)

                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                temp_path = temp_file.name
                temp_file.close()
                audio.export(temp_path, format="wav")

                sound = pygame.mixer.Sound(temp_path)
                sound.play()

                print(f"Tocando {arquivo} (velocidade {velocidade}x) após {tempo_a_esperar}s")

                time.sleep(audio.duration_seconds)
                os.remove(temp_path)

            except Exception as e:
                print(f"[music_me erro] {e}")

        threading.Thread(target=player, daemon=True).start()

    @staticmethod
    def elemento_musical_entonado(velocidade, entonacao, arquivo, tempo_a_esperar=0):
        """Toca um elemento musical com velocidade e entonação ajustáveis."""
        def player():
            try:
                if tempo_a_esperar > 0:
                    time.sleep(tempo_a_esperar)

                audio = AudioSegment.from_file(arquivo)
                audio = audio._spawn(audio.raw_data, overrides={
                    "frame_rate": int(audio.frame_rate * velocidade * entonacao)
                }).set_frame_rate(audio.frame_rate)

                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                temp_path = temp_file.name
                temp_file.close()
                audio.export(temp_path, format="wav")

                sound = pygame.mixer.Sound(temp_path)
                sound.play()

                print(f"Tocando {arquivo} (velocidade {velocidade}x, entonação {entonacao}x)")

                time.sleep(audio.duration_seconds)
                os.remove(temp_path)

            except Exception as e:
                print(f"[music_me erro] {e}")

        threading.Thread(target=player, daemon=True).start()
    def dell(elemento, tempo_após_o_inicio_da_reprodução_para_o_del):
        """
        Interrompe a reprodução do elemento após 'tempo' segundos.

        Parâmetros:
        - elemento: objeto de áudio (ex: pygame.mixer.Sound ou pygame.mixer.music)
        - tempo_após_o_inicio_da_reprodução_para_o_del: tempo em segundos até a interrupção
        """
        def parar():
            try:
                if hasattr(elemento, "get_busy") and elemento.get_busy():
                    elemento.stop()
                    print("Reprodução interrompida automaticamente.")
                else:
                    print(f"{elemento} não está reproduzindo ou não é válido.")
            except Exception as e:
                print(f"Erro ao tentar parar o elemento: {e}")

        threading.Timer(tempo_após_o_inicio_da_reprodução_para_o_del, parar).start()