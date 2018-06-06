
import rx

class User():
    def __init__(self, uid, uname):
        self.uid = uid
        self.uname = uname

    def search_name_by_uid(self, uid):
        return dict(uid=uid, uname="user1")    

USERS = {
    'u1': rx.subjects.Subject(),
    'u2': rx.subjects.Subject(),
}


if __name__ == '__main__':
    USERS['u1'].map(User('uid1', 'uname1')).subscribe(print)
    USERS['u2'].map(User('uid2', 'uname2')).subscribe(print)
    # s1 = USERS['u1']
    # s2 = USERS['u2']

    # s1.subscribe()
    # # s1.connect()
    # s1.on_next(0)
