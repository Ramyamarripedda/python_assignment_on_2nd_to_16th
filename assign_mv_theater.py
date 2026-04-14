total_seats = 350
available = total_seats

bookings = 0
sold = 0
rejected = 0

while available > 0:
    print("\nAvailable seats:", available)
    n = int(input("Enter tickets (0 to exit): "))

    if n == 0:
        break

    if n < 1 or n > 15:
        print("Invalid booking")
        continue

    if n > available:
        print("Not enough seats")
        rejected += 1
        continue

    valid = True

    for i in range(n):
        age = int(input(f"Age {i+1}: "))
        if age < 12:
            valid = False
            # skip remaining inputs
            for _ in range(i+1, n):
                input("Age: ")
            break

    if not valid:
        print("BOOKING REJECTED - Age restriction")
        rejected += 1
        continue

    print(f"BOOKING CONFIRMED - {n} tickets")
    bookings += 1
    sold += n
    available -= n

print("\nFINAL REPORT")
print("Total Bookings:", bookings)
print("Tickets Sold:", sold)
print("Rejected:", rejected)
print("Remaining Seats:", available)