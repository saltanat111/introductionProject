import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import tkinter.font as tkFont
import random
import winreg

name_meanings = {
    "Жыпар": "ароматная,приятная,любимая,лучистая",
    "Жыргал": "веселье, радость",
    "Зарема": "алая заря, за революцию мира",
    "Замира": "за мир",
    "Зейнеп": "свет, красота, украшение",
    "Зыйнат": "красота",
    "Кенже": "самый младший ребенок",
    "Кыял": "мысли, поиски, мечты",
    "Марал": "красивая, стройная",
    "Маржан": "красивая,как ожерелье из жемчуга",
    "Медина": "чистая и достойная",
    "Мейиз": "сладкая и содержательная жизнь",
    "Маржан": "спокойная , благодатная жизнь",
    "Мээрим": "доброта",
    "Жедигер": "продолжатель рода, завещание, подарок",
    "Женишбек": "победа",
    "Жолболду": "пожелание ровного жизненного пути, счастливого будущего",
    "Жолборс": "храбрый, сильный",
    "Жоомарт": "широкая душа,великодушие",
    "Жумгалбек": "восход",
    "Алиман": "возвышенная, мудрая",
    "Камчы": "мудрый управленец , хозяин в доме",
    "Каныбек": "крепкий , здоровый",
    "Канат": "опора родителей",
    "Карыбоз": "крепкий , здоровый , чтоб долго оставался здоровым",
    "Кудайберди": "подарок от бога ",
    "Куштарбек": "желанный",
    "АДИЛЕТ": "Кыз балага адилет жараткан: адилетчи болгон деген мааниде койгон.",
    "АЗИЗА": "Эске салуу: сыйлуу кыз болсун деген тилек менен коюлат.",
    "АЛИМА": "Билим менен жана көмөктөшкөн кыз болсун деп тилек коюлат.",
    "АЙДАЙ": "Ар кайыктан табанган: уйдоор жактырып келген деген мааниде тилек коюлат.",
    "АЙДАН": "Жаңылыштык: тазайтык: ата-ананын биргеликтүү эңсеги болсун деген тилекте коюлат.",
    "АЛТЫНАЙ": "Кечинге караган кыз болсун: жетишкенде эмилишсиз жатканат.",
    "БАРСБЕК": "Байыркы: 7-8-кылымдарда Енисейдеги Сибирдеги кыргыздардын кагандарынын башчысы: кол башчы: эл башчы. Ушул тарыхый инсандын атын урматтап: патриоттук духта эр балдарга деген тилек-максатта коюлуп: эл арасына бат тарап бара жатат.",
    "БАРЧЫН": "Тоң районунун Тоң айылында жашаган Аскын ата түш көрөт. Түшүндө куштун баласын кармайт колуна кондурат. Ичинен абдан кубанат. Ошол түш көргөн күнүнөн кийин бир жыл өткөндө уулду болот. Ошол түшүн жоруп: сүйүнүчүн жарыя кылып: уулунун атын Барчын 1974 коет.",
    "БЕКЖАН": "Бул баланын төрөлүшү жана энчилүү аты тууралы анын атасы Акылбек Исаков: \"Менин баламдын жаны бек болсун: өмүрү узак болсун: элдин арасында аман-эсен чоңоюп: элдин кызматына жараган: жаңы замананын агымында: шарданында жашап: калк сүймөнчүлүгүнө ээ болуп деген мааниде коюлат",
    "АБАКИР": "Мукамбет ар.Мухаммед: 570-632 пайгамбардын жолун жолдоочу: анын ишин идеясын улантуучу.",
    "АБДАНБЕК": "Жаны абдан өтө бек болсун: өлбөсүн: турмуш жолу узак болсун деп коюлат.",
    "АБДЫ: АБДУ": "Арабча “кул: кудайдын пендеси: адам” деген маанилерди билдирет ",
    "АВТАНДИЛ": "Ш.Руставелинин “Жолборс терисин жамынган баатыр” деген чыгармасындагы башкы каармандардын бири. Кыргызда мындай атты ошол каармандай баатыр: достукка бекем: сүйүүгө туруктуу: элжерин терең урматтаган адамдардан болсо экен деп коюшат.",
    "АДЕН": "1. Теңир тартуулаган күч: тынымсыз аракет: ошондон улам жаралган энергия; 2.Эркелетүү иретинде: Менин укмуштуу сыймыгым; 3. Шыктандыруучу: дем берүүчү.",    
    "АЖАР": "Кыз балдарга ажары ачылган сулуу: бетинен нуру төгүлгөн көркөмдүү: жылдызы жанган келбеттүү болсун деп коюлат.",
    "АЗАМАТ": "1. Өз эли менен жеринин чыныгы патриоту: кулуну болсун деп; 2. Өз элине: жерине кыйындык пайда болгондо: ошол абалды жөнгө салган оңдой ала турган азаматтардан болсун” деген тилекте койгон",
    "АКМАРАЛ": "“1. Маралдай маңкайган келишкен сулуу; 2. Ары ашкан акылдуу кыргыздын кыраан кыздарынан болсун",
    "АКПАР": "Улуу, зор, чоң, атактуу, урматтуу” деген маанилерди билдирет." ,
    "АКТИЛЕК": " 1.Ата – энесинин да: наристенин да тилеген тилеги 2.Ар дайыма ак таза болсун ",
    "АКЫЛЫЙМАН": "Бул кыздын энчилүү атын аталаш тууганы Осмонбек 1957: “Кыргыздын акылдуу дагы: ыймандуу дагы; улууну урматтап: кичүүнү ызаттаган элдин кызы болсун",
    "АЛМАЗ": "Баланын жаны алмаздай бек: катуу: бышык болсун: өмүрү: жашоосу узун болсун: бала алмаздай курч: өткүр: чыйрак болсун: бардык ишке: турмушка өтүмдүү болсун деген тилектер менен коюлат.",
    "АЛТАЙ": "1. Ата – бабаларыбыздын ыйык жана байыркы түпкү мекенин туу туткан киши болсун.",
    "АМАН": "Ар дайым аман болсун: өлбөсүн: өмүрү узун болсун деген тилекте көбүнчө эр балдарга: кээде кыз балдарга коюлат.",
    "АРУУЖАН": "1. Жаны – дили таптаза болсун; 2. Аруулук аны ар дайыма коштоп жүрсүн» - деген тилектер менен коюлат",
    "АРУУКЕ": "Арууке, Манас эпосундагы Алмамбет баатырдын зайыбы, Күлчоро баатырдын энеси. Аруу - таза сөзүнүн синоними. Көбүн учурда жан-дүйнөнүн тазалыгын билгизүү үчүн колдонулат.",
    "АСЕЛ": "Мындай энчилүү ат дээрлик кыз балдарга; “1. Аселдей өзү да: тили да ширин: жасаган тамагы да: элге болгон мамилеси да таттуу; 2. Агылып-төгүлгөн берешен болсун” деген аруу тилектер менен коюлат.",
}

