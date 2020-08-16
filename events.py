#  O365-Client -- A client to connect O365
#  Copyright (C) 2020  Micraow
#
#  This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
from mailboxactions import MailboxActions
from O365 import Account
import re

credentials = ('74424fcf-55d7-4e15-99d7-1663c0ba2e94', )
account = Account(credentials, auth_flow_type='public')

Mailbox = MailboxActions()
Mailbox.check_if_authenticated()


class Read:
    """专门用来读取日历"""
    def __init__(self):
        pass

    def get_event(self):
        """获取默认日历事件"""
        schedule = account.schedule()
        calendar_name = schedule.get_default_calendar()
        print(calendar_name)
        calendar = schedule.get_calendar(calendar_name='Calendar')
        # 说实话，我不知道query有什么用，好像无论赋值什么，都会输出所有日程，所以我删了它。
        events = calendar.get_events(include_recurring=False)
        for event in events:
            print(event)

    def clear_event(self):
        """输出经正则表达式处理过的日程（仅名称）"""
        schedule = account.schedule()
        calendar_name = schedule.get_default_calendar()
        print(calendar_name)
        calendar = schedule.get_calendar(calendar_name='Calendar')
        # 说实话，我不知道query有什么用，好像无论赋值什么，都会输出所有日程，所以我删了它。
        events = calendar.get_events(include_recurring=False)
        reg = r'Subject:?*\s'  #就是这里的正则总是报错 re.error: multiple repeat at position 9
        clear_event = re.match(reg,str(events))   #就是这里的正则总是报错 re.error: multiple repeat at position 9
        print(clear_event)