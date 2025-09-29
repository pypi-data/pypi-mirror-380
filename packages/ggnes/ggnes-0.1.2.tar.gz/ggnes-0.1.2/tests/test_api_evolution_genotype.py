"""
Comprehensive tests for evolution operations and genotype handling.
Tests mutation, crossover, selection, and population evolution.
"""

import os
import sys
import uuid

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes import CompositeGenotype, Genotype, LHSPattern, RHSAction, Rule
from ggnes.evolution.operators import mutate, uniform_crossover
from ggnes.rules.rule import EmbeddingLogic
from ggnes.utils.rng_manager import RNGManager


class TestGenotypeAPI:
    """Test Genotype creation and manipulation."""

    def test_genotype_creation_basic(self):
        """Basic genotype creation should work."""
        genotype = Genotype()
        assert genotype is not None
        assert hasattr(genotype, "rules")

    def test_genotype_with_initial_rules(self):
        """Should be able to create genotype with initial rules."""
        rules = [Rule(name="rule1"), Rule(name="rule2")]
        genotype = Genotype(rules=rules)
        assert len(genotype.rules) == 2

    def test_genotype_add_rule(self):
        """Should be able to add rules to genotype."""
        genotype = Genotype()

        rule = Rule(
            rule_id=uuid.uuid4(),
            lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
            rhs=RHSAction(add_nodes=None),
            embedding=EmbeddingLogic(),
        )

        initial_count = len(genotype.rules)
        genotype.add_rule(rule)
        assert len(genotype.rules) == initial_count + 1

    def test_genotype_serialization(self):
        """Should be able to save/load genotypes."""
        genotype = Genotype()

        # Should be able to serialize
        data = genotype.to_dict()
        assert isinstance(data, dict)

        # Should be able to recreate
        genotype2 = Genotype.from_dict(data)
        assert genotype2.id == genotype.id

    def test_genotype_clone(self):
        """Should be able to clone genotypes."""
        genotype = Genotype()
        clone = genotype.clone()

        assert clone.id != genotype.id  # Different ID
        assert len(clone.rules) == len(genotype.rules)  # Same rules


class TestMutationOperator:
    """Test mutation operations."""

    def test_mutation_simple(self):
        """Simple mutation should work intuitively."""
        genotype = Genotype()
        rng = RNGManager(seed=42)

        # Wrapper provides simple mutation without config
        from ggnes import mutate as simple_mutate

        mutated = simple_mutate(genotype, rng)
        assert mutated != genotype

    def test_mutation_with_config(self):
        """Test mutation with required config."""
        genotype = Genotype()
        rng = RNGManager(seed=42)

        config = {
            "mutation_rate": 0.1,
            "mutation_probs": {"add_rule": 0.5, "delete_rule": 0.3, "modify_rule": 0.2},
        }

        mutated = mutate(genotype, config, rng)
        assert mutated is not None

    def test_mutation_types(self):
        """Test different mutation types."""
        genotype = Genotype()
        # Add some initial rules
        for i in range(3):
            rule = Rule(
                rule_id=uuid.uuid4(),
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(add_nodes=None),
                embedding=EmbeddingLogic(),
            )
            genotype.add_rule(rule)

        rng = RNGManager(seed=42)

        # Test add mutation
        config_add = {
            "mutation_rate": 1.0,  # Always mutate
            "mutation_probs": {"add_rule": 1.0, "delete_rule": 0.0, "modify_rule": 0.0},
        }

        mutated_add = mutate(genotype, config_add, rng)
        # Should have more rules
        assert len(mutated_add.rules) >= len(genotype.rules)

    @pytest.mark.xfail(reason="No mutation validation")
    def test_mutation_validation(self):
        """Mutations should be validated."""
        genotype = Genotype()
        rng = RNGManager(seed=42)

        # Invalid config should raise error
        config = {
            "mutation_rate": 2.0,  # Invalid > 1
            "mutation_probs": {},
        }

        with pytest.raises(ValueError):
            mutate(genotype, config, rng)


