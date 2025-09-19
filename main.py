import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


window = tk.Tk()
window.title("Image Watermarker")
window.minsize(800, 800)


    
def show_home():
    

    # Remove all existing widgets
    for widget in window.winfo_children():
        widget.destroy()
    
    # Canvas that fills window
    canvas = tk.Canvas(window,  bg="#91ADC8")
    canvas.pack(expand=True, fill='both')
    
    # Add Welcome text
    canvas.create_text(400, 320 ,text="Welcome", font=('Arial', 30, 'bold'),fill='#FAFDD6')

    # Buttons (parent = canvas)
    button_start = tk.Button(canvas, text="Start",command=middle_page,height=2,width=12,font=('Arial', 14,'bold'),bd=0,highlightthickness=0,fg='#91ADC8')
    canvas.create_window(400,390, window=button_start)

    button_works = tk.Button(canvas, text="My Works",height=2,width=12,font=('Arial', 14,'bold'),bd=0,highlightthickness=0,fg='#91ADC8')
    canvas.create_window(400, 460, window=button_works)

def middle_page():
    # Remove all existing widgets
    for widget in window.winfo_children():
        widget.destroy()
    def download_file():
        for widget in window.winfo_children():
         widget.destroy()
        # Ask user where to save
        save_path = filedialog.askopenfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if save_path:
            watermarker_page(save_path)
        
    button_logo = tk.Button(window, text='Download', height=2, width=12,
                            font=('Arial', 14, 'bold'), bd=0, fg="#698BAA",
                            command=download_file)
    button_logo.pack(expand='True')
    

def watermarker_page(path):
    global copy_pil_image, tk_image, label, original_image
    # Remove all existing widgets
    for widget in window.winfo_children():
        widget.destroy()
        # Open PIL image
    original_image = Image.open(path)
    original_image.thumbnail((800, 400))  # fit window
    # Global working image
    copy_pil_image= original_image.copy()

    # Convert to Tkinter image
    tk_image = ImageTk.PhotoImage(original_image)
    # Save function
    def save_image():
        global copy_pil_image
        # Ask user where to save
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if save_path:
            copy_pil_image.save(save_path)

    # Clear button function
    def clear():
        global tk_image, copy_pil_image
        copy_pil_image=original_image.copy()
        tk_image = ImageTk.PhotoImage(copy_pil_image)
        label.config(image=tk_image)
        label.image = tk_image  # keep reference

    # Add text
    def add_text():
        global copy_pil_image ,tk_image
        # Text Entry
        text_entry = tk.Entry(window, font=('Arial', 14), fg='gray')
        text_entry.grid(column=0, row=2, padx=10, pady=10)
        text_entry.insert(0, "Text")
        def clear_text(event):
            if text_entry.get() == "Text":
                text_entry.delete(0, tk.END)
        text_entry.bind("<FocusIn>", clear_text)
        
        # Color Entry
        color_entry = tk.Entry(window, font=('Arial', 14), fg='gray')
        color_entry.grid(column=0, row=3, padx=10, pady=10)
        color_entry.insert(0, "Color")
        def clear_color(event):
            if color_entry.get() == "Color":
                color_entry.delete(0, tk.END)
        color_entry.bind("<FocusIn>", clear_color)
        
        # Font Size
        size_entry = tk.Entry(window, font=('Arial', 14), fg='gray')
        size_entry.grid(column=0, row=4, padx=10, pady=10)
        size_entry.insert(0, "Font Size")
        def clear_size(event):
            if size_entry.get() == "Font Size":
                size_entry.delete(0, tk.END)
        size_entry.bind("<FocusIn>", clear_size)
        
        # Reset Button
        button_reset = tk.Button(window, text="Reset", height=1, width=4, font=('Arial', 14, 'bold'),bd=0, fg='red', command=clear)
        button_reset.grid(column=1, row=6, pady=30)
        
        # Save Button
        button_save = tk.Button(text='Save', height=1, width=6,font=('Arial', 14, 'bold'), bd=0, fg="#45B88C",command=save_image)
        button_save.grid(column=2,row=6)

        # Submit Button
        def submit():
            global copy_pil_image, tk_image
            text = text_entry.get() 
            color = color_entry.get() 
            size = int(size_entry.get())
            
            # Always start from a fresh copy of original
            
            draw = ImageDraw.Draw(copy_pil_image)

            img_width, img_height = copy_pil_image.size
            font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", size=size)

            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            x = (img_width - text_width) / 2
            y = (img_height - text_height) / 2

            draw.text((x, y), text=text, fill=color, font=font)

            tk_image = ImageTk.PhotoImage(copy_pil_image)
            label.config(image=tk_image)
            label.image = tk_image  # keep reference

            text_entry.delete(0, tk.END)
            color_entry.delete(0, tk.END)
            size_entry.delete(0, tk.END)

        button_ok = tk.Button(window, text='OK', height=1, width=6,
                            font=('Arial', 14, 'bold'), bd=0, fg='#91ADC8',
                            command=submit)
        button_ok.grid(column=0, row=5)
        
    

    # Add logo
    def add_logo():
        global tk_image, copy_pil_image

        # If we already have a working copy, continue from that, else fresh copy
        if 'copy_pil_image' not in globals():
            copy_pil_image = original_image.copy()

        # Ask user to pick a logo file
        logo_path = filedialog.askopenfilename(
            title="Select Logo",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if logo_path:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((80, 40))  # fixed size (80x40)

            # Position: top-right
            x = copy_pil_image.width - logo.width
            y = 0

            copy_pil_image.paste(logo, (x, y), logo)

            tk_image = ImageTk.PhotoImage(copy_pil_image)
            label.config(image=tk_image)
            label.image = tk_image  # keep reference

            
        

    

    

    # Label
    label = tk.Label(window, image=tk_image, bg='#FAFDD6', width=800, height=400)
    label.grid(column=0, row=0, columnspan=4)

    # Buttons 
    button_text = tk.Button(window, text='Text', height=2, width=12,
                            font=('Arial', 14, 'bold'), bd=0, fg='#91ADC8',
                            command=add_text)
    button_text.grid(column=0, row=1, pady=30)

    button_logo = tk.Button(window, text='Logo', height=2, width=12,
                            font=('Arial', 14, 'bold'), bd=0, fg='#91ADC8',
                            command=add_logo)
    button_logo.grid(column=3, row=1, pady=30)

    


show_home() 

window.mainloop()
