#!/usr/bin/env python

"""
models.py

I'm trying to write the Particle/Particles containers in a way, so it 
can be used in an amuse.datamodel.particles.Particles-like way.
"""

import unittest

def main():
    """ 
    This is never run. I'm only outlining the desired behaviour.

    """
    particles = Particles(3)
    particles.x = [0, 1, 2]
    particles.y = [2, -1, 0]
    particles.z = [0, 1, 2]
    particles.vx = [-1, 2, -2]
    particles.vy = [-2, 1, 0]
    particles.vz = [0, -2, -1]

    p1 = Particle(position=[1,1], velocity=[2,0], mass=20)
    p2 = Particle(position=[-1,-1], velocity=[-2,0], mass=10)
    p3 = Particle(position=[-1,-1], mass=10)
   
    #order may be switched if keywords are used explicitly
    p4 = Particle(velocity=[2,0], position=[-1,-2], mass=10)

    #if arguments are given as positional arguments, then the arguments
    #are interpreted as position, velocity, mass. 
    p5 = Particle([1, -1], [1,-2], 20) 

    # len(Particle.position) == len(Particle.velocity) should evaluated true
    # In other words, the following should fail/raise an Exception
    # p6 = Particle([1, -1, 3], [1,-2], 20) 

    #Appending Particle objects to Particles object
    particles = Particles() #empty container 
    particles.append(p1)
    particles.append(p2)
    particles.append(p3)
    particles.append(p4)
    particles.append(p5)

    #Extending Particles object with Particle objects
    particles = Particles() #empty container 
    particles.extend([p1, p2, p3, p4, p5])

    #Broadcast positions/velocities/masses 
    particles = Particles(5)  
    particles.x = [1,2,3,4,5]
    particles.y = [1,2,3,4,5]
    particles.z = [1,2,3,4,5]
    particles.vx = [1,2,3,4,5]
    particles.vy = [1,2,3,4,5]
    particles.vz = [1,2,3,4,5]
    particles.mass = [5,4,3,2,1]
    
    return 0

class Particle(object):
    """ 
    yes:
    maybe:

    Valid keyword arguments:
    mass
    position
    velocity
    
    Attributes that should created when instance is initialised:
    x
    y
    z
    vx
    vy
    vz
    mass
    """
    def __init__(self, position=None, velocity=None, mass=None):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    @property
    def position(self):
        return self._position

    @position.setter 
    def position(self, position):
        if position:
            self._position = position
        else:
            self._position = [None, None, None]

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter 
    def velocity(self, velocity):
        if velocity:
            self._velocity = velocity
        else:
            self._velocity = [None, None, None]

    @property
    def x(self):
        try:
            return self._position[0]
        except IndexError:
            return None

    @x.setter
    def x(self, value):
        self._position[0] = value
                 
    @property
    def y(self):
        try:
            return self._position[1]
        except IndexError:
            return None

    @y.setter
    def y(self, value):
        self._position[1] = value
            
    @property
    def z(self):
        try:
            return self._position[2]
        except IndexError:
            return None
       
    @z.setter
    def z(self, value):
        self._position[2] = value

    @property
    def vx(self):
        try:
            return self._velocity[0]
        except IndexError:
            return None

    @vx.setter
    def vx(self, value):
        self._velocity[0] = value
                 
    @property
    def vy(self):
        try:
            return self._velocity[1]
        except IndexError:
            return None

    @vy.setter
    def vy(self, value):
        self._velocity[1] = value
            
    @property
    def vz(self):
        try:
            return self._velocity[2]
        except IndexError:
            return None
       
    @vz.setter
    def vz(self, value):
        self._velocity[2] = value


class Particles(list):
    """ 
    Yes:  
    - raise warnings when particles at same positions are added.
    - able to do Particles.extend([Particle(), Particle(), Particle()] 
    - printing strategies
    - method to check that particles are ready to be evolved. (i.e.
      positions/velocities/masses etc are well defined.)

    Maybe: 
    - implicitly use numpy if available

    """
    def __init__(self, nr_of_particles=0, name=None):
        self.extend([Particle() for i in range(nr_of_particles)])
        self.name = str(name)

    def __str__(self):
        return "{name}: {size}".format(name=self.name, size=len(self))

    def __repr__(self):
        return self.name 

    def __len__(self):
        """
        Maybe make len(Particles) more verbose then len(list) later.
        """
        return super().__len__()
    
    def append(self, particle):
        """ 
        Appends a single Particle instance.
        """
        assert isinstance(particle, Particle)
        super().append(particle)

    def extend(self, particles):
        """
        Extends self with another Particles OR list instance.
        """
        assert (isinstance(particles, Particles) or 
                isinstance(particles, list))
        super().extend(particles)

    def update(self, **kwargs):
        """ 
        Hook to update positions/velocities/masses etc.
        """
        pass 

    @property
    def mass(self):
        masses = [p.mass for p in self]
        return masses
 
    @mass.setter 
    def mass(self, masses):
        assert len(masses) == len(self)
        for i, mass in enumerate(masses):
            self[i].mass = mass

    @property
    def x(self):
        return [p.x for p in self]

    @x.setter
    def x(self, x_list):
        for i, x in enumerate(x_list):
            self[i].x = x

    @property
    def y(self):
        return [p.y for p in self]

    @y.setter
    def y(self, y_list):
        for i, y in enumerate(y_list):
            self[i].y = y

    @property
    def z(self):
        return [p.z for p in self]

    @z.setter
    def z(self, z_list):
        for i, z in enumerate(z_list):
            self[i].z = z

    @property
    def vx(self):
        return [p.vx for p in self]

    @vx.setter
    def vx(self, vx_list):
        for i, vx in enumerate(vx_list):
            self[i].vx = vx

    @property
    def vy(self):
        return [p.vy for p in self]

    @vy.setter
    def vy(self, vy_list):
        for i, vy in enumerate(vy_list):
            self[i].vy = vy

    @property
    def vz(self):
        return [p.vz for p in self]

    @vz.setter
    def vz(self, vz_list):
        for i, vz in enumerate(vz_list):
            self[i].vz = vz


