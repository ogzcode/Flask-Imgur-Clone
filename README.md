# Flask File Example

Bu proje, Flask framework'ü kullanılarak geliştirilmiş basit bir resim uygulamasını içerir. Bu uygulama sayesinde kullanıcılar resim yükleyebilir, görüntüleyebilir ve paylaşabilir.

## Başlangıç

Bu adımlar, projeyi yerel makinenizde çalıştırmak için gereken temel adımları içerir.

1. **Gereksinimleri Kurma:**

   Projenin düzgün çalışabilmesi için öncelikle gerekli bağımlılıkları kurmalısınız. Proje dizininde aşağıdaki komutu çalıştırarak bunu yapabilirsiniz:

```
pip install -r requirements.txt
```


2. **Veritabanı Ayarları:**

Proje, yüklenen resimleri ve ilgili verileri saklamak için bir veritabanına ihtiyaç duyar. `config.py` dosyasında veritabanı bağlantı bilgilerini ayarlayın.

3. **Uygulamayı Çalıştırma:**

Terminalde aşağıdaki komutla Flask uygulamasını başlatabilirsiniz:

```
flask run
```

Uygulama varsayılan olarak `http://localhost:5000` adresinde çalışacaktır. Tarayıcınızı açarak bu adrese giderek uygulamayı kullanabilirsiniz.

## Kullanım

Uygulama başlatıldığında ana sayfa karşınıza gelecektir. Bu sayfada aşağıdaki işlemleri yapabilirsiniz:

- "Yükle" düğmesine tıklayarak yeni bir resim yükleyebilirsiniz.
- Yüklenen resimleri ana sayfada görüntüleyebilirsiniz.
- Her resmin altında "Paylaş" düğmesi bulunur, bu düğmeye tıklayarak resminizi paylaşabilirsiniz.
