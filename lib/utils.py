# -*- coding:utf-8 -*-
import re

# keep the re's encoding consistent with name


def validName(name):
    USERNAME_RE = re.compile(u"^[a-zA-Z\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff_]\
[0-9a-zA-Z\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff_]{3,20}$")
    return USERNAME_RE.match(name)


if __name__ == '__main__':
    print validName('duck')
    print repr('字符集')
    print '字符集'.decode('utf-8')
    print validName('字符集')
