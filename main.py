# Nilai Keanggotaan

def nilaiKeanggotaanTekananDarah(type: int, x: float) -> float:
    # Tekanan darah normal  
    if type == 0:
        if x <= 100:
            return 1
        elif 100 < x <= 125:
            return (x-100)/(125-100)
        else:
            return 0
    # tekanan darah pra hipertensi        
    elif type == 1:
        if x <= 120 or x >= 145:
            return 0
        elif 120 < x <= 132.5:
            return (x-120)/(132.5-120)
        elif 132.5 < x <= 145:
            return (145-x)/(145-132.5)
    # Tekanan darah hipertensi
    else:
        if x <= 140:
            return 0
        elif 140 < x <= 160:
            return (x-140)/(160-140)
        elif x > 160:
            return 1

def nilaiKeanggotaanIMT(type: int, x: float) -> float:
    # IMT Underweight
    if type == 0 :
        if x <= 15.5:
            return 1
        elif 15.5 < x <= 18.5:
            return (18.5-x)/(18.5-15.5)
        else:
            return 0
    # IMT Normal
    elif type == 1:
        if x <= 15.5 or x >= 22.9:
            return 0
        elif 15.5 < x <= 20:
            return (x-15.5)/(20-15.5)
        elif 20 < x <= 22.9 :
            return (22.9-x)/(22.9-20)
    # IMT Overweight
    else :
        if x <= 20:
            return 0
        elif 20 < x <= 24.9:
            return (x-20)/(24.9-20)
        elif x > 24.9:
            return 1

def nilaiKeanggotaanKadarGlukosaDarah(type: int, x: float) -> float:
    # Kadar Glukosa Darah normal  
    if type == 0:
        if x <= 44 or x >= 146:
            return 0
        elif 44 < x <= 95:
            return (x-44)/(95-44)
        elif 95 < x < 146:
            return (146-x)/(146-95)
    # Kadar Glukosa Darah sedang
    elif type == 1:
        if x <= 141 or x >= 192:
            return 0
        elif 141 < x <= 169:
            return (x-141)/(169-141)
        elif 169 < x < 192:
            return (192-x)/(192-169)
    # Kadar Glukosa Darah tinggi
    else:
        if x <= 187:
            return 0
        elif 187 < x <= 232:
            return (232-x)/(232-187)
        elif x > 232:
            return 1

def nilaiKeanggotaanDiagnosis(type: int, x: float) -> float:
    # Diagnosis Normal
    if type == 0:
        if x <= 40:
            return 1
        elif 40 < x <= 45:
            return (45-x)/(45-40)
        else:
            return 0
    # Diagnosis Pradiabetes
    if type == 1:
        if x <= 40 or x >= 60:
            return 0
        elif 40 < x <= 55:
            return (x-40)/(55-40)
        elif 55 < x <= 60:
            return (60-x)/(60-55)
    # Diagnosis Diabetes
    else:
        if x <= 55:
            return 0
        elif 55 <= x <= 100:
            return (x-55)/(100-55)
        elif x >= 100:
            return 1

# Inferensi
    # Tipe keanggotaan
        # Tekanan Darah
            # 0 -> Normal
            # 1 -> Pra hipertensi
            # 2 -> Hipertensi

        # IMT
            # 0 -> Underweight
            # 1 -> Normal
            # 2 -> Overweight

        # Kadar Glukosa Darah
            # 0 -> Normal
            # 1 -> Sedang
            # 2 -> Tinggi

        # Diagnosis
            # 0 -> Normal
            # 1 -> Pradiabetes
            # 2 -> Diabetes

    # Tabel Inferensi
    # (Tekanan Darah, IMT, Kadar Glukosa Darah) -> Diagnosis
        # (0, 0, 0) -> 0
        # (0, 0, 1) -> 0
        # (0, 0, 2) -> 1
        # (0, 1, 0) -> 0
        # (0, 1, 1) -> 1 
        # (0, 1, 2) -> 2
        # (0, 2, 0) -> 0
        # (0, 2, 1) -> 1
        # (0, 2, 2) -> 2

        # (1, 0, 0) -> 0
        # (1, 0, 1) -> 1
        # (1, 0, 2) -> 2
        # (1, 1, 0) -> 0
        # (1, 1, 1) -> 1
        # (1, 1, 2) -> 1
        # (1, 2, 0) -> 0
        # (1, 2, 1) -> 2
        # (1, 2, 2) -> 2
        
        # (2, 0, 0) -> 0
        # (2, 0, 1) -> 1
        # (2, 0, 2) -> 2
        # (2, 1, 0) -> 0
        # (2, 1, 1) -> 1
        # (2, 1, 2) -> 2
        # (2, 2, 0) -> 0
        # (2, 2, 1) -> 1
        # (2, 2, 2) -> 2 


