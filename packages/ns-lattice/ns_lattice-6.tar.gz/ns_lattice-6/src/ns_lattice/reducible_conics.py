'''
Use of this source code is governed by a MIT-style license that can be found in the LICENSE file.
Created on Feb 25, 2024

We consider DPLattice objects which represent the Neron-Severi lattice of a weak del Pezzo surface.
For each class of a conic, we compute all possible reducible conics that have the same class. 
The number of such reducible conics are the singular values of a conic fibration and of interest 
in web geometry (see arXiv:2401.06711 by Luc Pirio). 

@author: Niels Lubbes
'''

from ns_lattice.class_dp_lattice import DPLattice
from ns_lattice.class_ns_tools import NSTools
from ns_lattice.sage_interface import sage_Combinations
from ns_lattice.class_div import Div


def get_reducible_conics( dpl ):
    '''
    Parameters
    ----------
    dpl : DPLattice
        Represents an equivalence class of the Neron-Severi lattice 
        of a real weak del Pezzo surface
    
    Returns
    -------
    dict{Div:list<Div>}
        The output dictionary has the following keys and values:
        
        Keys:
        Div objects representing classes of conics,
        namely elements of DPLattice.real_fam_lst.
        
        Values:
        A list of sublists of Div objects whose sum is equal to the dictionary key. 
        Each sublist contains exactly two (possibly equal) classes of lines in DPLattice.m1_lst, 
        and any number of pairwise different classes in DPLattice.d_lst.
        The sublists are pairwise different as sets.          
    '''
    # check if input was already computed
    #
    key = 'get_reducible_conics_'
    key += str( dpl.get_rank() ) + '_'
    key += dpl.get_marked_Mtype() + '_'
    key += dpl.get_real_type() + '_'
    key += str( dpl.get_numbers()[-2] ) + '_'  # len(self.real_m1_lst)
    key += str( dpl.get_numbers()[-1] )  # len(self.real_fam_lst)
    if key in NSTools.get_tool_dct():
        return NSTools.get_tool_dct()[key]

    # for all two (-1)-classes check if it adds up to the class of a real conic
    # up to the sum of effective (-2)-classes
    #
    f_dct = {}
    for u, v in list( sage_Combinations( dpl.m1_lst, 2 ) ) + [( u, u ) for u in dpl.m1_lst]:
        for dcomb in sage_Combinations( dpl.d_lst ):
            f = u + v
            for d in dcomb:
                f += d
            if f in dpl.real_fam_lst:
                if f not in f_dct.keys():
                    f_dct[f] = []
                f_dct[f] += [[u, v] + dcomb]

    # cache output
    #
    NSTools.get_tool_dct()[key] = f_dct
    NSTools.save_tool_dct()  # this takes a lot of time

    return f_dct


def print_classification_reducible_conics( max_rank ):
    '''
    Classification of root bases in root system of rank at most "max_rank".
    See "DPLattice.get_cls_root_bases()".
    
    For each entry in the classification DPLattice.get_cls(), 
    print the output of get_reducible_conics() in a formatted table.
    
    Parameters
    ----------
    max_rank : int
        Maximal rank.
    '''
    row_format = '{:<6}{:<5}{:<8}{:<16}{:<5}{:<5}{:<5}{:<5}{:<6}{:<7}{:<70}'
    row_head = [ 'rownr', 'deg', 'Mtype', 'type',
            '#-2', '#-1', '#fam', '#-2R', '#-1R', '#famR',
            '(#ConicalClasses,#ReducibleConics)', '(-2)-classes', 'conic decompositions']
    row_lst = [row_head]

    rownr = 0
    for rank in range( 3, max_rank + 1 ):
        dpcls = sorted( DPLattice.get_cls( rank ) )
        for dpl in dpcls:

            f_dct = get_reducible_conics( dpl )

            n1_lst = [len( f_dct[key] ) for key in f_dct.keys()]
            n2_lst = [( n1_lst.count( n1 ), n1 ) for n1 in n1_lst]
            n2_lst = list( set( n2_lst ) )

            row = [rownr, 10 - rank, dpl.get_marked_Mtype(), dpl.get_real_type() ]
            row += list( dpl.get_numbers() )
            row += [str( n2_lst )]
            rownr += 1

            # ignore rows
            #
            # if dpl.get_marked_Mtype() != 'A0': continue
            # if [ n2 for n2 in n2_lst if n2[0] > 4 and n2[1] in [3]] == []: continue
            # if [ n2 for n2 in n2_lst if n2[1] in [3]] == []: continue

            row_lst += [row]

            # print partial data to output in order to share as txt file
            #
            if False:
                NSTools.p( 'rownr = ' + str( rownr ) + ' deg = ' + str( 10 - rank ), dpl.get_marked_Mtype(), dpl.get_real_type(), ' effective (-2)-classes =', dpl.d_lst, ' reducible conics =', sorted( f_dct.items() ), ' (-1)-classes =', dpl.m1_lst )
                Div.short_output = False
                NSTools.p( 'rownr = ' + str( rownr ) + ' deg = ' + str( 10 - rank ), dpl.get_marked_Mtype(), dpl.get_real_type(), ' effective (-2)-classes =', dpl.d_lst, ' reducible conics =', sorted( f_dct.items() ), ' (-1)-classes =', dpl.m1_lst )
                Div.short_output = True

    NSTools.p( 'Formatted Table:' )
    s = ''
    for row in row_lst:
        s += row_format.format( *row ) + '\n'

    NSTools.p( 'Classification of root bases:\n' + s )
    NSTools.p( 'max_rank =', max_rank, ', #rows =', rownr )
    NSTools.p( 80 * '#' )


def rownr_to_dpl( rownr ):
    '''
    Parameters
    ----------
    rownr : int
        A natural number denoting the row number in Table 7 of the following article: 
        Title = "Webs of rational curves on real surfaces and 
         a classification of real weak del Pezzo surfaces"
        Arxiv = https://arxiv.org/abs/1807.05881           
               
    Returns
    -------
    DPLattice
        The DPLattice objects corresponding to the row number.
    '''
    rowidx = 0
    for rank in range( 3, 9 + 1 ):
        for dpl in sorted( DPLattice.get_cls( rank ) ):
            if rowidx == rownr:
                return dpl
            rowidx += 1


if __name__ == '__main__':
    NSTools.filter( ['reducible_conics.py'] )  # show only output printed from this module
    NSTools.filter( None )  # uncomment to show all output

    dct = print_classification_reducible_conics( 9 )

    if False:
        rownr = 119
        dpl = rownr_to_dpl( rownr )
        f_dct = get_reducible_conics( dpl )
        print( dpl )
        print( 'Reducible conics' )
        for key in f_dct.keys():
            print( '    ', key, ' : ', f_dct[key] )

    NSTools.p( 'The End' )
