# Show Duration in Leave Allocation

Odoo 17 module that displays the allocated **duration** directly in the Leave Allocation view, so managers and employees can see total days/hours per leave type at a glance — no manual calculation needed. The duration auto-recalculates whenever an allocation changes.

It also adds a `get_leave_balance` method on `hr.employee` to fetch the leave balance for a specific date (useful in payroll salary rules).

## Private Time Off calendar

By default in Odoo 17 the "Everyone's Time Off" calendar (the `hr.leave.report.calendar`
model) ships with only a multi-company rule, so every employee can see everyone's time
off on the calendar. This module locks that down: **normal users can only see their own
time off** and can never see each other's calendars unless an admin explicitly raises
their access level.

### Dedicated access-rights selector

The module adds its own access-rights category so you can control calendar visibility
per user from **Settings → Users & Companies → Users → *(a user)* → Access Rights**. It
is labelled **`Time Off Calendar Visibility (holiday_allocation_date_app)`** — the
`holiday_allocation_date_app` tag on the category and every option makes it obvious the
selector comes from this module. Because the options form a hierarchy, they show as a
single **dropdown / select**:

| Selector value (dropdown)                        | Sees on the calendar    |
|--------------------------------------------------|-------------------------|
| `Own Time Off Only (holiday_allocation_date_app)`   *(default for all users)* | Their own time off only |
| `Own + Team Time Off (holiday_allocation_date_app)` | Their own + their team |
| `Everyone's Time Off (holiday_allocation_date_app)` | Everyone |

Every internal user is granted **Own Time Off Only** automatically, which is what keeps
normal users from seeing each other's calendars. Odoo's existing Time Off roles are
mapped onto the higher tiers out of the box (Team Approver → *Own + Team*, Officer /
Administrator → *Everyone*), so behaviour matches the standard access levels — but an
admin can override any single user straight from the dropdown.

The three groups and the category are defined in a separate file,
`security/hr_leave_calendar_groups.xml`; the record rules that enforce them live in
`security/hr_leave_calendar_security.xml`.

## Details

- **Technical name:** `oi_hr_holidays_allocation_date`
- **Version:** 17.0.0.0.3
- **Depends on:** `hr_holidays`
- **Author:** Openinside
- **Developer:** [Mohamed Amine Bentaieb](https://github.com/medaminebt/)
- **License:** OPL-1

## Install

Copy the module into your Odoo addons path, update the apps list, and install **Show Duration in Leave Allocation**.

## Links

- Odoo Apps: https://apps.odoo.com/apps/modules/17.0/oi_hr_holidays_allocation_date
