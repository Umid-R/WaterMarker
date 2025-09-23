from tkinter import *
from PIL import Image, ImageTk
import tkmacosx
from tkinter import font, filedialog
from tkinter import colorchooser
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter



# ----- GUI -----
window = Tk()
window.minsize(1000,800)
window.title("ImageWaterMarker")
window.config(bg="#234C6A")

# ----- Global variables -----

image_original=None
marked_image=None
image_width=None
image_height=None
image_x=None
image_y=None
logo=None
logo_width=20
logo_height=20
watermark=''
logo_y=10
logo_x=None
font_family='Arial'
font_color="#821B1B"
font_size=20
blur=0
rotate=0


def show_home():
    

    # Remove all existing widgets
    for widget in window.winfo_children():
        widget.destroy()
    
    # Canvas that fills window
    canvas = Canvas(window,  bg="#91ADC8")
    canvas.pack(expand=True, fill='both')
    
    # Add Welcome text
    canvas.create_text(500, 320 ,text="Welcome", font=('Arial', 30, 'bold'),fill='#FAFDD6')

    # Buttons (parent = canvas)
    button_start = Button(canvas, text="Start",command=middle_page,height=2,width=12,font=('Arial', 14,'bold'),bd=0,highlightthickness=0,fg='#91ADC8')
    canvas.create_window(500,390, window=button_start)

    
    
def middle_page():
    # Remove all existing widgets
    for widget in window.winfo_children():
        widget.destroy()
    def download_file():
        global image_original, marked_image, image_height, image_width, image_x, image_y, logo_x
        for widget in window.winfo_children():
         widget.destroy()
        # Ask user where to save
        save_path = filedialog.askopenfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if save_path:
            image_original=Image.open(save_path)
            marked_image=image_original.copy()
            image_width=image_original.size[0]
            image_height=image_original.size[1]
            image_x=image_width/2
            image_y=image_height/2
            logo_x=image_width-logo_width-10
            
            
            watermarker()
            
        
    button_logo =Button(window, text='Download', height=2, width=12,
                            font=('Arial', 14, 'bold'), bd=0, fg="#698BAA",
                            command=download_file)
    button_logo.pack(expand='True')

