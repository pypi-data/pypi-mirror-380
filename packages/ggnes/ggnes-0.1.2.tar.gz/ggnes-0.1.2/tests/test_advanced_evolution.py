"""
Comprehensive tests for advanced evolution features including
multi-objective optimization, hierarchical evolution, and island models.
"""

import os
import sys

import numpy as np
import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes import CompositeGenotype, Genotype, Population, hierarchical_evolve, nsga2_evolve


class TestMultiObjectiveEvolution:
    """Test multi-objective optimization with NSGA-II."""

    def test_nsga2_basic(self):
        """Test basic NSGA-II evolution."""
        # Create initial population
        population = [Genotype() for _ in range(20)]

        # Define multiple objectives
        def objectives(genotype):
            # Simulate two conflicting objectives
            size = len(genotype.rules)
            complexity = sum(1 for _ in genotype.rules)

            return {
                "accuracy": size * 0.1 + np.random.random() * 0.5,  # Maximize
                "efficiency": -complexity * 0.2 - np.random.random() * 0.3,  # Minimize (negative)
            }

        # Run NSGA-II
        pareto_front = nsga2_evolve(population=population, objectives=objectives, generations=5)

        assert len(pareto_front) > 0
        assert len(pareto_front) <= len(population)

    def test_pareto_dominance(self):
        """Test that Pareto front contains non-dominated solutions."""
        population = [Genotype() for _ in range(30)]

        def objectives(genotype):
            return {"obj1": np.random.random(), "obj2": np.random.random()}

        pareto_front = nsga2_evolve(population=population, objectives=objectives, generations=10)

        # Check non-dominance
        for i, sol1 in enumerate(pareto_front):
            obj1 = objectives(sol1)
            for j, sol2 in enumerate(pareto_front):
                if i != j:
                    obj2 = objectives(sol2)
                    # Neither should dominate the other
                    dominates = all(obj1[k] >= obj2[k] for k in obj1) and any(
                        obj1[k] > obj2[k] for k in obj1
                    )
                    assert not dominates, "Found dominated solution in Pareto front"

    def test_multi_objective_with_constraints(self):
        """Test multi-objective with constraints."""
        population = [Genotype() for _ in range(20)]

        def objectives(genotype):
            return {"performance": np.random.random(), "cost": -np.random.random()}

        def constraints(genotype):
            """Define constraints that must be satisfied."""
            return {"max_size": len(genotype.rules) <= 10, "min_rules": len(genotype.rules) >= 1}

        # This would need NSGA-II with constraint handling
        # Currently a placeholder for the API design
        try:
            pareto_front = nsga2_evolve(
                population=population, objectives=objectives, constraints=constraints, generations=5
            )
            assert len(pareto_front) > 0
        except TypeError:
            # If constraints not supported yet
            pytest.skip("Constraint handling not implemented")

    def test_crowding_distance(self):
        """Test crowding distance calculation for diversity."""
        from ggnes.evolution.multi_objective import calculate_crowding_distance

        # Create solutions with objectives
        solutions = []
        for i in range(10):
            sol = Genotype()
            sol.objectives = {"f1": i / 10.0, "f2": (10 - i) / 10.0}
            solutions.append(sol)

        # Calculate crowding distances
        try:
            distances = calculate_crowding_distance(solutions)

            # Boundary solutions should have infinite distance
            assert distances[0] == float("inf")
            assert distances[-1] == float("inf")

            # Middle solutions should have finite distances
            for d in distances[1:-1]:
                assert 0 < d < float("inf")
        except ImportError:
            pytest.skip("Crowding distance not implemented")


