# Show Duration in Leave Allocation

Odoo 17 module that displays the allocated **duration** directly in the Leave Allocation view, so managers and employees can see total days/hours per leave type at a glance — no manual calculation needed. The duration auto-recalculates whenever an allocation changes.

It also adds a `get_leave_balance` method on `hr.employee` to fetch the leave balance for a specific date (useful in payroll salary rules).

## Private Time Off calendar

By default in Odoo 17 the "Everyone's Time Off" calendar (the `hr.leave.report.calendar`
model) ships with only a multi-company rule, so every employee can see everyone's time
off on the calendar. This module adds record rules that make the calendar respect the
**existing Time Off role dropdown** (Settings → Users → *Time Off* access level):

| Role (existing dropdown)      | Sees on the calendar  |
|-------------------------------|-----------------------|
| Member / User (`base.group_user`) | Their own time off only |
| Team Approver (`group_hr_holidays_responsible`) | Their own + their team |
| Officer (`group_hr_holidays_user`) | Everyone |
| Administrator (`group_hr_holidays_manager`) | Everyone |

This mirrors the per-employee privacy Odoo already enforces on the leave history and
allocation list views, and introduces **no new security groups** — you switch a member's
visibility simply by changing their Time Off role in the standard dropdown.

> To restrict *Officers* too (so that **only** Administrators see everyone), change the
> domain of `hr_leave_report_calendar_rule_officer` in
> `security/hr_leave_calendar_security.xml`.

## Details

- **Technical name:** `oi_hr_holidays_allocation_date`
- **Version:** 17.0.0.0.2
- **Depends on:** `hr_holidays`
- **Author:** Openinside
- **License:** OPL-1

## Install

Copy the module into your Odoo addons path, update the apps list, and install **Show Duration in Leave Allocation**.

## Links

- Odoo Apps: https://apps.odoo.com/apps/modules/17.0/oi_hr_holidays_allocation_date
