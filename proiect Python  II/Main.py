import math
from tkinter import *
import customtkinter as ctk
from PIL import Image
from CTkMenuBar import *
from MaterialCompozitStratificat import MaterialCompozitStratificat, session
import tkinter as tk
from lamina import Lamina
import SQLDB
from SQLDB import *
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np
from sandwich import Sandwich

image = customtkinter.CTkImage(light_image=Image.open("resources/tech1.jpg"),
                               dark_image=Image.open("resources/tech1.jpg"),
                               size=(600, 600))

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x800")
root.title("Calculator 1.0")
font = customtkinter.CTkFont(family="Helvetica", size=34,
                             weight="bold", slant="italic", underline=True, overstrike=False)
menu = CTkMenuBar(root)

def addComposite():
    ################################################################ modificat
    image3 = customtkinter.CTkImage(light_image=Image.open("resources/tech1.jpg"),
                                    dark_image=Image.open("resources/tech1.jpg"),
                                    size=(600, 400))

    newWindow = customtkinter.CTkToplevel()
    newWindow.grid()

    newWindow.title("Create composite material")

    laminaFrameComposite = customtkinter.CTkFrame(master=newWindow, fg_color="transparent", bg_color="transparent",
                                                  width=420, height=150)
    laminaFrameComposite.grid(row=0, column=0, padx=20, pady=20)

    l_number = customtkinter.CTkLabel(laminaFrameComposite, text="Number of Laminas")
    l_number.grid(row=0, column=0, padx=5, pady=5)
    laminaNumber = customtkinter.CTkEntry(laminaFrameComposite, placeholder_text="Enter lamina number!",
                                          placeholder_text_color="white", width=200)
    laminaNumber.grid(row=0, column=1, padx=5, pady=5)

    l_orientation = customtkinter.CTkLabel(laminaFrameComposite, text="Laminas Orientation")
    l_orientation.grid(row=1, column=0, padx=5, pady=5)
    laminaOrientation = customtkinter.CTkEntry(laminaFrameComposite, placeholder_text="eg. 90/45/0/45/90",
                                               placeholder_text_color="white", width=200)
    laminaOrientation.grid(row=1, column=1, padx=5, pady=5)

    variable3 = StringVar()

    l_selectLamina = customtkinter.CTkLabel(laminaFrameComposite, text="Select Existing Lamina")
    l_selectLamina.grid(row=2, column=0, padx=5, pady=5)
    selectLamina = customtkinter.CTkComboBox(laminaFrameComposite, width=200, variable=variable3, state='readonly')
    selectLamina.set('Select')

    selectLamina.grid(row=2, column=1, padx=5, pady=5)

    laminaFrame = customtkinter.CTkScrollableFrame(master=newWindow, fg_color="transparent", bg_color="transparent",
                                                   width=380, height=320)
    laminaFrame.grid(row=1, column=0, padx=20, pady=20)

    label2 = customtkinter.CTkLabel(newWindow, text="", image=image3)
    label2.grid(row=2, column=0)

    l_name = customtkinter.CTkLabel(laminaFrame, text="Lamina Name")  # nu fct textvariable
    l_name.grid(row=0, column=0, padx=5, pady=5)
    laminaName = customtkinter.CTkEntry(laminaFrame, placeholder_text="Lamina Name",
                                        placeholder_text_color="white", width=200)  # , textvariable= text)
    laminaName.grid(row=0, column=1, padx=5, pady=5)
    l_description = customtkinter.CTkLabel(laminaFrame, text="Lamina Description")
    l_description.grid(row=1, column=0, padx=5, pady=5)
    laminaDescription = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter lamina description!",
                                               placeholder_text_color="white", width=200)
    laminaDescription.grid(row=1, column=1, padx=5, pady=5)
    l_grosime = customtkinter.CTkLabel(laminaFrame, text="Thickness - [mm]")
    l_grosime.grid(row=2, column=0, padx=5, pady=5)
    laminaGrosime = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter thickness!",
                                           placeholder_text_color="white", width=200)
    laminaGrosime.grid(row=2, column=1, padx=5, pady=5)
    l_Ef = customtkinter.CTkLabel(laminaFrame, text="Ef")
    l_Ef.grid(row=3, column=0, padx=5, pady=5)
    laminaEf = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Ef!", placeholder_text_color="white",
                                      width=200)
    laminaEf.grid(row=3, column=1, padx=5, pady=5)
    l_Uf = customtkinter.CTkLabel(laminaFrame, text="Uf")
    l_Uf.grid(row=4, column=0, padx=5, pady=5)
    laminaUf = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Uf!", placeholder_text_color="white",
                                      width=200)
    laminaUf.grid(row=4, column=1, padx=5, pady=5)
    l_Gf = customtkinter.CTkLabel(laminaFrame, text="Gf")
    l_Gf.grid(row=5, column=0, padx=5, pady=5)
    laminaGf = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Gf!", placeholder_text_color="white",
                                      width=200)
    laminaGf.grid(row=5, column=1, padx=5, pady=5)
    l_Em = customtkinter.CTkLabel(laminaFrame, text="Em")
    l_Em.grid(row=6, column=0, padx=5, pady=5)
    laminaEm = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Em!", placeholder_text_color="white",
                                      width=200)
    laminaEm.grid(row=6, column=1, padx=5, pady=5)
    l_Um = customtkinter.CTkLabel(laminaFrame, text="Um")
    l_Um.grid(row=7, column=0, padx=5, pady=5)
    laminaUm = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Um!", placeholder_text_color="white",
                                      width=200)
    laminaUm.grid(row=7, column=1, padx=5, pady=5)
    l_Gm = customtkinter.CTkLabel(laminaFrame, text="Gm")
    l_Gm.grid(row=8, column=0, padx=5, pady=5)
    laminaGm = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Gm!", placeholder_text_color="white",
                                      width=200)
    laminaGm.grid(row=8, column=1, padx=5, pady=5)
    l_Fi = customtkinter.CTkLabel(laminaFrame, text="Fi")
    l_Fi.grid(row=9, column=0, padx=5, pady=5)
    laminaFi = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Fi!", placeholder_text_color="white",
                                      width=200)
    laminaFi.grid(row=9, column=1, padx=5, pady=5)
    l_Nxx = customtkinter.CTkLabel(laminaFrame, text="Nxx")
    l_Nxx.grid(row=10, column=0, padx=5, pady=5)
    laminaNxx = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Nxx!", placeholder_text_color="white",
                                       width=200)
    laminaNxx.grid(row=10, column=1, padx=5, pady=5)
    l_Nyy = customtkinter.CTkLabel(laminaFrame, text="Nyy")
    l_Nyy.grid(row=11, column=0, padx=5, pady=5)
    laminaNyy = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Nyy!", placeholder_text_color="white",
                                       width=200)
    laminaNyy.grid(row=11, column=1, padx=5, pady=5)
    l_Nxy = customtkinter.CTkLabel(laminaFrame, text="Nxy")
    l_Nxy.grid(row=12, column=0, padx=5, pady=5)
    laminaNxy = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Nxy!", placeholder_text_color="white",
                                       width=200)
    laminaNxy.grid(row=12, column=1, padx=5, pady=5)

    Apply_button = customtkinter.CTkButton(laminaFrameComposite, corner_radius=15, text="Apply selected lamina",
                                           cursor='hand2'
                                           , command=lambda: insertLamina())
    Apply_button.grid(pady=20)

    calculate_button = customtkinter.CTkButton(laminaFrameComposite, corner_radius=15, text="Calculate",
                                               command=lambda: compute_mar_elast(),
                                               cursor='hand2')
    calculate_button.grid(pady=20)

    ################################################################

    def retriveAllLaminas():
        laminas = fetch_all_laminas()
        selectLamina.configure(values=laminas)

    def insertLamina():
        selection = variable3.get()
        var_name = StringVar()
        var_description = StringVar()
        var_thickness = StringVar()
        var_ef = StringVar()
        var_uf = StringVar()
        var_gf = StringVar()
        var_em = StringVar()
        var_um = StringVar()
        var_gm = StringVar()
        var_fi = StringVar()
        var_nxx = StringVar()
        var_nyy = StringVar()
        var_nxy = StringVar()
        row = search_lamina(selection)
        var_name.set(str(row[0]))
        var_description.set(str(row[1]))
        var_thickness.set(str(row[2]))
        var_ef.set(str(row[3]))
        var_uf.set(str(row[4]))
        var_gf.set(str(row[5]))
        var_em.set(str(row[6]))
        var_um.set(str(row[7]))
        var_gm.set(str(row[8]))
        var_fi.set(str(row[9]))
        var_nxx.set(str(row[10]))
        var_nyy.set(str(row[11]))
        var_nxy.set(str(row[12]))

        print(type(var_fi.get()))
        laminaFi.insert(0, var_fi.get())
        laminaNxx.insert(0, var_nxx.get())
        laminaNyy.insert(0, var_nyy.get())
        laminaNxy.insert(0, var_nxy.get())
        laminaName.insert(0, var_name.get())
        laminaDescription.insert(0, var_description.get())
        laminaGrosime.insert(0, var_thickness.get())
        laminaEf.insert(0, var_ef.get())
        laminaUf.insert(0, var_uf.get())
        laminaGf.insert(0, var_gf.get())
        laminaEm.insert(0, var_em.get())
        laminaUm.insert(0, var_um.get())
        laminaGm.insert(0, var_gm.get())
        print(laminaName.get(), type(laminaDescription.get()), type(laminaGrosime.get()), laminaEf.get())
        print(selectLamina.get())
        print(type(row[3]))
        ########################################################################

    def show():
        l_description.grid()

    retriveAllLaminas()

    def compute_mar_elast():
        newWindow = customtkinter.CTkToplevel()
        newWindow.grid()
        newWindow.title("Results!!!")

        laminaFrameComposite = customtkinter.CTkFrame(master=newWindow, fg_color="transparent", bg_color="transparent",
                                                      width=420, height=150)
        laminaFrameComposite.grid(row=0, column=0, padx=20, pady=20)

        marimi_elast_label = customtkinter.CTkLabel(laminaFrameComposite, text="Marimi elastice = ")
        marimi_elast_label.grid(row=0, column=0, padx=5, pady=5)
        marimi_elast_label1 = customtkinter.CTkLabel(laminaFrameComposite)
        marimi_elast_label1.grid(row=0, column=1, padx=5, pady=5)
        marimi_elast_label2 = customtkinter.CTkLabel(laminaFrameComposite)
        marimi_elast_label2.grid(row=1, column=1, padx=5, pady=5)
        marimi_elast_label3 = customtkinter.CTkLabel(laminaFrameComposite)
        marimi_elast_label3.grid(row=2, column=1, padx=5, pady=5)
        marimi_elast_label4 = customtkinter.CTkLabel(laminaFrameComposite)
        marimi_elast_label4.grid(row=3, column=1, padx=5, pady=5)
        marimi_elast_label5 = customtkinter.CTkLabel(laminaFrameComposite)
        marimi_elast_label5.grid(row=4, column=1, padx=5, pady=5)

        compliante_lam_label = customtkinter.CTkLabel(laminaFrameComposite, text="Compliante = ")
        compliante_lam_label.grid(row=5, column=0, padx=5, pady=5)
        compliante_lam_label1 = customtkinter.CTkLabel(laminaFrameComposite)
        compliante_lam_label1.grid(row=5, column=1, padx=5, pady=5)
        compliante_lam_label2 = customtkinter.CTkLabel(laminaFrameComposite)
        compliante_lam_label2.grid(row=6, column=1, padx=5, pady=5)
        compliante_lam_label3 = customtkinter.CTkLabel(laminaFrameComposite)
        compliante_lam_label3.grid(row=7, column=1, padx=5, pady=5)
        compliante_lam_label4 = customtkinter.CTkLabel(laminaFrameComposite)
        compliante_lam_label4.grid(row=5, column=2, padx=5, pady=5)
        compliante_lam_label5 = customtkinter.CTkLabel(laminaFrameComposite)
        compliante_lam_label5.grid(row=6, column=2, padx=5, pady=5)
        compliante_lam_label6 = customtkinter.CTkLabel(laminaFrameComposite)
        compliante_lam_label6.grid(row=7, column=2, padx=5, pady=5)

        tensiuni_stratif_label = customtkinter.CTkLabel(laminaFrameComposite, text="Tensiuni = ")
        tensiuni_stratif_label.grid(row=8, column=0, padx=5, pady=5)
        tensiuni_stratif_label1 = customtkinter.CTkLabel(laminaFrameComposite)
        tensiuni_stratif_label1.grid(row=8, column=1, padx=5, pady=5)
        tensiuni_stratif_label2 = customtkinter.CTkLabel(laminaFrameComposite)
        tensiuni_stratif_label2.grid(row=9, column=1, padx=5, pady=5)
        tensiuni_stratif_label3 = customtkinter.CTkLabel(laminaFrameComposite)
        tensiuni_stratif_label3.grid(row=10, column=1, padx=5, pady=5)

        alungiri_stratif_label = customtkinter.CTkLabel(laminaFrameComposite, text="Alungiri = ")
        alungiri_stratif_label.grid(row=11, column=0, padx=5, pady=5)
        alungiri_stratif_label1 = customtkinter.CTkLabel(laminaFrameComposite)
        alungiri_stratif_label1.grid(row=11, column=1, padx=5, pady=5)
        alungiri_stratif_label2 = customtkinter.CTkLabel(laminaFrameComposite)
        alungiri_stratif_label2.grid(row=12, column=1, padx=5, pady=5)
        alungiri_stratif_label3 = customtkinter.CTkLabel(laminaFrameComposite)
        alungiri_stratif_label3.grid(row=13, column=1, padx=5, pady=5)

        lunecari_lamine_label = customtkinter.CTkLabel(laminaFrameComposite, text="Lunecari Lamine = ")
        lunecari_lamine_label.grid(row=14, column=0, padx=5, pady=5)
        lunecari_lamine_label1 = customtkinter.CTkLabel(laminaFrameComposite)
        lunecari_lamine_label1.grid(row=14, column=1, padx=5, pady=5)
        lunecari_lamine_label2 = customtkinter.CTkLabel(laminaFrameComposite)
        lunecari_lamine_label2.grid(row=15, column=1, padx=5, pady=5)
        lunecari_lamine_label3 = customtkinter.CTkLabel(laminaFrameComposite)
        lunecari_lamine_label3.grid(row=16, column=1, padx=5, pady=5)

        tensiuni_lamine_label = customtkinter.CTkLabel(laminaFrameComposite, text="Tensiuni Lamine = ")
        tensiuni_lamine_label.grid(row=17, column=0, padx=5, pady=5)
        tensiuni_lamine_label1 = customtkinter.CTkLabel(laminaFrameComposite)
        tensiuni_lamine_label1.grid(row=17, column=1, padx=5, pady=5)
        tensiuni_lamine_label2 = customtkinter.CTkLabel(laminaFrameComposite)
        tensiuni_lamine_label2.grid(row=18, column=1, padx=5, pady=5)
        tensiuni_lamine_label3 = customtkinter.CTkLabel(laminaFrameComposite)
        tensiuni_lamine_label3.grid(row=19, column=1, padx=5, pady=5)

        list_of_lists_compl = []
        lista_lamine = []
        lista_lunecari_lamine = []
        lista_tensiuni_lamine = []
        try:
            print(laminaFi.get(), "111")
            # print(convert())
            stratificat3 = MaterialCompozitStratificat(convert())  # creaza material stratificat si calculeaza marimile
            result = stratificat3.marimi_elast()
            marimi_elast = result
            marimi_elast_label1.configure(text="e_paralel " + str(round(marimi_elast[0], 3)), fg_color='red')
            marimi_elast_label2.configure(text="niu_perp " + str(round(marimi_elast[1], 3)), fg_color='red')
            marimi_elast_label3.configure(text="e_perp " + str(round(marimi_elast[2], 3)), fg_color='red')
            marimi_elast_label4.configure(text="niu_paralel " + str(round(marimi_elast[3], 3)), fg_color='red')
            marimi_elast_label5.configure(text="g_sharp " + str(round(marimi_elast[4], 3)), fg_color='red')

            lista_unghiuri = laminaOrientation.get().split(
                '/')  # ia lista de unghiuri si creaza lamine cu orientarea definita in lista
            print(lista_unghiuri)
            for i in lista_unghiuri:
                alpha = math.radians(int(i))
                lamina = Lamina(alpha)
                result_compl = lamina.compliante_lamina(result)
                list_of_lists_compl.append(result_compl)  # creaza o lista cu listele rezultatelor pt fiecare lamina
                lista_lamine.append(lamina)
            lista_finala_compl = [sum(x) for x in zip(*list_of_lists_compl)]
            compliante_lam_label1.configure(text="c11 " + str(round(lista_finala_compl[0], 3)), fg_color='green')
            compliante_lam_label2.configure(text="c22 " + str(round(lista_finala_compl[1], 3)), fg_color='green')
            compliante_lam_label3.configure(text="c33 " + str(round(lista_finala_compl[2], 3)), fg_color='green')
            compliante_lam_label4.configure(text="c12 " + str(round(lista_finala_compl[3], 3)), fg_color='green')
            compliante_lam_label5.configure(text="c13 " + str(round(lista_finala_compl[4], 3)), fg_color='green')
            compliante_lam_label6.configure(text="c23 " + str(round(lista_finala_compl[5], 3)), fg_color='green')

            result_tensiuni_str = stratificat3.tensiuni_stratificat()
            tensiuni_stratif_label1.configure(text="sigma_xx " + str(round(result_tensiuni_str[0], 3)), fg_color='blue')
            tensiuni_stratif_label2.configure(text="sigma_yy " + str(round(result_tensiuni_str[1], 3)), fg_color='blue')
            tensiuni_stratif_label3.configure(text="thau_xy " + str(round(result_tensiuni_str[2], 3)), fg_color='blue')

            result_alungiri = stratificat3.alungiri_stratificat(lista_compliante=lista_finala_compl,
                                                                lista_tensiuni=result_tensiuni_str)
            alungiri_stratif_label1.configure(text="epsilon_xx " + str(round(result_alungiri[0], 3)), fg_color='red')
            alungiri_stratif_label2.configure(text="epsilon_yy " + str(round(result_alungiri[1], 3)), fg_color='red')
            alungiri_stratif_label3.configure(text="gamma_xy " + str(round(result_alungiri[2], 3)), fg_color='red')

            for lamina in lista_lamine:
                result_lunecari = lamina.lunecari_lamina(result_alungiri)
                lista_lunecari_lamine.append(result_lunecari)
                lista_tensiuni_lamine.append(lamina.tensiuni_lamine(marimi_elast, result_lunecari))
            lista_lunecari_lamine1 = [[round(x, 3) for x in sublist] for sublist in lista_lunecari_lamine]
            lista_tensiuni_lamine1 = [[round(x, 3) for x in sublist] for sublist in lista_tensiuni_lamine]
            lunecari_lamine_label1.configure(text="epsilon_paralel " + str(lista_lunecari_lamine1[0]), fg_color='blue')
            lunecari_lamine_label2.configure(text="epsilon_perp " + str(lista_lunecari_lamine1[1]), fg_color='blue')
            lunecari_lamine_label3.configure(text="gamma_sharp " + str(lista_lunecari_lamine1[2]), fg_color='blue')
            print(lista_lunecari_lamine)
            tensiuni_lamine_label1.configure(text="sigma_paralel " + str(lista_tensiuni_lamine1[0]), fg_color='green')
            tensiuni_lamine_label2.configure(text="sigma_perp " + str(lista_tensiuni_lamine1[1]), fg_color='green')
            tensiuni_lamine_label3.configure(text="thau_perp " + str(lista_tensiuni_lamine1[2]), fg_color='green')

            laminaFi.delete(0, customtkinter.END)
            laminaNxx.delete(0, customtkinter.END)
            laminaNyy.delete(0, customtkinter.END)
            laminaNxy.delete(0, customtkinter.END)
            laminaName.delete(0, customtkinter.END)
            laminaDescription.delete(0, customtkinter.END)
            laminaGrosime.delete(0, customtkinter.END)
            laminaEf.delete(0, customtkinter.END)
            laminaUf.delete(0, customtkinter.END)
            laminaGf.delete(0, customtkinter.END)
            laminaEm.delete(0, customtkinter.END)
            laminaUm.delete(0, customtkinter.END)
            laminaGm.delete(0, customtkinter.END)

        except ValueError:
            show_error_message("Ceva nu a mers bine")

    def convert():
        lista_param_calc = [float(laminaFi.get()), float(laminaNxx.get()), float(laminaNyy.get()),
                            float(laminaNxy.get()), float(laminaGrosime.get()), float(laminaEf.get()),
                            float(laminaUf.get()), float(laminaGf.get()), float(laminaEm.get()), float(laminaUm.get()),
                            float(laminaGm.get()), str(laminaDescription.get()), str(laminaName.get()),
                            int(laminaNumber.get()), str(laminaOrientation.get())]
        print(lista_param_calc)
        return lista_param_calc

