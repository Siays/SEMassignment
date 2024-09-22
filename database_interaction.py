
from firebase_admin import storage,firestore
import fb_admin_sdk

# Access the Firebase Admin SDK (using get_firebase_app)
app = fb_admin_sdk.get_firebase_app()
bucket = storage.bucket(app=app)

# Initialize Firestore
db = firestore.client()

def upload_file_to_firebase(item_file_path, db_file_path):
    #item_file_path : item to be sotred
    #db_file_path: store to specified location of db
    #ex:
    # location of the db
    # blob = bucket.blob("db/images/nav_bar_logo.png")
    # local file path
    # blob.upload_from_filename("images/nav_bar_logo.png")

    # Get the bucket
    bucket = storage.bucket()

    # Upload a file to Firebase Storage
    blob = bucket.blob(db_file_path)
    if blob.exists():
        # print(f"Error: File '{db_file_path}' already exists in Firebase Storage.")
        print(f"File '{db_file_path}' that exists in Firebase Storage will be delete.")
        delete_file_from_firebase(db_file_path)
        # return

    try:
        blob.upload_from_filename(item_file_path)
        print("File successfully uploaded")

    except Exception as e:
        print(f"Error uploading file: {e}")


def retrieve_file_from_firebase(db_file_path):
    # Get the bucket
    bucket = storage.bucket()

    # Get the blob
    blob = bucket.blob(db_file_path)

    try:
        # Download the file as a byte string
        data = blob.download_as_string()
        return data
    except Exception as e:
        print(f"Error retrieving the file: {e}")


def rename_file_in_firebase(old_db_file_path, new_db_file_path):
    # Get the bucket
    bucket = storage.bucket()

    # Check if the old file exists
    old_blob = bucket.blob(old_db_file_path)
    if not old_blob.exists():
        print(f"Error: File '{old_db_file_path}' does not exist in Firebase Storage.")
        return

    # Check if the new file already exists
    new_blob = bucket.blob(new_db_file_path)
    if new_blob.exists():
        print(f"Error: File '{new_db_file_path}' already exists in Firebase Storage.")
        return

    # Rename the file
    try:
        old_blob.rename(new_db_file_path)
    except Exception as e:
        print(f"Error renaming file: {e}")


def delete_file_from_firebase(db_file_path):
    # Get the bucket
    bucket = storage.bucket()

    # Get the blob
    blob = bucket.blob(db_file_path)

    # Check if the file exists
    if not blob.exists():
        print(f"Error: File '{db_file_path}' does not exist in Firebase Storage.")
        return

    # Delete the file
    try:
        blob.delete()
    except Exception as e:
        print(f"Error deleting file: {e}")


# Fetching all documents from a Firestore collection
def fetch_all_data_from_collection(collection_name):
    try:
        collection_ref = db.collection(collection_name)
        docs = collection_ref.stream()

        return docs

    except Exception as e:
        print(f"Error fetching data: {e}")

# Fetching a single document by ID from a collection
def fetch_single_document(collection_name, document_id):
    try:
        doc_ref = db.collection(collection_name).document(document_id)
        doc = doc_ref.get()

        return doc

    except Exception as e:
        print(f"Error fetching data: {e}")

# Fetch all batches from Firestore
def fetch_batches_from_firestore():
    try:
        batches_ref = db.collection('batches')
        docs = batches_ref.stream()
        return [doc.get('batch_name') for doc in docs]
    except Exception as e:
        print(f"Error fetching batches: {e}")
        return None

# Fetch all courses from Firestore
def fetch_courses_from_firestore():
    try:
        courses_ref = db.collection('courses')
        docs = courses_ref.stream()
        return [doc.get('course_name') for doc in docs]
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return None

# Insert a record into Firestore (for both batches and courses)
def insert_record_into_firestore(collection_name, data):
    try:
        db.collection(collection_name).add(data)
        print(f"Record added to {collection_name} collection.")
    except Exception as e:
        print(f"Error adding record to {collection_name}: {e}")

# Delete a record from Firestore (for both batches and courses)
def delete_record_from_firestore(collection_name, name):
    try:
        docs = db.collection(collection_name).where('batch_name' if collection_name == 'batches' else 'course_name', '==', name).stream()
        for doc in docs:
            db.collection(collection_name).document(doc.id).delete()
            print(f"Record '{name}' deleted from {collection_name} collection.")
    except Exception as e:
        print(f"Error deleting record from {collection_name}: {e}")