class TestCrossoverOperator:
    """Test crossover operations."""

    def test_crossover_simple(self):
        """Simple crossover should work intuitively."""
        parent1 = Genotype()
        parent2 = Genotype()
        rng = RNGManager(seed=42)

        # Wrapper provides simple crossover without config
        from ggnes import crossover as simple_crossover

        child = simple_crossover(parent1, parent2, rng)
        assert child is not None

    def test_crossover_with_config(self):
        """Test crossover with required config."""
        parent1 = Genotype()
        parent2 = Genotype()

        # Add different rules to parents
        for i in range(3):
            rule1 = Rule(
                rule_id=uuid.uuid4(),
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(add_nodes=None),
                embedding=EmbeddingLogic(),
                metadata={"parent": 1, "index": i},
            )
            parent1.add_rule(rule1)

            rule2 = Rule(
                rule_id=uuid.uuid4(),
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(add_nodes=None),
                embedding=EmbeddingLogic(),
                metadata={"parent": 2, "index": i},
            )
            parent2.add_rule(rule2)

        rng = RNGManager(seed=42)
        config = {"crossover_probability_per_rule": 0.5}

        child1, child2 = uniform_crossover(parent1, parent2, config, rng)

        assert child1 is not None
        assert child2 is not None
        # Children should have rules from both parents
        assert len(child1.rules) > 0
        assert len(child2.rules) > 0

    @pytest.mark.xfail(reason="No crossover validation")
    def test_crossover_validation(self):
        """Crossover should validate compatibility."""
        parent1 = Genotype()
        parent2 = CompositeGenotype()  # Different type

        rng = RNGManager(seed=42)
        config = {}

        with pytest.raises(TypeError):
            uniform_crossover(parent1, parent2, config, rng)


class TestEvolutionWorkflow:
    """Test complete evolution workflows."""

    def test_simple_evolution(self):
        """Simple evolution should work."""
        from ggnes.evolution import evolve

        # Create initial population
        population = [Genotype() for _ in range(10)]

        # Define fitness function
        def fitness(genotype):
            return len(genotype.rules)  # Simple: more rules = better

        # Evolve
        final_population = evolve(
            population=population,
            fitness_function=fitness,
            generations=10,
            mutation_rate=0.1,
            crossover_rate=0.5,
        )

        assert len(final_population) == len(population)
        # Best individual should have improved
        best = max(final_population, key=fitness)
        assert fitness(best) > 0

    def test_selection_operators(self):
        """Test different selection strategies."""
        from ggnes.evolution.selection import (
            elitism_selection,
            roulette_selection,
            tournament_selection,
        )

        population = [Genotype() for _ in range(20)]
        fitness_scores = [i for i in range(20)]  # Simple scores

        # Tournament selection
        selected = tournament_selection(
            population, fitness_scores, tournament_size=3, num_select=10
        )
        assert len(selected) == 10

        # Roulette selection
        selected = roulette_selection(population, fitness_scores, num_select=10)
        assert len(selected) == 10

        # Elitism
        elite = elitism_selection(population, fitness_scores, num_elite=5)
        assert len(elite) == 5
        # Should be the best individuals
        assert all(f >= 15 for f in [fitness_scores[population.index(e)] for e in elite])

    def test_population_management(self):
        """Test population creation and management."""
        from ggnes.evolution import Population

        # Create population
        pop = Population(size=50)
        assert len(pop) == 50

        # Evaluate population
        pop.evaluate(fitness_function=lambda g: len(g.rules))

        # Get best individuals
        best = pop.get_best(n=5)
        assert len(best) == 5

        # Get statistics
        stats = pop.get_statistics()
        assert "mean_fitness" in stats
        assert "max_fitness" in stats
        assert "min_fitness" in stats
        assert "diversity" in stats

    def test_multi_objective_evolution(self):
        """Test multi-objective optimization."""
        from ggnes.evolution import nsga2_evolve

        population = [Genotype() for _ in range(20)]

        # Multiple objectives
        def objectives(genotype):
            return {
                "accuracy": len(genotype.rules),  # Maximize
                "complexity": -len(genotype.rules),  # Minimize (negative)
            }

        pareto_front = nsga2_evolve(population=population, objectives=objectives, generations=10)

        assert len(pareto_front) > 0
        # Should have trade-off solutions


class TestCompositeGenotype:
    """Test CompositeGenotype for hierarchical evolution."""

    def test_composite_genotype_creation(self):
        """Should be able to create composite genotypes."""
        composite = CompositeGenotype()
        assert composite is not None

    def test_composite_with_components(self):
        """Should be able to add component genotypes."""
        composite = CompositeGenotype()

        # Add component genotypes
        structure_genotype = Genotype()
        weight_genotype = Genotype()

        composite.add_component("structure", structure_genotype)
        composite.add_component("weights", weight_genotype)

        assert len(composite.components) == 2
        assert "structure" in composite.components

    @pytest.mark.xfail(reason="No hierarchical evolution")
    def test_hierarchical_evolution(self):
        """Test evolution with composite genotypes."""
        from ggnes.evolution import hierarchical_evolve

        # Create population of composite genotypes
        population = []
        for _ in range(10):
            composite = CompositeGenotype()
            composite.add_component("layer1", Genotype())
            composite.add_component("layer2", Genotype())
            population.append(composite)

        # Hierarchical fitness
        def fitness(composite):
            layer1_score = len(composite.components["layer1"].rules)
            layer2_score = len(composite.components["layer2"].rules)
            return layer1_score + layer2_score

        final_pop = hierarchical_evolve(
            population=population,
            fitness_function=fitness,
            generations=10,
            evolution_strategy="coevolution",  # or 'sequential'
        )

        assert len(final_pop) == len(population)
