""" Sahana Eden Module Automated Tests - HRM005 Add Staff To Organization

    @copyright: 2011-2012 (c) Sahana Software Foundation
    @license: MIT

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.
"""
from gluon import current
import unittest
from tests.web2unittest import SeleniumUnitTest
from selenium.common.exceptions import NoSuchElementException
from s3 import s3_debug
from tests import *
#import unittest, re, time
import time

class AddStaffToOrganisation(SeleniumUnitTest):
    def test_hrm005_add_staff_to_organization(self):
        
        """
            @case: HRM005
            @description: Add a premade made staff to a Organisation
            
            @TestDoc: https://docs.google.com/spreadsheet/ccc?key=0AmB3hMcgB-3idG1XNGhhRG9QWF81dUlKLXpJaFlCMFE
            @Test Wiki: http://eden.sahanafoundation.org/wiki/DeveloperGuidelines/Testing
        """
        
        self.login(account="admin", nexturl="org/organisation/41/human_resource")

        
        self.create("hrm_human_resource", 
                    [( "first_name",
                       "Herculano",
                       "pr_person"),
                     ( "last_name",
                       "Hugh",
                       "pr_person"),
                     ( "email",
                       "herculandfo@icandodfmybest.com",
                       "pr_person"),
                     ( "job_role_id",
                       "Chairman",
                       "option"),
                     ]
                     )

