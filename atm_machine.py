import datetime
import random
from member import Member

atm = Member(id)

while True:

    id = int(input("Masukan pin ATM anda :"))
    trial = 0
    pin = atm.getPinInfo()

    while (id != pin and trial < 4):
        if trial == 3:
            print("maaf pin yang anda masukan tidak benar!!")
            exit()

        id = int(input("Pin anda salah silakan Masukan pin ATM anda :"))
        trial += 1

    while True:
        print(f"Selamat Datang di progate ATM ")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        member_select = int(input("\nsilahkan masukan menu pilihan anda : "))

        if member_select == 1:
            print("jumlah saldo anda sekarang : " + str(atm.getSaldoInfo()))

        elif member_select == 2:
            member_choice = input("apakah anda ingin melakukan penarikan? y/n:")

            if member_choice == "y" or member_choice == "yes":
                print("\njumlah saldo anda " + str(atm.getSaldoInfo()))
                jumlah_debet = int(input("\n masukan jumlah nominal :"))

                member_choice1 = input("apakah anda yakin akan melakukan penarikan y/n :")

                if member_choice1 == "y" or member_choice1 == "yes":
                    if jumlah_debet <= int(atm.getSaldo()):
                        atm.setDebet(jumlah_debet)
                        print("\nsisa saldo anda " + str(atm.getSaldoInfo())+"\n")
                    else:
                        print("\nmaaf jumlah saldo anda tidak cukup")


        elif member_select == 3:
            nominal = float(input("\n Masukkan nominal saldo: "))
            verify_deposit = input("\n Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " :")

            if verify_deposit == "y" or verify_deposit == "yes":
                atm.setSimpan(nominal)

        elif member_select == 4:
            member_update = int(input("\nsilahkan masukan pin baru anda (pin harus berupa angka!!) : "))

            if atm.getPinInfo() != member_update:
                member_choice =input("apakah anda yakin akan mengubah pin? y/n : ")

                if member_choice  == "y" or member_choice == "yes":
                    atm.pin = member_update

        elif member_select == 5:
             print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
             print("No. Rekord: ", random.randint(100000, 1000000))
             print("Tanggal: ", datetime.datetime.now())
             print("Saldo akhir: ", atm.getSaldoInfo())
             print("Terima kasih telah menggunakan ATM Progate!")
             exit()
        else:
            print(0)