class test_Particles_initialisation(unittest.TestCase):
    """ 
    Tests Particles object creation and tests its methods. 
    """
    
    def setUp(self):
        self.particles = Particles(4, 'Euler')

    def test_name(self):
        self.assertEqual(self.particles.name, 'Euler')
 
    def test_string(self):
        self.assertEqual(self.particles.__str__(), 'Euler: 4')

    def test_len(self):
        self.assertEqual(len(self.particles), 4)

    def test_append(self):
        self.particles.append(Particle())
        self.assertEqual(len(self.particles), 5)

    def test_indexing(self):
        self.assertTrue(isinstance(self.particles[0], Particle))
        self.assertTrue(isinstance(self.particles[1], Particle))
        self.assertTrue(isinstance(self.particles[2], Particle))
        self.assertTrue(isinstance(self.particles[3], Particle))

    def test_broadcast_position(self):
        self.particles.x = [1, 2, 3, 4]
        self.assertEqual(self.particles[0].x, 1.0)
        self.assertEqual(self.particles[1].x, 2.0)
        self.assertEqual(self.particles[2].x, 3)
        self.assertEqual(self.particles[3].x, 4)

        self.particles.y = [1, 2, 3, 4]
        self.assertEqual(self.particles[0].y, 1.0)
        self.assertEqual(self.particles[1].y, 2.0)
        self.assertEqual(self.particles[2].y, 3)
        self.assertEqual(self.particles[3].y, 4)

        self.particles.z = [1, 2, 3, 4]
        self.assertEqual(self.particles[0].z, 1.0)
        self.assertEqual(self.particles[1].z, 2.0)
        self.assertEqual(self.particles[2].z, 3)
        self.assertEqual(self.particles[3].z, 4)

        self.assertEqual(self.particles[0].position, [1,1,1])
        self.assertEqual(self.particles[1].position, [2,2,2])
        self.assertEqual(self.particles[2].position, [3,3,3])
        self.assertEqual(self.particles[3].position, [4,4,4])

    def test_broadcast_velocity(self):
        self.particles.vx = [1, 2, 3, 4]
        self.assertEqual(self.particles[0].vx, 1.0)
        self.assertEqual(self.particles[1].vx, 2.0)
        self.assertEqual(self.particles[2].vx, 3)
        self.assertEqual(self.particles[3].vx, 4)

        self.particles.vy = [1, 2, 3, 4]
        self.assertEqual(self.particles[0].vy, 1.0)
        self.assertEqual(self.particles[1].vy, 2.0)
        self.assertEqual(self.particles[2].vy, 3)
        self.assertEqual(self.particles[3].vy, 4)

        self.particles.vz = [1, 2, 3, 4]
        self.assertEqual(self.particles[0].vz, 1.0)
        self.assertEqual(self.particles[1].vz, 2.0)
        self.assertEqual(self.particles[2].vz, 3)
        self.assertEqual(self.particles[3].vz, 4)

        self.assertEqual(self.particles[0].velocity, [1,1,1])
        self.assertEqual(self.particles[1].velocity, [2,2,2])
        self.assertEqual(self.particles[2].velocity, [3,3,3])
        self.assertEqual(self.particles[3].velocity, [4,4,4])

    def test_broadcast_mass(self):
        self.particles.mass = [4, 3, 2, 1]
        self.assertEqual(self.particles[0].mass, 4)
        self.assertEqual(self.particles[1].mass, 3)
        self.assertEqual(self.particles[2].mass, 2)
        self.assertEqual(self.particles[3].mass, 1)
        self.assertEqual(self.particles.mass, [4, 3, 2, 1])

