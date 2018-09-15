# coding: utf-8

class LogicError(BaseException):
    '''程序内部逻辑错误'''
    code = None

    def __str__(self):
        return self.__class__.__name__


def gen_error(name: str, err_code: int) -> LogicError:
    return type(name, (LogicError,), {'code': err_code})

# 正常
OK = gen_error('OK', 0)

# 通用错误
InternalError = gen_error('InternalError', 1000)        # 服务器内部错误
ParamsError = gen_error('ParamsError', 1001)            # 参数错误
DataError = gen_error('DataError', 1002)                # 数据错误
DoseNotExist = gen_error('DoseNotExist', 1003)          # 不存在
ReachUpperLimit = gen_error('ReachUpperLimit', 1004)    # 达到上限
PermissionDenied = gen_error('PermissionDenied', 1005)  # 没有权限
# 用户类错误
LoginRequired = gen_error('LoginRequired', 2000)    # 用户未登录
NameConflict = gen_error('NameConflict', 2001)      # 名字冲突
MoneyNotEnough = gen_error('MoneyNotEnough', 2002)  # 金钱不足
UserNotExist = gen_error('UserNotExist', 2003)      # 用户不存在
NotYourFriend = gen_error('NotYourFriend', 2004)    # 不是好友关系
