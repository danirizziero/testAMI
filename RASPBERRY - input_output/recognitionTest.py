# speech recognition packages
import speech_recognition as sr
import inputTest
import datetime



def recognition_test():
    yes_dictionary = ["yes", "yesh", "yeah", "yep", "yet", "yay",
                      "ye", "yeadon", "yeck", "yeckley", "yedda",
                      "yeh", "yehle", "yell", "yelp", "yen",
                      "yepez", "yesen", "yest", "yeske",
                      "yesterday", "yett", "yoest"]

    no_dictionary = ["no", "know", "na",
                     "now", "wow", "bow", "go", "mo",
                     "mow", "noa", "noaa", "noah",
                     "noble", "noce", "node", "noe",
                     "noh", "nohl", "nold", "noll",
                     "nome", "nomo", "nolf"]
    lets_go = 1
    YN = 1
    while (lets_go):

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
        
        
        found = False
        for yes_word in yes_dictionary: #controllo le possibili foneticamente simili a YES
            print(recognised_answer," <-> ",yes_word," --> ",recognised_answer.find(yes_word))
            if recognised_answer.find(yes_word) != -1:
                print("\n\tHai detto YES")
                found = True
                break
        if not found:
            for no_word in no_dictionary: #controllo le possibili foneticamente simili a YES
                print("\t\t",recognised_answer," <-> ",no_word," --> ",recognised_answer.find(no_word))
                if recognised_answer.find(no_word) != -1:
                    print("\n\tHai detto NO")
                    found = True
                    break
        if not found: # ho riconosciuto un altra parola! LA SALVO!!
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
