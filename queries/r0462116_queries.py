
events_query = "select event_name, date, description, num_participants, max_participants from scoopheaven.events where date > curdate() order by date limit 5"

reservations_query = "select first_name, last_name, email_address, date_tm, amount_of_people, remarks from scoopheaven.reservations where email_address = %s"