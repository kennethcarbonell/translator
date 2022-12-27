import tkinter as tk
import langdetect
from googletrans import Translator

# tkinter window
window = tk.Tk()
window.title("Language Translator")

# Sets size and centers window
window.geometry("600x400+{}+{}".format(int((window.winfo_screenwidth() - 600) / 2), int((window.winfo_screenheight() - 400) / 2)))

# Label prompt
label = tk.Label(window, text="Enter some text to translate:", font=("Helvetica", 16))
label.pack(padx=20, pady=20)

# Creates the text box for user input
input_text_box = tk.Text(window, height=5, wrap="word")
input_text_box.pack(padx=10, pady=10)

# Binds the enter button to also act is if it pressed the translate button
input_text_box.bind("<Return>", lambda event: translate(input_text_box, output_text))
input_text_box.pack(padx=10, pady=10)

# Initialize translator
translator = Translator()

# text label to display what you typed
input_text_label = tk.Label(window, font=("Verdana", 12))
input_text_label.pack(padx=10, pady=10)

# Label to indicate where translated text is outputted
output_text = tk.Text(window, height=2, width=30, font=("Verdana", 16), wrap="word", state="disabled")
output_text.pack()

# Label for the pronunciation is outputted
pronunciation_label = tk.Label(window, font=("Helvetica", 13))
pronunciation_label.pack()

# Creates button to get user input and translate
button = tk.Button(window, text="Translate", command=lambda: translate(input_text_box, output_text))
button.pack(padx=10, pady=10)

# translate function that does the translating
def translate(input_text_box, output_text):

  # Gets user input
  input_text = input_text_box.get("1.0", "end")
  input_text_label.config(text=input_text)
  
  # Detect the language of the input text
  detected_lang = langdetect.detect(input_text)
  
  # Set the destination language
  if detected_lang == 'en':
    dest_lang = 'ja'
  else:
    dest_lang = 'en'
  
  # Translate the input text
  translated = translator.translate(input_text, dest=dest_lang)

  # Print the text
  pronunce = f"{translated.pronunciation}"
  build_output_text = f"{translated.text}"

  # Outputs the text into a text box which you can copy from
  output_text.config(state="normal")
  output_text.delete("1.0", "end")
  output_text.insert("1.0", build_output_text, "center")
  output_text.tag_config("center", justify="center")
  output_text.config(state="disabled")

  pronunciation_label.config(text=pronunce)

  input_text_box.delete("1.0", "end")

window.mainloop()