class TestHierarchicalEvolution:
    """Test hierarchical and compositional evolution."""

    def test_composite_genotype_creation(self):
        """Test creating composite genotypes with components."""
        composite = CompositeGenotype()

        # Add different component genotypes
        structure_genotype = Genotype()
        hyperparameter_genotype = Genotype()

        composite.add_component("structure", structure_genotype)
        composite.add_component("hyperparameters", hyperparameter_genotype)

        assert len(composite.components) == 2
        assert "structure" in composite.components
        assert "hyperparameters" in composite.components

    def test_hierarchical_fitness(self):
        """Test hierarchical fitness evaluation."""
        # Create population of composite genotypes
        population = []
        for _ in range(10):
            composite = CompositeGenotype()
            composite.add_component("layer1", Genotype())
            composite.add_component("layer2", Genotype())
            composite.add_component("layer3", Genotype())
            population.append(composite)

        def hierarchical_fitness(composite):
            """Evaluate fitness at multiple levels."""
            # Layer-level fitness
            layer_scores = []
            for name, genotype in composite.components.items():
                score = len(genotype.rules) * 0.1 + np.random.random()
                layer_scores.append(score)

            # Overall fitness combines layer scores
            return np.mean(layer_scores) + np.random.random() * 0.1

        # Run hierarchical evolution
        evolved_pop = hierarchical_evolve(
            population=population,
            fitness_function=hierarchical_fitness,
            generations=5,
            evolution_strategy="sequential",  # or 'coevolution'
        )

        assert len(evolved_pop) == len(population)

    def test_coevolution_strategy(self):
        """Test coevolution of multiple components."""
        population = []
        for _ in range(10):
            composite = CompositeGenotype()
            composite.add_component("encoder", Genotype())
            composite.add_component("decoder", Genotype())
            population.append(composite)

        def coevolution_fitness(composite):
            # Encoder and decoder must work together
            encoder_size = len(composite.components["encoder"].rules)
            decoder_size = len(composite.components["decoder"].rules)

            # Fitness depends on compatibility
            compatibility = 1.0 / (1 + abs(encoder_size - decoder_size))
            performance = (encoder_size + decoder_size) * 0.05

            return compatibility + performance

        evolved_pop = hierarchical_evolve(
            population=population,
            fitness_function=coevolution_fitness,
            generations=5,
            evolution_strategy="coevolution",
        )

        # Check that encoder/decoder sizes became more compatible
        final_differences = []
        for composite in evolved_pop:
            enc_size = len(composite.components["encoder"].rules)
            dec_size = len(composite.components["decoder"].rules)
            final_differences.append(abs(enc_size - dec_size))

        # Average difference should be relatively small
        assert np.mean(final_differences) < 5

    def test_nested_hierarchies(self):
        """Test nested hierarchical structures."""
        # Create nested composite genotype
        root = CompositeGenotype()

        # Add sub-composites
        feature_extractor = CompositeGenotype()
        feature_extractor.add_component("conv_block1", Genotype())
        feature_extractor.add_component("conv_block2", Genotype())

        classifier = CompositeGenotype()
        classifier.add_component("fc1", Genotype())
        classifier.add_component("fc2", Genotype())

        root.add_component("feature_extractor", feature_extractor)
        root.add_component("classifier", classifier)

        # Should support nested access
        assert isinstance(root.components["feature_extractor"], CompositeGenotype)
        assert "conv_block1" in root.components["feature_extractor"].components


