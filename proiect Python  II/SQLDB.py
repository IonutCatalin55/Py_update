import sqlite3
from tkinter import messagebox

import customtkinter
from customtkinter import *

def insert_lamina(name, description, thickness, Ef, Uf, Gf, Em, Um, Gm, Fi, Nxx, Nyy, Nxy):
    try:
        if not (name and description and thickness and Ef and Uf and Gf and Em and Um and Gm and Fi and Nxx and Nyy and Nxy):
            show_error_message("Enter all fields")
            return

        name_value = str(name)
        description_value = str(description)
        thickness_value = float(thickness)
        Ef_value = float(Ef)
        Uf_value = float(Uf)
        Gf_value = float(Gf)
        Em_value = float(Em)
        Um_value = float(Um)
        Gm_value = float(Gm)
        Fi_value = int(Fi)
        Nxx_value = int(Nxx)
        Nyy_value = int(Nyy)
        Nxy_value = int(Nxy)

        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS lamina (name TEXT UNIQUE, description TEXT, thickness REAL, Ef REAL, Uf REAL, "
            "Gf REAL, Em REAL, Um REAL, Gm REAL, Fi REAL, Nxx INTEGER, Nyy INTEGER, Nxy INTEGER)"
        )

        # Check if an entry with the same name already exists
        cur.execute("SELECT * FROM lamina WHERE name = ?", (name_value,))
        if cur.fetchone():
            show_error_message(f"Entry with name '{name_value}' already exists.")
        else:
            cur.execute(
                "INSERT INTO lamina (name, description, thickness, Ef, Uf, Gf, Em, Um, Gm, Fi, Nxx, Nyy, Nxy) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name_value, description_value, thickness_value, Ef_value, Uf_value, Gf_value, Em_value, Um_value, Gm_value, Fi_value, Nxx_value, Nyy_value, Nxy_value)
            )
            con.commit()
            show_info_message()

        con.close()
    except ValueError:
        show_error_message("Check entered data!")
    except sqlite3.Error as e:
        show_error_message(f"Database error: {e}")
    except Exception as e:
        show_error_message(f"Unexpected error: {e}")

def search_lamina(query):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM lamina WHERE name = ?", (query,))
    row = cur.fetchone()
    con.commit()
    con.close()
    return row

def fetch_all_laminas():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("SELECT name FROM lamina")
    rows = cur.fetchall()
    con.close()
    return [i[0] for i in rows]

def show_error_message(entry):
    """
    Valorile nu sunt corespunzatoare
    """
    messagebox.showerror("Error", entry)

def show_info_message():
    """
    Displays an informational popup message.
    """
    messagebox.showinfo("Success", "Lamina added successfully.")
