import dotenv

try:
    from dotenv import load_dotenv
    print("✅ Библиотека найдена и работает!")
except ImportError:
    print("❌ Библиотека действительно не видна")