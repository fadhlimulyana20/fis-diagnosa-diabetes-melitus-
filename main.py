# Nilai Keanggotaan

def nilaiKeanggotaanTekananDarah(type: int, x: float) -> float:
    # Tekanan darah normal  
    if type == 0 :
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
        elif 132.5 < x <= 145 :
            return (145-x)/(145-132.5)
    # Tekanan darah hipertensi
    else :
        if x >= 140:
            return 0
        elif 140 < x <= 160:
            return (x-140)/(160-140)
        elif x > 160:
            return 1

# Interferensi
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

        # Diagnoisis
            # 0 -> Normal
            # 1 -> Pradiabetes
            # 2 -> Diabetes

    # Tabel Interferensi
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
        # (1, 0, 1) -> 2
        # (1, 0, 2) -> 1
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

if __name__ == "__main__":
    print(nilaiKeanggotaanTekananDarah(0, 115.0))