## 🕒 0:00 - 0:10 | The Kickoff & The Joke

* **Goal:** Hook them, explain the scenario, and introduce Git conceptually.
* **Action:** Have the repository pulled up on a screen or projector.

**You:** "Alright everyone, welcome to the club! Today, we are taking over as the lead engineering team for the Intergalactic Zoo. Unfortunately, our previous lead developer abruptly quit to go become a moisture farmer on Tatooine. They left our brand-new *Cosmic Critter Care System* in a very buggy, half-finished state. The zoo opens soon, the Venusian Slimes are getting cranky, and we have to fix the code.

To do this together without deleting each other's work, we are going to use a tool called Git, and a platform called GitHub. Has anyone here ever used Git before?

*(Wait for answers/groans)*

At its core, Git is just a way to save versions of our code and share them without overriding each other. The two main things you do in Git are **Pull** code down from the internet, and **Push** your changes back up.

Which reminds me of a cartoon I saw once. A developer is standing outside a building, yanking on a door handle. The sign on the door in giant letters says 'PUSH'. The developer says, 'Whenever I see a door that says PUSH, I always pull first, just to be safe.'

That is exactly what we are doing today. Before you push your code, always pull to make sure you have the latest updates! Today, we are going to use GitHub Desktop—also known as the Purple Kitty—to grab tasks, fix bugs, and create 'Pull Requests.' Let's get our environment set up."

---

## 🕒 0:10 - 0:25 | Orientation & Setup

* **Goal:** Get everyone logged in, cloned, and understanding the rules.
* **Action:** Have them navigate to the repo URL and accept your collaboration invites.

**You:** "First, everyone go to the GitHub link I shared and accept the invite to collaborate. Once you're in, open GitHub Desktop and clone the repository to your machine.

Now, I need to warn you. I have installed a security system on this repository called a 'Branch Ruleset.' If you try to push your code directly to the `main` branch, the system will block you. You *must* create your own branch, push it, and open a Pull Request. Furthermore, you can't merge your own code. You have to get one of your teammates here to review it and click 'Approve'. We are doing real peer reviews today."

---

## 🕒 0:25 - 0:45 | Phase 1: The Happy Path

* **Goal:** Everyone successfully completes one simple issue end-to-end without stepping on each other's toes.
* **Action:** Assign Tickets 1 through 4. Walk around and help them through the Purple Kitty UI.

**You:** "Go to the **Issues** tab on GitHub. I want everyone to claim one of the first four tickets. Leave a comment saying 'I got this one!' so we don't duplicate work.

Notice that Ticket 1 is in `utils.py`, Ticket 2 is in `critter.py`, and so on. In the real world, we break code into multiple files specifically so multiple engineers can work at the same time without overwriting each other's work. As long as you only edit the file your ticket tells you to, your code will merge perfectly with everyone else's.

Here is your workflow:

1. In GitHub Desktop, make sure you are on `main` and click  **Fetch/Pull** .
2. Click **New Branch** and name it something like `fix-typo`.
3. Open the code, fix the bug in your specific file, and save it. Test it by running `python main.py` in your terminal!
4. Go back to GitHub Desktop, write a summary at the bottom left, and hit  **Commit** .
5. Hit  **Publish Branch** , then click that magic **Create Pull Request** button."

*(Once PRs start rolling in)*
**You:** "Awesome, PRs are up! Now, turn to the person next to you. Go to the PR tab, look at their code, make sure they only changed the file they were supposed to, and if it won't break the zoo, hit 'Approve' and let them merge it!"

## 🕒 0:45 - 0:65 | Phase 2: The Merge Conflict Zone

* **Goal:** Intentionally trigger a merge conflict and resolve it as a group.
* **Action:** Tell everyone to pull the newly updated `main` branch. Ask for two volunteers to take Tickets 5 and 6.

**You:** "Great job! Everyone, go to GitHub Desktop, switch back to your `main` branch, and click **Pull** so you have everyone's new code.

Now, I need two brave volunteers for a special mission. I want you to claim Tickets 5 and 6. They both require changing the exact same menu loop in `main.py`. I want you both to create a branch, do the work, and make a PR."

*(Wait for them to make their PRs. Have the first one merge. The second one will get the big red CONFLICT warning).*

**You:** "Stop! Look at the screen. We have a  **Merge Conflict** . This isn't an error; it just means Git is confused because two people changed the exact same lines of code, and it doesn't want to guess who is right. Let's fix it together."

* **Action:** Project the second student's screen (or yours). Show how GitHub Desktop highlights the conflicting files. Open the file in VS Code, show the `<<<<<<< HEAD` markers, explain what they mean, delete the markers, keep both changes, save, and commit the resolution.

---

## 🕒 0:65 - 0:80 | Phase 3: Cross-File & Free Play

* **Goal:** Let them tackle the complex, multi-file bugs and the new game features.
* **Action:** Turn them loose on the remaining issues.

**You:** "Now that we know how to handle conflicts, it's a free-for-all. Look at the remaining issues. Some of them require editing multiple files at once. Some of them are totally new features like adding sound effects or an economy system. Claim what looks fun, remember to pull `main` before you branch, and ask for reviews when you're done!"

*(Walk around, help debug Python logic, and encourage them to review each other's code).*

---

## 🕒 0:80 - 0:90 | Bonus: The `gh` CLI Demo (Time Permitting)

* **Goal:** Show the terminal-curious kids that the CLI is basically magic.
* **Action:** Project your terminal.

**You:** "Before we wrap up, you've all been using the Purple Kitty today, which is fantastic. But for those of you who like feeling like a hacker in the matrix, I want to show you how I managed this whole project without ever opening a web browser.

I use a tool called the GitHub CLI, or `gh` for short. Watch this."

*(Run these commands one by one, explaining them as you go)*

1. **"Let's see what issues are left open:"**
   `gh issue list`
   *"See? It prints out exactly what's left on our to-do list right here in the terminal."*
2. **"Let's check if there are any PRs waiting for my approval:"**
   `gh pr list`
   *"It shows me who is waiting for a review."*
3. **"What if I want to review your code right here? I can checkout your PR branch instantly:"**
   `gh pr checkout <PR-NUMBER>`
   *"Now I have your code on my machine, and I can run it to see if your new sound effects actually work."*
4. **"And if I want to instantly jump to the repo in my browser to change a setting?"**
   `gh repo view --web`
   *"Boom. Opens right up."*

**You:** "The UI is great for learning, but once you get comfortable, the command line is like a superpower. Great job today, team. The Intergalactic Zoo is officially saved from the cranky Venusian Slimes. Keep poking at those bonus issues if you want to keep practicing. See you next week!"
