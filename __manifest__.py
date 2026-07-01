# -*- coding: utf-8 -*-
{
'name': 'Show Duration in Leave Allocation',
'summary': 'Show Duration in Leave Allocation, Leave, Timeoff, Allocation, HR, Human '
           'Resources, Management, Payroll, Rules, Salary Rules, Payslip, Openinside, '
           'Odoo',
'version': '17.0.0.0.3',
'category': 'Human Resources',
'website': 'https://www.open-inside.com',
'description': '''
'''
               '''		* Show Duration in Leave Allocation
'''
               '		* get_leave_balance method in hr.employee to get balance for specific '
               '''date to use it in payroll rules
'''
               '''		* Private Time Off calendar: normal users can only see their own time '''
               '''off and cannot see each other's calendars. Visibility is controlled by a '''
               '''dedicated access-rights selector "Time Off Calendar Visibility '''
               '''(holiday_allocation_date_app)" on the user's Access Rights tab, with three '''
               '''tiers: Own Time Off Only (default), Own + Team, and Everyone's Time Off.
'''
               '    ',
'images': ['static/description/cover.png'],
'author': 'Openinside, Mohamed Amine Bentaieb',
'maintainer': 'Mohamed Amine Bentaieb',
'contributors': ['Mohamed Amine Bentaieb <https://github.com/medaminebt/>'],
'license': 'OPL-1',
'price': 0.0,
'currency': 'USD',
'installable': True,
'depends': ['hr_holidays'],
'data': [
    'security/hr_leave_calendar_groups.xml',
    'security/hr_leave_calendar_security.xml',
    'view/hr_leave_allocation.xml',
],
'odoo-apps': True,
'application': False
}