'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Jan 21, 2018
@author: Niels Lubbes
'''

from orbital.sage_interface import sage_vector
from orbital.sage_interface import sage_factor
from orbital.sage_interface import sage_QQ
from orbital.sage_interface import sage_pi

from orbital.class_orb_tools import OrbTools

from orbital.class_orb_ring import OrbRing

from orbital.povray.class_pov_input import PovInput

from orbital.povray.povray import create_pov
from orbital.povray.povray_aux import get_time_str

from orbital.sphere.sphere_transform import get_rot_S3
from orbital.sphere.sphere_transform import get_trn_S3
from orbital.sphere.sphere_transform import get_scale_S3
from orbital.sphere.sphere_transform import get_hp_P4


def dp8_clifford():
    '''    
    Construct povray image of octic del Pezzo surface in S^3.
    The surface is created as the Clifford translation of a
    great circle along a little circle.        
    '''

    # construct surface as pointwise hamiltonian product of
    # two circles in S^3
    #
    T = get_trn_S3( [0, 0, 0] )
    R = get_rot_S3( 6 * [0] )
    S = get_scale_S3( 1 )
    A = S * R * T

    q32 = sage_QQ( 3 ) / 2
    T = get_trn_S3( [q32, 0, 0] )
    R = get_rot_S3( 6 * [0] )
    S = get_scale_S3( 1 )
    B = S * R * T

    c0, s0, c1, s1 = OrbRing.coerce( 'c0,s0,c1,s1' )
    u = list( A * sage_vector( [1, c0 , s0 , 0, 0] ) )
    v = list( B * sage_vector( [1, c1 , s1 , 0, 0] ) )
    p = get_hp_P4( u, v )
    pmz_AB_lst = [ p[0] - p[4], p[1], p[2], p[3] ]

    for pmz in pmz_AB_lst:
        OrbTools.p( '\t\t', sage_factor( pmz ) )

    # PovInput dp8 clifford
    #
    pin = PovInput()

    pin.path = './' + get_time_str() + '_dp8_clifford/'
    pin.fname = 'orb'
    pin.scale = 1
    pin.cam_dct['location'] = ( 0, 0, 4 )
    pin.cam_dct['lookat'] = ( 0, 0, 0 )
    pin.cam_dct['rotate'] = ( 0, 0, 0 )
    pin.shadow = True
    pin.light_lst = [( 0, 0, -10 ), ( 0, -10, 0 ), ( -10, 0, 0 ),
                     ( 0, 0, 10 ), ( 0, 10, 0 ), ( 10, 0, 0 ) ]
    pin.axes_dct['show'] = False
    pin.axes_dct['len'] = 1.2
    pin.height = 400
    pin.width = 800
    pin.quality = 11
    pin.ani_delay = 10

    pin.impl = None

    pin.pmz_dct['A'] = ( pmz_AB_lst, 0 )
    pin.pmz_dct['B'] = ( pmz_AB_lst, 1 )

    pin.pmz_dct['FA'] = ( pmz_AB_lst, 0 )
    pin.pmz_dct['FB'] = ( pmz_AB_lst, 1 )

    v0_lst = [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 0, 360, 5 )]
    v1_lst_A = [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 0, 180, 10 )]
    v1_lst_A += [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 180, 360, 20 )]
    v1_lst_B = [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 0, 360, 10 )]

    v1_lst_FA = [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 0, 180, 1 )]
    v1_lst_FA += [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 180, 360, 2 )]
    v1_lst_FB = [ ( sage_QQ( i ) / 180 ) * sage_pi for i in range( 0, 360, 1 )]

    pin.curve_dct['A'] = {'step0':v0_lst, 'step1':v1_lst_A, 'prec':10, 'width':0.04}
    pin.curve_dct['B'] = {'step0':v0_lst, 'step1':v1_lst_B, 'prec':10, 'width':0.04}
    pin.curve_dct['FA'] = {'step0':v0_lst, 'step1':v1_lst_FA, 'prec':10, 'width':0.02}
    pin.curve_dct['FB'] = {'step0':v0_lst, 'step1':v1_lst_FB, 'prec':10, 'width':0.02}

    col_A = ( 0.6, 0.4, 0.1, 0.0 )
    col_B = ( 0.1, 0.15, 0.0, 0.0 )
    colFF = ( 0.1, 0.1, 0.1, 0.0 )
    pin.text_dct['A'] = [True, col_A, 'phong 0.2 phong_size 5' ]
    pin.text_dct['B'] = [True, col_B, 'phong 0.2 phong_size 5' ]
    pin.text_dct['FA'] = [True, colFF, 'phong 0.2 phong_size 5' ]
    pin.text_dct['FB'] = [True, colFF, 'phong 0.2 phong_size 5' ]

    # raytrace image/animation
    create_pov( pin, ['A', 'B'] )
    create_pov( pin, ['A', 'B', 'FA', 'FB'] )
    create_pov( pin, ['A', 'FA', 'FB'] )
    create_pov( pin, ['B', 'FA', 'FB'] )

