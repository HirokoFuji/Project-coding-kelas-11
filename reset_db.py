import os
from app import create_app, db
from app.models.models import Schedule, Category, Product

def reset_database():
    # Hapus file database jika ada
    if os.path.exists('data.db'):
        os.remove('data.db')
        print("Database lama dihapus.")
    
    # Buat aplikasi Flask
    app = create_app()
    
    # Buat database baru dan semua tabel
    with app.app_context():
        # Drop all tables first to ensure clean state
        db.drop_all()
        # Create all tables
        db.create_all()
        print("Database baru berhasil dibuat dengan semua tabel yang diperlukan.")

if __name__ == '__main__':
    reset_database() 