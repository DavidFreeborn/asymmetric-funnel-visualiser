# Physics and scope

## What the model is

The visualiser treats each particle as a point particle moving at fixed speed in a two-dimensional closed billiard. The outer boundary, central divider, and funnel are static. Collisions are perfectly specular: the component of velocity normal to the wall changes sign and the tangential component is preserved.

No friction, gravity, thermal bath, moving flap, particle-particle collision, or other dissipative mechanism is included.

## Equilibrium

At fixed energy, the natural invariant equilibrium measure is uniform over accessible position and isotropic over velocity direction. For equal chamber volumes, equilibrium gives equal spatial probability density in the two chambers.

The funnel can rearrange trajectories without creating a preferred equilibrium transport direction. A selected incoming ensemble can nevertheless have very different transmission behaviour from a superficially similar ensemble sent from the other side.

## Time reversal

The billiard dynamics is time-reversal symmetric. If a microstate consists of particle positions and velocities `(x_i, v_i)`, reversing every velocity gives `(x_i, -v_i)`. Under ideal specular dynamics, the reversed state retraces the original evolution.

The prepared-beam reversal demonstrations use the complete final microstate of the corresponding forward demonstration. No particle is selected or discarded.

## Liouville's theorem

Hamiltonian evolution preserves phase-space volume. The funnel may concentrate a family of trajectories in position only by producing a compensating change in momentum-direction structure. It cannot compress a finite phase-space volume into a smaller one.

This is the underlying reason a rigid, passive, time-reversal-symmetric funnel is not a genuine one-way valve for an equilibrium gas.

## Ergodicity and mixing

Three claims should be kept distinct:

1. **Invariant equilibrium measure**: the equilibrium distribution is preserved by the dynamics.
2. **Ergodicity**: long-time averages along a typical trajectory reproduce equilibrium averages.
3. **Mixing or coarse-grained relaxation**: an initially non-equilibrium ensemble may become increasingly indistinguishable from equilibrium for suitable macroscopic observables.

Ergodicity by itself does not imply that an initially collimated fine-grained phase-space distribution literally converges to equilibrium. Liouville evolution preserves the information in that distribution. The present polygonal billiard is therefore not used as a proof of mixing.

The cumulative passage-imbalance plot is a transport statistic. It should not be read as a direct measurement of convergence of the instantaneous particle-density field to equilibrium.

## Numerical interpretation

The visualiser is an explanatory simulation rather than a general-purpose billiards research code. Its scientific claims are deliberately limited to the ideal model above. Any modification that adds dissipation, moving boundaries, thermalisation, external forcing, or stochastic collisions changes the physical problem and should be analysed separately.
