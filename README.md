# AI Infrastructure-as-Code (IaC) Automation Agent

##  Overview

The **AI Infrastructure-as-Code (IaC) Automation Agent** is a CLI-based AI system that generates, validates, and secures Terraform infrastructure code using an LLM-powered agent combined with DevOps tooling.

It bridges the gap between **natural language infrastructure requests** and **real-world cloud infrastructure deployment workflows**, integrating automation, validation, and security scanning in a single pipeline.

---
##  Tools Used

- Python
- LangChain
- Groq API (LLaMA 3 model)
- Terraform CLI
- Checkov (IaC security scanning)
- Subprocess automation
---
##  How It Works

1. User enters an infrastructure request in natural language
2. The AI agent interprets the request and generates Terraform code
3. Code is written to local `.tf` files
4. Terraform commands are executed (validate / plan)
5. Checkov scans infrastructure for security misconfigurations
6. Results are returned to the user

---

##  Example Usage

```bash
You: Create a secure AWS S3 bucket with versioning enabled
```

## Agent workflow:

Generates Terraform configuration
Writes main.tf
Runs terraform validate
Runs Checkov security scan
Returns results and fixes if needed