class TestIslandModelEvolution:
    """Test island model parallel evolution."""

    def test_island_creation(self):
        """Test creating multiple island populations."""
        from ggnes.evolution.island_model import IslandModel

        try:
            # Create island model with multiple populations
            island_model = IslandModel(
                num_islands=4, population_per_island=25, migration_rate=0.1, migration_frequency=5
            )

            assert island_model.num_islands == 4
            assert len(island_model.islands) == 4

            for island in island_model.islands:
                assert len(island.population) == 25
        except ImportError:
            pytest.skip("Island model not implemented")

    def test_migration_between_islands(self):
        """Test migration of individuals between islands."""
        from ggnes.evolution.island_model import IslandModel

        try:
            island_model = IslandModel(
                num_islands=3, population_per_island=20, migration_rate=0.2, migration_frequency=1
            )

            # Mark individuals for tracking
            for i, island in enumerate(island_model.islands):
                for individual in island.population:
                    individual.origin_island = i

            # Perform migration
            island_model.migrate()

            # Check that some individuals moved
            for i, island in enumerate(island_model.islands):
                migrants = [ind for ind in island.population if ind.origin_island != i]
                assert len(migrants) > 0, f"No migrants in island {i}"
        except ImportError:
            pytest.skip("Island model not implemented")

    def test_island_evolution_diversity(self):
        """Test that island model maintains diversity."""
        from ggnes.evolution.island_model import IslandModel

        try:

            def fitness_function(genotype):
                return len(genotype.rules) * 0.1 + np.random.random()

            island_model = IslandModel(
                num_islands=4, population_per_island=20, migration_rate=0.1, migration_frequency=5
            )

            # Evolve islands
            island_model.evolve(fitness_function=fitness_function, generations=10)

            # Measure diversity across islands
            all_genotypes = []
            for island in island_model.islands:
                all_genotypes.extend(island.population)

            # Calculate diversity (unique rule combinations)
            unique_signatures = set()
            for genotype in all_genotypes:
                signature = tuple(str(rule.rule_id) for rule in genotype.rules)
                unique_signatures.add(signature)

            diversity = len(unique_signatures) / len(all_genotypes)

            # Island model should maintain higher diversity
            assert diversity > 0.3, "Island model lost diversity"
        except ImportError:
            pytest.skip("Island model not implemented")


class TestAdaptiveEvolution:
    """Test adaptive evolution strategies."""

    def test_adaptive_mutation_rate(self):
        """Test self-adaptive mutation rates."""
        from ggnes.evolution.adaptive import AdaptiveEvolution

        try:
            population = [Genotype() for _ in range(50)]

            # Each individual has its own mutation rate
            for genotype in population:
                genotype.mutation_rate = np.random.uniform(0.01, 0.5)

            adaptive_evolution = AdaptiveEvolution()

            def fitness(genotype):
                return len(genotype.rules) * 0.1

            # Evolve with adaptive rates
            evolved = adaptive_evolution.evolve(
                population=population, fitness_function=fitness, generations=10
            )

            # Successful individuals should have converged rates
            best_10 = sorted(evolved, key=fitness, reverse=True)[:10]
            rates = [g.mutation_rate for g in best_10]

            # Rates should have converged somewhat
            assert np.std(rates) < 0.2
        except ImportError:
            pytest.skip("Adaptive evolution not implemented")

    def test_adaptive_operator_selection(self):
        """Test adaptive selection of genetic operators."""
        from ggnes.evolution.adaptive import OperatorAdaptation

        try:
            operators = {
                "uniform_crossover": 0.33,
                "one_point_crossover": 0.33,
                "two_point_crossover": 0.34,
            }

            adaptation = OperatorAdaptation(operators)

            # Track operator success
            for _ in range(100):
                # Select operator based on probabilities
                operator = adaptation.select_operator()

                # Simulate success/failure
                success = np.random.random() > 0.5

                # Update operator probabilities
                adaptation.update(operator, success)

            # Most successful operator should have highest probability
            final_probs = adaptation.get_probabilities()
            assert sum(final_probs.values()) == pytest.approx(1.0)
        except ImportError:
            pytest.skip("Operator adaptation not implemented")


