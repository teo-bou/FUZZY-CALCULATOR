import math
import random

class Intervalle_net_continu() : 
    def __init__(self, a1, a2) :
        self.a1 = a1
        self.a2 = a2
    
    def __str__(self) :
        return "[" + str(self.a1) + ", " + str(self.a2) + "]"

    def __add__(self, other) :
        return Intervalle_net(self.a1 + other.a1, self.a2 + other.a2)

    def __neg__(self) :
        return Intervalle_net(-self.a2, -self.a1)

    def __sub__(self, other) :
        return self + (-other)

    def __mul__(self, other) :
        return Intervalle_net(max([self.a1 * other.b1, self.a1 * other.b2, self.a2 * other.b1, self.a2 * other.b2]), 
                              max([self.b1 * other.a1, self.b1 * other.a2, self.b2 * other.a1, self.b2 * other.a2]))

    def __pow__(self, value) :
        if value != -1 : 
            raise ValueError("Only -1 is supported")
        if self.a1 == 0 or self.a2 == 0 : 
            raise ValueError("Only non-zero intervals are supported")
        if self.a1 <= 0 <= self.a2 : 
            raise ValueError("Only  strictly positive or strictly négative intervals are supported by this operation.")
        return Intervalle_net(1/self.a2, 1/self.a1)

    def __div__(self, other) :
        return self * (other**-1)

    def union(self, other) :
        if self.a2 < other.a1 or other.a2 < self.a1 :
            raise ValueError("The intervals must be joined")

        return Intervalle_net(min(self.a1, other.a1), max(self.a2, other.a2))
    

class Intervalle_net() :
    def __init__(self, *args) :
        if len(args%2 != 0) :
            raise ValueError("The number of arguments must be even")
    
        self.intervalles_continus = []
        for i in range(0, len(args), 2) :
            if args[i] >= args[i+1] :
                raise ValueError("The arguments must be ordered")
            self.intervalles_continus.append(Intervalle_net_continu(args[i], args[i+1]))
    
    def simplifier(self) :
        """
        Untested, coded by codeium AI
        """
        for i in range(len(self.intervalles_continus)) :
            for j in range(i+1, len(self.intervalles_continus)) :
                if self.intervalles_continus[i].a2 >= self.intervalles_continus[j].a1 :
                    self.intervalles_continus[i] = self.intervalles_continus[i] + self.intervalles_continus[j]
                    del self.intervalles_continus[j]
                    break
        

class Trapèseflou() :
    def __init__(self, a1, a2, a3,a4, h) :
        if not (a1 <= a2 <= a3) :
            raise ValueError("The arguments must be ordered")
        if h <= 0 : 
            raise ValueError("The height must be positive")
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.h = h
    def __add__(self, other) :
        if self.h != other.h :
            raise ValueError("The two NFTs must have the same height")
        return Trapèseflou(self.a1 + other.a1, self.a2 + other.a2, self.a3 + other.a3, self.a4 + other.a4, self.h)

    def __mul__(self, other) :
        """
        réparer
        """
        if self.h != other.h :
            raise ValueError("The two NFTs must have the same height")
        return Trapèseflou(self.a1 * other.a1, self.a2 * other.a2, self.a3 * other.a3, self.a4 * other.a4, self.h)

    def __pow__(self, value) :
        if value != -1 :
            raise ValueError("Only -1 is supported")
        return Trapèseflou(1/self.a4, 1/self.a3, 1/self.a2, 1/self.a1, self.h)
    
    def __div__(self, other) :
        return self * (other**-1)
    
    def __neg__(self) :
        return Trapèseflou(-self.a4, -self.a3, -self.a2, -self.a1, self.h)
    
    def __sub__(self, other) :
        return self + (-other)
    
    def __str__(self) -> str:
        return f"({self.a1}, {self.a2}, {self.a3}, {self.a4}, {self.h})"
    
#def alpha_coupe(alpha,self.a1, self.a2, a3, a4, h) : 
#    return Intervalle_net((self.a2-self.a1)*(alpha/h) + a1, -(self.a4-self.a3)*(alpha/h) + self.a4 )


        

        
        
            