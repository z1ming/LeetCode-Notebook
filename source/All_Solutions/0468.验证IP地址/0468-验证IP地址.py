class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isSubIp4(s):
            if not re.match('[1-9][0-9]?[0-9]?$|0$', s): return False
            if int(s) > 255: return False
            return True
        def isSubIp6(s):
            if not re.match('([0-9a-fA-F]?){3}([0-9a-fA-F])$', s): return False
            return True
        def isIP4(s):
            ip_list = s.split('.')
            if len(ip_list) != 4:
                return False
            for ip in ip_list:
                if not isSubIp4(ip):
                    return False
            return True
        def isIP6(s):
            ip_list = s.split(':')
            if len(ip_list) != 8:
                return False
            for ip in ip_list:
                if not isSubIp6(ip):
                    return False
            return True

        if isIP4(IP):
            return 'IPv4'
        elif isIP6(IP):
            return 'IPv6'
        else:
            return 'Neither'
