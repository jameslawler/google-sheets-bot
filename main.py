#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import gaenv_lib
from src.synonymly import synonymly

class EnglishBeginner(webapp2.RequestHandler):
    def get(self):
        synonymlyObj = synonymly("English", "Beginner")
        synonymlyObj.run()
        self.response.write("Finished")

class EnglishIntermediate(webapp2.RequestHandler):
    def get(self):
        synonymlyObj = synonymly("English", "Intermediate")
        synonymlyObj.run()
        self.response.write("Finished")

class EnglishAdvanced(webapp2.RequestHandler):
    def get(self):
        synonymlyObj = synonymly("English", "Advanced")
        synonymlyObj.run()
        self.response.write("Finished")

app = webapp2.WSGIApplication([
    ('/tweet/english/beginner', EnglishBeginner),
    ('/tweet/english/intermediate', EnglishIntermediate),
    ('/tweet/english/advanced', EnglishAdvanced),
], debug=True)
