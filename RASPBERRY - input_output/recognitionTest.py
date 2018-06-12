# speech recognition packages
import speech_recognition as sr
import inputTest
import datetime


def recognition_test():
    yes_dictionary = ["yes", "yes yes", "yes yes yes",
                      "yesh", "yes please", "oh yes",
                      "yeah", "yep", "yet", "yay", "yes sir",
                      "ye", "yeadon", "yeck", "yeckley", "yedda",
                      "yeh", "yehle", "yell", "yelp", "yen",
                      "yepez", "yesen", "yest", "yeske",
                      "yesterday", "yett", "yoest"]

    no_dictionary = ["no", "no thanks", "no no no",
                     "no no", "know", "na",
                     "now", "wow", "bow", "go", "mo",
                     "mow", "noa", "noaa", "noah",
                     "noble", "noce", "node", "noe",
                     "noh", "nohl", "nold", "noll",
                     "nome", "nomo", "nolf"]
    lets_go = 1
    YN = 1
    while (lets_go == 1):

        # todo nel caso di input live, SCOMMENTATE
        print("\n\nTalk!")
        inputTest.input_test()

        # use the audio file as the audio source
        r = sr.Recognizer()
        answer_from_user = 'ANSWER.wav'
        with sr.AudioFile(answer_from_user) as source:
            audio = r.record(source)  # read the entire audio file

        try:
            recognised_answer = r.recognize_sphinx(audio)
            print("-->", recognised_answer)

        except sr.UnknownValueError:
            # COMUNICO L'ERRORE E L'UTENTE DEVE REINSERIRE
            return -1
            pass

        if (recognised_answer in yes_dictionary):  # OK
            print("\n\tHai detto YES")
        else:  # OK
            if (recognised_answer in no_dictionary):
                print("\n\tHai detto NO")
            else:  # ho riconosciuto un altra parola! LA SALVO!!
                print("\n\t\tAltra parola trovata! --> ", recognised_answer)

        YN = input("\n\t\t\t\t\tEra un YES o NO? 1/0")
        if (YN):
            yes_dictionary.append(recognised_answer)
        else:
            no_dictionary.append(recognised_answer)
        lets_go = input("\n\nAltro input? 1/0")

    print("\nEcco le parole estranee riconosciute per YES:")
    print(yes_dictionary)
    print("\nEcco le parole estranee riconosciute per NO:")
    print(no_dictionary)

    input("\n\nPremere un tasto per uscire!")


if __name__ == "__main__":
    recognition_test()
