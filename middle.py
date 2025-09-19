import tkinter as tk
from tkinter import filedialog



window=tk.Tk()
window.minsize(800,800)
def middle_page():
    def download_file():
        # Ask user where to save
        save_path = filedialog.askopenfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if save_path:
            return save_path
        
    button_logo = tk.Button(window, text='Logo', height=2, width=12,
                            font=('Arial', 14, 'bold'), bd=0, fg='#91ADC8',
                            command=download_file)
    button_logo.pack(expand='True')


    window.mainloop()