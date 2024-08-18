import tkinter as tk
from tkinter import ttk
import obd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class OBDTool:
    def __init__(self, interface='usb'):
        self.interface = interface
        self.connection = self.connect()
        self.root = tk.Tk()
        self.root.title("OBD-II Tool")
        self.create_widgets()
        self.running = False
        self.root.mainloop()

    def connect(self):
        if self.interface == 'usb':
            # Connect with USB
            connection = obd.OBD()  # Assuming pyobd handles usb
        return connection

    def create_widgets(self):
        # Create a frame for the chart and terminal output
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # Create a frame for the chart
        self.chart_frame = tk.Frame(self.frame)
        self.chart_frame.pack(fill="both", expand=True)

        # Create a figure and axis for the chart
        self.figure, self.axis = plt.subplots()
        self.axis.set_title("Engine Data")
        self.axis.set_xlabel("Time")
        self.axis.set_ylabel("Value")

        # Create a canvas for the chart
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a label to display the terminal output
        self.label = tk.Label(self.frame, text="Terminal Output:")
        self.label.pack()

        # Create a text box to display the terminal output
        self.text_box = tk.Text(self.frame)
        self.text_box.pack()

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(fill="x")

        # Create a start button
        self.start_button = tk.Button(self.button_frame, text="RUN", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        # Create a stop button
        self.stop_button = tk.Button(self.button_frame, text="STOP", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)

        # Create a clear button
        self.clear_button = tk.Button(self.button_frame, text="CLEAR", command=self.clear)
        self.clear_button.pack(side=tk.LEFT)

    def start(self):
        self.running = True
        self.update_data()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def clear(self):
        self.text_box.delete(1.0, tk.END)

    def update_data(self):
        if self.running:
            # Read data from the OBD-II connection
            engine_data = self.connection.query(obd.commands.SPEED)

            if engine_data.value is not None:
                # Update the chart
                self.axis.plot(engine_data.value, label="Engine Speed")
                self.canvas.draw()

                # Update the terminal output
                self.text_box.insert(tk.END, f"Engine Speed: {engine_data.value}\n")
            else:
                self.text_box.insert(tk.END, "No data available. Check OBD-II connection.\n")

            # Call this function again after a short delay
            self.root.after(1000, self.update_data)

if __name__ == "__main__":
    tool = OBDTool(interface='usb')