class test_Particle_initialisation(unittest.TestCase):

      def setUp(self):
          self.particle = Particle(position=[1, 2, 3], 
              velocity=[-1, -2, -3], mass=10)

      def test_xyz_position_attributes(self):
          self.assertEqual(self.particle.x, 1)
          self.assertEqual(self.particle.y, 2)
          self.assertEqual(self.particle.z, 3)
          self.assertEqual(self.particle.x, 1.0)
          self.assertEqual(self.particle.y, 2.0)
          self.assertEqual(self.particle.z, 3.0)

      def test_xyz_velocity_attributes(self):
          self.assertEqual(self.particle.vx, -1.0)
          self.assertEqual(self.particle.vy, -2.0)
          self.assertEqual(self.particle.vz, -3.0)
          self.assertEqual(self.particle.vx, -1)
          self.assertEqual(self.particle.vy, -2)
          self.assertEqual(self.particle.vz, -3)

      def test_position_attribute(self):
          self.assertEqual(self.particle.position, [1, 2, 3])
          self.assertEqual(self.particle.position, [1.0, 2.0, 3.0])

      def test_velocity_attribute(self):
          self.assertEqual(self.particle.velocity, [-1, -2, -3])
          self.assertEqual(self.particle.velocity, [-1.0, -2.0, -3.0])

      def test_mass_attribute(self):
          self.assertEqual(self.particle.mass, 10.0)
          self.assertEqual(self.particle.mass, 10)

      def test_position_update(self):
          self.particle.position = [3, 2, 1]
          self.assertEqual(self.particle.x, 3.0)
          self.assertEqual(self.particle.y, 2.0)
          self.assertEqual(self.particle.z, 1.0)
          self.assertEqual(self.particle.x, 3)
          self.assertEqual(self.particle.y, 2)
          self.assertEqual(self.particle.z, 1)
          
      def test_velocity_update(self):
          self.particle.velocity = [3, 2, 1]
          self.assertEqual(self.particle.vx, 3.0)
          self.assertEqual(self.particle.vy, 2.0)
          self.assertEqual(self.particle.vz, 1.0)
          self.assertEqual(self.particle.vx, 3)
          self.assertEqual(self.particle.vy, 2)
          self.assertEqual(self.particle.vz, 1)

      def test_mass_update(self):
          self.particle.mass = 23.3
          self.assertEqual(self.particle.mass, 23.3)

      def test_all_attributes(self):
          self.assertEqual(self.particle.x, 1)
          self.assertEqual(self.particle.y, 2)
          self.assertEqual(self.particle.z, 3)
          self.assertEqual(self.particle.x, 1.0)
          self.assertEqual(self.particle.y, 2.0)
          self.assertEqual(self.particle.z, 3.0)

          self.assertEqual(self.particle.vx, -1.0)
          self.assertEqual(self.particle.vy, -2.0)
          self.assertEqual(self.particle.vz, -3.0)
          self.assertEqual(self.particle.vx, -1)
          self.assertEqual(self.particle.vy, -2)
          self.assertEqual(self.particle.vz, -3)

          self.assertEqual(self.particle.position, [1, 2, 3])
          self.assertEqual(self.particle.position, [1.0, 2.0, 3.0])

          self.assertEqual(self.particle.velocity, [-1, -2, -3])
          self.assertEqual(self.particle.velocity, [-1.0, -2.0, -3.0])

          self.assertEqual(self.particle.mass, 10.0)
          self.assertEqual(self.particle.mass, 10)

class test_Particle_initialisation_empty(unittest.TestCase):
      def setUp(self):
          self.particle = Particle()

      def test_position_assignment_1(self):
          self.particle.position = [1.2]
          self.assertEqual(self.particle.x, 1.2)
          self.assertEqual(self.particle.y, None)
          self.assertEqual(self.particle.z, None)
          
      def test_position_assignment_2(self):
          self.particle.position = [1.2, 1.3]
          self.assertEqual(self.particle.x, 1.2)
          self.assertEqual(self.particle.y, 1.3)
          self.assertEqual(self.particle.z, None)

      def test_position_assignment_3(self):
          self.particle.position = [1.2, 1.3, 1.4]
          self.assertEqual(self.particle.x, 1.2)
          self.assertEqual(self.particle.y, 1.3)
          self.assertEqual(self.particle.z, 1.4)

      def test_velocity_assignment_1(self):
          self.particle.velocity = [1.2]
          self.assertEqual(self.particle.vx, 1.2)
          self.assertEqual(self.particle.vy, None)
          self.assertEqual(self.particle.vz, None)
          
      def test_velocity_assignment_2(self):
          self.particle.velocity = [1.2, 1.3]
          self.assertEqual(self.particle.vx, 1.2)
          self.assertEqual(self.particle.vy, 1.3)
          self.assertEqual(self.particle.vz, None)

      def test_velocity_assignment_3(self):
          self.particle.velocity = [1.2, 1.3, 1.4]
          self.assertEqual(self.particle.vx, 1.2)
          self.assertEqual(self.particle.vy, 1.3)
          self.assertEqual(self.particle.vz, 1.4)

      def test_mass_assignment(self):
          self.particle.mass = 20 
          self.assertEqual(self.particle.mass, 20)
          self.assertEqual(self.particle.vx, None)
          self.assertEqual(self.particle.vy, None)
          self.assertEqual(self.particle.vz, None)
 

if __name__ == '__main__':
    unittest.main(verbosity=2)













