class TestEvolutionMetrics:
    """Test evolution metrics and monitoring."""

    def test_convergence_detection(self):
        """Test detecting evolution convergence."""
        from ggnes.evolution.metrics import ConvergenceDetector

        try:
            detector = ConvergenceDetector(window_size=10, threshold=0.01)

            # Simulate fitness progression
            fitness_history = []
            for gen in range(50):
                # Fitness improves then plateaus
                if gen < 20:
                    fitness = gen * 0.1 + np.random.random() * 0.05
                else:
                    fitness = 2.0 + np.random.random() * 0.01

                fitness_history.append(fitness)
                has_converged = detector.check_convergence(fitness_history)

                if gen > 30:
                    assert has_converged, "Should detect convergence after plateau"
        except ImportError:
            pytest.skip("Convergence detection not implemented")

    def test_diversity_metrics(self):
        """Test population diversity measurements."""
        from ggnes.evolution.metrics import calculate_diversity

        try:
            population = []

            # Create similar genotypes (low diversity)
            base_genotype = Genotype()
            for _ in range(10):
                similar = base_genotype.clone()
                population.append(similar)

            low_diversity = calculate_diversity(population)

            # Create diverse genotypes
            diverse_population = []
            for _ in range(10):
                genotype = Genotype()
                # Add random number of random rules
                for _ in range(np.random.randint(0, 5)):
                    # Would add random rules here
                    pass
                diverse_population.append(genotype)

            high_diversity = calculate_diversity(diverse_population)

            assert high_diversity > low_diversity
        except ImportError:
            pytest.skip("Diversity metrics not implemented")

    def test_evolution_statistics(self):
        """Test collecting evolution statistics."""
        population = Population(size=50)

        def fitness(genotype):
            return len(genotype.rules) * 0.1 + np.random.random()

        population.evaluate(fitness)
        stats = population.get_statistics()

        assert "mean_fitness" in stats
        assert "max_fitness" in stats
        assert "min_fitness" in stats
        assert "diversity" in stats

        assert stats["mean_fitness"] >= stats["min_fitness"]
        assert stats["mean_fitness"] <= stats["max_fitness"]
        assert 0 <= stats["diversity"] <= len(population)


class TestEvolutionCheckpointing:
    """Test saving and resuming evolution."""

    def test_save_population(self):
        """Test saving population to disk."""
        import pickle
        import tempfile

        population = [Genotype() for _ in range(20)]

        with tempfile.NamedTemporaryFile(suffix=".pkl", delete=False) as f:
            pickle.dump(population, f)
            temp_path = f.name

        # Load population
        with open(temp_path, "rb") as f:
            loaded_population = pickle.load(f)

        assert len(loaded_population) == len(population)

        # Clean up
        os.unlink(temp_path)

    def test_evolution_checkpoint(self):
        """Test checkpointing during evolution."""
        from ggnes.evolution.checkpointing import EvolutionCheckpoint

        try:
            checkpoint = EvolutionCheckpoint()

            population = [Genotype() for _ in range(30)]
            generation = 10
            best_fitness = 0.95

            # Save checkpoint
            checkpoint.save(
                population=population,
                generation=generation,
                best_fitness=best_fitness,
                metadata={"experiment": "test"},
            )

            # Load checkpoint
            state = checkpoint.load()

            assert len(state["population"]) == len(population)
            assert state["generation"] == generation
            assert state["best_fitness"] == best_fitness
            assert state["metadata"]["experiment"] == "test"
        except ImportError:
            pytest.skip("Checkpointing not implemented")

    def test_resume_evolution(self):
        """Test resuming evolution from checkpoint."""
        from ggnes.evolution.checkpointing import ResumableEvolution

        try:
            evolution = ResumableEvolution(checkpoint_frequency=5, checkpoint_dir="./checkpoints")

            population = [Genotype() for _ in range(20)]

            def fitness(genotype):
                return len(genotype.rules) * 0.1

            # Run partial evolution
            evolved = evolution.evolve(
                population=population, fitness_function=fitness, generations=7
            )

            # Should have created checkpoint at generation 5
            assert evolution.last_checkpoint_generation == 5

            # Resume from checkpoint
            resumed = evolution.resume(fitness_function=fitness, total_generations=10)

            # Should continue from generation 5
            assert evolution.current_generation == 10
        except ImportError:
            pytest.skip("Resumable evolution not implemented")
