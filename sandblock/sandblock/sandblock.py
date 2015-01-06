"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources, json, os, mimetypes

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment
from webob.response import Response


class SandBlock(XBlock):
	"""
	TO-DO: document what your XBlock does.
	"""

	has_score = True
	icon_class = 'problem'
	weight = 1

	# Fields are defined on the class.  You can access them in your code as
	# self.<fieldname>.
	display_name = String(
		default = 'Virtual World Sandbox',
		scope = Scope.settings,
		help = 'The name of this component'
	)

	url = String(
		default = 'http://ec2-54-173-64-18.compute-1.amazonaws.com:3000/adl/sandbox/Fr7zUN4vwmK3ToGB/',
		scope = Scope.settings,
		help = 'The URL to the virtual world you want to embed'
	)

	score = Integer(
		default = -1,
		scope = Scope.user_state,
		help = 'The graded score of this component'
	)

	maxscore = Integer(
		default = 1,
		scope = Scope.settings,
		help = 'The maximum score for this component'
	)


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
		frag.add_javascript(self.resource_string("static/js/sandblock.js"))
		frag.add_javascript(self.resource_string("static/js/jschannel.js"))
		frag.initialize_js('SandBlock')
		return frag

	@XBlock.handler
	def query_grade(self, request, suffix=''):

		#print request
		#print self.max_score()
		if request.method == 'POST':

			try:
				data = json.loads(request.body)
			except e:
				return Response(status=500, body='Could not parse request body as JSON')

			self.score = 1 if data['grade'] else 0
			self.maxscore = 1

			self.runtime.publish(self, 'grade', {
				'value': self.score,
				'max_value': self.maxscore
			})

		return Response(json_body={'value': repr(self.score), 'max_value': repr(self.maxscore)})

	@XBlock.handler
	def static(self, request, suffix=''):
		filename = os.path.join( os.path.dirname(__file__), 'static', suffix )
		mime = mimetypes.guess_type(filename)[0]
		content = None
		try:
			content = open(filename,'rb').read()

		except Exception as e:
			print e
			return Response(status=404)
		else:
			res = Response(content_type=mime)
			if mime.startswith('text'):
				res.body = content.format(self=self)
			else:
				res.body = content
			return res

	def get_score(self):

		return {
			'score': self.score,
			'total': self.maxscore
		}

	def max_score(self):
		return self.maxscore

	def get_progress(self):
		return None

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
