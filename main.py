import sys

from helpers import get_data, plot


def main():

    if len(sys.argv) == 4 or len(sys.argv) == 3:

        airfoil_digits = sys.argv[1]
        analysis_type = sys.argv[2]

        if analysis_type not in ['v', 'i']:
            print("Error: analysis_type must be 'v' for viscid or 'i' for inviscid.")
            return
        
        if len(sys.argv) == 4:
            Re = sys.argv[3]
            plot(get_data(airfoil_digits, analysis_type, Re), analysis_type)

        plot(get_data(airfoil_digits, analysis_type), analysis_type)
    else:
        print("Error: Expected 3 arguments - airfoil_name (str), analysis_type (str), Re (int)")


if __name__ == "__main__":
    main()
