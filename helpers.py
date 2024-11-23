import sys
import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
# Get Data from Xfoil and save it
# Airfoil name, command line arguments
# for viscid enter: 0015 v 0 20 1
# for inviscid enter: 0015 i 0 20 1

alfa_i = 0
alfa_f = 20
alfa_s = 1


def get_data(airfoil_digits, analysis_type, Re):

    if not os.path.exists("polar data"):
        os.makedirs("polar data")

    airfoil_path = f"polar data/NACA_{airfoil_digits}.txt"
    input_file = f"input_file.in"

    if os.path.exists(airfoil_path):
        os.remove(airfoil_path)

    with open(input_file, "w") as f:
        f.write(f"NACA {airfoil_digits}\n")
        f.write(f"OPER\n")
        # An extra command must be run for viscous analysis
        if analysis_type == "v":
            f.write(f"Visc {int(Re)} \n")
        f.write("PACC\n")
        f.write(f"{airfoil_path}\n\n")
        f.write(f"aseq {alfa_i} {alfa_f} {alfa_s}\n")
        f.write("\n\n")
        f.write("quit\n")

    subprocess.call("xfoil.exe < input_file.in", shell=True)


def plot(file_name):
    df = pd.read_csv(file_name, delim_whitespace=True, skiprows=12,
                     names=["alfa", "CL", "CD", "CDp", "CM", "TopX", "BottomX"])

    # plt.plot(df["alfa"], df["CL"], marker='o')
    # plt.xlabel("Alfa")
    # plt.ylabel("CL")
    # plt.title("CL vs alfa - NACA 0015")
    # plt.show()

    plt.plot(df["CD"], df["CL"], marker="o")
    plt.xlabel("CD")
    plt.ylabel("CL")
    plt.title("CD vs CL - NACA 0015")
    plt.show()


plot("polar data/NACA_0015.txt")
