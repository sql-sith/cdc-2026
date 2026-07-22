from mmap import ACCESS_COPY

global Accu

global guess_num
global guess
global guess_mult
global tarnum
tarnum = float(346.789)
guess_num = 0
Accu = 0.0000001
tar_digit = len(str(tarnum))
tar_whole_digit = len(str(int(tarnum)))
print(tar_whole_digit)
guess_mult = 10 ** (tar_whole_digit - 2)
guess = pow(guess_mult, 1)


def fSqRt(tarnum, guess, guess_num, guess_mult):
    Diff = tarnum - (pow(guess, 2))

    while Accu > (abs(Diff)):
        while Diff > (10 ** guess_mult):
            guess = guess + (10 ** guess_mult)
            guess_num = guess_num + 1
            Diff = tarnum - (guess**2)
        else:
            guess_num = guess_num + 1
            guess_mult = guess_mult-1
    else:
        return guess
        return guess_num

fSqRt(tarnum, guess, guess_num, guess_mult)

print(fSqRt(tarnum, guess, guess_num, guess_mult))




