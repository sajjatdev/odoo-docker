# Part of Qplexity. See LICENSE file for full copyright and licensing details.
{
    'name': 'Taiwan - Accounting',
    'website': 'https://www.Qplexity.com/documentation/master/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['tw'],
    'author': 'Qplexity PS',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the base module to manage the accounting chart for Taiwan in Qplexity.
==============================================================================
    """,
    'depends': [
        'account',
        'base_address_extended',
    ],
    'auto_install': ['account'],
    'data': [
        'data/res.country.state.csv',
        'data/res_currency_data.xml',
        'data/res_country_data.xml',
        'data/res.city.csv',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
