import tkinter as tk
import qrcode
from PIL import Image, ImageTk
def generate_qr_code():
    data = qr_data_entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image = qr_image.resize((200, 200), Image.ANTIALIAS)
        qr_photo = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_photo)
        qr_label.photo = qr_photo
    else:
        qr_label.config(image="")
        qr_label.photo = None
# Create a tkinter window
window = tk.Tk()
window.title("QR Code Generator")
# Create a label
qr_label = tk.Label(window)
qr_label.pack()
# Create an entry for QR code data
qr_data_label = tk.Label(window, text="Enter data:")
qr_data_label.pack()
qr_data_entry = tk.Entry(window)
qr_data_entry.pack()
# Create a button to generate QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()
# Start the GUI main loop
window.mainloop()