def addLamina():
    image2 = customtkinter.CTkImage(light_image=Image.open("resources/360_F.jpg"),
                                    dark_image=Image.open("resources/360_F.jpg"),
                                    size=(300, 300))

    newWindow = customtkinter.CTkToplevel()
    newWindow.grid()

    newWindow.title("Add Lamina")

    # newWindow.geometry("300x900")
    laminaFrame = customtkinter.CTkScrollableFrame(master=newWindow, fg_color="transparent", bg_color="transparent",
                                                   width=380)
    laminaFrame.grid(row=0, column=0, padx=20, pady=20)

    label2 = customtkinter.CTkLabel(newWindow, text="", image=image2)
    label2.grid(row=1, column=0)

    l_name = customtkinter.CTkLabel(laminaFrame, text="Lamina Name")
    l_name.grid(row=0, column=0, padx=5, pady=5)
    laminaName = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter lamina name!",
                                        placeholder_text_color="white", width=200)
    laminaName.grid(row=0, column=1, padx=5, pady=5)
    l_description = customtkinter.CTkLabel(laminaFrame, text="Lamina Description")
    l_description.grid(row=1, column=0, padx=5, pady=5)
    laminaDescription = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter lamina description!",
                                               placeholder_text_color="white", width=200)
    laminaDescription.grid(row=1, column=1, padx=5, pady=5)
    l_grosime = customtkinter.CTkLabel(laminaFrame, text="Thickness - [mm]")
    l_grosime.grid(row=2, column=0, padx=5, pady=5)
    laminaGrosime = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter thickness!",
                                           placeholder_text_color="white", width=200)
    laminaGrosime.grid(row=2, column=1, padx=5, pady=5)
    l_Ef = customtkinter.CTkLabel(laminaFrame, text="Ef")
    l_Ef.grid(row=3, column=0, padx=5, pady=5)
    laminaEf = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Ef!", placeholder_text_color="white",
                                      width=200)
    laminaEf.grid(row=3, column=1, padx=5, pady=5)
    l_Uf = customtkinter.CTkLabel(laminaFrame, text="Uf")
    l_Uf.grid(row=4, column=0, padx=5, pady=5)
    laminaUf = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Uf!", placeholder_text_color="white",
                                      width=200)
    laminaUf.grid(row=4, column=1, padx=5, pady=5)
    l_Gf = customtkinter.CTkLabel(laminaFrame, text="Gf")
    l_Gf.grid(row=5, column=0, padx=5, pady=5)
    laminaGf = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Gf!", placeholder_text_color="white",
                                      width=200)
    laminaGf.grid(row=5, column=1, padx=5, pady=5)
    l_Em = customtkinter.CTkLabel(laminaFrame, text="Em")
    l_Em.grid(row=6, column=0, padx=5, pady=5)
    laminaEm = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Em!", placeholder_text_color="white",
                                      width=200)
    laminaEm.grid(row=6, column=1, padx=5, pady=5)
    l_Um = customtkinter.CTkLabel(laminaFrame, text="Um")
    l_Um.grid(row=7, column=0, padx=5, pady=5)
    laminaUm = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Um!", placeholder_text_color="white",
                                      width=200)
    laminaUm.grid(row=7, column=1, padx=5, pady=5)
    l_Gm = customtkinter.CTkLabel(laminaFrame, text="Gm")
    l_Gm.grid(row=8, column=0, padx=5, pady=5)
    laminaGm = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Gm!", placeholder_text_color="white",
                                      width=200)
    laminaGm.grid(row=8, column=1, padx=5, pady=5)
    l_Fi = customtkinter.CTkLabel(laminaFrame, text="Fi")
    l_Fi.grid(row=9, column=0, padx=5, pady=5)
    laminaFi = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Fi!", placeholder_text_color="white",
                                      width=200)
    laminaFi.grid(row=9, column=1, padx=5, pady=5)
    l_Nxx = customtkinter.CTkLabel(laminaFrame, text="Nxx")
    l_Nxx.grid(row=10, column=0, padx=5, pady=5)
    laminaNxx = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Nxx!", placeholder_text_color="white",
                                       width=200)
    laminaNxx.grid(row=10, column=1, padx=5, pady=5)
    l_Nyy = customtkinter.CTkLabel(laminaFrame, text="Nyy")
    l_Nyy.grid(row=11, column=0, padx=5, pady=5)
    laminaNyy = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Nyy!", placeholder_text_color="white",
                                       width=200)
    laminaNyy.grid(row=11, column=1, padx=5, pady=5)
    l_Nxy = customtkinter.CTkLabel(laminaFrame, text="Nxy")
    l_Nxy.grid(row=12, column=0, padx=5, pady=5)
    laminaNxy = customtkinter.CTkEntry(laminaFrame, placeholder_text="Enter Nxy!", placeholder_text_color="white",
                                       width=200)
    laminaNxy.grid(row=12, column=1, padx=5, pady=5)

    def close():
        insert_lamina(str(laminaName.get()), str(laminaDescription.get()), float(laminaGrosime.get()),
                      float(laminaEf.get()), float(laminaUf.get()),
                      float(laminaGf.get()), float(laminaEm.get()), float(laminaUm.get()), float(laminaGm.get()),
                      float(laminaFi.get()),
                      int(laminaNxx.get()), int(laminaNyy.get()), int(laminaNxy.get()))
        show_info_message()
        newWindow.destroy()
        newWindow.update()

    save_button = customtkinter.CTkButton(newWindow, corner_radius=15, text="Save and exit", command=close,
                                          cursor='hand2')
    save_button.grid(pady=20)


