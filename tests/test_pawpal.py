from pawpal_system import Task, Pet


def test_mark_complete_sets_completed_true():
    task = Task(name="Walk", time="07:00", priority=3, description="Morning walk")
    task.mark_complete()
    assert task.completed is True


def test_assign_task_increases_pet_task_count():
    pet = Pet(name="Buddy", species="Dog", breed="Labrador", age=3)
    task = Task(name="Feeding", time="08:00", priority=1, description="Dry food")
    pet.assign_task(task)
    assert len(pet.tasks) == 1
