#coding=utf-8 
#https://www.codeday.top/2017/02/19/21195.html
#スレッドをお互いに待ってデッドロック


import time 
import threading 
class Account: 
  def __init__(self, _id, balance, lock): 
    self.id = _id 
    self.balance = balance 
    self.lock = lock 
 
  def withdraw(self, amount): 
    self.balance -= amount 
 
  def deposit(self, amount): 
    self.balance += amount 
 
 
def transfer(_from, to, amount): 
  if _from.lock.acquire():# Lock your account  
    _from.withdraw(amount) 
    time.sleep(1)# Let the transaction time becomes longer ，2 Time overlap ， Have enough time to make a life and death lock  
    print('wait for lock...')
    if to.lock.acquire():# Lock in each other's account  
      to.deposit(amount) 
      to.lock.release() 
    _from.lock.release() 
  print('finish...') 
 
a = Account('a',1000, threading.Lock()) 
b = Account('b',1000, threading.Lock()) 
threading.Thread(target = transfer, args = (a, b, 100)).start() 
threading.Thread(target = transfer, args = (b, a, 200)).start() 
