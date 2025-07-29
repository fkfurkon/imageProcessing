class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processing App")
        
        self.image_label = Label(master, text="No image loaded")
        self.image_label.pack()

        self.process_button = Button(master, text="Process Image", command=self.process_image)
        self.process_button.pack()

        self.brightness_label = Label(master, text="Brightness:")
        self.brightness_label.pack()
        self.brightness_scale = Scale(master, from_=0, to=100, orient=HORIZONTAL)
        self.brightness_scale.pack()

        self.filter_label = Label(master, text="Filter:")
        self.filter_label.pack()
        self.filter_options = ["None", "Grayscale", "Sepia"]
        self.filter_var = StringVar(master)
        self.filter_var.set(self.filter_options[0])
        self.filter_menu = OptionMenu(master, self.filter_var, *self.filter_options)
        self.filter_menu.pack()

        self.graph_button = Button(master, text="Show Graph", command=self.show_graph)
        self.graph_button.pack()

    def process_image(self):
        # Logic to process the image based on GUI parameters
        pass

    def show_graph(self):
        # Logic to display the graph based on processed image properties
        pass