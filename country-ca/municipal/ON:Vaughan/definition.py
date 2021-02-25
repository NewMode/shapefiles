import re
from datetime import date

import boundaries

boundaries.register('Vaughan wards',
    domain='Vaughan, ON',
    last_updated=date(2012, 8, 13),
    name_func=boundaries.clean_attr('DESCRIP'),
    id_func=lambda f: re.sub(r'\D+', '', f.get('WARD_NO')),
    authority='City of Vaughan',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3519028'},
)
