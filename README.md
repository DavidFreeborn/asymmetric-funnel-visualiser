# Particles with an asymmetric funnel

An interactive billiard simulation showing what an asymmetric funnel can, and cannot, do in a reversible closed system.

A fixed asymmetric funnel can strongly affect selected families of trajectories. It does not thereby become a one-way valve at equilibrium. The visualiser lets you compare equilibrium-like starting states, collimated beams from either side, and exact time reversal of the prepared-beam demonstrations.

## Live visualiser

The project is a single self-contained HTML file. Open `index.html` directly in a modern browser, or publish the repository with GitHub Pages.

If this repository is named `asymmetric-funnel-visualiser` under the `davidfreeborn` account, the Pages URL will be:

`https://davidfreeborn.github.io/asymmetric-funnel-visualiser/`

## What the visualiser includes

### Starting states

- **Random gas**: particles begin throughout the two chambers with isotropic directions.
- **Collimated beam from A**: a narrow range of directions is prepared in chamber A, then the closed system evolves normally.
- **Collimated beam from B**: the exact mirrored preparation from chamber B.

The ordinary starting states run indefinitely. Measurements include chamber occupancy, passage counts, and cumulative A→B versus B→A passage imbalance.

### Prepared-beam demonstration

The demonstration uses the same collimated initial ensembles as the ordinary starting states, but stops the forward run at a fixed time so that time reversal can be shown cleanly.

1. **A → B beam**
2. **Same beam B → A**
3. **Reverse A → B final state**
4. **Reverse B → A final state**

For the reverse demonstrations, the complete final microstate is used. Every particle velocity is reversed. The reversed run then stops when the ensemble returns to the original prepared state.

### Analysis

The analysis panel contains:

- current chamber occupancy and passage counts;
- cumulative passage imbalance over time;
- a position-and-direction view of crossing states;
- a short account of reversibility, Liouville's theorem, ergodicity, and mixing.

Trajectories are optional in the ordinary simulation and enabled by default in the prepared-beam demonstration.

## Physical model

The simulation is an ideal specular billiard:

- point particles;
- fixed particle speed;
- static reflecting walls;
- perfectly specular collisions;
- no friction or gravity;
- no particle-particle collisions.

The equilibrium invariant measure is uniform in accessible position at fixed energy, with the corresponding isotropic velocity-direction distribution. Time reversal maps `(x, p)` to `(x, -p)`.

An initially collimated ensemble should not be described as literally converging to the fine-grained equilibrium distribution. Liouville evolution preserves phase-space measure. Ergodicity concerns long-time averages; relaxation of an instantaneous ensemble toward equilibrium requires stronger assumptions such as mixing or an appropriate coarse-grained description. See [PHYSICS.md](PHYSICS.md) for the scope of the claims made by the visualiser.

## Controls

- **Play / Pause**
- **Reset**
- **Reverse velocities**
- **Trajectories**
- **Particle number**
- **Simulation speed**
- **Starting state**
- **A/B starting proportion** for the random gas
- **Opening width**

## Running locally

No build step and no server are required. You can simply open `index.html`.

If you prefer to serve it locally:

```bash
python -m http.server 8000
```

then open `http://localhost:8000/`.

## GitHub Pages

The simplest deployment is:

1. Create a repository and upload this pack to the repository root.
2. Push the default branch to GitHub.
3. In **Settings → Pages**, choose **Deploy from a branch**.
4. Select the default branch and `/ (root)`.

The included `.nojekyll` file tells GitHub Pages to serve the repository as plain static files.

## Repository structure

```text
.
├── index.html
├── README.md
├── PHYSICS.md
├── CITATION.cff
├── LICENSE
├── .nojekyll
├── .gitignore
├── scripts/
│   └── validate.py
└── .github/
    └── workflows/
        └── validate.yml
```

## Validation

The repository includes a lightweight automated check that:

- confirms the visualiser remains a self-contained HTML document;
- extracts the embedded JavaScript and checks its syntax with Node;
- rejects accidental external script or stylesheet dependencies;
- rejects leftover `TODO`, `FIXME`, or `console.log` debugging statements.

Run it locally with:

```bash
python scripts/validate.py
```

The simulation itself should still be inspected interactively after substantive changes to physics or rendering.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). GitHub will expose this through its **Cite this repository** interface.

## Licence

MIT. See [`LICENSE`](LICENSE).
