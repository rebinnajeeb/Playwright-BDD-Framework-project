# Git + Azure DevOps Pipeline Guide (Beginner Reference)

> My personal reference for: setting up an Azure DevOps pipeline for this Playwright + Behave project,
> and the full Git workflow (change code → branch → PR → merge). Follow one step at a time.

---

## ⚠️ 3 gotchas to remember first

1. The parallelism form **needs your org name** → create the Azure account FIRST, then request it.
2. You **cannot approve your OWN pull request** (GitHub disables it) → when solo, just merge it directly.
3. PR checks only appear if you connected via the **GitHub App** (not OAuth) → otherwise nothing shows.

---

# PART A — Setting up the Azure pipeline

**Big picture:** A pipeline is a robot computer in Microsoft's cloud that fetches your code from GitHub
and runs your commands (like `behave`). You are NOT moving your code — it stays in GitHub, Azure just reads it.

## Step 1 — Create your Azure account
1. Go to **dev.azure.com** → click **Start free**
2. Sign in with a **personal Microsoft account** (outlook/hotmail — NOT the Cognizant email)
3. Confirm country/language → **Continue**
4. It creates your **organization** → keep or rename (e.g. `rebin-devops`)
5. 📝 Write down your org name — it's in the URL `dev.azure.com/your-org-name`

## Step 2 — Request free parallelism grant (do now)
New orgs get ZERO permission to run pipelines (error: "No hosted parallelism has been purchased or granted").
Free but takes 2–3 days to approve.
1. Open **https://aka.ms/azpipelines-parallelism-request**
2. Sign in (same Microsoft account)
3. Fill: name, email, **org name** (from Step 1)
4. If asked Public/Private → **Private**
5. **Submit** → wait 2-3 days (build everything else meanwhile)

> Faster path (optional): link the org to a free Azure subscription (billing setup, costs nothing for free tier)
> — often unlocks parallelism instantly, no waiting.

## Step 3 — Create a Project
1. **+ New project** (top-right)
2. Name: `Playwright-BDD-Pipeline`
3. Visibility: **Private** → **Create**

## Step 4 — Connect your GitHub repo
1. Left sidebar → **Pipelines** → **Create Pipeline**
2. "Where is your code?" → **GitHub**
3. Sign in to GitHub → if asked, **Authorize Azure Pipelines**
4. On "Install Azure Pipelines":
   - Choose account `rebinnajeeb`
   - Pick **"Only select repositories"** → select `Playwright-BDD-Framework-project`
   - Click green **Approve & Install**
5. Back in Azure → **Select a repository** → click your repo

> Repo not showing? Go to github.com/settings/installations → Azure Pipelines → ensure repo is listed.

## Step 5 — Paste your yml & run
1. "Configure your pipeline" → **Starter pipeline**
2. In editor: **Ctrl+A** then **Delete** (empty it)
3. Paste:

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.11'
    displayName: 'Use Python 3.11'

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: |
      playwright install --with-deps
    displayName: 'Install Playwright browsers'

  - script: |
      behave -f allure_behave.formatter:AllureFormatter -o allure-results
    displayName: 'Run Behave tests'
    continueOnError: true

  - task: PublishPipelineArtifact@1
    inputs:
      targetPath: 'allure-results'
      artifact: 'allure-results'
    displayName: 'Publish Allure results'
    condition: always()
```

4. **Save and run** → leave file path at default (`/azure-pipelines.yml`)
5. Keep "Commit directly to the main branch" → **Save and run** again

> Notes:
> - Needs a `requirements.txt` in the repo (behave, playwright, allure-behave). Don't have one?
>   Run `pip freeze > requirements.txt` locally, commit + push first.
> - Lots of `apt` text during browser install is NORMAL (`--with-deps` installs OS libraries).

## Step 6 — Watch it run
1. Click the **Job** (spinning = running)
2. Watch steps stream live
3. Icons: ✅ passed, ❌ failed, ⚠️ ran but reported a problem

> "No hosted parallelism" error = grant not arrived yet (Step 2). Wait a day, click **Run pipeline** again.

## Step 7 — Read results
- **Summary tab** → overall + artifacts
- **Tests tab** → likely "no results" (we publish Allure artifacts, not JUnit — fine for now)
- **Artifacts** → download `allure-results` zip → unzip → `allure serve allure-results` locally

## ⚠️ Honest truth: AEG tests fail on cloud
Tests open `t1-aeg-uat-a.eluxmkt.com` = inside Cognizant network behind Zscaler.
A public cloud machine can't reach it → fails at "open website" with timeout.
**This is EXPECTED, not your mistake.** You still proved the pipeline works.
Real-world fix = a **self-hosted agent** inside the corporate network (next lesson + interview story).

---

# PART B — The full Git cycle (change → branch → PR → merge)

**Mental model:** `main` = clean shared copy everyone trusts. Never edit directly.
Make a branch (safe copy), work there, then a PR asks "please merge my copy into main."

## Step 1 — Sync main first (ALWAYS)
```powershell
git checkout main
git pull
```

## Step 2 — Make your branch
```powershell
git checkout -b feature/search-page
```
Naming: `feature/` (new), `fix/` (bug), `chore/` (cleanup). Lowercase, hyphens, no spaces.

## Step 3 — Edit code, then save
```powershell
git add .
git commit -m "Add SearchPage page object for product search"
```
> Always use `-m "..."`. Forgot it and Vim opened? Press `Esc`, type `:wq`, press `Enter`.

## Step 4 — Upload your branch
```powershell
git push origin feature/search-page
```
First push on a new branch may need:
```powershell
git push --set-upstream origin feature/search-page
```

## Step 5 — Open the PR
- **Easy:** after pushing, click the yellow banner **"Compare & pull request"**
- **Manual:** Pull requests tab → **New pull request** → base = `main`, compare = `feature/search-page`
  → title + description → **Create pull request**
- Memory trick: **base = destination, compare = my work**

## Step 6 — What happens on the PR
1. **Automatic checks (pipeline runs):**
   - Only shows if connected via **GitHub App** (not OAuth)
   - Only runs once **parallelism granted** — else check sits stuck/queued (not red)
   - Then yellow → running → ✅/❌ (AEG test goes red at website step — expected)
2. **Human review:**
   - Teammate clicks **Approve**
   - You CANNOT approve your OWN PR → solo? Just **merge directly**

## Step 7 — Merge
1. Green **Merge pull request**
2. **Confirm merge**
3. Grey **Delete branch** (appears after merge)

## Step 8 — Clean up your laptop
```powershell
git checkout main
git pull
git branch -d feature/search-page
```
> If `-d` refuses after a GitHub squash-merge, use `-D` (safe in that case).

## Bonus — merge conflict
```powershell
git checkout feature/search-page
git pull origin main
```
Git marks clash with `<<<<<<<` `=======` `>>>>>>>`. Keep the right code, delete markers, then:
```powershell
git add .
git commit -m "Resolve merge conflict"
git push
```

---

## 📌 Pocket cheat-sheet
```powershell
git checkout main; git pull                    # 1. sync
git checkout -b feature/search-page            # 2. branch
# ...edit code...
git add .; git commit -m "Add SearchPage"      # 3. save
git push origin feature/search-page            # 4. upload
# ...open PR -> checks + review -> merge -> delete branch...
git checkout main; git pull                    # 5. re-sync
git branch -d feature/search-page              # 6. clean up
```
