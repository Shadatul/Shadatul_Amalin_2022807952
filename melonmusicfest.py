import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="melon_music_festival"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():

    # List to store selected stages
    selected_stages = []

    # Check which stages are selected
    if stage_type_var_Sky_Rocket_Melon_Stage.get():
        selected_stages.append("Sky Rocket Melon Stage")
    if stage_type_var_Sugar_Kiss_Melon_Stage.get():
        selected_stages.append("Sugar Kiss Melon Stage")
    if stage_type_var_Honey_Globe_Melon_Stage.get():
        selected_stages.append("Honey Globe Melon Stage")

    stage_type = selected_stages
    ticket_type = ticket_type_var.get()
    pack = int(pack_entry.get())
    full_name = str(full_name_entry.get())

    # Calculate the total price. This will be derived from your selection (stage_type, ticket_type, pack).
    price_per_ticket = {
        "VIP": 550,
        "General Admission": 350
    }
    
    # Calculate the total price for multiple selected stages
    total_price = sum(price_per_ticket[ticket_type] * pack for _ in selected_stages)

     # To insert your Data to your database
    sql = "INSERT INTO `mmf_stage` (full_name, stage_type, ticket_type, pack, price) VALUES (%s, %s, %s, %s, %s)"
    val = (full_name, ", ".join(selected_stages), ticket_type, pack, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output
    output_label.config(text=f"Name: {full_name} \nStages: {', '.join(selected_stages)}\n Ticket type: {ticket_type}\n Pack: {pack}\n Total Price: RM{total_price}")


# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Melon Music Festival")
root.geometry('700x710')


# Page Title
label = tk.Label(root, text='Melon Music Festival Ticketing', font=("Segoe UI Black",14, "bold"))
label.pack(ipadx=5, ipady=5)

# Prices List by using textbox
prices_text = tk.Text(root, height=15, width=100, font= ("Perpetua", 11))
prices_text.pack(pady=5)

# The defined list by using pricebox
prices_text.insert(tk.END, "Stages & Prices:\n\n")
prices_text.insert(tk.END, "Sky Rocket Melon Stage \nDate: 24th April 2024 \nLineup:\nTilly Birds, Mirrr, Scrubb, Only Monday, Safeplanet, Polycat, Three Man Down, Cocktail, MEAN, Getsunova, \nFellow Fellow, Slapkiss, HYBS, Anatomy Rabbit, Dept, Pop Pongkool, Qler, TaitosmitH, Yented, Paper Planes \nPrices: \nVIP:RM550 General Admission:RM350\n\n")
prices_text.insert(tk.END, "Sugar Kiss Melon Stage \nDate: 25th April 2024 \nLineup: \nMorvasu, Pearwah, Serious Bacon, Ploychompoo, Sarah Salola, Nont Tanont, Jeff Satur, Timethai, Autta, Jaonaay, \nALLY, Nanon, Meyou, Ink Waruntorn, Bowkylion, Luss, Viollete Wautier, The Toys, Zom Marie, Jaokhun \nPrices: \nVIP:RM550 General Admission:RM350\n\n")
prices_text.insert(tk.END, "Honey Globe Melon Stage \nDate: 26th April 2024 \nLineup: \n9by9th, 4EVE, Sizzy, DIDIxDADA, New Country, Trinity, BILLKINxPP KRIT, Atlas, 4Miz, LYKN, \nJAYLERRxICE PARIS, Perses, Proxie, Bus, PiXXiE, GEMINIxFOURTH, LAZ1, Bamm, Pretzele, Mxfruit \nPrices: \nVIP:RM550 General Admission:RM350\n\n")
prices_text.configure(state='disabled')

# Name Entry. Label and user can insert data thru entry
full_name_label = tk.Label(root, text="Full Name:")
full_name_label.pack()
full_name_entry = tk.Entry(root)
full_name_entry.pack()

# Stage Type Checkbox (Label)
packs_label = tk.Label(root, text="Select Stages")
packs_label.pack()

# Stage Type Checkboxes
stage_type_var=tk.Label(root)
stage_type_var_Sky_Rocket_Melon_Stage = tk.BooleanVar(root)
stage_type_var_Sugar_Kiss_Melon_Stage = tk.BooleanVar(root)
stage_type_var_Honey_Globe_Melon_Stage = tk.BooleanVar(root)

Sky_Rocket_Melon_Stage_checkbox = tk.Checkbutton(root, text="Sky Rocket Melon Stage", variable=stage_type_var_Sky_Rocket_Melon_Stage)
Sky_Rocket_Melon_Stage_checkbox.pack()

Sugar_Kiss_Melon_Stage_checkbox = tk.Checkbutton(root, text="Sugar Kiss Melon Stage", variable=stage_type_var_Sugar_Kiss_Melon_Stage)
Sugar_Kiss_Melon_Stage_checkbox.pack()

Honey_Globe_Melon_Stage_checkbox = tk.Checkbutton(root, text="Honey Globe Melon Stage", variable=stage_type_var_Honey_Globe_Melon_Stage)
Honey_Globe_Melon_Stage_checkbox.pack()

# Ticket Type Dropdown
ticket_type_var = tk.StringVar(root)
ticket_type_var.set("Select Your Ticket Type")  # Default value before your selection
trip_dropdown = tk.OptionMenu(root, ticket_type_var, "VIP", "General Admission")
trip_dropdown.pack(pady=5)

# Packs Entry. Label and user can insert data thru entry
pack_label = tk.Label(root, text="Packs:")
pack_label.pack()
pack_entry = tk.Entry(root)
pack_entry.pack()

# Save Button
save_button = tk.Button(root, text="Total", command=collect_data)
save_button.pack(pady=5)


# Output Label & result
label = tk.Label(root, text='Total Prices', font=("Sylfaen",12))
label.pack(ipadx=10, ipady=5)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()