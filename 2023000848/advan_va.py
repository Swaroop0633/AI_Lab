def is_goal(state):
    return state["A"] == "Clean" and state["B"] == "Clean"

def vacuum_world():
    state = {"A": "Dirty", "B": "Dirty"}
    location = "A"

    while not is_goal(state):
        print(f"Location: {location}, State: {state}")

        if state[location] == "Dirty":
            print("Action: Suck")
            state[location] = "Clean"
        elif location == "A":
            print("Action: Move Right")
            location = "B"
        else:
            print("Action: Move Left")
            location = "A"

    print(f"Final State: {state}")
    print("All rooms are clean. Goal achieved!")

vacuum_world()
