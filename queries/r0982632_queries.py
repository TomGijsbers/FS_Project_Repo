#Geert Vuurstaek

insert_applications_query = 'INSERT INTO scoopheaven.applicationform (firstName, lastName, birthdate, gender, emailaddress) VALUES (%s, %s, %s, %s, %s);'

scoopheaven_reviews = 'SELECT c.name, c.avatar, r.reviewText, r.rating, r.time FROM scoopheaven.reviews r JOIN customers c ON r.customersId = c.customersId;'

scoopheaven_personel = 'SELECT name, job, avatar, quote FROM scoopheaven.personnel WHERE job = %s'