from pawpal_system import Owner, Pet, Scheduler

# --- Setup ---
owner = Owner(name="Alex", email="alex@email.com")
owner.scheduler = Scheduler(owner=owner)

# --- Pets ---
buddy = Pet(name="Buddy", species="Dog", breed="Labrador", age=3)
whiskers = Pet(name="Whiskers", species="Cat", breed="Siamese", age=5)

owner.register_pet(buddy)
owner.register_pet(whiskers)

# --- Tasks for Buddy ---
buddy.assign_task(owner.create_task("Morning Walk",     time="07:00", priority=3, description="Walk around the block",  frequency="daily"))
buddy.assign_task(owner.create_task("Feeding",          time="08:00", priority=1, description="Dry food, 1 cup",          frequency="daily"))
buddy.assign_task(owner.create_task("Grooming",         time="10:00", priority=5, description="Brush coat",               frequency="weekly"))

# --- Tasks for Whiskers ---
whiskers.assign_task(owner.create_task("Feeding",       time="08:00", priority=1, description="Wet food, half can",       frequency="daily"))
whiskers.assign_task(owner.create_task("Playtime",      time="15:00", priority=4, description="Feather toy session",      frequency="daily"))
whiskers.assign_task(owner.create_task("Litter Box",    time="18:00", priority=2, description="Clean and refill",         frequency="weekly"))

# --- Today's Schedule ---
plan = owner.scheduler.generate_plan()

print("=" * 40)
print("        TODAY'S SCHEDULE")
print("=" * 40)

for i, task in enumerate(plan, start=1):
    status = "Done" if task.completed else "Pending"
    print(f"{i}. [{task.priority}] {task.name:<15} {task.time}  |  {task.frequency:<8}  |  {status}")
    print(f"   {task.description}")
    print()

print("=" * 40)
print(f"Total tasks: {len(plan)}")
print("=" * 40)
