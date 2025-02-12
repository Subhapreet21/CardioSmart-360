from tkinter import *

Icon_window = Tk()
Icon_window.title("Info")
Icon_window.geometry("700x700+300+100")

# icon_image
icon_image = PhotoImage(file="Images/info.png")
Icon_window.iconphoto(False, icon_image)

# Heading
Label(Icon_window, text="Information related to dataset", font="robot 19 bold").pack(padx=20, pady=20)

# Info with ranges
Label(Icon_window, text="age - age in years (Range: 18-100)", font="arial 11").place(x=20, y=100)
Label(Icon_window, text="sex - sex (1 = male; 0 = female)", font="arial 11").place(x=20, y=130)
Label(Icon_window, text="cp - chest pain type (Range: 0-3)", font="arial 11").place(x=20, y=160)
Label(Icon_window, text="trestbps - resting blood pressure (Range: 90-200 mm Hg)", font="arial 11").place(x=20, y=190)
Label(Icon_window, text="chol - serum cholesterol (Range: 120-600 mg/dl)", font="arial 11").place(x=20, y=220)
Label(Icon_window, text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)", font="arial 11").place(x=20, y=250)
Label(Icon_window, text="restecg - resting ECG results (Range: 0-2)", font="arial 11").place(x=20, y=280)
Label(Icon_window, text="thalach - maximum heart rate achieved (Range: 70-220 bpm)", font="arial 11").place(x=20, y=310)
Label(Icon_window, text="exang - exercise induced angina (1 = yes; 0 = no)", font="arial 11").place(x=20, y=340)
Label(Icon_window, text="oldpeak - ST depression (Range: 0-6 mm)", font="arial 11").place(x=20, y=370)
Label(Icon_window, text="slope - ST segment slope (Range: 0-2)", font="arial 11").place(x=20, y=400)
Label(Icon_window, text="ca - major vessels (Range: 0-4)", font="arial 11").place(x=20, y=430)
Label(Icon_window, text="thal - Thalassemia (Range: 0-2)", font="arial 11").place(x=20, y=460)
Label(Icon_window, text="smoker - smoking risk (0 = low; 1 = high)", font="arial 11").place(x=20, y=490)

# Adding a note for clarity
Label(Icon_window, text="Note: Ranges are indicative and may vary based on dataset.", font="arial 10 italic", fg="blue").place(x=20, y=530)

Icon_window.mainloop()
