"""
Firebase Handler - Gerencia conexão com Firebase
"""

import os
import json
from dotenv import load_dotenv

load_dotenv()

class FirebaseHandler:
    """Gerencia conexão com Firebase"""
    
    def __init__(self):
        """Inicializa conexão com Firebase"""
        try:
            import firebase_admin
            from firebase_admin import credentials
            from firebase_admin import db
            
            # Verificar se Firebase já está inicializado
            if not firebase_admin._apps:
                # Carregar credenciais do .env ou arquivo
                self.firebase_config = {
                    "apiKey": os.getenv("FIREBASE_API_KEY"),
                    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
                    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
                    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
                    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
                    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
                    "appId": os.getenv("FIREBASE_APP_ID")
                }
                
                # Inicializar Firebase
                cred = credentials.Certificate("firebase_key.json")
                firebase_admin.initialize_app(cred)
            
            self.db = db
            self.connected = True
        except Exception as e:
            print(f"⚠️ Firebase não disponível: {str(e)}")
            self.connected = False
    
    def save_analysis(self, user_id, analysis_data):
        """Salva análise no Firebase"""
        if not self.connected:
            return {"status": "offline", "message": "Firebase não conectado"}
        
        try:
            ref = self.db.reference(f"users/{user_id}/analysis")
            ref.set(analysis_data)
            return {"status": "success", "message": "Análise salva"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_analysis_history(self, user_id):
        """Recupera histórico de análises"""
        if not self.connected:
            return []
        
        try:
            ref = self.db.reference(f"users/{user_id}/analysis")
            return ref.get().val() or []
        except:
            return []
    
    def save_recommendation(self, user_id, recommendation_data):
        """Salva recomendação no Firebase"""
        if not self.connected:
            return {"status": "offline"}
        
        try:
            ref = self.db.reference(f"users/{user_id}/recommendations")
            ref.push(recommendation_data)
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    handler = FirebaseHandler()
    print(f"Firebase conectado: {handler.connected}")
