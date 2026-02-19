# EVA Suit Life Support Simulator — Stack (emergencies) + Queue (events) + OOP
from suit import Suit

def print_header():
    print()
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║      EVA SUIT LIFE SUPPORT SIMULATOR         ║")
    print("  ║         Stack  •  Queue  •  OOP                  ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print("  Mission: Airlock A  ──►  Solar Panel B  (8 steps)")
    print()
    print("  Rules:")
    print("  • Each step has an ambient EVENT (queue, FIFO)")
    print("  • Emergencies stack up and resolve LIFO")
    print("  • Energy ≤ 0  →  mission failed")
    print()

def ask_action(step: int, total: int) -> str:
    print(f"  ┌─ Step {step}/{total} ─────────────────────────────────┐")
    print("  │  What do you do?                                 │")
    print("  │   [1] Advance   [2] Stay calm                   │")
    print("  └──────────────────────────────────────────────────┘")
    while True:
        choice = input("  > ").strip()
        if choice in ("1", "2"):
            return choice
        print("  Please enter 1 or 2.")

def print_step(suit: Suit, step: int):
    print()
    print(f"  ── Result: Step {step}/{suit.TOTAL_STEPS} " + "─" * 28)
    print(suit.vitals())
    print()
    for msg in suit.get_messages():
        print(msg)
    print()
    print(f"  Stack (top→bottom) : {suit.stack_display()}")
    print(f"  Queue remaining    : {suit.queue_remaining()} event(s)")
    print()

def main():
    print_header()
    input("  Press ENTER to start the mission...")
    print()

    suit = Suit()

    while True:
        action = ask_action(suit.step_count + 1, suit.TOTAL_STEPS)
        suit.take_step(action)
        print_step(suit, suit.step_count)

        if suit.is_dead():
            print("  ╔══════════════════════════════════════════════════╗")
            print("  ║  ✖  MISSION FAILED — Astronaut did not survive   ║")
            print("  ╚══════════════════════════════════════════════════╝")
            break

        if suit.is_done():
            if suit.stack_display() == "empty":
                print("  ╔══════════════════════════════════════════════════╗")
                print("  ║  MISSION COMPLETE — All systems nominal       ║")
                print("  ╚══════════════════════════════════════════════════╝")
            else:
                print("  ╔══════════════════════════════════════════════════╗")
                print("  ║  ARRIVED — Unresolved emergencies remain      ║")
                print("  ╚══════════════════════════════════════════════════╝")
            break

        input("  Press ENTER to continue...\n")

if __name__ == "__main__":
    main()
