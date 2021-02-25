import re
from datetime import date

import boundaries

boundaries.register('Richmond Hill wards',
    domain='Richmond Hill, ON',
    last_updated=date(2012, 11, 22),
    name_func=boundaries.clean_attr('WARD'),
    id_func=lambda f: re.sub(r'\D+', '', f.get('WARD')),
    authority='Town of Richmond Hill',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3519038'},
)
