"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import json
import random
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String, List


class MyXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

   
    score = Integer(
        default = 0, cope=Scope.user_state,
        help="Score",
    )

    maxScore = Integer(
        default = 0, cope=Scope.user_state,
        help="Maximum Score",
    )

    question = String(
        default="question", scope=Scope.user_state,
        help="Question",
    )

    answer = String(
        default="answer", scope=Scope.user_state,
        help="Answer",
    )

    time = Integer(
        default=9999, scope=Scope.user_state,
        help="Question Time Limit",
    )

    questions = List(
        default = [], scope=Scope.user_state,
        help = "All questions"
    )



    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
    
        myJson = self.resource_string("public/data.json")
        self.score = 0
        self.questions = json.loads(myJson)["questions"]
        self.maxScore = len(self.questions)
        random.seed
        n = random.randint(0, len(self.questions) - 1)
        self.question = self.questions[n]["question"]
        self.answer = self.questions[n]["answer"]
        self.time = self.questions[n]["time"]
        self.questions.pop(n)
        html = self.resource_string("static/html/myxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/myxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/myxblock.js"))
        frag.initialize_js("MyXBlock")
        return frag

    @XBlock.json_handler
    def check_answer(self, data, suffix=''):
        if data['userAnswer'] == self.answer:
            self.score += 1
        if self.questions:
            n = random.randint(0, len(self.questions) - 1)
            self.question = self.questions[n]["question"]
            self.answer = self.questions[n]["answer"]
            self.time = self.questions[n]["time"]
            self.questions.pop(n)
            return {"score": self.score, "maxScore":self.maxScore, "question": self.question, "isDone" : False}
        else:
            return {"score": self.score, "maxScore":self.maxScore, "isDone" : True}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MyXBlock",
             """<myxblock/>
             """),
            ("Multiple MyXBlock",
             """<vertical_demo>
                <myxblock/>
                <myxblock/>
                <myxblock/>
                </vertical_demo>
             """),
        ]
