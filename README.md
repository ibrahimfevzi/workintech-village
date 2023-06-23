# Python - OOP Intro 

### Proje Kurulumu

Projeyi VS Code kullanarak açabilirsiniz.
Projelerimizi belli bir düzen içerisinde tutmak iyi bir alışkanlıktır.
Örnek bir Lokasyon: C:/Users/Documents/Workintech/Python/OOP.

### Workintech Köyü'nün Sana İhtiyacı Var !!!!

Workintech Köy'ünde yaşayan köy sakinleri 2023 kışının çok soğuk ve karlı geçeceğinden dolayı endişeliler. Kışın köyde ciddi bir yiyecek kıtlığı olabileceğini düşünüyorlar.
Köyleri için bugünden itibaren yiyecek stoğu yapabilecekleri bir Silo'ya ihtiyaçları olduklarını karar verdiler. Bu Silo'yu tasarlamak için senin kapını çaldılar.

### Görevimiz:

* Silo sınıfının hangi değişkenleri olmalı ?
* ```Silo``` isimli bir sınıf oluşturmalıyız.
* Silo sınıfı için  ```radius```, ```height``` isimli 2 tane ````instance variable```` tanımlamalıyız. Bunun dışında bir Silo da olması gerekebilecek minimum 3 adet daha ````instance variable```` tanımlamalıyız.
* Silo sınıfı için tüm  ````instance variable```` değerlerini ekleyebileceğimiz bir ```constructor``` yazamamız gerekmekte.
* Tüm sınıf değişkenlerimiz için ```getter&setter``` metodları yazmalıyız. Hiçbir şekilde sınıf değişkenlerimize getter veya setter metodları olmadan erişmemeliyiz.
* Köy sakinleri silomuzun kaplayacağı alanı merak ediyorlar. Bu yüzden Silo sınıfımızda bir metod(fonksiyonu) tanımlamalıyız. ```getArea``` isiminde olabilir. ```radius*radius*PI``` şeklinde hesaplama yapmalı ve alan değerini dönmeli.
* Köy sakinlerinin bir diğer merak ettikleri konu yapılan siloya ne kadar malzeme depolayabilecekleri ? Bu işlem içinde silonun hacmini hesaplamalıyız.```getVolume``` isimli bir metod(fonksiyonu) işimizi görebilir. ```getArea()*height``` değerini dönmeli.
* Silomuzun tüm özelliklerini görebileceğimiz bir ```__str__``` metodu(fonksiyonu) tanımlamalıyız.
* Silomuz için tanımladığımız değişkenlerin durumlarında(state) değişiklik yapabileceğimiz(behaviour) 3 tane daha metod(fonksiyonu) tanımlamalıyız.


### Uygulamayı Test Etmek

Uygulamada bir adet ```main``` metodu olmalı ve içerisinde Silo sınıfı kullanılarak bir silo objesi tanımlamalısınız.

```getArea()``` fonksiyonu radius=3.75 için 44.1786466911 değerini dönmeli.

```getVolume()``` fonksiyonu radius=3.75 ve height = 2 için 88.3572933822 değerini dönmeli.

Yazdığımız diğer tüm metodları test etmeliyiz ve doğru çalıştıklarından emin olmalıyız.


### Optional

*Silomuzun yere deydiği kısmının çevresini hesaplayabileceğimiz bir metodu nasıl yazardık ?

