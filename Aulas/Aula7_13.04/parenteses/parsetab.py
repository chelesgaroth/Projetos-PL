
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PA PFS : ParPar : PA Par PF ParPar : '
    
_lr_action_items = {'PA':([0,3,5,],[3,3,3,]),'$end':([0,1,2,5,6,],[-3,0,-1,-3,-2,]),'PF':([3,4,5,6,],[-3,5,-3,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'Par':([0,3,5,],[2,4,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> Par','S',1,'p_axioma','par_yacc.py',20),
  ('Par -> PA Par PF Par','Par',4,'p_parentesis','par_yacc.py',24),
  ('Par -> <empty>','Par',0,'p_parentesis_empty','par_yacc.py',28),
]
