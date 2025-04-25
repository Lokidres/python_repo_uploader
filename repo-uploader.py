from github import Github
import os
from getpass import getpass
import time
import sys
from tqdm import tqdm
import base64

def show_loading_animation():
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for i in range(10):
        sys.stdout.write("\rYükleniyor " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.2)

def github_repo_yukleyici():
    print("\n=== GitHub Repo Yükleyici ===\n")
    print("Token Oluşturma Adımları:")
    print("1. GitHub.com > Settings > Developer settings > Personal access tokens > Tokens (classic)")
    print("2. 'Generate new token (classic)' seçin")
    print("3. Note kısmına bir isim yazın")
    print("4. Expiration: No expiration seçin")
    print("5. Select scopes kısmında 'repo' ve 'workflow' kutucuklarını işaretleyin")
    print("6. Generate token butonuna tıklayın\n")
    
    token = getpass("Oluşturduğunuz token'ı yapıştırın: ")
    
    try:
        # Maksimum dosya boyutu (100MB)
        MAX_FILE_SIZE = 100 * 1024 * 1024  
        
        g = Github(token)
        user = g.get_user()
        username = user.login
        print(f"\n✅ Bağlantı başarılı! Hoş geldin {username}")
        
        repo_name = input("\nOluşturulacak repo adı: ")
        repo_description = input("Repo açıklaması: ")
        is_private = input("Private repo olsun mu? (e/h): ").lower() == 'e'
        
        print("\nRepo oluşturuluyor...")
        repo = user.create_repo(
            name=repo_name,
            description=repo_description,
            private=is_private,
            auto_init=True
        )
        
        print(f"\n✅ Repo başarıyla oluşturuldu: {repo.html_url}")
        
        while True:
            print("\nDosya/Klasör yükleme seçenekleri:")
            print("1. Tek dosya yükle")
            print("2. Klasör yükle")
            print("3. Çıkış")
            
            secim = input("\nSeçiminiz (1-3): ")
            
            if secim == "1":
                while True:
                    dosya_yolu = input("\nYüklenecek dosyanın tam yolunu girin: ")
                    if os.path.isfile(dosya_yolu):
                        try:
                            with open(dosya_yolu, 'r', encoding='utf-8') as file:
                                content = file.read()
                                repo.create_file(
                                    path=os.path.basename(dosya_yolu),
                                    message="Dosya yüklendi",
                                    content=content
                                )
                            print(f"\n✅ {os.path.basename(dosya_yolu)} başarıyla yüklendi!")
                            break
                        except Exception as e:
                            print(f"\n❌ Hata: {str(e)}")
                    else:
                        print("\n❌ Dosya bulunamadı! Tekrar deneyin.")
            
            elif secim == "2":
                while True:
                    klasor_yolu = input("\nYüklenecek klasörün tam yolunu girin: ")
                    if os.path.isdir(klasor_yolu):
                        try:
                            total_files = sum([len(files) for r, d, files in os.walk(klasor_yolu)])
                            with tqdm(total=total_files, desc="Dosyalar yükleniyor") as pbar:
                                for root, dirs, files in os.walk(klasor_yolu):
                                    for file in files:
                                        full_path = os.path.join(root, file)
                                        file_size = os.path.getsize(full_path)
                                        
                                        if file_size > MAX_FILE_SIZE:
                                            print(f"\n⚠️ {file} dosyası çok büyük (>100MB), atlanıyor...")
                                            continue
                                            
                                        try:
                                            with open(full_path, 'rb') as f:
                                                content = f.read()
                                                # Binary dosyalar için base64 encoding
                                                if not is_text_file(file):
                                                    content = base64.b64encode(content).decode()
                                                
                                                relative_path = os.path.relpath(full_path, klasor_yolu)
                                                repo.create_file(
                                                    path=relative_path,
                                                    message=f"{relative_path} eklendi",
                                                    content=content
                                                )
                                                pbar.update(1)
                                        except Exception as e:
                                            print(f"\n⚠️ {file} yüklenirken hata: {str(e)}")
                                            continue
                            
                            print("\n✅ Klasör içeriği başarıyla yüklendi!")
                            break
                        except Exception as e:
                            print(f"\n❌ Hata: {str(e)}")
                    else:
                        print("\n❌ Klasör bulunamadı! Tekrar deneyin.")
            
            elif secim == "3":
                print("\n👋 Program sonlandırılıyor...")
                break
            
            else:
                print("\n❌ Geçersiz seçim!")

    except Exception as e:
        print(f"\n❌ Bir hata oluştu: {str(e)}")

def is_text_file(filename):
    """Dosyanın text dosyası olup olmadığını kontrol eder"""
    text_extensions = {'.txt', '.py', '.js', '.html', '.css', '.json', '.md', '.xml', '.csv'}
    return os.path.splitext(filename)[1].lower() in text_extensions

if __name__ == "__main__":
    github_repo_yukleyici()