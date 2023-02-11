import time

def atm():
    kullanici = 'orhan'
    sifrem = '1234'
    bakiye = 5000
    borc = 3000
    hak = 3

    while True:
        hesap = input('Kullanıcı adınızı giriniz =')
        sifre = input('Şifrenizi giriniz =')
        hak -= 1

        if hesap == kullanici and sifre == sifrem:
            while True:
                print('''İşlemler :
                1-Para Çekme
                2-Para Yatırma
                3-Para Gönderme
                4-Borç Yatırma
                5-Şifre Değiştirme
                6-Bakiye Sorgulama
                7-Çıkış''')
                islem = int(input('Yapmak istediğiniz işlem numarasını giriniz ='))

                if islem == 1:
                    #bakiye sorgula, yetmiyorsa tekrar sor, eğer yetiyorsa bakiyeden düşecek.
                    while True:
                        cek = int(input('Çekmek istediğiniz miktarı giriniz ='))
                        if cek <= bakiye:
                            onay = input(f'{cek}TL para çekme işlemini onaylıyor musunuz? (E/H) =')
                            onay=onay.upper()
                            if onay == 'E':
                                bakiye -= cek
                                print('Çekilen Miktar:',cek)
                                print('Kalan Bakiye:',bakiye)
                                break
                            elif onay == 'H':
                                print('İşlem iptal ediliyor...')
                                break
                            else:
                                print('Geçersiz işlem yaptınız, tekrar deneyiniz...')
                        else:
                            print('Yetersiz Bakiye!')

                elif islem == 2:
                    #para miktarı istenecek, para bakiyeye eklenecek.
                    yatir = int(input('Yatırmak istediğiniz miktarı giriniz ='))
                    onay = input(f'{yatir}TL para yatırma işlemini onaylıyor musunuz? (E/H) =')
                    onay = onay.upper()
                    if onay == 'E':
                        bakiye += yatir
                        print('Yatırılan Miktar',yatir)
                        print('Güncel Bakiye',bakiye)
                    elif onay == 'H':
                        print('İşlem iptal ediliyor....')
                    else:
                        print('geçersiz giriş yapıldı. İşlem iptal ediliyor...')

                elif islem == 3:
                    # Gönderilmek istenen miktar, bakiye kontrol, gönderilecek hesap no, onay, bakiyeden düşür
                    while True:
                        gonder = int(input('Gönderilmek istenen tutarı giriniz ='))
                        if gonder <= bakiye:
                            hesapNo = int(input('Gönderilecek Hesap Numarası ='))
                            onay = input(f'{hesapNo} Hesap Numaralı kullanıcıya {gonder}TL para transferini onayllıyor musunuz? (E/H) =')
                            onay=onay.upper()
                            if onay == 'E':
                                bakiye -= gonder
                                print(f'{hesapNo} numaralı hesaba {gonder}TL gönderildi.')
                                print('Kalan Bakiye:',bakiye)
                                break
                            elif onay == 'H':
                                print('işlem iptal edildi. Tekrar giriş yapınız.')
                            else:
                                print('Geçersiz giriş yaptınız. İşlemden çıkılıyor..')
                                break
                        else:
                            print('Yetersiz Bakiye!')
                elif islem == 4:
                    #borc kontrol,borc, ödeme miktarı, bakiye kontrol, onay, bakiye düşecek
                    if borc > 0:
                        print('Güncel Borcunuz:',borc)
                        while True:
                            borcYatir = int(input('Yatırmak istediğiniz borç miktarını giriniz ='))
                            if borcYatir <= bakiye:
                                if borcYatir <= borc:
                                    onay = input(f'{borcYatir}TL Ödeme işlemini onaylıyor musunuz? (E/H) =')
                                    onay = onay.upper()
                                    if onay == 'E':
                                        borc -= borcYatir
                                        bakiye -= borcYatir
                                        print('Ödenen Borç Miktarı: ',borcYatir)
                                        print('Güncel Kalan Borç Miktarı: ', borc)
                                        print('Güncel Bakiye: ',bakiye)
                                        break
                                    elif onay =='H':
                                        print('İşlem iptal ediliyor...')
                                        break
                                    else:
                                        print('Geçersiz giriş yapıldı.İşlem iptal ediliyor...')
                                        break
                                else:
                                    print('Borcunuzdan fazlasını yatıramazsınız!')
                            else:
                                print('Yetersiz Bakiye!')
                    else:
                        print('Borcunuz bulunmamaktadır.')

                elif islem == 5:
                    #eski şifre kontrolü, 3hak, yeni şifre
                    hakYeni = 3
                    while True:
                        eski = input('Mevcut şifrenizi giriniz =')
                        hakYeni -= 1
                        if eski == sifrem:
                            yeniSifre = input('Yeni şifrenizi giriniz =')
                            sifrem = yeniSifre
                            print('Şifreniz güncellenmiştir.')
                            break
                        elif hakYeni==0:
                            print('Hakkınız bitti işlem iptal ediliyor...')
                            break
                        else:
                            
                            print('Hatalı şifre girdiniz!!!')

                elif islem == 6:
                    if bakiye > 0:
                        print('Mevcut Bakiyeniz:',bakiye)
                    else:
                        print('Bakiyeniz bulunmuyor')
                
                elif islem == 7:
                    print('Program kapatılıyor...')
                    time.sleep(2)
                    print('Bizi tercih ettiğiniz için teşekkür ederiz.')
                    break
            break
        elif hak == 0:
            print('Hakkınız bitmiştir. Program kapatılıyor...')
            break
        elif hesap != kullanici and sifre != sifrem:
            print('Kullanıcı adı ve şifre hatalı!')
        elif hesap != kullanici:
            print('Kullanıcı adı hatalı!')
        elif sifre != sifrem:
            print('Şifre hatalı!')

atm()