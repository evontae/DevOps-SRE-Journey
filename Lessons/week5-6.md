### Lesson Plan: Advanced Python Scripting for Automation

#### Weeks 5-6: Enhancing Python Skills for DevOps

### Objective:

Develop advanced Python scripting capabilities to automate and optimize DevOps tasks, integrating Python with key tools like Ansible and Docker.

### Reading Assignments:

-   "Automate the Boring Stuff with Python" by Al Sweigart:
    -   Chapters 13-15: Focus on working with Excel spreadsheets, PDFs, and automating emails, which are practical for various automation tasks in DevOps.

### Video Tutorials:

-   Python Virtual Environments Tutorial by Corey Schafer:
    -   [Watch Here](https://www.youtube.com/watch?v=N5vscPTWKOk) - Learn how to set up and manage isolated Python environments, crucial for project-specific dependencies.
-   Python Exception Handling Tutorial by Corey Schafer:
    -   [Watch Here](https://www.youtube.com/watch?v=NIWwJbo-9_8) - Detailed explanation on handling errors in Python, an essential skill for writing robust automation scripts.

### "Things to Try" - Practical Coding Snippets:

1.  Python Virtual Environments:

    -   Description: Learn how to set up and manage isolated Python environments to manage project-specific dependencies without affecting global Python packages.
    -   Snippet:

        bash

        Copy code

        `# On Windows
        python -m venv myenv
        myenv\Scripts\activate

        # On Unix or MacOS
        python3 -m venv myenv
        source myenv/bin/activate`

    -   Task: Install a package (`requests`) within this environment and print its version to confirm installation.
2.  Error Handling in Python:

    -   Description: Practice implementing error handling in file operations to prevent script crashes and manage exceptions gracefully.
    -   Snippet:

        python

        Copy code

        `try:
            with open('example.txt', 'r') as file:
                read_data = file.read()
        except FileNotFoundError:
            print("The file was not found")
        except Exception as e:
            print(f"An error occurred: {e}")`

    -   Task: Modify this snippet to attempt to open a non-existent file and handle the specific error.
3.  Automating Emails with Python:

    -   Description: Develop a script to automate sending emails, useful for notifications in DevOps workflows.
    -   Snippet:

        python

        Copy code

        `import smtplib
        from email.mime.text import MIMEText

        msg = MIMEText('This is a test email from Python.')
        msg['Subject'] = 'Python Email Test'
        msg['From'] = 'your_email@example.com'
        msg['To'] = 'recipient_email@example.com'

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()`

    -   Task: Send an email to yourself to test the functionality. Modify the message body and subject as needed.

### Exercises:

-   Automate Excel Report Generation: Script to read CSV data, perform summary statistics, and write to an Excel file.
-   PDF Processing: Combine multiple PDF files into one or extract specific pages.
-   Email Automation: Script to send automated emails based on system status reports.

### Mini Project: Dynamic Environment Setup Tool

-   Create a comprehensive script that automates the setup of development environments, handling tasks such as dependency installation, environment configuration, and version control operations.

### Resources for Learning:

-   Python Official Documentation: [Python Docs](https://docs.python.org/3/)
-   Additional GitHub repositories and code examples demonstrating Python in automation.

### Submission Guidelines:

-   Code: All scripts should be uploaded to your GitHub repository in the `Python/Advanced` directory.
-   Documentation: Include detailed README files for each script and the project, explaining the purpose, how to set up, and run the scripts.