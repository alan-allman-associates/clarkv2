# -*- coding: utf-8 -*-
{
    'name': 'AAA base',
    'installed_version': '12.0.1.1',
    'author': 'Auguria SAS',
    'licence': 'LGPL Version 3',
    'summary': 'Initialize projet',
    'sequence': 15,
    'description': """
Initialize project
    """,
    'category': 'Base',
    'website': 'https://www.auguria.fr',
    'images': [],
    'depends': [
                #'muk_utils',
                'crm',
                'website',
                'project',
                'account',
                'sale_management',
                'base_address_extended',
                'hr_timesheet',
                'note',
                'website_crm',
                'hr',
                'hr_recruitment',
                'hr_expense',
                'account_bank_statement_import',
                'account_facturx',
                'account_payment',
                'analytic',
                'auth_signup',
                'barcodes',
                'base',
                'base_iban',
                'base_import',
                'base_setup',
                'base_vat',
                'board',
                'bus',
                'calendar_sms',
                'contacts',
                'decimal_precision',
                'digest',
                'document',
                'fetchmail',
                'gamification_sale_crm',
                'hr_contract',
                'hr_gamification',
                'hr_holidays',
                'hr_org_chart',
                'hr_recruitment_survey',
                'iap',
                'l10n_fr',
                'l10n_fr_fec',
                'mail',
                'mail_bot',
                #'muk_autovacuum',
                #'muk_web_theme',
                #'muk_web_utils',
                'partner_autocomplete',
                'partner_autocomplete_address_extended',
                'payment',
                'payment_transfer',
                'product',
                'product_email_template',
                'product_margin',
                'project_timesheet_holidays',
                'rating',
                'resource',
                'sale',
                'sale_crm',
                'sale_expense',
                'sale_margin',
                'sale_quotation_builder',
                'sale_timesheet',
                'sales_team',
                'sms',
                'snailmail',
                'snailmail_account',
                'social_media',
                'survey_crm',
                'uom',
                'utm',
                'web',
                'web_diagram',
                'web_editor',
                'web_kanban_gauge',
                'web_settings_dashboard',
                'web_tour',
                'web_unsplash',
                'website_form',
                'website_form_project',
#                 'office365_mail',
#                 'office365_calendar_sync',
                'aaa_security',
        ],
    'data': ['security/ir.model.access.csv',
             'views/res_partner_view.xml',
             'views/res_users_view.xml',
             'views/res_company_view.xml',
             #'data/menu_icon.xml',
             'data/ir_cron.xml',
#              'views/res_config_settings_view.xml',
#              'data/ir_config_parameter.xml'
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
}