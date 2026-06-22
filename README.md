# Show Duration in Leave Allocation

Odoo 17 module that displays the allocated **duration** directly in the Leave Allocation view, so managers and employees can see total days/hours per leave type at a glance — no manual calculation needed. The duration auto-recalculates whenever an allocation changes.

It also adds a `get_leave_balance` method on `hr.employee` to fetch the leave balance for a specific date (useful in payroll salary rules).

## Details

- **Technical name:** `oi_hr_holidays_allocation_date`
- **Version:** 17.0.0.0.1
- **Depends on:** `hr_holidays`
- **Author:** Openinside
- **License:** OPL-1

## Install

Copy the module into your Odoo addons path, update the apps list, and install **Show Duration in Leave Allocation**.

## Links

- Odoo Apps: https://apps.odoo.com/apps/modules/17.0/oi_hr_holidays_allocation_date
