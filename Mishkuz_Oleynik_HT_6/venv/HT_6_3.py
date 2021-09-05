import pickle


def pars_dict(dict_in):
    dict_out = {}
    for key in sorted(dict_in.keys()):
        key_out = str.split(key , sep = ",")[0]
        dict_out[key_out] = str.split(key , sep = "," )
    return dict_out


users = {}
with open("SNP.csv", "r", encoding="utf-8") as snp:
    # hobby_gen = (st for st in hobby)
    with open("Hobby.csv" , "r", encoding="utf-8") as hobby:
        users_gen = (key[:-1] for key in snp)
        hobby_gen = (val[:-1] for val in hobby)
        for key in users_gen:
            try:
                users[key] = hobby_gen.__next__()
            except:
                users[key] = None
print(type(users), users)
with open("users_dict.bin" , "wb") as dict_file:
    pickle.dump(users, dict_file)


SNP = pars_dict(users)
print(SNP)

