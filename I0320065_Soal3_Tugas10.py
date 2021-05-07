#biodata dengan a

nama = input ('nama: ')
umur = input ('umur: ')
alamat= input('alamat: ')
hobi = input ('hobi: ')

print('namaku adalah %s, aku berumur %s, aku tinggal di %s, dan hobiku adalah %s'%(nama,umur,alamat,hobi))

teks = "nama: {}\n umur:{}\nalamat:{}\nhobi:{}".format(nama,umur,alamat,hobi)

file_bio = open ("I0320065_soal 3_tugas 10.txt", "a")

file_bio.write(teks)

file_bio.close()