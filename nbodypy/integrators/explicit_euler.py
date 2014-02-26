"""
explicit_euler.py

Euler's explicit method for an N-body system in R^2.

"""

import unittest

def y_n_plus_1(y_n, stepsize):
    """ 
    y_n: [x_n, v_n]
    stepsize: timestep
    """
    x_n = y_n[0]
    v_n = y_n[1]

    a_n = 42 #acceleration of this particle, calc later.

    x_n_plus_1 = x_n + v_n * stepsize
    v_n_plus_1 = v_n + a_n * stepsize

    return [x_n_plus_1, v_n_plus_1]


def get_forces(particles):
    """
    MOVE THIS LATER 

    particles: Particles class
    
    return
    ------
    a list forces
    """
    forces = []
    for p_i in particles:
        # is this correct? need testcase for calculating forces
        # how does this handle positions = [ 1, None, None ] ?
        # Particle class needs hashkey to compare p_i is not p_j?
        total_force_acting_on_p_i = sum( [force_ij(p_i, p_j) for p_j in \
                                          particles if p_i is not p_j  ] )
        forces.append(total_force_acting_on_p_i)
    return forces
        

def force_ij(p_i, p_j):
    """
    MOVE THIS LATER 

    Calculates the force between two particles.

    numpy solution:
        Fij =  -G * p_i.mass * p_j.mass / numpy.linalg.norm(p_i.position - p_j.position)**2
        
    """
    G = 1 #gravitational constant
    Fij =  -G * p_i.mass * p_j.mass / distance(p_i.position, p_j.position)**2
    return Fij
   

def distance(p_i, p_j):
    """
    MOVE THIS LATER 

    Calculates the distance between two particles.

    Numpify later?:

        def distance(p_i, p_j):
            seperation_vector = p_i - p_j
            r_ij = seperation_vector.dot(seperation_vector)**0.5
            return r_ij

    """
    seperation_vector = [i - j for i, j  in zip(p_i, p_j)] 
    r_ij = magnitude(seperation_vector)
    return r_ij

def magnitude(vector):
    """
    MOVE THIS LATER 
    vector: a python list
    """
    mag = sum([i**2 for i in vector])**0.5
    return mag 



class test_Something(unittest.TestCase):
    def setUp(self):
        self.obj = 1

    def test_1(self):
        pass

    def test_2(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