class BabyNameGeneratorApp:
    def __init__(self, master):
        
        self.master = master
		
        self.master.title("Baby Name Generator")
        self.master.geometry("500x450")

        self.gender = tk.StringVar()
        self.gender.set("эркек")

        self.create_widgets()

    def create_widgets(self):
        self.gender_label = tk.Label(self.master, text="Баланын жынысы(эркек,кыз):",font=(20))
        self.gender_label.pack()
        
		# self.gender_label = tk.Label(self.master, text="Enter the gender (boy/girl):", font=("Helvetica", 24))
        # self.gender_label.pack()

        self.gender_entry = tk.Entry(self.master,font=(16))
        self.gender_entry.pack()

        self.submit_gender_button = tk.Button(self.master, text="кийинки", command=self.show_initial_letter,font=(16))
        self.submit_gender_button.pack()

    def show_initial_letter(self):
        self.gender = self.get_valid_gender()

        initial_letter_label = tk.Label(self.master, text="Аттын биринчи тамгасын киргизгиле:",font=(20))
        initial_letter_label.pack()

        self.initial_letter_entry = tk.Entry(self.master,font=(16))
        self.initial_letter_entry.pack()

        submit_initial_letter_button = tk.Button(self.master, text="кийинки", command=self.show_names,font=(16))
        submit_initial_letter_button.pack()

    def show_names(self):
        initial_letter = self.initial_letter_entry.get().lower()
        names = generate_names(self.gender, initial_letter)
        if not names:
            tk.messagebox.showinfo("No Names", "No names available for the given criteria. Please try again.",font=(20))
            self.reset_ui()
            return

        self.names_combobox = ttk.Combobox(self.master, values=names, state="readonly",font=(20))
        self.names_combobox.set("Атын тандаңыз",)
        self.names_combobox.pack()

        self.submit_name_button = tk.Button(self.master, text="кийинки", command=self.show_meaning,font=(16))
        self.submit_name_button.pack()

    def show_meaning(self):
        selected_name = self.names_combobox.get()

        if not selected_name:
            tk.messagebox.showinfo("Invalid Input", "Please choose a name.")
            return

        meaning = get_name_meaning(selected_name)

        tk.messagebox.showinfo("Name and Meaning", f"{selected_name}\nАттын мааниси: {meaning}")

        like_name = tk.messagebox.askyesno("Name Confirmation", f"Тандаган ат жактыбы '{selected_name}'?")

        if not like_name:
            self.show_names()

    def get_valid_gender(self):
        while True:
            gender = self.gender_entry.get().lower()

            if gender in ['эркек', 'кыз']:
                self.gender_entry.config(state="disabled")
                return gender
            else:
                tk.messagebox.showinfo("Invalid Input", "Please enter 'boy' or 'girl'.")
                self.gender_entry.delete()

    def reset_ui(self):
        self.gender_entry.config(state="normal")
        self.gender_entry.delete(0, tk.END)
        self.initial_letter_entry.destroy()
        self.submit_gender_button.pack()

   
def generate_names(gender, initial_letter):
    boy_names = ["Куштарбек", "Кудайберди", "Карыбоз", "Канат", "Каныбек", "Камчы", "Жумгалбек", "Жоомарт", "Жолборс", "Жолболду", "Женишбек", "Жедигер"]
    girl_names = ["Жыпар","Жыргал", "Замира", "Зейнеп", "Зыйнат", "Кенже", "Кыял", "Марал", "Маржан", "Медина", "Мейиз", "Маржан", "Мээрим"]

    names_list = boy_names if gender == 'эркек' else girl_names

    if initial_letter:
        names_list = [name for name in names_list if name.lower().startswith(initial_letter)]

    return names_list

def get_name_meaning(name):
    return name_meanings.get(name, "Мааниси жок")

def main():
    root = tk.Tk()
    app = BabyNameGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()