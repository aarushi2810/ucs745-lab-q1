# Steps – Q1 Git Conflict Lab (UCS 745)

Exact commands used in order, with explanations.

---

## 1. Create project folder and files

```bash
mkdir -p ucs745-lab/q1-git-conflict
cd ucs745-lab/q1-git-conflict
# Created calc.py and README.md manually / via agent
```

## 2. Initialise Git repository

```bash
git init
git config user.email "student@ucs745.lab"
git config user.name "UCS745 Student"
git checkout -b main
```

## 3. Initial commit

```bash
git add .
git commit -m "Initial commit: add calc.py and README.md"
```

## 4. Connect GitHub remote and push main

```bash
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
git push -u origin main
```
> Replace the URL with your actual repository URL.

## 5. Create feature-multiply branch

```bash
git checkout -b feature-multiply
# Edit calc.py: change `return a + b` → `return a * b`
git add calc.py
git commit -m "feature-multiply: change calculate to return a * b"
git push -u origin feature-multiply
```

## 6. Create feature-subtract branch (from main)

```bash
git checkout main
git checkout -b feature-subtract
# Edit calc.py: change `return a + b` → `return a - b`
git add calc.py
git commit -m "feature-subtract: change calculate to return a - b"
git push -u origin feature-subtract
```

## 7. Merge feature-multiply into main (clean merge)

```bash
git checkout main
git merge feature-multiply -m "Merge feature-multiply into main (clean merge)"
git push origin main
```

## 8. Merge feature-subtract into main (conflict!)

```bash
git merge feature-subtract
# CONFLICT (content): Merge conflict in calc.py
# Automatic merge failed; fix conflicts and then commit the result.
```

## 9. Capture conflict state

```bash
git status        > conflict-log.txt
git diff         >> conflict-log.txt
cat calc.py      >> conflict-log.txt
# (all three captured into conflict-log.txt)
```

## 10. Alternative resolution approaches (do NOT run all at once)

```bash
# Option A – Abort the merge entirely
git merge --abort

# Option B – Keep our version (main's multiply)
git checkout --ours calc.py
git add calc.py
git commit -m "Resolved: kept ours (multiply)"

# Option C – Keep their version (feature-subtract)
git checkout --theirs calc.py
git add calc.py
git commit -m "Resolved: kept theirs (subtract)"

# Option D – Undo partial manual edits without aborting
git restore --merge calc.py
```

## 11. Manual resolution (what was actually done)

```bash
# Edited calc.py to support op parameter (keeping both behaviours)
git add calc.py conflict-log.txt
git commit -m "Resolve merge conflict: keep both behaviours via op parameter"
git push origin main
```

## 12. Capture resolution state

```bash
git status                        > resolution-log.txt
git log --oneline --graph --all  >> resolution-log.txt
```

## 13. Add and commit all documentation files

```bash
git add resolution-log.txt reflection.md steps.md
git commit -m "docs: add conflict logs, reflection, and steps"
git push origin main
```
