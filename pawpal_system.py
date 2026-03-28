from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    name: str
    time: str
    priority: int
    description: str
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def edit(self, name: str, time: str, priority: int, description: str, frequency: str) -> None:
        # Overwrites the task's attributes with the provided values.
        self.name = name
        self.time = time
        self.priority = priority
        self.description = description
        self.frequency = frequency

    def mark_complete(self) -> None:
        # Sets the task as completed.
        self.completed = True

    def renew(self) -> "Task":
        # Returns a new Task instance due at the next occurrence (daily: +1 day, weekly: +7 days).
        if self.frequency == "daily":
            next_due = self.due_date + timedelta(days=1)
        elif self.frequency == "weekly":
            next_due = self.due_date + timedelta(days=7)
        else:
            next_due = self.due_date
        return Task(
            name=self.name,
            time=self.time,
            priority=self.priority,
            description=self.description,
            frequency=self.frequency,
            due_date=next_due,
        )

    @property
    def due_in(self) -> str:
        # Returns a human-readable string of how many days until the task is due.
        days = (self.due_date - date.today()).days
        if days == 0:
            return "Due today"
        elif days == 1:
            return "Due tomorrow"
        else:
            return f"Due in {days} days"


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def assign_task(self, task: Task) -> None:
        # Adds a task to the pet's task list.
        self.tasks.append(task)

    def get_summary(self) -> str:
        # Returns a formatted string of the pet's details and assigned task names.
        task_names = ", ".join(t.name for t in self.tasks) if self.tasks else "None"
        return f"{self.name} ({self.species}, {self.breed}, age {self.age}) | Tasks: {task_names}"


@dataclass
class Scheduler:
    owner: "Owner"

    def get_all_tasks(self) -> list[Task]:
        # Collects and returns all tasks from every pet owned by the owner.
        return [task for pet in self.owner.pets for task in pet.tasks]

    def generate_plan(self) -> list[Task]:
        # Returns all tasks sorted by priority, lowest number first (1 = highest priority).
        return sorted(self.get_all_tasks(), key=lambda t: t.priority)
    def filter_tasks(self, pet_name: str | None = None, completed: bool | None = None) -> list[Task]:
        # Returns tasks filtered by pet name and/or completion status. None means no filter applied.
        return [
            task
            for pet in self.owner.pets
            for task in pet.tasks
            if (pet_name is None or pet.name == pet_name)
            and (completed is None or task.completed == completed)
        ]

    def sort_by_time(self) -> list[Task]:
        # Returns all tasks sorted by their time attribute in HH:MM format, earliest first.
        return sorted(self.get_all_tasks(), key=lambda t: t.time)


@dataclass
class Owner:
    name: str
    email: str
    pets: list[Pet] = field(default_factory=list)
    scheduler: Scheduler = None

    def register_pet(self, pet: Pet) -> None:
        # Adds a pet to the owner's pet list.
        self.pets.append(pet)

    def create_task(self, name: str, time: str, priority: int, description: str, frequency: str = "daily") -> Task:
        # Instantiates and returns a new Task with the given attributes.
        return Task(name=name, time=time, priority=priority, description=description, frequency=frequency)
