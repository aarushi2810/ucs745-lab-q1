# Reflection – Git Merge Conflict (UCS 745 Lab, Q1)

## What Happened?

When I started this project I created a simple Python file called `calc.py` with a function `calculate(a, b)` that returned `a + b`. I committed this to the `main` branch.

Then I created two feature branches from `main`:

- **`feature-multiply`** – I changed the return line to `a * b` (multiplication).
- **`feature-subtract`** – From the same `main` base, I changed the same return line to `a - b` (subtraction).

Both branches touched exactly the same line in the same file. When I merged `feature-multiply` into `main` first, it went smoothly because main had no competing change. But when I then tried to merge `feature-subtract`, Git could not decide automatically which version of that line to keep. It marked the conflict in the file with markers like `<<<<<<< HEAD`, `=======`, and `>>>>>>> feature-subtract`, and stopped the merge so I could decide.

## Why Did the Conflict Happen?

A **merge conflict** happens in Git when two branches independently change the same part of the same file and Git cannot auto-merge them. Git does a line-by-line diff. Here, three-way merge detected:

- **Ancestor (base):** `return a + b`
- **HEAD (main after first merge):** `return a * b`
- **Incoming (feature-subtract):** `return a - b`

Because both sides changed the same line differently, Git had no safe way to pick one, so it asked me to resolve it manually.

## How I Resolved It

Instead of simply picking one branch's version and discarding the other, I decided that both operations (multiply and subtract) are valid and useful. I rewrote `calculate` to accept an extra parameter `op` (operator):

```python
def calculate(a, b, op="*"):
    if op == "+":   return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b
    elif op == "/": return a / b
```

This approach:
1. **Preserves both features** that the two branches introduced.
2. **Improves the function** by making it more general.
3. **Avoids data loss** – neither developer's work is thrown away.

After editing, I ran `git add calc.py` to mark the conflict as resolved, then `git commit` to complete the merge.

## Alternative Ways to Resolve a Conflict

There are cases where a full manual edit is not needed:

| Command | What it does |
|---|---|
| `git merge --abort` | Cancels the merge entirely and goes back to the state before you ran `git merge`. Use this if you realise you are not ready to resolve yet. |
| `git checkout --ours calc.py` | Keeps **our** version of the file (the branch you are merging into, here `main` with multiply). |
| `git checkout --theirs calc.py` | Keeps **their** version (the branch being merged in, here feature-subtract). |
| `git restore --merge calc.py` | Restores the conflicted state (undoes any manual edits you started, in case you want to start over without aborting the whole merge). |

After using `--ours` or `--theirs` you still need `git add <file>` and `git commit` to finish the merge.

## What I Learned About Distributed Version Control

Working through this exercise taught me several key ideas:

1. **Branches are cheap and safe.** Creating a branch costs almost nothing in Git, and it protects `main` from being broken by experimental work.

2. **Merge conflicts are normal.** They are not errors; they are Git's way of asking for a human decision when it cannot figure out what to do automatically. Teams that communicate well (and split work so the same lines are rarely touched simultaneously) have fewer conflicts, but they will never be zero in a real project.

3. **The distributed model enables parallel work.** Because every developer has a full copy of the repository, two developers could work on `feature-multiply` and `feature-subtract` simultaneously, offline if needed, and merge later. No single server is a bottleneck.

4. **A good resolution is better than a quick one.** Instead of just picking one branch, I looked at what both developers were trying to achieve and found a solution (`op` parameter) that satisfied both. This is the right attitude in a team setting.

5. **Git log tells the full story.** Running `git log --oneline --graph --all` shows the branch structure visually, so anyone joining the project later can understand what happened, why the merge was needed, and how it was resolved.

6. **Push discipline matters.** Each branch should be pushed to the remote before merging, so teammates can review or pull-request the changes before they hit main. This is the foundation of workflows like GitHub Flow.

Overall, this exercise gave me hands-on experience with one of the most important and sometimes intimidating parts of collaborative software development, and I now feel confident handling merge conflicts in a real team project.

