
import rx
 
class StatefulOperator(object):
    def default(self, tup):
        msg = 'Default method called with ' + str(tup)
        return dict(message=msg)
 
    def __call__(self, tup):
        method_name = tup.pop('method_name', 'default')
        return getattr(self, method_name)(tup)
 
    def __repr__(self):
        return str(self.__dict__)
 
 
class Bottle(StatefulOperator):
    def __init__(self, uid, water_amount=0, capacity=10):
        self.uid = uid
        self.water = water_amount
        self.capacity = capacity

    #内部からしか呼んでないので_をつけてる
    def _algebric_sum(self, amount):
        tot = self.water + amount
        esit = tot <= self.capacity and tot >= 0
        if esit: self.water = tot
        return esit

    def pour_in(self, tup):
        print('>> POUR_IN', str(tup), str(self))
 
        amount = tup.get('amount', 0)
        res = self._algebric_sum(abs(amount))
        msg = 'OK' if res else 'KO'
        return dict(message=msg + ' -> ' + str(self))
 
    def drink(self, tup):
        print('>> DRINK', str(tup), str(self))
 
        amount = tup.get('amount', 0)
        res = self._algebric_sum(abs(amount) * -1)
        msg = 'OK' if res else 'KO'
        return dict(message=msg + ' -> ' + str(self))
 
    def drink_and_spit(self, tup):
        print('>> DRINK_AND_SPIT', str(tup), str(self))
 
        amount = tup.get('amount', 0)
        res = self._algebric_sum(abs(amount) * -1)
 
        msg = 'OK' if res else 'KO'
        resp = dict(message=msg + ' -> ' + str(self))
        other = tup.get('to')
 
        if res and other:
            tup = dict(method_name='pour_in', amount=amount)
            # this is the moment in which
            # the operator becomes conscious of the
            # other ones and discovers them using
            # their name (`uid`).
            USERS[other].on_next(tup)
 
        return resp
 
USERS = {
    'u1': rx.subjects.Subject(),
    'u2': rx.subjects.Subject(),
}

USERS['u1'].map(Bottle('b1')).subscribe(print)
USERS['u2'].map(Bottle('b2', capacity=20)).subscribe(print)

if __name__ == '__main__':
    s1 = USERS['u1']
    s2 = USERS['u2']
 
    def tup(mname, amount, to=''):
        #dictを返す
        if to:
            return dict(method_name=mname, amount=amount, to=to)
        return dict(method_name=mname, amount=amount)
 
    s1.on_next(tup('pour_in', 5))
    s2.on_next(tup('pour_in', 5))
 
    s1.on_next(tup('pour_in', 20))
    s2.on_next(tup('pour_in', 20))
 
    s1.on_next(tup('drink', 10))
    s2.on_next(tup('drink', 10))
 
    s1.on_next(tup('drink', 3))
    s2.on_next(tup('drink', 3))
 
    s1.on_next(tup('drink_and_spit', 3, 'u2'))
    s1.on_next(tup('drink_and_spit', 2, 'u2'))
    s2.on_next(tup('drink_and_spit', 4, 'u1'))
