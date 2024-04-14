
events_query = "select event_name, date, description, num_participants, max_participants, image_filepath from scoopheaven.events where date > curdate() order by date limit 5"

reservations_query = "select first_name, last_name, email_address, date_tm, amount_of_people, remarks from scoopheaven.reservations where email_address = %s"

insert_reservation = "INSERT INTO scoopheaven.reservations (first_name, last_name, email_address, date_tm, amount_of_people, remarks) VALUES (%s, %s, %s, %s, %s, %s)"