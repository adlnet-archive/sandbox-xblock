"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources, json

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment
from webob.response import Response


class SandBlock(XBlock):
	"""
	TO-DO: document what your XBlock does.
	"""

	# Fields are defined on the class.  You can access them in your code as
	# self.<fieldname>.

	url = String(
		default = 'http://ec2-54-173-64-18.compute-1.amazonaws.com:3000/adl/sandbox/Fr7zUN4vwmK3ToGB/',
		scope = Scope.settings,
		help = 'The URL to the virtual world you want to embed'
	)

	has_score = True

	def resource_string(self, path):
		"""Handy helper for getting resources from our kit."""
		data = pkg_resources.resource_string(__name__, path)
		return data.decode("utf8")

	# TO-DO: change this view to display your data your own way.
	def student_view(self, context=None):
		"""
		The primary view of the SandBlock, shown to students
		when viewing courses.
		"""
		html = self.resource_string("static/html/sandblock.html")
		frag = Fragment(html.format(self=self))
		frag.add_css(self.resource_string("static/css/sandblock.css"))
		frag.add_javascript(self.resource_string("static/js/src/sandblock.js"))
		frag.add_javascript(self.resource_string("static/js/jschannel.js"))
		frag.initialize_js('SandBlock')
		return frag

	@XBlock.json_handler
	def receive_grade(self, data, suffix=''):

		#module = StudentModule.objects.get(pk=request.params['module_id'])
		#state = json.loads(module.state)
		#state['score']

		self.runtime.publish('grade', {
			'value': 1 if data['grade'] else 0,
			'max_value': 1
		})

		return {'success': True}


	@staticmethod
	def workbench_scenarios():
		"""A canned scenario for display in the workbench."""
		return [
			("SandBlock",
			 """<vertical_demo>
				<sandblock/>
				</vertical_demo>
			 """),
		]
