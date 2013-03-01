# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase
from gaiatest.apps.clock.app import Clock
import time


class TestClockTurnOnOffAlarm(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)

        # launch the Clock app
        self.clock = Clock(self.marionette)
        self.clock.launch()

        # create a new alarm with the default values that are available
        new_alarm = self.clock.tap_new_alarm()
        self.clock = new_alarm.tap_done()
        self.clock.wait_for_banner_not_visible()

    def test_clock_turn_on_off_alarm(self):
        """ Turn on/off the alarm
        https://moztrap.mozilla.org/manage/case/1779/
        """

        alarm = self.clock.alarms[0]

        # turn on the alarm
        origin_alarm_checked = alarm.is_alarm_active

        alarm.tap_checkbox()

        time.sleep(2)
        new_alarm_checked = alarm.is_alarm_active

        self.assertTrue(origin_alarm_checked != new_alarm_checked, 'user should be able to turn on the alarm.')

        origin_alarm_checked = alarm.is_alarm_active

        alarm.tap_checkbox()

        time.sleep(2)
        new_alarm_checked = alarm.is_alarm_active
        self.assertTrue(origin_alarm_checked != new_alarm_checked, 'user should be able to turn off the alarm.')

    def tearDown(self):
        # delete any existing alarms
        self.data_layer.delete_all_alarms()

        GaiaTestCase.tearDown(self)