def optimizer():
    def verificare2():
        print(type(combo_material_miez.get()))
        print(combo_material_invelis.get())
        print(materialDict_miez[combo_material_miez.get()])
        print(materialDict_invelis[combo_material_invelis.get()])

    materialDict_miez = {'Divinycell H60': {'Dens': 60,
                                            'Ec': 55,
                                            'Gc': 22,
                                            'Tc': 0.6,
                                            'Cost': 6
                                            },
                         'Divinycell H100': {'Dens': 100,
                                             'Ec': 95,
                                             'Gc': 38,
                                             'Tc': 1.2,
                                             'Cost': 10
                                             },
                         'Divinycell H130': {'Dens': 130,
                                             'Ec': 125,
                                             'Gc': 47,
                                             'Tc': 1.6,
                                             'Cost': 13
                                             },
                         'Divinycell H200': {'Dens': 200,
                                             'Ec': 195,
                                             'Gc': 75,
                                             'Tc': 3.0,
                                             'Cost': 20
                                             }
                         }

    materialDict_invelis = {'Otel': {'Dens': 7800,
                                     'Ef': 205000,
                                     'Sigf': 300,
                                     'Cost': 0.4
                                     },
                            'Aluminiu': {'Dens': 2700,
                                         'Ef': 70000,
                                         'Sigf': 200,
                                         'Cost': 0.7
                                         },
                            'GFRP': {'Dens': 1600,
                                     'Ef': 20000,
                                     'Sigf': 400,
                                     'Cost': 4
                                     },
                            'CFRP': {'Dens': 1500,
                                     'Ef': 70000,
                                     'Sigf': 1000,
                                     'Cost': 80
                                     }
                            }

    window_sandwich = ctk.CTkToplevel()
    window_sandwich.grid()
    window_sandwich.title("Sandwich Optimization")
    window_sandwich.configure(padx=50, pady=50)

    ################################ Date de intrare #################################
    material_miez_label = ctk.CTkLabel(window_sandwich, text="Material Miez:")
    material_invelis_label = ctk.CTkLabel(window_sandwich, text="Material Invelis:")
    lungime_label = ctk.CTkLabel(window_sandwich, text="Lungime:1000 -> 4000 mm")
    latime_label = ctk.CTkLabel(window_sandwich, text="Latime: 500")
    tc_miez_label = ctk.CTkLabel(window_sandwich, text="Grosime miez:30 mm -> 60")
    tf_invelis_label = ctk.CTkLabel(window_sandwich, text="Grosime invelis:0.5 -> 1 mm")
    greutate = ctk.CTkLabel(window_sandwich, text="Greutate -> 150")
    mass_label = ctk.CTkLabel(window_sandwich, text="Masa: N/A")
    incarcare_label = ctk.CTkLabel(window_sandwich, text="Incarcare: 150 kg")

    ################################ Entries #################################
    var_material_miez = ctk.StringVar()
    combo_material_miez = ctk.CTkComboBox(window_sandwich, values=list(materialDict_miez.keys()), justify="center",
                                          variable=var_material_miez)
    var_material_invelis = ctk.StringVar()
    combo_material_invelis = ctk.CTkComboBox(window_sandwich, values=list(materialDict_invelis.keys()),
                                             justify="center", variable=var_material_invelis)

    # Definirea listelor de valori
    lungime = [numar for numar in range(1000, 4001, 200)]
    latime = 500
    grosime_miez = [numar for numar in range(30, 61, 10)]
    grosime_invelis = [numar / 10 for numar in range(5, 10)]

    # Crearea matricei pentru a stoca combinațiile
    lista_valori = []
    # Iterarea prin toate combinațiile posibile și adăugarea acestora în matrice
    for l in lungime:
        for gm in grosime_miez:
            for gi in grosime_invelis:
                lista_valori.append([l, latime, gm, gi])

    # Lista pentru salvarea rezultatelor
    lista_pentru_grafic = []

    def plot_graph():
        matrice_rezultate = np.array(lista_pentru_grafic, dtype=object)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 24))

        for gm in grosime_miez:
            for gi in grosime_invelis:
                subset = np.array([row for row in matrice_rezultate if row[2] == gm and row[3] == gi], dtype=object)
                if len(subset) > 0:
                    subset = np.array(subset)
                    print(subset)  # Adăugăm acest rând pentru a investiga conținutul lui subset
                    ax1.plot(subset[:, 0].astype(float), subset[:, 4].astype(float),
                             label=f'grosime miez: {gm} mm, grosime înveliș: {gi} mm', color='black')
                    ax2.plot(subset[:, 0].astype(float), subset[:, 6].astype(float),
                             label=f'grosime miez: {gm} mm, grosime înveliș: {gi} mm', color='red')
                    ax3.plot(subset[:, 0].astype(float), subset[:, 5].astype(float),
                             label=f'grosime miez: {gm} mm, grosime înveliș: {gi} mm', color='blue')

        # Setări pentru primul grafic (masă)
        ax1.set_xlabel('Lungime (mm)')
        ax1.set_ylabel('Masă (kg)')
        ax1.set_title(var_material_miez)
        # ax1.legend( loc='upper left', fontsize='small')

        # Setări pentru al doilea grafic (preț per kg)
        ax2.set_xlabel('Lungime (mm)')
        ax2.set_ylabel('Euro/kg ')
        # ax2.set_title('Preț per kg în funcție de lungime pentru diferite grosimi de miez și înveliș')
        # ax2.legend()

        # Setări pentru al treilea grafic (rigiditate)
        ax3.set_xlabel('Lungime (mm)')
        ax3.set_ylabel('Rigiditate (unitate)')
        # ax3.set_title('Rigiditate în funcție de lungime pentru diferite grosimi de miez și înveliș')
        # ax3.legend()

        # Adăugarea tabelelor subgraficelor
        tabla1 = ax3.table(cellText=matrice_rezultate[:, :4].astype(str),
                           colLabels=['Lungime', 'Latime', 'Grosime miez', 'Grosime invelis'], loc='bottom',
                           cellLoc='center')
        tabla1.auto_set_font_size(False)
        tabla1.set_fontsize(8)
        tabla1.scale(1, 1.5)

        plt.tight_layout()
        plt.show()

    # Functia de calcul
    def calculate():

        try:
            for x in lista_valori:
                sandwich = Sandwich(
                    lista_geometrie=x,
                    material_miez=materialDict_miez[combo_material_miez.get()],
                    material_invelis=materialDict_invelis[combo_material_invelis.get()],
                    incarcare=float(150)
                )
                result_masa = sandwich.calcul_masa()
                result_rigid = sandwich.calcul_rigiditate()
                result_cost = sandwich.calcul_cost()
                result_tensiuni = sandwich.calcul_tensiuni()

                # Adăugarea rezultatelor într-o listă

                lista_pentru_grafic.append(
                    [x[0], x[1], x[2], x[3], result_masa, result_rigid, result_cost, result_tensiuni])
                print(lista_pentru_grafic)
                # Afișarea masei în UI (opțional)
                mass_label.configure(text=f"Masa: {str(result_masa)} kg")

        except ValueError:
            mass_label.configure(text="Ceva nu e bine.")

    # Conversia listei în matrice numpy
    matrice_rezultate = np.array(lista_pentru_grafic)

    # Afișarea matricei rezultate și a dimensiunii acesteia
    print(matrice_rezultate)
    print("Dimensiunea matricei rezultate:", matrice_rezultate.shape)

    def tabel():
        scrollbar = ctk.CTkScrollbar(window_sandwich, orientation="horizontal")

        tree = ttk.Treeview(window_sandwich, columns=(
        "Lungime", "Latime", "Grosime miez", "Grosime invelis", "Masa", "Rigiditate", "Pret", "Tensiuni"),
                            show="headings")
        tree.grid(row=4, column=3,
                  sticky="nsew")  # Adaugă opțiunea sticky pentru a face Treeview să se extindă pe orizontală

        scrollbar.configure(command=tree.xview)
        scrollbar.grid(row=5, column=3,
                       sticky="ew")  # Folosește sticky pentru a face scrollbar-ul să se extindă pe orizontală

        tree.column("Lungime", width=60)
        tree.heading("Lungime", text="Lungime")
        tree.column("Latime", width=60)
        tree.heading("Latime", text="Latime")
        tree.column("Grosime miez", width=75)
        tree.heading("Grosime miez", text="Grosime miez")
        tree.column("Grosime invelis", width=75)
        tree.heading("Grosime invelis", text="Grosime invelis")
        tree.column("Masa", width=60)
        tree.heading("Masa", text="Masa")
        tree.column("Rigiditate", width=60)
        tree.heading("Rigiditate", text="Rigiditate")
        tree.column("Pret", width=60)
        tree.heading("Pret", text="Pret")
        tree.column("Tensiuni", width=75)
        tree.heading("Tensiuni", text="Tensiuni")

        tree.tag_configure('highlight', background='lightgreen')

        lista = lista_pentru_grafic
        for element in lista:
            if element[6] < 30 and \
                    (4.75 < element[5] < 5.25) and \
                    (element[7][0] * 5 < materialDict_miez[combo_material_miez.get()]['Tc']) and \
                    (element[7][1] * 5 < materialDict_invelis[combo_material_invelis.get()]['Sigf']):
                tree.insert("", tk.END, values=element, tags=('highlight',))
            else:
                tree.insert("", tk.END, values=element)
        scrollbar.configure(command=tree.xview)
        tree.configure(xscrollcommand=scrollbar.set)

        def on_horizontal_scroll(*args):
            tree.xview(*args)

    ################################ Buttons #################################
    calculate_button = ctk.CTkButton(window_sandwich, text="Calculeaza", command=calculate)
    reset_button = ctk.CTkButton(window_sandwich, text="Grafic", command=plot_graph)
    table_button = ctk.CTkButton(window_sandwich, text="Tabel Date Calculate", command=tabel)
    ################################ Settings #################################
    material_miez_label.grid(row=0, column=1)
    material_invelis_label.grid(row=1, column=1)
    lungime_label.grid(row=2, column=1)
    latime_label.grid(row=3, column=1)
    tc_miez_label.grid(row=4, column=1)
    tf_invelis_label.grid(row=5, column=1)
    greutate.grid(row=6, column=1)
    combo_material_miez.grid(row=0, column=2)
    combo_material_invelis.grid(row=1, column=2)

    calculate_button.grid(row=7, column=1, columnspan=2)
    reset_button.grid(row=7, column=3, columnspan=2)
    mass_label.grid(row=8, column=1, columnspan=2)
    table_button.grid(row=9, column=3, columnspan=2)


