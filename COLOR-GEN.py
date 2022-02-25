##############################################################
#
# NAME: COLOR-GEN
# DESCRIPTION: GENERATES A RANDOMIZED COLOR ( RGB AND HEX ).
# AUTHOR: JOSHUA WOOTEN
#
##############################################################
import random

def generate_HEX(RGB_L):
    Rval = RGB_L[0]
    Gval = RGB_L[1]
    Bval = RGB_L[2]
    # GEN HEX
    return ('#{:02x}{:02x}{:02x}').format(Rval, Gval, Bval)

def generate_COLOR():
    # GENERATES ONE COLOR ( RGB AND HEX CODE )
    print('GENERATING A RANDOM COLOR ...')

    # GEN RGB
    R = random.randrange(0, 255, 1)
    G = random.randrange(0, 255, 1)
    B = random.randrange(0, 255, 1)
    RGB_ARR = [R, G, B]
    print(f'RGB -- R={R}, G={G}, B={B}')

    # GEN HEX
    HEXCODE = str(generate_HEX(RGB_ARR).upper())
    print(f'HEX -- {HEXCODE}')
    print("")

def generate_PALETTE(palette_size):
    # GENERATES MULTIPLE COLORS ( RGB AND HEX CODES )
    for color in range(0, palette_size):
        generate_COLOR()

def main():
    color_num = int(input('Enter the number of colors to generate: '))
    if color_num > 1:
        generate_PALETTE(color_num)
    elif color_num == 1:
        generate_COLOR()
    else:
        print(f'Cannot generate {color_num} colors.  Try a positive or nonzero number.')
        exit()
    
    print("DONE.")

if __name__ == "__main__":
    main()