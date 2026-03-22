import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseHandler:
    def __init__(self, service_account_key):
        self.service_account_key = service_account_key
        self.app = None
        self.db = None

    def initialize_app(self):
        if not self.app:
            cred = credentials.Certificate(self.service_account_key)
            self.app = firebase_admin.initialize_app(cred)
            self.db = firestore.client()

    def add_document(self, collection, document_id, data):
        self.initialize_app()  # Ensure app is initialized
        doc_ref = self.db.collection(collection).document(document_id)
        doc_ref.set(data)

    def get_document(self, collection, document_id):
        self.initialize_app()  # Ensure app is initialized
        doc_ref = self.db.collection(collection).document(document_id)
        return doc_ref.get().to_dict()

    def update_document(self, collection, document_id, data):
        self.initialize_app()  # Ensure app is initialized
        doc_ref = self.db.collection(collection).document(document_id)
        doc_ref.update(data)

    def delete_document(self, collection, document_id):
        self.initialize_app()  # Ensure app is initialized
        doc_ref = self.db.collection(collection).document(document_id)
        doc_ref.delete()