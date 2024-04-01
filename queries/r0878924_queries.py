
photo_query = "SELECT id,name,path,description,upload_date FROM scoopheaven.photos;"


insert_contact_query = "INSERT INTO scoopheaven.contact (contact_id, first_name_sender, last_name_sender, email_sender, message, created_at) VALUES (%s, %s, %s, %s, %s, %s);"

