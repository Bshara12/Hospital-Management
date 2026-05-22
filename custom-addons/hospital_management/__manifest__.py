{
    "name": "Hospital Management",
    "version": "1.0",
    "summary": "Hospital Management System",
    "author": "Your Name",
    "category": "Management",
    # "depends": ["base"],
        "depends": [
        "base",
        "hr",
        "stock",
        "purchase",
        "maintenance",
        "account",
        "project",
    ],
    "data": [
        "security/security.xml",
                "security/project_security.xml",

        "security/ir.model.access.csv",
        "views/patient_views.xml",
        "views/doctor_views.xml",
        "views/appointment_views.xml",
        "views/medical_supply_views.xml",
        "views/appointment_supply_view.xml",
                "views/project_menus.xml",

    ],
    "installable": True,
    "application": True,
}
