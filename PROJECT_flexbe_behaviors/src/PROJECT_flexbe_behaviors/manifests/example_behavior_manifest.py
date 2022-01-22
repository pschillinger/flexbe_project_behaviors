example_behavior = {
	'name': 'Example Behavior',
	'executable': {
		'package_path': 'PROJECT_flexbe_behaviors.example_behavior_sm',
		'class': 'ExampleBehaviorSM'
	},

	'author': 'Philipp Schillinger',
	'date': 'Fri Aug 21 2015',
	'tagstring': 'demo',
	'description': """
		This is a simple example for a behavior.
	""",

	# Contained behaviors
	'contained_behaviors': [
	],

	# Available parameters
	'params': [
		{
			'type': 'numeric',
			'name': 'waiting_time',
			'default': '3',
			'label': 'Waiting Time',
			'hint': 'Sets the time to wait after logging.',
			'additional': {
				'min': '1',
				'max': '5',
			},
		},
	],
}
