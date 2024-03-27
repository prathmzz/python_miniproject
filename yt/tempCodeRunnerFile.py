filename = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
    if filename:
        try:
            image = Image.open(filename)
            image_data = open(filename, 'rb').read()
            insert_user_data('', '', '', image_data)
            switch_to_card_page()  # After uploading image, switch to card page
        except Exception as e:
            print("Error opening or processing image:", e)