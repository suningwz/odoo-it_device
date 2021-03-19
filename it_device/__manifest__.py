# -*- coding: utf-8 -*-

{
    'name': 'IT Devices',
    'version': '1.1',
    'author': 'Daniel Demedziuk',
    'sequence': 110,
    'summary': 'IT Devices, Manage IT Devices and specifications',
    'license': 'OPL-1',
    'price':   9,
    'currency':   'EUR',
    'description': """
IT Device Management
==================================
This module supports the management and storage of IT equipment in the company.
From now on, control over moved devices and their specifications is much easier. You get the possibility of gathering computers, phones and other IT devices in one place. Each group of devices has its own specification and technical data. Moreover, in the employee card a new page "Equipment" appears, where you can see the equipment owned by the employee. This module should only be operated by employees assigned to this task. Unauthorized people should not be able to access it.

If you need help, please contact the author of the module.

e-mail: daniel.demedziuk@gmail.com

Main features
-------------
* Add computers.
* Add phones
* Add other devices
* Managing and storing IT device specifications
* Manage equipment transfers
* Generate protocols
* Device overview
* Database of models, processors, mobile networks, device types

""",
    'category': 'Tool',
    'depends': [
        'base',
        'mail',
        'board',
        'hr',
    ],
    'data': [
        'views/it_device_view.xml',
        'views/it_device_brands.xml',
        'views/hr_employee_inherited_view.xml',
        'security/it_device_security.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/it_dev.jpg'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
