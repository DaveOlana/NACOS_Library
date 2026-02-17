# NACOS Library

A Django-based digital library management system designed for the National Association of Computer Science Students (NACOS), enabling students to share and access academic materials across different departments, levels, and semesters.

## Overview

NACOS Library provides a centralized platform for computer science students to upload, browse, and download course materials. The system features a moderated approval workflow to ensure quality control and includes comprehensive user profiles linked to academic hierarchies.

## Features

### Academic Structure Management
- Multi-tiered organization by **School**, **Department**, **Level**, and **Semester**
- Support for ND (National Diploma) and HND (Higher National Diploma) programs
- Dynamic academic state tracking to manage current level and semester

### Material Management
- Upload course materials as image-based pages
- Categorization by department, level, and semester
- Three-tier approval workflow: **Pending**, **Approved**, **Rejected**
- Detailed audit logging for all material-related actions

### User System
- Student profiles linked to academic information (school, department, level)
- Admin role assignment for moderators
- Automatic profile creation upon user registration
- Secure password validation with complexity requirements

### Moderation & Auditing
- Material approval and rejection system with reason tracking
- Comprehensive action logs for accountability
- Moderator-controlled content verification

## Tech Stack

- **Framework**: Django 6.0.2
- **Database**: SQLite (development)
- **Python**: 3.x
- **Authentication**: Django built-in authentication system

## Project Structure

```
NACOS_Library/
├── core/               # Project configuration
├── library/            # Main app for materials and academic structure
│   ├── models.py       # Database models
│   ├── signals.py      # Auto-profile creation
│   └── management/     # Custom management commands
├── accounts/           # User authentication and profiles
├── templates/          # HTML templates
└── manage.py           # Django management script
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd NACOS_Library
   ```

2. **Install dependencies**
   ```bash
   pip install django pillow
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Seed initial data** (levels and semesters)
   ```bash
   python manage.py seed_levels_and_semesters
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Application: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Database Models

### Academic Structure
- `School` - Educational institution
- `Department` - Academic departments within schools
- `Level` - Academic levels (ND1, ND2, HND1, HND2, etc.)
- `Semester` - Semester periods (1st, 2nd)
- `AcademicState` - Current system-wide academic session

### User Management
- `StudentProfile` - Extended user profile with academic information

### Materials
- `Material` - Learning materials with metadata and approval status
- `MaterialPage` - Individual pages of materials (stored as images)

### Moderation
- `Approval` - Records of approved materials
- `Rejection` - Records of rejected materials with reasons
- `ActionLog` - Audit trail of user actions

## Usage

### For Students
1. Register and complete your profile with school, department, and level information
2. Browse materials filtered by your academic criteria
3. Upload materials for your courses (subject to admin approval)

### For Administrators
1. Review pending material submissions
2. Approve or reject materials with feedback
3. Monitor action logs for system activity
4. Manage academic structure (schools, departments, levels, semesters)

## Security

- Password validation enforces:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character
- CSRF protection enabled
- XFrame security middleware active

## Contributing

Contributions are welcome! Please ensure your code follows Django best practices and includes appropriate documentation.

## License

This project is intended for educational purposes within NACOS communities.

## Contact

For questions or support, please reach out to the NACOS IT committee.

---

**Built with Django for the NACOS community**
