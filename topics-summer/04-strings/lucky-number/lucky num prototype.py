from pip._internal.index import collector

#Created by Naomi S
def lucky_num_generator(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    x = name.split()
    #print(x)
    first_name_len = len(x[0])
    last_name_len = len(x[1])
    #print(first_name_len)
    #print(last_name_len)
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_fn_cnt = 0
    for char in x[0]:
        if char in vowels:
            vowel_fn_cnt += 1
    #print(vowel_fn_cnt)
    const_fn_cnt =first_name_len - vowel_fn_cnt
    #print(const_fn_cnt)
    vowel_ln_cnt = 0
    for char in x[1]:
        if char in vowels:
            vowel_ln_cnt += 1
    #print(vowel_ln_cnt)
    const_ln_cnt =last_name_len - vowel_ln_cnt
    #print(const_ln_cnt)

    sm_name = first_name_len if first_name_len < last_name_len else last_name_len
    #print("sm ", sm_name)
    lg_name = first_name_len if first_name_len > last_name_len else last_name_len
    #print("lg ", lg_name)

    sm_vowel = vowel_fn_cnt if vowel_fn_cnt < vowel_ln_cnt else vowel_ln_cnt
    #print("sm v", sm_vowel)
    lg_vowel = vowel_fn_cnt if vowel_fn_cnt > vowel_ln_cnt else vowel_ln_cnt
    #print("lg v", lg_vowel)

    sm_cnst = const_fn_cnt if const_fn_cnt < const_ln_cnt else const_ln_cnt
    #print("sm c ", sm_cnst)
    lg_cnst = const_fn_cnt if const_fn_cnt > const_ln_cnt else const_ln_cnt
    #print("lg c ", lg_cnst)

    big = lg_cnst * lg_name * lg_vowel
    small = sm_cnst * sm_name * sm_vowel
    #print("big ", big)
    #print("small ", small)

    lucky = big - small
    if lucky == 0:
        lucky = 13
    print(f'Hi, {name}', "you're lucky # is ", lucky)
# Press the green button in the gutter to run the script.
lucky_num_generator('john doe')
lucky_num_generator('chloe perez')
lucky_num_generator('naomi skarphol')
lucky_num_generator('olivia lewis')