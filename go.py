import os
import sys

DIR=os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(DIR, 'deps'))

import djangogo

parser=djangogo.make_parser()
args=parser.parse_args()
djangogo.main(args,
	project='tag_proj',
	app='tag',
	database='tag_database',
	user='tag_user',
	heroku_url='https://boiling-caverns-77453.herokuapp.com/',
)
