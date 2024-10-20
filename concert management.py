import mysql.connector
# from mysql.connector import (connection)

# Establishing the connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Medhansh",
  database="ConcertManagement"
)
cursor = db.cursor()


def create_table():
    # Creating the Concerts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Concerts (
            concert_id INT AUTO_INCREMENT PRIMARY KEY,
            artist_name VARCHAR(255),
            venue VARCHAR(255),
            date DATE,
            time TIME,
            ticket_price DECIMAL(10,2),
            total_tickets INT,
            genre VARCHAR(255),
            description TEXT,
            ticket_sales_status VARCHAR(255),
            organizer VARCHAR(255)
        )
    """)


def add_concert():
    # Adding a new concert to the database
    artist_name = input("Enter artist/band name: ")
    venue = input("Enter venue name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter start time (HH:MM:SS): ")
    ticket_price = float(input("Enter ticket price: "))
    total_tickets = int(input("Enter total number of tickets: "))
    genre = input("Enter musical genre: ")
    description = input("Enter a brief description: ")
    ticket_sales_status = input("Enter ticket sales status: ")
    organizer = input("Enter concert organizer/promoter name: ")

    insert_query = """
        INSERT INTO Concerts (artist_name, venue, date, time, ticket_price, total_tickets,
        genre, description, ticket_sales_status, organizer)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    insert_values = (artist_name, venue, date, time, ticket_price, total_tickets,
                     genre, description, ticket_sales_status, organizer)
    cursor.execute(insert_query, insert_values)
    db.commit()
    print("Concert added successfully!")


def update_concert():
    # Updating an existing concert in the database
    concert_id = int(input("Enter concert ID to update: "))

    # Check if concert exists
    cursor.execute("SELECT * FROM Concerts WHERE concert_id = {}".format(concert_id))
    concert = cursor.fetchone()
    if concert is None:
        print("Concert not found!")
        return

    # Get the updated concert details
    artist_name = input("Enter updated artist/band name: ")
    venue = input("Enter updated venue name: ")
    date = input("Enter updated date (YYYY-MM-DD): ")
    time = input("Enter updated start time (HH:MM:SS): ")
    ticket_price = float(input("Enter updated ticket price: "))
    total_tickets = int(input("Enter updated total number of tickets: "))
    genre = input("Enter updated musical genre: ")
    description = input("Enter updated brief description: ")
    ticket_sales_status = input("Enter updated ticket sales status: ")
    organizer = input("Enter updated concert organizer/promoter name: ")

    update_query = """
        UPDATE Concerts SET artist_name = %s, venue = %s, date = %s, time = %s,
        ticket_price = %s, total_tickets = %s, genre = %s, description = %s,
        ticket_sales_status = %s, organizer = %s WHERE concert_id = %s
    """
    update_values = (artist_name, venue, date, time, ticket_price, total_tickets,
                     genre, description, ticket_sales_status, organizer, concert_id)
    cursor.execute(update_query, update_values)
    db.commit()
    print("Concert updated successfully!")


def search_concert():
    # Searching for a concert by artist name
    artist_name = input("Enter artist/band name to search: ")

    search_query = "SELECT * FROM Concerts WHERE artist_name LIKE '%{}%'".format(artist_name)
    cursor.execute(search_query)
    concerts = cursor.fetchall()

    if len(concerts) == 0:
        print("No concerts found!")
        return

    print("\nSearch results:")
    for concert in concerts:
        print("Concert ID:", concert[0])
        print("Artist/Band Name:", concert[1])
        print("Venue:", concert[2])
        print("Date:", concert[3])
        print("Time:", concert[4])
        print("Ticket Price:", concert[5])
        print("Total Tickets:", concert[6])
        print("Genre:", concert[7])
        print("Description:", concert[8])
        print("Ticket Sales Status:", concert[9])
        print("Organizer:", concert[10])
        print("\n")


def display_concerts():
    # Displaying all concerts in the database
    display_query = "SELECT * FROM Concerts"
    cursor.execute(display_query)
    concerts = cursor.fetchall()

    if len(concerts) == 0:
        print("No concerts found!")
        return

    print("Concerts List:")
    for concert in concerts:
        print("Concert ID:", concert[0])
        print("Artist/Band Name:", concert[1])
        print("Venue:", concert[2])
        print("Date:", concert[3])
        print("Time:", concert[4])
        print("Ticket Price:", concert[5])
        print("Total Tickets:", concert[6])
        print("Genre:", concert[7])
        print("Description:", concert[8])
        print("Ticket Sales Status:", concert[9])
        print("Organizer:", concert[10])
        print("\n")


def delete_concert():
    # Deleting a concert from the database
    concert_id = int(input("Enter concert ID to delete: "))

    delete_query = "DELETE FROM Concerts WHERE concert_id = {}".format(concert_id)
    cursor.execute(delete_query)
    db.commit()
    print("Concert deleted successfully!")


# Creating the ConcertManagement database and table
create_table()

# Menu-driven program
while True:
    print("----------- ConcertManagement ------------")
    print("1. Add Concert")
    print("2. Update Concert")
    print("3. Search Concert")
    print("4. Display All Concerts")
    print("5. Delete Concert")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add_concert()
    elif choice == 2:
        update_concert()
    elif choice == 3:
        search_concert()
    elif choice == 4:
        display_concerts()
    elif choice == 5:
        delete_concert()
    elif choice == 6:
        break
    else:
        print("Invalid choice!")

# Closing the database connection
db.close()