#######################################################################
def AddSand():
    def temp_text2(e):
        lungime_entry.delete(0, "end")

    def temp_text3(e):
        latime_entry.delete(0, "end")

    def temp_text4(e):
        tc_miez_entry.delete(0, "end")

    def temp_text5(e):
        tf_invelis_entry.delete(0, "end")

    def temp_text6(e):
        incarcare_entry.delete(0, "end")

    def calculate():
        try:
            sandwich = Sandwich(lista_geometrie=convert_sandwich(),
                                material_miez=materialDict_miez[combo_material_miez.get()],
                                material_invelis=materialDict_invelis[combo_material_invelis.get()],
                                incarcare=float(incarcare_entry.get()))
            result_masa = sandwich.calcul_masa()
            mass_label.configure(text=f"Masa: {str(result_masa)} kg")
            print(111222)
            result_rigid = sandwich.calcul_rigiditate()
            if result_rigid > 4.75 or result_rigid < 5.25:
                rigid_label.configure(text=f"Rigiditate (k): {str(result_rigid)} N/mm", fg_color="red")
            else:
                rigid_label.config(text=f"Rigiditate (k): {str(result_rigid)} N/mm", fg_color="green")

            result_cost = sandwich.calcul_cost()
            if result_cost < 30:
                cost_label.configure(text=f"Cost: {str(result_cost)} €", fg_color="green")
            else:
                cost_label.configure(text=f"Cost: {str(result_cost)} €", fg_color="red")

            result_tensiuni = sandwich.calcul_tensiuni()
            if result_tensiuni[0] < materialDict_miez[combo_material_miez.get()]['Tc']:
                thau_c_label.configure(text=f"Thau C: {str(result_tensiuni[0])} MPa", fg_color="green")
            else:
                thau_c_label.configure(text=f"Thau C: {str(result_tensiuni[0])} MPa", fg_color="red")

            if result_tensiuni[1] < materialDict_invelis[combo_material_invelis.get()]['Sigf']:
                sig_f_label.configure(text=f"Sigma F: {str(result_tensiuni[1])} MPa", fg_color="green")
            else:
                sig_f_label.configure(text=f"Sigma F: {str(result_tensiuni[1])} MPa", fg_color="red")

        except ValueError:
            mass_label.configure(text="Ceva nu e bine.")

    def convert_sandwich():
        lungime = float(lungime_entry.get())
        latime = float(latime_entry.get())
        grosime_miez = float(tc_miez_entry.get())
        grosime_invelis = float(tf_invelis_entry.get())
        return [lungime, latime, grosime_miez, grosime_invelis]

    def verificare2():
        print(type(combo_material_miez.get()))
        print(combo_material_invelis.get())
        print(lungime_entry.get())
        print(latime_entry.get())
        print(tc_miez_entry.get())
        print(tf_invelis_entry.get())
        print(incarcare_entry.get())
        print(materialDict_miez[combo_material_miez.get()])
        print(materialDict_invelis[combo_material_invelis.get()])

    materialDict_miez = {'Divinycell H60': {'Dens': 60,
                                            'Ec': 55,
                                            'Gc': 22,
                                            'Tc': 0.6,
                                            'Cost': 6
                                            },
                         'Divinycell H100': {'Dens': 100,
                                             'Ec': 95,
                                             'Gc': 38,
                                             'Tc': 1.2,
                                             'Cost': 10
                                             },
                         'Divinycell H130': {'Dens': 130,
                                             'Ec': 125,
                                             'Gc': 47,
                                             'Tc': 1.6,
                                             'Cost': 13
                                             },
                         'Divinycell H200': {'Dens': 200,
                                             'Ec': 195,
                                             'Gc': 75,
                                             'Tc': 3.0,
                                             'Cost': 20
                                             }
                         }

    materialDict_invelis = {'Otel': {'Dens': 7800,
                                     'Ef': 205000,
                                     'Sigf': 300,
                                     'Cost': 0.4
                                     },
                            'Aluminiu': {'Dens': 2700,
                                         'Ef': 70000,
                                         'Sigf': 200,
                                         'Cost': 0.7
                                         },
                            'GFRP': {'Dens': 1600,
                                     'Ef': 20000,
                                     'Sigf': 400,
                                     'Cost': 4
                                     },
                            'CFRP': {'Dens': 1500,
                                     'Ef': 70000,
                                     'Sigf': 1000,
                                     'Cost': 80
                                     }
                            }

    window_sandwich = ctk.CTkToplevel()
    window_sandwich.grid()
    window_sandwich.title("Material Compozit - Sandwich")
    window_sandwich.configure(padx=50, pady=50)

    ################################ Date de intrare #################################
    material_miez_label = ctk.CTkLabel(window_sandwich, text="Material Miez:")
    material_invelis_label = ctk.CTkLabel(window_sandwich, text="Material Invelis:")
    lungime_label = ctk.CTkLabel(window_sandwich, text="Lungime:")
    latime_label = ctk.CTkLabel(window_sandwich, text="Latime:")
    tc_miez_label = ctk.CTkLabel(window_sandwich, text="Grosime miez:")
    tf_invelis_label = ctk.CTkLabel(window_sandwich, text="Grosime invelis:")
    mass_label = ctk.CTkLabel(window_sandwich, text="Masa: N/A")
    incarcare_label = ctk.CTkLabel(window_sandwich, text="Incarcare:")
    rigid_label = ctk.CTkLabel(window_sandwich, text="Rigiditate (k):")
    cost_label = ctk.CTkLabel(window_sandwich, text="Cost:")
    thau_c_label = ctk.CTkLabel(window_sandwich, text="Thau C:")
    sig_f_label = ctk.CTkLabel(window_sandwich, text="Sigma F:")

    ################################ Entries #################################
    var_material_miez = ctk.StringVar()
    combo_material_miez = ctk.CTkComboBox(window_sandwich, values=list(materialDict_miez.keys()), justify="center",
                                          variable=var_material_miez)
    var_material_invelis = ctk.StringVar()
    combo_material_invelis = ctk.CTkComboBox(window_sandwich, values=list(materialDict_invelis.keys()),
                                             justify="center", variable=var_material_invelis)
    lungime_entry = ctk.CTkEntry(window_sandwich, width=70)
    latime_entry = ctk.CTkEntry(window_sandwich, width=70)
    tc_miez_entry = ctk.CTkEntry(window_sandwich, width=70)
    tf_invelis_entry = ctk.CTkEntry(window_sandwich, width=70)
    incarcare_entry = ctk.CTkEntry(window_sandwich, width=70)

    ################################ Buttons #################################
    calculate_button = ctk.CTkButton(window_sandwich, text="Calculeaza", command=calculate)
    reset_button = ctk.CTkButton(window_sandwich, text="Reseteaza", command=verificare2)

    ################################ Settings #################################
    material_miez_label.grid(row=0, column=1)
    material_invelis_label.grid(row=1, column=1)
    lungime_label.grid(row=2, column=1)
    latime_label.grid(row=3, column=1)
    tc_miez_label.grid(row=4, column=1)
    tf_invelis_label.grid(row=5, column=1)
    combo_material_miez.grid(row=0, column=2)
    combo_material_invelis.grid(row=1, column=2)
    lungime_entry.grid(row=2, column=2)
    latime_entry.grid(row=3, column=2)
    tc_miez_entry.grid(row=4, column=2)
    tf_invelis_entry.grid(row=5, column=2)
    incarcare_label.grid(row=6, column=1)
    incarcare_entry.grid(row=6, column=2)
    calculate_button.grid(row=7, column=1, columnspan=2)
    reset_button.grid(row=7, column=3, columnspan=2)
    mass_label.grid(row=8, column=1, columnspan=2)
    rigid_label.grid(row=9, column=1, columnspan=2)
    cost_label.grid(row=10, column=1, columnspan=2)
    thau_c_label.grid(row=11, column=1, columnspan=2)
    sig_f_label.grid(row=12, column=1, columnspan=2)

    # Settings # General Settings
    lungime_entry.insert(0, "mm")
    latime_entry.insert(0, "mm")
    tc_miez_entry.insert(0, "mm")
    tf_invelis_entry.insert(0, "mm")
    incarcare_entry.insert(0, "kg")

    lungime_entry.bind("<FocusIn>", temp_text2)
    latime_entry.bind("<FocusIn>", temp_text3)
    tc_miez_entry.bind("<FocusIn>", temp_text4)
    tf_invelis_entry.bind("<FocusIn>", temp_text5)
    incarcare_entry.bind("<FocusIn>", temp_text6)


