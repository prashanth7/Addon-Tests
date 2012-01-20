#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Bebe <florin.strugariu@softvision.ro>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from selenium.webdriver.common.by import By

from pages.page import Page


class BreadcrumbsRegion(Page):

    _breadcrumb_locator = (By.ID, 'breadcrumbs')  # Base locator
    _breadcrumbs_locator = (By.CSS_SELECTOR, " li") #breadcrumbs elements locator
    _link_locator = (By.CSS_SELECTOR, ' a')

    def __init__(self, testsetup):
        Page.__init__(self, testsetup)

    def click_breadcrumb(self, lookup=None):
        if lookup == None:
            self.selenium.find_element(*self._link_locator).click()
        else:
            breadcrumb = self.selenium.find_element(*self._breadcrumb_locator)
            breadcrumb.find_element(By.LINK_TEXT, lookup).click()

    def get_breadcrumb_item_text(self, lookup):
        """ Returns the label of the given item in the breadcrumb menu. """
        breadcrumb = self.selenium.find_element(*self._breadcrumb_locator)
        return breadcrumb.find_element(By.CSS_SELECTOR, 'li:nth-child(%s)' % lookup).text

    @property
    def get_breadcrumb_item_text_all(self):
        """ Returns the label of all the items in the breadcrumb menu. """
        return self.selenium.find_element(*self._breadcrumb_locator).text

    def click_breadcrumb_item(self, lookup):
        """ Clicks on the given item in the breadcrumb menu. """
        breadcrumb = self.selenium.find_element(*self._breadcrumb_locator)
        breadcrumb.find_element(By.LINK_TEXT, lookup).click()


