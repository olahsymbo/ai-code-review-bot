# AI Code Review Bot 🤖

AI Code Review Bot automates code analysis, detects potential issues, enforces best practices, and optimizes performance in your repository.  

## 📌 Features  
- Automated code reviews using AI  
- Detection of common coding issues  
- Performance optimization suggestions  
- Enforces best practices and coding standards  
- Runs automatically on new commits and pull requests  

## 📂 Repository Structure  
```
├── .github/workflows/
│   ├── ai-code-reviewer.yaml  # GitHub Actions workflow for automated code review
├── test_example.py             # Example test file
├── README.md                   
```

## Setup & Usage  

### 1️⃣ Enable GitHub Actions  
Ensure GitHub Actions is enabled in your repository to allow the workflow to run.  

### 2️⃣ Configure Required Secrets  
Before running the bot, you need to set the following **GitHub repository secrets**:  

1. **`TOKENGITHUB`** – Your GitHub personal access token (PAT) with repository access.  
2. **`OPENAI_API_KEY`** – Your OpenAI API key for AI-powered code review.  

#### Steps to Add Secrets:  
1. Go to your GitHub repository.  
2. Navigate to **Settings** > **Secrets and variables** > **Actions**.  
3. Click **New repository secret** and add:  
   - `TOKENGITHUB` with your GitHub PAT.  
   - `OPENAI_API_KEY` with your OpenAI API key.  

### 3️⃣ Run Code Review  
- Push a new commit or create a pull request.  
- The bot will automatically review the code and leave comments on detected issues.  