def show_lamina():
    # Creare fereastră secundară
    lamina_screen = ctk.CTkToplevel()
    lamina_screen.title("Lamine")
    lamina_screen.configure(padx=50, pady=50)
    lamina_screen.geometry("1200x600")
    # Creare cadru scrollabil
    lamina_frame = ctk.CTkScrollableFrame(lamina_screen)
    lamina_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Conectare la baza de date și extragerea datelor
    conn = sqlite3.connect('tutorial.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lamina')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    # Creare stil personalizat pentru TreeView
    style = ttk.Style()
    style.configure("Custom.Treeview", font=("Helvetica", 12))  # Setează fontul și dimensiunea textului
    style.configure("Custom.Treeview.Heading", font=("Helvetica", 14, "bold"))  # Setează fontul și dimensiunea anteturilor

    # Creare și configurare TreeView
    tree = ttk.Treeview(lamina_frame, style="Custom.Treeview")
    tree['columns'] = (
        'name', 'description', 'thickness', 'Ef', 'Uf', 'Gf', 'Em', 'Um', 'Gm', 'Fi', 'Nxx', 'Nyy', 'Nxy'
    )

    # Configurare anteturi coloane
    tree.column('#0', width=0, stretch=ctk.NO)
    tree.column('name', anchor=tk.CENTER, width=100)
    tree.column('description', anchor=tk.CENTER, width=200)
    tree.column('thickness', anchor=tk.CENTER, width=100)
    tree.column('Ef', anchor=tk.CENTER, width=100)
    tree.column('Uf', anchor=tk.CENTER, width=100)
    tree.column('Gf', anchor=tk.CENTER, width=100)
    tree.column('Em', anchor=tk.CENTER, width=100)
    tree.column('Um', anchor=tk.CENTER, width=100)
    tree.column('Gm', anchor=tk.CENTER, width=100)
    tree.column('Fi', anchor=tk.CENTER, width=100)
    tree.column('Nxx', anchor=tk.CENTER, width=100)
    tree.column('Nyy', anchor=tk.CENTER, width=100)
    tree.column('Nxy', anchor=tk.CENTER, width=100)

    tree.heading('#0', text='', anchor=tk.CENTER)
    tree.heading('name', text='Name', anchor=tk.CENTER)
    tree.heading('description', text='Description', anchor=tk.CENTER)
    tree.heading('thickness', text='Thickness', anchor=tk.CENTER)
    tree.heading('Ef', text='Ef', anchor=tk.CENTER)
    tree.heading('Uf', text='Uf', anchor=tk.CENTER)
    tree.heading('Gf', text='Gf', anchor=tk.CENTER)
    tree.heading('Em', text='Em', anchor=tk.CENTER)
    tree.heading('Um', text='Um', anchor=tk.CENTER)
    tree.heading('Gm', text='Gm', anchor=tk.CENTER)
    tree.heading('Fi', text='Fi', anchor=tk.CENTER)
    tree.heading('Nxx', text='Nxx', anchor=tk.CENTER)
    tree.heading('Nyy', text='Nyy', anchor=tk.CENTER)
    tree.heading('Nxy', text='Nxy', anchor=tk.CENTER)

    # Configurare tag-uri pentru alternanță culoare
    tree.tag_configure('odd', background='lightgrey')
    tree.tag_configure('even', background='white')

    # Adăugare date în TreeView
    for i, row in enumerate(rows):
        tag = 'odd' if i % 2 == 0 else 'even'
        tree.insert('', tk.END, values=row, tags=(tag,))

    tree.pack(pady=20, fill="both", expand=True)
