print('SELAMAT BERBELANJA DI KOREAN JASTIP')
print('HAPPY SHOPPING')
nama = str(input('Masukkan nama : '))
keterangan_barang = str(input('Masukkan keterangan barang : '))
pembayaran = str(input('Masukkan metode pembayaran : '))
durasi_pembayaran = int(input('Masukkan durasi pembayaran : '))

metode = ['DP']
if(pembayaran not in metode and durasi_pembayaran <= 60 ):
    print('Selamat pembayaran Anda telah berhasil')
else:
    print('Maaf pembayaran Anda gagal')
