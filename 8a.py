class Television(object):
        """A virtual television simulation"""

        def __init__(self):
                print("The television is off.")

        def power_button(self, power="off"):
                if power == "off":
                        power = "on"
                        print("The power is now on.")
                else:
                        power = "off"
                        print("The power is now off.")

        def volume_button(self, volume=0):
                up_or_down = input(
                    "Do you want to increase or decrease the volume? (up/down): ")
                if up_or_down == "up":
                        amount = int(input("By how much? (Enter a number): "))
                        volume += amount
                        if volume > 10:
                                volume = 10
                        print("The volume is now", volume)
                elif up_or_down == "down":
                        amount = int(input("By how much? (Enter a number): "))
                        volume += amount
                        if volume < 0:
                                volume = 0
                        print("The volume is now", volume)
                else:
                        print("That is not a valid choice.")

        def channel_button(self, channel=1):
                new_channel = int(
                    input("What channel do you want to watch? (Enter a number between 1 and 10.): "))
                if new_channel < 1 or new_channel > 10:
                        print("That is not a valid channel!")
                else:
                        channel = new_channel
                        print("The channel is now", channel)

#create the main part of the program, the television simulation


def main():
        tv = Television()

        choice = None
        while choice != "0":
                print("""
                Television simulation
	
                0 - Quit
                1 - Turn the television on or off
                2 - Change the volume
                3 - Change the channel
                """)

                choice = input("Choice: ")
                print(choice)

                #exit
                if choice == "0":
                        print("Good-bye.")

                #turn the television on or off
                elif choice == "1":
                        tv.power_button()

                #increase or decrease the volume
                elif choice == "2":
                        tv.volume_button()

                #change the channel
                elif choice == "3":
                        tv.channel_button()

                else:
                        print("\nInvalid choice!")


main()
("\n\nPress the enter key to exit.")