def show_composit():
    composit_screen = ctk.CTkToplevel()
    composit_screen.title("Compozite")
    composit_screen.configure(padx=50, pady=50)
    composit_screen.geometry("1200x600")
    style = ttk.Style()
    style.configure("Custom.Treeview", font=("Helvetica", 12))  # Setează fontul și dimensiunea textului
    style.configure("Custom.Treeview.Heading", font=("Helvetica", 14, "bold"))  # Setează fontul și dimensiunea anteturilor

    # Creare cadru scrollabil
    composit_frame = ttk.Frame(composit_screen)
    composit_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Creare și configurare TreeView
    tree = ttk.Treeview(composit_frame, style="Custom.Treeview", columns=(
        '_fi', '_nxx', '_nyy', '_nxy', '_grosime_totala', '_e_f', '_niu_f', '_g_f',
        '_e_m', '_niu_m', '_g_m', '_description', '_name', '_lamina_number', '_lamina_orientation'
    ))

    # Configurare anteturi coloane
    tree.heading('#0', text='ID')
    tree.heading('_fi', text='Fi')
    tree.heading('_nxx', text='Nxx')
    tree.heading('_nyy', text='Nyy')
    tree.heading('_nxy', text='Nxy')
    tree.heading('_grosime_totala', text='Grosime Totala')
    tree.heading('_e_f', text='Ef')
    tree.heading('_niu_f', text='Niu F')
    tree.heading('_g_f', text='G F')
    tree.heading('_e_m', text='Em')
    tree.heading('_niu_m', text='Niu M')
    tree.heading('_g_m', text='G M')
    tree.heading('_description', text='Description')
    tree.heading('_name', text='Name')
    tree.heading('_lamina_number', text='Lamina Number')
    tree.heading('_lamina_orientation', text='Lamina Orientation')

    # Adăugare date în TreeView din baza de date SQLAlchemy
    materials = session.query(MaterialCompozitStratificat).all()
    for i, material in enumerate(materials):
        tag = 'odd' if i % 2 == 0 else 'even'
        tree.insert('', tk.END, text=material._id, values=(
            material._fi, material._nxx, material._nyy, material._nxy, material._grosime_totala,
            material._e_f, material._niu_f, material._g_f, material._e_m, material._niu_m,
            material._g_m, material._description, material._name, material._lamina_number,
            material._lamina_orientation
        ), tags=(tag,))

