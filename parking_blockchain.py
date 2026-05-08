import hashlib
import datetime
import time

class Block:

    def __init__(self, index, vehicle_no, vehicle_type,
                 slot, hours, amount, entry_time,
                 exit_time, previous_hash):

        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
        self.slot = slot
        self.hours = hours
        self.amount = amount
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def generate_hash(self):

        block_data = (
            str(self.index)
            + self.timestamp
            + self.vehicle_no
            + self.vehicle_type
            + self.slot
            + str(self.hours)
            + str(self.amount)
            + self.entry_time
            + self.exit_time
            + self.previous_hash
        )

        return hashlib.sha256(block_data.encode()).hexdigest()


class ParkingBlockchain:

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):

        return Block(
            0,
            "SYSTEM",
            "SYSTEM",
            "START",
            0,
            0,
            "START",
            "START",
            "0"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def calculate_amount(self, vehicle_type, hours):

        if vehicle_type.lower() == "bike":
            return hours * 20

        elif vehicle_type.lower() == "car":
            return hours * 50

        elif vehicle_type.lower() == "bus":
            return hours * 100

        else:
            return hours * 30

    def add_parking_record(self):

        vehicle_no = input("Enter Vehicle Number : ")
        vehicle_type = input("Enter Vehicle Type (Bike/Car/Bus) : ")
        slot = input("Enter Parking Slot : ")
        hours = int(input("Enter Parking Hours : "))

        amount = self.calculate_amount(vehicle_type, hours)

        entry_time = str(datetime.datetime.now())

        time.sleep(1)

        exit_time = str(datetime.datetime.now())

        latest_block = self.get_latest_block()

        new_block = Block(
            len(self.chain),
            vehicle_no,
            vehicle_type,
            slot,
            hours,
            amount,
            entry_time,
            exit_time,
            latest_block.hash
        )

        self.chain.append(new_block)

        print("\nParking Record Added Successfully")
        print("Parking Amount : Rs.", amount)

    def display_records(self):

        print("\n=========== PARKING BLOCKCHAIN RECORDS ===========\n")

        for block in self.chain:

            print("Block Index      :", block.index)
            print("Timestamp        :", block.timestamp)
            print("Vehicle Number   :", block.vehicle_no)
            print("Vehicle Type     :", block.vehicle_type)
            print("Parking Slot     :", block.slot)
            print("Parking Hours    :", block.hours)
            print("Parking Amount   : Rs.", block.amount)
            print("Entry Time       :", block.entry_time)
            print("Exit Time        :", block.exit_time)
            print("Previous Hash    :", block.previous_hash)
            print("Current Hash     :", block.hash)

            print("-" * 70)

    def validate_blockchain(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.generate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def search_vehicle(self):

        search_no = input("Enter Vehicle Number to Search : ")

        found = False

        for block in self.chain:

            if block.vehicle_no == search_no:

                print("\nVehicle Record Found\n")

                print("Vehicle Number :", block.vehicle_no)
                print("Vehicle Type   :", block.vehicle_type)
                print("Parking Slot   :", block.slot)
                print("Parking Hours  :", block.hours)
                print("Parking Amount : Rs.", block.amount)

                found = True

        if not found:
            print("\nVehicle Record Not Found")


# Admin Login
username = input("Enter Admin Username : ")
password = input("Enter Admin Password : ")

if username == "admin" and password == "1234":

    print("\nLogin Successful")

    parking_system = ParkingBlockchain()

    while True:

        print("\n========= SMART PARKING MENU =========")
        print("1. Add Parking Record")
        print("2. Display Blockchain Records")
        print("3. Validate Blockchain")
        print("4. Search Vehicle Record")
        print("5. Exit")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            parking_system.add_parking_record()

        elif choice == "2":
            parking_system.display_records()

        elif choice == "3":

            print("\n========== BLOCKCHAIN VALIDATION ==========\n")

            if parking_system.validate_blockchain():
                print("Blockchain is VALID and SECURE")

            else:
                print("Blockchain has been TAMPERED")

        elif choice == "4":
            parking_system.search_vehicle()

        elif choice == "5":

            print("\nExiting Smart Parking Blockchain System")
            break

        else:
            print("\nInvalid Choice")

else:
    print("\nInvalid Username or Password")