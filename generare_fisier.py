# Generare, respectiv editare fisier joc_log.txt
from datetime import datetime
from tkinter import messagebox
import webbrowser


def generare() -> None:
    """Generare, respectiv dupa caz editare fisier joc_log.txt"""
    edit_data: str = datetime.now().strftime('Te-ai jucat in data: %d/%m/%Y | Ora: %H:%M:%S')
    try:
        open('./joc_log.txt')
    except FileNotFoundError:
        messagebox.showinfo(title="Atentie!",
                            message="ATENTIE!!!...Iti voi genera un fisier >> joc_log.txt << "
                                    "pt a afisa de cate ori ai pornit fizzBuzz")
        with open('./joc_log.txt', 'a') as fisier:
            fisier.writelines(edit_data + ', pana acum ai pornit aplicatia o data.')
    else:
        with open('./joc_log.txt', 'r') as fisier1:
            len_randuri: int = len(fisier1.readlines())
        with open('./joc_log.txt', 'a') as fisier:
            fisier.writelines('\n' + edit_data + f', pana acum ai pornit aplicatia de {len_randuri + 1} ori.')


def generare_dialog() -> None:
    """Caseta dialog"""
    generare_action = messagebox.askquestion(title="Powered by Cadfrunze",
                        message="Doresti sa vezi mai multe proiecte?")

    if generare_action == 'yes':
        webbrowser.open_new_tab('https://github.com/cadfrunze?tab=repositories')
    else:
        pass