def getDiagnosis(i: int, j: int, k: int) -> int:
    tabel_inferensi = {
        "000" : 0,
        "001" : 0,
        "002" : 1,
        "010" : 0,
        "011" : 1, 
        "012" : 2,
        "020" : 0,
        "021" : 1,
        "022" : 2,
        "100" : 0,
        "101" : 1,
        "102" : 2,
        "110" : 0,
        "111" : 1,
        "112" : 1,
        "120" : 0,
        "121" : 2,
        "122" : 2,
        "200" : 0,
        "201" : 1,
        "202" : 2,
        "210" : 0,
        "211" : 1,
        "212" : 2,
        "220" : 0,
        "221" : 1,
        "222" : 2
    }

    key = "{}{}{}".format(i, j, k)
    return tabel_inferensi[key]

def fuzzyInference(tds: float, imt: float, kgd: float):
    # Mencari nilai keanggotaan untuk masing-masing diagnosis
    # nk[0] -> nilai kaeanggotaan diagnosis normal
    # nk[1] -> nilai kaeanggotaan diagnosis pradiabetes
    # nk[2] -> nilai kaeanggotaan diagnosis diabetes

    z = [] # nilai z
    a = [] # nilai alpha predikat

    for i in range(3):
        for j in range(3):
            for k in range(3):
                nk_tds = nilaiKeanggotaanTekananDarah(i, tds)
                nk_imt = nilaiKeanggotaanIMT(j, imt)
                nk_kgd = nilaiKeanggotaanKadarGlukosaDarah(k, kgd)

                # mencari nilai minimum dari nilai keanggotaan untuk mendapatkan alpha predikat
                alpha_predikat = min(nk_tds, nk_imt, nk_kgd)
                a.append(alpha_predikat)
                diagnosis = getDiagnosis(i, j, k)

                if diagnosis == 0: # If diagnosis normal
                    nilai_z = 45 - (alpha_predikat*(45-40))
                    z.append(nilai_z)
                elif diagnosis == 1:  # elif diagnosis pradiabetes
                    nilai_za = 40 + (alpha_predikat*(55-40))
                    nilai_zb = 60 - (alpha_predikat*(60-55))
                    nilai_z = (nilai_za+nilai_zb)/2
                    z.append(nilai_z)
                else : #elif diagnosis diabetes
                    nilai_z = 55 + (alpha_predikat*(100-55))
                    z.append(nilai_z)   
    print(z)
    print(a)

    # Defuzzyfikasi
    ap_kali_z = 0
    sum_a = 0

    # Menghitung nilai ap*z dan sum_a
    for i in range(len(z)):
        sum_a += a[i]
        ap_kali_z += z[i]*a[i]

    Z = ap_kali_z/sum_a
    print("Z : {}".format(Z))
    nk = [0, 0, 0]
    nk[0] = nilaiKeanggotaanDiagnosis(0, Z)
    nk[1] = nilaiKeanggotaanDiagnosis(1, Z)
    nk[2] = nilaiKeanggotaanDiagnosis(2, Z)

    print("Nilai Keanggotaan Diagnosis Normal[{}] = {}".format(Z, nk[0]))
    print("Nilai Keanggotaan Diagnosis Pradiabetes[{}] = {}".format(Z, nk[1]))
    print("Nilai Keanggotaan Diagnosis Diabetes[{}] = {}".format(Z, nk[2]))

    max_value = max(nk)
    max_idx = nk.index(max_value)

    return {
        "diagnosis": max_idx,
        "nk": nk
    }
        
if __name__ == "__main__":
    fuzzyInference(187, 0, 0)