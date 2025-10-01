estuaire Solver
--------------
The enclosed PDE solver was developped to solve the estuaire Equation subject to boundary condition.

Building (Python 3)
-------------------

The project now targets Python 3 toolchains.  The Cython sources are rendered
from Mako templates during the build step, so no manual preprocessing is
required.  A typical build looks like::

    python -m pip install --upgrade pip
    python -m pip install build
    python -m build --wheel

This generates a wheel in ``dist/`` containing the ``estuaire`` package.  The
legacy OpenCL experiments have been removed as part of the port to Python 3.

.. math::
    |\Delta u(x)| = f(x)

In its current state, it uses a second order derivative estimation in a Fast Marching Method iteration scheme. It is used in the forward modeling to simulate the propagation of wavefronts. The algorithm scale very badly on parallel architecture since it rely on the causality of the solution in an iterative scheme. The current solution is limited to Regular grid with a constant spacing along axes.

Furthermore, the method needs a fully positive input grid to work correctly which is always the case for wavefront propagation with velocity.

For more information on the Fast Marching Method, please refer to papers from Sethian, J.A. : A Fast Marching Level Set Method for Monotically Advancing Fronts.

Raytracing and Frechet Derivatives
-----------------------------------
The Raytracing and Frechet Derivatives calculation uses a second order b-spline velocity grid parametrization inside a Runge-Kutta method. It uses the velocity grid and the traveltime calculated from the estuaire solver to solve the raypath.


C++ API
--------
The low level API for the estuaire solver and the raytracing is for internal use only and wont be supported in this documentation. Although, the comments in the code are pretty straight forward and should pose no problems at all.

Python API
-----------
