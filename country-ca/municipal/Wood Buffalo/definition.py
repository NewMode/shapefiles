from datetime import date

import boundaries

boundaries.register('Wood Buffalo wards',
    domain='Wood Buffalo, AB',
    last_updated=date(2018, 12, 4),
    name_func=boundaries.attr('NAME'),
    id_func=lambda f: f.get('DISTRICTID').replace('0', ''),
    authority='Regional Municipality of Wood Buffalo',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4816037'},
)
