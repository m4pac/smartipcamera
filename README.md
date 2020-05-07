Görüntü Sistemlerinin Akıllılaştırılması
-
Projenin amacı hali hazırda görüntü sistemlerini kullanan işyeri/kurum sahibi ya da son kullanıcılar tarafından mevcutta bulunan görüntüleme sistemlerini (Ip kameralar) maliyet tasarrufu sağlayarak yenilemelerine imkan tanıyor. 

Görüntü işleme teknolojileri giderek gelişiyor. Fakat artan maliyetler ve düşük karlılık oranları yüzünden çoğu işyeri/son kullanıcı mevcuttaki sistemlerini yenileriyle değiştiremiyorlar. 

Bu Proje ile Nelere Çözüm Sunmayı Umuyorum?
-
Hareket algılama özelliği bulunmayan, bundan dolayı hareket bazlı log alamayan görüntü sistemlerini akıllılaştırmayı amaçlıyorum. Bu sayede kullanıcılar geçmişe dönük kayıt ararken zaman harcamayacaklar. 

Özellikler:
-
Log Alma
-
Hareket algılanan her saniye günlüğe eklenir. Bu sayede arama kolaylığı sağlanır. Kargocunun gelip gelmediğinden emin değil misin? Bunun için koskoca günün tüm kayıtlarını dakika dakika izlemek zorunda değilsin. Hareket algılanan dakika loglarına bakarak zamandan tasarruf et :)

Ayrıca bu sistemin AVM gibi yerlerdeki güvenlik kameralarında kullanılması günde hangi saatlerde yoğunluk olduğu vs. günlüklerden analiz edilebilir. 

Hareket Algılama Durumunda Alarm/Müzik Çalma
-
Programın bulunduğu aynı dizin altında hareket algılanması sırasında çalınması istenen ses dosyası ismi kod kısmına eklenerek çalınması sağlanabilir. 

Kaynak Kayıt Haricinde Ayrı Bir Kayıt Alma
-
Kayıt cihazının aldığı kayıtlar haricinde program analiz ettiği görüntüleri analiz görüntüleriyle birlikte ayrı olarak kaydeder.

Örnek topoloji: 
Ip Camera > Router > Rasberry Pi smartipcamera.py

OpenCV Sürüm: 4.2.0.34


Python Sürüm: 3.7.6

Playsound icin:
pip install playsound

Opencv icin: 
pip install opencv-python
