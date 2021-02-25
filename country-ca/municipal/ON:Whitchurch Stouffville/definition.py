from datetime import date

import boundaries

boundaries.register('Whitchurch-Stouffville wards',
    domain='Whitchurch-Stouffville, ON',
    last_updated=date(2017, 1, 4),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUM'),
    id_func=boundaries.attr('WARDNUM'),
    authority='Town of Whitchurch-Stouffville',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3519044'},
)
