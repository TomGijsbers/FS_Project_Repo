# contact_name_query = "SELECT contact_id FROM scoopheaven.contact;"
photo_query = "SELECT id,name,path,description,upload_date FROM scoopheaven.photos;"


insert_contact_query = "INSERT INTO scoopheaven.contact (first_name_sender, last_name_sender, email_sender, message) VALUES (%s, %s, %s, %s);"

faq_query = "SELECT c.contact_id, c.message AS question, a.answer FROM scoopheaven.contact c JOIN scoopheaven.answers a ON c.contact_id = a.contact_id;"