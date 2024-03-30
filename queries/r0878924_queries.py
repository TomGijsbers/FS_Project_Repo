# contact_name_query = "SELECT contact_id FROM scoopheaven.contact;"
photo_query = "SELECT id,name,path,description,upload_date FROM scoopheaven.photos;"
# insert_photo_query = "INSERT INTO scoopheaven.photos (name, path, description, upload_date) VALUES (%s, %s, %s, %s);"

insert_contact_query = "INSERT INTO scoopheaven.contact (contact_id, first_name_sender, last_name_sender, email_sender, message, created_at) VALUES (%s, %s, %s, %s, %s, %s);"

