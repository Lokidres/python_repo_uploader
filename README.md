GitHub Repo Yükleyici Aracı
📋 Açıklama
Bu araç, GitHub API'sini kullanarak kolayca GitHub depoları oluşturmanıza ve dosyaları/klasörleri otomatik olarak yüklemenize olanak tanır. GitHub depolarınızı yönetmek için basit bir komut satırı arayüzü sunar.

⚙️ Özellikler
Yeni GitHub depoları oluşturma
Tek dosya yükleme
Tüm klasörleri yükleme
İlerleme göstergeleri
Hata yönetimi
Kullanıcı dostu arayüz
🔧 Kurulum

1. Bu depoyu klonlayın:
```bash
git clone https://github.com/kullaniciadi/repo-uploader.git
cd repo-uploader
```

2. Gerekli paketleri yükleyin:
```bash
pip install PyGithub
pip install tqdm
```

3. Gerekli Python sürümü: Python 3.6 veya üzeri

📦 Gerekli Kütüphaneler
- PyGithub: GitHub API entegrasyonu için
- tqdm: İlerleme çubuğu için
- os: Dosya sistemi işlemleri için
- base64: Binary dosya kodlaması için

🚀 Kullanım Adımları
GitHub Personal Access Token Alın:

GitHub.com > Settings > Developer settings
"Personal access tokens" > "Tokens (classic)" seçin
"Generate new token (classic)" tıklayın
Not kısmını doldurun ve "No expiration" seçin
"repo" ve "workflow" izinlerini işaretleyin
"Generate token" butonuna tıklayın
Token'ı güvenli bir yere kaydedin
Programı Çalıştırın:

Programı başlatın
Token'ınızı girin
Repo adı ve açıklaması belirleyin
Menüden işlem seçin (dosya/klasör yükleme)
Yüklemek istediğiniz dosya/klasör yolunu girin
⚠️ Önemli Notlar
Token'ınızı kimseyle paylaşmayın
Yüklenecek dosyaların UTF-8 formatında olduğundan emin olun
Maksimum dosya boyutu: 100MB
Binary dosyalar otomatik olarak base64 ile kodlanır

🐛 Hata Çözümleri
Token hatası: Token'ın doğru yetkilere sahip olduğundan emin olun
Dosya bulunamadı: Dosya yolunun doğru olduğunu kontrol edin
Yükleme hatası: Dosya içeriğinin uygun formatta olduğunu kontrol edin
📝 Lisans
MIT License

🤝 Katkıda Bulunma
Bu depoyu fork edin
Yeni bir branch oluşturun
Değişikliklerinizi commit edin
Branch'inizi push edin
Pull request oluşturun