def watermarker():
    
    
    

    # ----- Main Functions -----

    def show_image():
        global marked_image
        # Create a drawing object
        draw = ImageDraw.Draw(marked_image)
        # Draw text
        draw.text((image_x,image_y),watermark, font=ImageFont.truetype(font_family, font_size), fill=font_color)
        
        #Put blur
        # marked_image=marked_image.convert('RGBA')
        marked_image=marked_image.filter(ImageFilter.GaussianBlur(radius=blur)) 
        if logo:
            #Put Logo
            r_logo=logo.resize((logo_width,logo_height))
            marked_image.paste(r_logo, (logo_x, logo_y), r_logo)
        marked_image=marked_image.rotate(rotate,expand=True)
        
        
        
        
        
        
        
        
        tk_img = ImageTk.PhotoImage(marked_image.resize((400, 400)))
        image_label.config(image=tk_img)
        image_label.image = tk_img
        
    def update_watermark():
        global watermark , marked_image
        marked_image=image_original.copy()
        watermark=waterMark.get()
        
        show_image()
        
        
    def update_color():
        global font_color, marked_image
        marked_image=image_original.copy()
        font_color= colorchooser.askcolor()[1]
        color_button.config(bg=font_color)
        
        show_image()
        
    def update_fontfamily(font):
        global font_family, marked_image
        marked_image=image_original.copy()
        
        font_family=font
        show_image()
        
        
    def update_fontsize(val):
        global font_size, marked_image
        marked_image=image_original.copy()
        font_size = int(val)  # val comes from the slider
        show_image() 
        
    def set_blur(val):
        global blur , marked_image
        marked_image=image_original.copy()
        blur=int(val)
        
        show_image()
        
    def resize_logo(val):
        global logo_height, logo_width , marked_image
        marked_image=image_original.copy()
        
        logo_width=int(val)
        logo_height=int(val)
        
        show_image()
        
    def text_up():
        global image_y, marked_image
        marked_image = image_original.copy()
        if image_y <= 0:
            return
        image_y -= 10
        show_image()

    def text_down():
        global image_y, marked_image
        marked_image = image_original.copy()
        if image_y >= image_height-20:
            return
        image_y += 10
        show_image()

    def get_logo():
        global  logo, marked_image
        
        logo_path = filedialog.askopenfilename(
                title="Select Logo",
                filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if logo_path:
            marked_image = image_original.copy()
            logo=Image.open(logo_path).convert('RGBA')
            show_image()
        
    def text_left():
        global image_x, marked_image
        marked_image = image_original.copy()
        if image_x <= 0:
            return
        image_x -= 10
        show_image()

    def text_right():
        global logo_x, marked_image
        marked_image = image_original.copy()
        if logo_x >= image_width-30:
            return
        logo_x += 10
        show_image()



    def logo_up():
        global logo_y, marked_image
        marked_image = image_original.copy()
        if logo_y <= 0:
            return
        logo_y -= 10
        show_image()

    def logo_down():
        global logo_y, marked_image
        marked_image = image_original.copy()
        if logo_y >= image_height-20:
            return
        logo_y += 10
        show_image()

    def logo_left():
        global logo_x, marked_image
        marked_image = image_original.copy()
        if logo_x <= 0:
            return
        logo_x -= 10
        show_image()

    def logo_right():
        global logo_x, marked_image
        marked_image = image_original.copy()
        if logo_x >= image_width-30:
            return
        logo_x += 10
        show_image()
        

        
    def rotate_left():
        global marked_image,rotate
        marked_image=image_original.copy()
        rotate+=90
        
        show_image()
        
    def rotate_right():
        global marked_image,rotate
        marked_image=image_original.copy()
        rotate-=90
        
        show_image()
        
    def reset():
        global image_x,image_y,logo_width,logo_height, watermark, logo_y, logo_x,font_family, font_size,font_color, blur,marked_image,logo
        marked_image=image_original.copy()
        image_y=image_height/2
        logo=None
        logo_width=20
        logo_height=20
        watermark=''
        logo_y=10
        logo_x=image_width-logo_width-10
        font_family='Arial'
        font_color="#821B1B"
        font_size=20
        blur=0
        
        show_image()
        
    def save():
        global marked_image
        save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
            )
        if save_path:
            marked_image.save(save_path)
        
        
        
        
        










    #----- Buttons -----

    # Image Placeholder
    image_label=Label( image=None,  bg="#D2C1B6", width=1000, height=400)
    image_label.grid(row=0, column=0, columnspan=8)

    #Image Size Info
    image_info=Label(text=f'Image Size {image_height}/{image_width}(height/weight)',font=('Arial', 12), bg='#234C6A', fg="#E3D9D9")
    image_info.grid(row=1, column=0, columnspan=8)

    # Input Watermark
    waterMark = Entry(window, font=('Arial', 12), bg="#A7B9CA", width=25)
    waterMark.grid(row=2, column=0, columnspan=3,padx=(0,70))
    waterMark.insert(0, "Water Mark")
    def clear_text(event):
        if waterMark.get() == "Water Mark":
            waterMark.delete(0, END)
        
    waterMark.bind("<FocusIn>", clear_text)

    show_button=tkmacosx.Button(window,text='Show',font=('Arial', 12),width=60, fg='#91ADC8',command=update_watermark )
    show_button.grid(row=2, column=2)

    # Rotate Buttons
    icon1=Image.open('images/refresh-arrow.png').resize((20, 20))
    tk_icon1= ImageTk.PhotoImage(icon1)
    rotate_1=tkmacosx.Button(image=tk_icon1, bg='#234C6A', borderless=1,width=40,command=rotate_left)
    rotate_1.grid(row=2, column=3,sticky='E')

    icon2=Image.open('images/rotate-arrow.png').resize((20, 20))
    tk_icon2 = ImageTk.PhotoImage(icon2)
    rotate_2=tkmacosx.Button(image=tk_icon2, bg='#234C6A', borderless=1,width=40, command=rotate_right)
    rotate_2.grid(row=2, column=4,sticky='W')

    # Logo  Button
    logo_button=tkmacosx.Button(text='Select Logo',font=('Arial', 12), height=40, fg='#91ADC8',command=get_logo )
    logo_button.grid(row=2, column=5,columnspan=3)

    # Watermarker Controllers
    up1=Image.open('images/caret-arrow-up.png').resize((60,30))
    up_icon1 = ImageTk.PhotoImage(up1)
    up1=tkmacosx.Button( image=up_icon1,bg='#234C6A', borderless=1, command=text_up)
    up1.grid(row=3, column=0, columnspan=3)

    left1=Image.open('images/black-triangular-arrowhead-pointing-to-left-direction.png').resize((30,60))
    left_icon1 = ImageTk.PhotoImage(left1)
    left1=tkmacosx.Button( image=left_icon1,bg='#234C6A', borderless=1,command=text_left)
    left1.grid(row=4, column=0,sticky='E')

    right1=Image.open('images/arrowhead-pointing-to-the-right.png').resize((30,60))
    right_icon1 = ImageTk.PhotoImage(right1)
    right1=tkmacosx.Button( image=right_icon1,bg='#234C6A', borderless=1,command=text_right)
    right1.grid(row=4, column=2,sticky='W')

    down1=Image.open('images/down.png').resize((60,30))
    down_icon1 = ImageTk.PhotoImage(down1)
    down1=tkmacosx.Button( image=down_icon1,bg='#234C6A', borderless=1, command=text_down)
    down1.grid(row=5, column=0, columnspan=3)





    up2=Image.open('images/caret-arrow-up.png').resize((60,30))
    up_icon2 = ImageTk.PhotoImage(up2)
    up2=tkmacosx.Button( image=up_icon2,bg='#234C6A', borderless=1,command=logo_up)
    up2.grid(row=3, column=5, columnspan=3, sticky="S")

    left2=Image.open('images/black-triangular-arrowhead-pointing-to-left-direction.png').resize((30,60))
    left_icon2 = ImageTk.PhotoImage(left2)
    left2=tkmacosx.Button( image=left_icon2,bg='#234C6A', borderless=1,command=logo_left)
    left2.grid(row=4, column=5,sticky="E")

    right2=Image.open('images/arrowhead-pointing-to-the-right.png').resize((30,60))
    right_icon2 = ImageTk.PhotoImage(right2)
    right2=tkmacosx.Button( image=right_icon2,bg='#234C6A', borderless=1,command=logo_right)
    right2.grid(row=4, column=7)

    down2=Image.open('images/down.png').resize((60,30))
    down_icon2 = ImageTk.PhotoImage(down2)
    down2=tkmacosx.Button( image=down_icon2,bg='#234C6A', borderless=1,command=logo_down)
    down2.grid(row=5, column=5, columnspan=3,sticky='N')


    # Blur 
    blur_label=Label(text='Blur',font=('Arial', 12), bg='#234C6A', pady=5 )
    blur_label.grid(row=4, column=3,pady=(15,0))

    blur_slider = Scale( from_=0, to=20, orient=HORIZONTAL, bg='#234C6A', command=set_blur)
    blur_slider.grid(row=4, column=4)

    #Font
    font_label=Label(text='Font',font=('Arial', 12), bg='#234C6A', pady=5 )
    font_label.grid(row=6, column=0,pady=(20,0))
    #Font Family Path
    font_paths = {
        "Arial": "/System/Library/Fonts/Supplemental/Arial.ttf",
        "Courier New": "/System/Library/Fonts/Supplemental/Courier New.ttf",
        "Times New Roman": "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
        "Verdana": "/System/Library/Fonts/Supplemental/Verdana.ttf",
        "Georgia": "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "Helvetica": "/System/Library/Fonts/Helvetica.ttc"
    }

    # Font family list
    all_fonts = ["Arial","Courier New","Times New Roman","Verdana","Georgia","Helvetica"]  # all available system fonts
    # Font family dropdown
    font_var = StringVar(value="Arial")
    font_menu = OptionMenu( window,font_var, *all_fonts,command=update_fontfamily)
    font_menu.grid(row=6, column=1,pady=(20,0))


    #Color
    color_label=Label(text='Color',font=('Arial', 12), bg='#234C6A', pady=5 )
    color_label.grid(row=7, column=0)

    color_button=tkmacosx.Button(width=25, height=25, bg=font_color, borderless=1, command=update_color)
    color_button.grid(row=7, column=1,)

    #Font size
    fontsize_label=Label(text='Font size',font=('Arial', 12), bg='#234C6A', pady=5 )
    fontsize_label.grid(row=8, column=0,pady=(10,0))

    size_slider = Scale( from_=8, to=400, orient=HORIZONTAL, bg='#234C6A',command=update_fontsize)
    size_slider.set(20)
    size_slider.grid(row=8, column=1)

    # Reset Button
    button_reset = Button(window, text="Reset", height=1, width=4, font=('Arial', 14, 'bold'),bd=0, fg='red',command=reset)
    button_reset.grid(column=3, row=8)
            
    # Save Button
    button_save = Button(text='Save', height=1, width=6,font=('Arial', 14, 'bold'), bd=0, fg="#45B88C",command=save)
    button_save.grid(column=4,row=8)


    #Logo size
    fontsize_label=Label(text='Size',font=('Arial', 12), bg='#234C6A', pady=5 )
    fontsize_label.grid(row=8, column=6,pady=(15,0))

    size_slider = Scale( from_=8, to=800, orient=HORIZONTAL, bg='#234C6A', command=resize_logo)
    size_slider.set(20)
    size_slider.grid(row=8, column=7)


    show_image()

show_home()


# ----- App Mainloop ----- 
window.mainloop()
