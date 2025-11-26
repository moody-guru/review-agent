import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env")
else:
    print(f"🔑 Using Key: {api_key[:10]}...")
    genai.configure(api_key=api_key)

    print("\n📡 Connecting to Google AI...")
    try:
        found = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ AVAILABLE: {m.name}")
                found = True
        
        if not found:
            print("❌ No models found. Your API key might be invalid or has no permissions.")
            
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        print("\n💡 TIP: Check if you enabled the API in Google Cloud Console.")