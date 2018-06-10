# speech recognition packages
import speech_recognition as sr

if __name__ == "__main__":
    # FILE contenente la risposta:

    lets_go = 1
    recognised_yes = ["yes", "yes yes", "yes yes yes", "yesh", "yes please", "oh yes", "now", "wow"]
    recognised_no = ["no", "no thanks", "no no", "no no no", "know", "na", "bow", "go", "mo", "mow"]
    YN=1
    while (lets_go):

        # todo nel caso di input live, SCOMMENTATE
        # inputTest()

        # use the audio file as the audio source
        r = sr.Recognizer()
        AUDIO_FILE = 'noTest.wav'
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        try:
            recognised_answer = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            # COMUNICO L'ERRORE E L'UTENTE DEVE REINSERIRE
            #return -1
            pass

        if (recognised_answer in recognised_yes):  # OK
            print("\n\t\thai detto YES")
        else:  # OK
            if (recognised_answer in recognised_no):
                print("\n\t\thai detto NO")
            else:  # ho riconosciuto un altra parola! LA SALVO!!
                print("\n\t\tAltra parola trovata! --> ", recognised_answer)
                print("\n\t\t\t\t\tEra un YES o NO? 1/0")
        input(YN)
        if (YN):
            recognised_yes.append(recognised_answer)
        else:
            recognised_no.append(recognised_answer)
        print("\n\nAltro input? 1/0")
        input(lets_go)

    print("\nEcco le parole estranee riconosciute per YES:")
    print(recognised_yes)
    print("\nEcco le parole estranee riconosciute per NO:")
    print(recognised_no)

    input(lets_go)
