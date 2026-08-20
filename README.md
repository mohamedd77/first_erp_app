# Leave Request Management System

A custom Frappe/ERPNext application that manages employee leave requests with a complete approval workflow, built to demonstrate core Frappe Framework development skills.

## Features

- **Leave Request DocType** with linked Employee and Leave Type
- **Server-side Validation**: prevents invalid date ranges and past-dated requests
- **Client-side Logic**: real-time calculation of total leave days as dates are entered
- **Approval Workflow**: Draft → Pending Approval → Approved/Rejected, controlled via Whitelisted Methods
- **REST API Endpoint**: `get_approved_leaves` returns approved leave data as JSON, filterable by employee
- **Query Report**: "Leave Summary" aggregates total approved days per employee using SQL

## Tech Stack

- Frappe Framework (Python)
- MariaDB
- JavaScript (Client Scripts)

## Key Learnings Demonstrated

- DocType architecture (Parent & Child tables)
- Server Scripts vs Client Scripts
- Whitelisted Methods for client-server communication
- REST API design in Frappe
- Query Reports with SQL aggregation
- Git version control workflow

## Installation

```bash
bench get-app https://github.com/mohamedd77/first_erp_app
bench --site your-site install-app my_custom_app
```

## API Usage Example
GET /api/method/my_custom_app.api.get_approved_leaves?employee=HR-EMP-00001

Returns:
```json
{
  "message": [
    {
      "name": "...",
      "employee": "HR-EMP-00001",
      "leave_type": "Annual Leave",
      "from_date": "2026-08-18",
      "to_date": "2026-08-25",
      "total_days": 8
    }
  ]
}
```