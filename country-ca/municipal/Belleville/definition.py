from datetime import date

import boundaries

boundaries.register('Belleville wards',
    domain='Belleville, ON',
    last_updated=date(2018, 3, 28),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Belleville',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3512005'},
    notes='Load the shapefile manually:\nfab alpheus update_boundaries:args="--merge union -d data/shapefiles/private/boundaries/ocd-division/country:ca/csd:3512005"',
)
