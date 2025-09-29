from pyroute2 import NetlinkError
from libifstate.util import logger

netlinkerror_classes = (NetlinkError)

class ExceptionCollector():
    def __init__(self, ifname, netns):
        self.ifname = ifname
        self.netns = netns
        self.reset()

    def reset(self):
        self.excpts = []
        self.quiet = False

    def add(self, op, excpt, **kwargs):
        self.excpts.append({
            'op': op,
            'excpt': excpt,
            'args': kwargs,
        })
        if not self.quiet:
            logger.warning('{} failed: {}'.format(
                op, excpt.args[1]),
                extra={'iface': self.ifname, 'netns': self.netns})

    def has_op(self, op):
        for e in self.excpts:
            if e['op'] == op:
                return True
        return False

    def has_errno(self, errno):
        for e in self.excpts:
            if type(e['excpt']) == NetlinkError and e['excpt'].code == errno:
                return True
        return False

    def get_all(self, cb=None):
        if not cb:
            return self.excpts
        else:
            return filter(cb, self.excpts)

    def set_quiet(self, quiet):
        self.quiet = quiet

class FeatureMissingError(Exception):
    def __init__(self, feature):
        self.feature = feature

    def exit_code(self):
        return 5

class NetNSNotRoot(Exception):
    def exit_code(self):
        return 6

class LinkCannotAdd(Exception):
    pass


class LinkTypeUnknown(Exception):
    pass


class LinkDuplicate(Exception):
    pass

class LinkCircularLinked(Exception):
    def exit_code(self):
        return 5

class LinkNoConfigFound(Exception):
    pass

class ParserValidationError(Exception):
    def __init__(self, detail):
        self.detail = detail

    def exit_code(self):
        return 4

class ParserOSError(Exception):
    def __init__(self, oserr):
        self.fn = oserr.filename
        self.msg = oserr.strerror

class ParserOpenError(ParserOSError):
    def exit_code(self):
        return 1

class ParserIncludeError(ParserOSError):
    def exit_code(self):
        return 3

class ParserParseError(Exception):
    def exit_code(self):
        return 2

class RouteDuplicate(Exception):
    pass

class NetnsUnknown(Exception):
    def __init__(self, netns):
        self.args = (None, "netns '{}' is unknown".format(netns))