# Configurare culoare rânduri alternative
    tree.tag_configure('odd', background='lightgrey')
    tree.tag_configure('even', background='white')

    ctk_scrollbar = customtkinter.CTkScrollbar(composit_screen, orientation ="horizontal", command=tree.xview)
    ctk_scrollbar.pack( side="bottom", fill="x")
    tree.configure(xscrollcommand=ctk_scrollbar.set)
    tree.pack(fill="both", expand=True)

button_1 = menu.add_cascade("Compozits")
button_2 = menu.add_cascade("Material")

dropdown1 = CustomDropdownMenu(widget=button_1)
dropdown1.add_option(option="Add New Composite Material", command=lambda: addComposite())
dropdown1.add_option(option="Sandwisch Calculator", command=lambda: AddSand())
dropdown1.add_option(option="Sandwisch Optimization", command=lambda: optimizer())

dropdown1.add_separator()
sub_menu = dropdown1.add_submenu("Open")
sub_menu.add_option(option="Laminas", command=lambda: show_lamina())
sub_menu.add_option(option="Compozits", command=lambda : show_composit())

dropdown2 = CustomDropdownMenu(widget=button_2)
dropdown2.add_option(option="Add Lamina", command=lambda: addLamina())
dropdown2.add_option(option="Add Layer")
dropdown2.add_option(option="Add Core")


label1 = customtkinter.CTkLabel(root, text="Welcome to the Composite Material \n Design Tool!", text_color="white",
                                font=font)
label1.size()
label1.pack(pady=20)

label = customtkinter.CTkLabel(root, text="", image=image)
label.size()
label.pack(pady=20)

root.mainloop()
