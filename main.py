import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
      return MED[(S, T)]

  if S == "":
      return len(T)
  elif T == "":
      return len(S)
  elif S[0] == T[0]:
      MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
  else:
      MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

  return MED[(S, T)]


def fast_align_MED(S, T, MED={}):
    if S == "":
        result = (len(T), (len(T) * '-', T))
    elif T == "":
        result = (len(S), (S, len(S) * '-'))
    else:
        if S[0] == T[0]:
            cost, (aligned_S, aligned_T) = fast_align_MED(S[1:], T[1:], MED)
            result = (cost, (S[0] + aligned_S, T[0] + aligned_T))
        else:
            del_cost, (del_S, del_T) = fast_align_MED(S[1:], T, MED)
            ins_cost, (ins_S, ins_T) = fast_align_MED(S, T[1:], MED)
            sub_cost, (sub_S, sub_T) = fast_align_MED(S[1:], T[1:], MED)

            if del_cost < ins_cost and del_cost < sub_cost:
                result = (1 + del_cost, ('-' + del_S, T[0] + del_T))
            elif ins_cost < del_cost and ins_cost < sub_cost:
                result = (1 + ins_cost, (S[0] + ins_S, '-' + ins_T))
            else:
                result = (1 + sub_cost, (S[0] + sub_S, T[0] + sub_T))
    MED[(S, T)] = result
    return result

