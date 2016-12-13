#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple delaunay2D test
  
Written by Jose M. Espadero <josemiguel.espadero@urjc.es>
"""
import numpy as np
import delaunay2D as D

if __name__ == '__main__':
    
    ###########################################################        
    # Generate 'numSeeds' random seeds in a square of size 'radius'
    numSeeds = 24
    radius = 100
    seeds = radius * np.random.random((numSeeds, 2))
    print("seeds:\n", seeds)
    print("BBox Min:", np.amin(seeds, axis=0), "Bbox Max: ", np.amax(seeds, axis=0) )

    #Compute our Delaunay triangulation of seeds.
    #It is recommended to use the radius to create a noticeable margin
    DT = D.Delaunay2D(seeds, 100 * radius)

    #Extract our result (without extended BBox coordinates)
    DT_x, DT_y, DT_tris = DT.exportDT()
    print("DT_tris:", len(DT_tris), "triangles")
    print("DT_tris:\n", DT_tris)

    """
    How to plot triangular grids. (just for debug)
    """
    import matplotlib.pyplot as plt
    import matplotlib.tri

    # Create a plot with matplotlib.pyplot
    fig, ax = plt.subplots()
    ax.margins(0.1)
    ax.set_aspect('equal')

    #plot our Delaunay triangulation (plot in blue)
    ax.triplot(matplotlib.tri.Triangulation(DT_x, DT_y, DT_tris), 'bo-.')

    #DEBUG: Use matplotlib method to create a Delaunay triangulation (plot in green)
    #DEBUG: It should be equal to our result in DT_tris (plot in blue)
    #DEBUG: If boundary is diferent, try to increase the value of your margin
    #ax.triplot(matplotlib.tri.Triangulation(DT_x, DT_y), 'g-.')

    #DEBUG: plot our extended triangulation (plot in red)
    #EDT_x, EDT_y, EDT_tris = DT.exportExtendedDT()
    #print("Extended DT_tris:", len(EDT_tris), "triangles")
    #ax.triplot(matplotlib.tri.Triangulation(EDT_x, EDT_y, EDT_tris), 'ro-.')

    plt.show()
