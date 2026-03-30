# PawPal+ Project Reflection

## 1. System Design
Actions:
Add/remove tasks
Register pets
View and order tasks(Schedule building)

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The classes I chose were Owner, Pet, Schedule, and Task. My UML was as follows: An owner owns a pet, creates a schedule and creates a task. The pet has a schedule and is assigned a task. A schedule contains a task. The owner could register a pet, create a task and a schedule. Pets could be assigned tasks,schedules, and can generate summaries. Schedules can add and remove tasks, as well as generate a plan based on priority. A task is lowest on the UML diagram, being able to be edited and marked complete.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, it did change. Originally, both the schedule and the pet had tasks as attributes. The issue was that they were both pointing to the same tasks in two different methods, which would cause issues with updating one another. Because of this, we changed the task list from pet to a derived property from the schedule tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers priority as a constraint. Tasks are given priority, and based on that are ordered. This mattered the most because an owner would like to priortize different things, like walking before cleaning, or eating before walking, so this just made those priorities clearer, which is why I picked this as my contraint

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff I made was that when generating a plan, the scheduler sorts purely based on priority, ignoring time. However, I found this tradeoff reasonable because inherintely, priority comes with an ordered timing, and some things may need to happen no matter of the time. Priority makes more sense to order than duration. Also, detect conflicts only relies on if the HH:MM matches. For example, you could have one thing at 08:00 and another at 08:10. Even if the activities overlap, you are able to put them both because the times are different. This is reasonable for now because it is for simplicity, but overlaps can happen.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI heavily for brainstorming and implementation. For the classes, attributes and methods, I had AI draft an idea, which from there I tweaked and refined. This was the same for each part. The prompt that was most helpful was "Do not focus on code, we are just ideating." This made claude less code oriented, and more feature and idea oriented.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One example is when I asked it to look at the renew function, and see if I could simplify it. However, it told me to swap the if else statements with a dictionary lookup. While this was technically a more efficient and pythonic way of doing things, I figured it was harder to follow what it was doing. Thus, I kept the if else statements in order to make it human readable.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I ran tests that cover ensuring completed actually gets marked, tasks are added to the list, out-of-order tasks become sorted, conflict detection is ensured, making sure an empty schedule does not crash, a task on pet a blocks pet b at the same time, a completed task still blocks a new task at the same time, and with two pets and mixed completion only the completed pets task is returned.

I decided that these tesrs are the most important because these are the core features that users will be using and working with. If these things break, the users experience is ruined, and there are risks of crashing.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that the scheduler will work correctly, roughly a 4/5. The core happy path is mostly covered, and they should run under normal scenarios. Also multi-pet scenarios are all functional, which handles some edge cases. Only reason i am not confident is because overdue tasks aren't really handled, and could cause issues in the system, but it wasn't an issue I experienced at the moment, so I didn't need to test it there.

Some edge cases I would test if I had more time would be editing a task, testing for overdue tasks, and testing the generate plan function, ensuring its accurate in terms of priority.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am  most satisfied with the task implementation. I think all of my attributes are properly implemented, the completion feature seems to be working well, and I am especially proud of the way I implemented the sorting and filtering methods. It looks professional, and the implementation is very clean. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the generate schedule feature better. Since it was an optional feature that I added, but I didnt implement it fully. Next iteration, I believe this is a feature that I would want to work on more

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

While AI is good at designing algorithms, it needs to have a strong plan with examples implemented before applying it. If its not given this blueprint, it will implement this algorithm wrong. By using the UML and describing each feature I wanted implemented fully, the AI was able to make these algorithms more effectively, and not generate thousands of lines of code.