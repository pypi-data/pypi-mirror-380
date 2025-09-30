# XAMPP Fixer

**XAMPP Fixer** is a small Python CLI tool that automatically resolves common XAMPP issues on Windows. It is designed to save you time by detecting and fixing problems with Apache, MySQL, and other XAMPP services without manual configuration.

---

## Features

- **Fix Apache Port Conflicts**  
  Automatically detects port conflicts (e.g., port 80 or 443 already in use) and updates Apache configuration files to use available ports.

- **Resolve MySQL Service Issues**  
  Fixes common MySQL startup problems such as locked data directories or missing configuration entries.

- **Other XAMPP Service Fixes**  
  - Resolves PHP configuration conflicts  
  - Backup before any file deletion
  - Fixes common permission issues  

- **Easy to Use CLI**  
  Run the tool from the command line with a single command:

  ```bash
  xfix
